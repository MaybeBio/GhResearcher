# GhResearcher


without leaving YOUR terminal

主要参考：
- https://docs.github.com/en/search-github
- https://cli.github.com/manual/
- https://docs.github.com/en/rest/activity/events?apiVersion=2026-03-10

---

## 核心功能说明 / Core Features

### 1. 动态追踪模块 / Monitoring Module (`monitor`)

#### 🇬🇧 English Description
The `monitor` command allows you to track and view the recent events of a specific GitHub user, organization, or repository. It provides a comprehensive timeline of GitHub activity, such as pushing commits, starring repositories, following other users, or watching repo-level events.

**Usage:**
```bash
ghresearcher monitor [OPTIONS] [TARGET]
```

**Arguments:**
- `TARGET`: The GitHub username or organization you want to monitor (e.g., `teorth` or `GENTEL-lab`). [Optional if using `--file`]

**Options:**
- `-f, --file PATH`: File containing GitHub targets (one per line) for batch monitoring.
- `-R, --repo`: Treat the target (or list of targets) as a Repository in `owner/repo` format.
- `-O, --org`: Treat the target (or list of targets) as an Organization instead of a regular User. Useful for tracking an entire group/lab.
- `-r, --received`: Switch into "Dashboard" mode. Instead of showing what the target user did, this fetches the "received events" feed. This displays the activities of the repositories and people the target user follows.
- `-l, --limit INTEGER`: The maximum number of recent events to fetch per user. (Default: 30, automatically paginates to bypass GitHub's 100 per-page limit).
- `--since YYYY-MM-DD`: Filter events on or after this date.
- `--until YYYY-MM-DD`: Filter events on or before this date.
- `--help`: Show the help message and exit.
- `--expand-commits`: When enabled, the tool will make additional GitHub API calls to fetch commit details for `PushEvent`s that lack a `commits` array in the event payload. Default: off.

**Notes:**
- **Global Chronological Timeline**: When batch monitoring multiple users using `-f`, all events from all target users are fetched concurrently, automatically merged, and sorted chronologically to form a unified global timeline.
- **Compact Commit Display**: For `PushEvent`, the commit SHA hash is truncated to the first 7 characters, and only the first line of the commit message is shown to keep the terminal output clean.
- **Rich Payload Labels**: `IssuesEvent` and `PullRequestEvent` now include the issue/PR title when available, and `ReleaseEvent` shows the release tag or release name when GitHub provides one.
- **GitHub API Limits**: The API inherently restricts the timeline to a maximum of 300 recent events or events within the past 90 days, regardless of the limit specified.

- **Expanded Commit Retrieval (`--expand-commits`)**: If a `PushEvent` does not include a `commits` array (this is common in the Events API), enabling `--expand-commits` will make an extra call to `GET /repos/{owner}/{repo}/commits/{head}` (using the event's `payload.head`) to retrieve a representative commit message and SHA. Expanded commits are marked with the prefix `(expanded)` in the output so you can distinguish them from the original feed data. This option is off by default because it increases API calls and may trigger rate limits when used on large batches.

**Implementation summary**:
- Files modified: `ghresearcher/ghresearcher/tracker.py`, `ghresearcher/ghresearcher/cli.py`.
- Behavior: when `--expand-commits` is set and `PushEvent.payload.commits` is empty, `tracker` will attempt to fetch `repos/{repo}/commits/{head}` and display a single expanded commit line (sha truncated to 7 chars, first line of message). If the fetch fails or `head` is missing, the event remains labeled `(no commit info)`.

**Caveats & recommendations**:
- Enabling `--expand-commits` is useful for single-user investigation or small batches. Avoid enabling it for large concurrent multi-user queries unless you add rate-limit handling or reduce concurrency.
- The expanded fetch uses your `gh` authentication (same as other API calls). Consider running authenticated and monitor `gh` rate-limit headers if you plan to expand many commits.

**Examples:**
1. **Track a developer's public actions** (What did they do recently?):
   ```bash
   ghresearcher monitor teorth
   ```
2. **Batch monitor an expert group** (Merge events from users in a file into one timeline):
   ```bash
   ghresearcher monitor -f top_researchers.txt --since 2026-05-01 --until 2026-05-12
   ```
3. **Track a developer's information feed** (What are the people/repos they follow doing?):
   ```bash
   # This is great for discovering new tool landscapes curated by experts
   ghresearcher monitor teorth --received
   ```
4. **Track a repository directly** (Watch the event stream for one repo):
   ```bash
   ghresearcher monitor isblab/disobind --repo
   ```

---

#### 🇨🇳 中文详细说明
`monitor` 命令用于全方位追踪特定 GitHub 用户、组织或仓库的最新动态。它可以让你像“刷朋友圈”一样，快速了解某个领域的大佬最近在写什么代码、点赞了什么新项目、关注了哪些研究员，或者直接观察某个仓库的事件流。这对于科研人员追踪前沿代码和方案非常有帮助。

**基本用法:**
```bash
ghresearcher monitor [选项] [用户名]
```

**命令参数:**
- `USERNAME/OWNER/REPO`: 你想要监控的核心目标 GitHub 用户名、组织名或仓库名 (例如：`teorth`、`GENTEL-lab`、`isblab/disobind`)。[结合 `--file` 使用时非必填参数]

**可选参数 (Options):**
- `-f, --file 文件路径`: 包含多名 GitHub 用户名的文本文件（每行一个），用于批量监控。
- `-R, --repo`: 将目标解释为仓库，格式必须是 `owner/repo`。
- `-r, --received`: 获取“接收到的事件”列表（Feed流）。如果不加该参数，你看到的是“这个大佬做了什么”；**加上该参数后，你看到的是“这个大佬关注的人和仓库在发生什么”**（相当于查看他的 GitHub 首页信息流）。
- `-l, --limit 整数`: 限制提取每个用户的动态条数。默认显示最新的 30 条动态，支持无缝跨页抓取（自动突破 GitHub API 单页 100 条的限制）。
- `--since YYYY-MM-DD`: 仅显示该日期及之后的动态。
- `--until YYYY-MM-DD`: 仅显示该日期及之前的动态。
- `--help`: 打印当前命令的帮助与参数说明。

**补充说明:**
- **全局时间线合并**: 当使用 `-f` 批量监控多个用户时，后台将高并发拉取所有人的动态，并将结果打乱按时间戳降序合并，最终形成一个类似“学术圈朋友圈”的全局视角 Timeline。
- **时间提前阻断**: 配合 `--since` 选项能够高效避免拉取过期的无效分页数据，这极大提升性能并保护了访问限额。
- **Commit 信息截断**: 为了保证终端输出紧凑美观，在遇到代码推送（`PushEvent`）时，提交的 SHA-1 哈希值会被强制截断为前 7 位，且 Commit Message 仅显示第一行主标题。
- **事件标题增强**: `IssuesEvent`、`PullRequestEvent` 会补出 issue/PR 的标题；`ReleaseEvent` 会展示 release 的 tag 名或 release 名称，方便直接定位具体对象。
- **GitHub 原生限制**: 无论 `limit` 设置多大，受到 GitHub 官方 API 的服务层限制，其实际最多只能返回过去 90 天内或最近的 300 条活动记录。

**实战用法示例:**
1. **追踪佬本人的公开行为** (他最近干了啥？是否推送了新仓库？):
   ```bash
   ghresearcher monitor teorth
   ```
2. **批量订阅指定专家的开源朋友圈** (读取列表，截取特定五一假期间动态):
   ```bash
   ghresearcher monitor -f experts.txt --since 2026-05-01 --until 2026-05-05
   ```
3. **追踪整个课题组/实验室的公开组织动态**:
   ```bash
   ghresearcher monitor GENTEL-lab --org
   ```
4. **直接追踪仓库动态**:
   ```bash
   ghresearcher monitor isblab/disobind --repo
   ```
5. **窥探大佬的信息流/视野** (他关注的同行最近在搞什么黑科技？):
   ```bash
   # 这相当于借用目标大佬的视角来进行文献和工具拓荒
   ghresearcher monitor teorth -r   
   ```


## Cases

### 1. 追踪动态

我们以中国时区为主，将所有时间转换为 CST 格式。

这里以我为例子，查看我自己的动态（我是主动方，我是执行视角）：

```bash
ghresearcher monitor MaybeBio
```

the log shows
```bash
❯ ghresearcher monitor MaybeBio
Fetching recent events for MaybeBio...

2026-05-12 13:19:57 | ⭐️ MaybeBio starred gennaro-tedesco/gh-s
2026-05-12 10:41:18 | 🚀 MaybeBio pushed to MaybeBio/bioinfor_script_modules (no commit info)
2026-05-12 08:24:44 | ⭐️ MaybeBio starred aqlaboratory/openfold-3
2026-05-12 08:22:52 | ⭐️ MaybeBio starred Yuan1z0825/nature-skills
2026-05-11 19:18:10 | 🚀 MaybeBio pushed to MaybeBio/bioinfor_script_modules (no commit info)
2026-05-11 18:58:56 | 🚀 MaybeBio pushed to MaybeBio/AlphaFold3-SeqVisToolkit (no commit info)
2026-05-11 18:28:59 | 🚀 MaybeBio pushed to MaybeBio/personal_private (no commit info)
2026-05-11 18:19:49 | 🔹 MaybeBio performed ReleaseEvent on MaybeBio/AlphaFold3-SeqVisToolkit
2026-05-11 18:18:35 | 🚀 MaybeBio pushed to MaybeBio/AlphaFold3-SeqVisToolkit (no commit info)
2026-05-11 18:09:12 | 🚀 MaybeBio pushed to MaybeBio/personal_private (no commit info)
2026-05-11 15:14:51 | ⭐️ MaybeBio starred buua436/PAPERFlow
2026-05-11 15:10:22 | ⭐️ MaybeBio starred Satorica/Hierarchy-RAG
2026-05-11 14:53:40 | ⭐️ MaybeBio starred Robbings/chatgpt-graph-navigator
2026-05-11 00:01:49 | 🚀 MaybeBio pushed to MaybeBio/pyPaperFlow (no commit info)
2026-05-10 15:29:21 | 🚀 MaybeBio pushed to MaybeBio/DL4Proteins (no commit info)
2026-05-10 14:59:26 | 🚀 MaybeBio pushed to MaybeBio/personal_private (no commit info)
2026-05-10 14:54:53 | 🚀 MaybeBio pushed to MaybeBio/personal_private (no commit info)
2026-05-10 14:51:49 | 🚀 MaybeBio pushed to MaybeBio/personal_private (no commit info)
2026-05-10 14:26:58 | 🚀 MaybeBio pushed to MaybeBio/personal_private (no commit info)
2026-05-10 12:58:43 | 🚀 MaybeBio pushed to MaybeBio/personal_private (no commit info)
2026-05-09 16:33:01 | ⭐️ MaybeBio starred microsoft/markitdown
2026-05-09 16:13:43 | ⭐️ MaybeBio starred datalab-to/marker
2026-05-09 15:09:22 | 🚀 MaybeBio pushed to MaybeBio/personal_private (no commit info)
2026-05-09 14:58:25 | 🚀 MaybeBio pushed to MaybeBio/personal_private (no commit info)
2026-05-09 14:09:56 | 🚀 MaybeBio pushed to MaybeBio/personal_private (no commit info)
2026-05-09 13:43:26 | 🚀 MaybeBio pushed to MaybeBio/personal_private (no commit info)
2026-05-09 13:34:53 | 🚀 MaybeBio pushed to MaybeBio/personal_private (no commit info)
2026-05-09 13:27:44 | 🚀 MaybeBio pushed to MaybeBio/personal_private (no commit info)
2026-05-09 13:27:19 | 🚀 MaybeBio pushed to MaybeBio/personal_private (no commit info)
2026-05-09 11:57:32 | 🚀 MaybeBio pushed to MaybeBio/pyResearchFlow (no commit info)

```

查看我所关注的人和仓库在发生什么，也就是查看我的 GitHub 首页信息流（我是被动方，观察视角）。

```bash
ghresearcher monitor -r MaybeBio 
```

the log shows
```bash
Fetching recent events for MaybeBio...

2026-05-12 15:38:00 | 🚀 teorth pushed to leanprover-community/mathlib-at-ICERM26 (no commit info)
2026-05-12 15:35:29 | 🚀 teorth pushed to leanprover-community/mathlib-at-ICERM26 (no commit info)
2026-05-12 15:35:10 | 🔹 Vizards performed IssueCommentEvent on deepseek-ai/awesome-deepseek-agent
2026-05-12 15:32:30 | 🔹 Vizards performed IssueCommentEvent on deepseek-ai/awesome-deepseek-agent
2026-05-12 15:30:44 | ⭐️ Msadekq starred deepseek-ai/DeepSeek-LLM
2026-05-12 15:28:46 | 🚀 teorth pushed to leanprover-community/mathlib-at-ICERM26 (no commit info)
2026-05-12 15:28:06 | ⭐️ LiangsLi starred deepseek-ai/awesome-deepseek-agent
2026-05-12 15:25:57 | 🔀 mdziedzic-jetbrains opened PR in agentclientprotocol/registry
2026-05-12 15:22:31 | 🍴 cxt888 forked deepseek-ai/DeepSeek-R1
2026-05-12 15:22:09 | 🚀 teorth pushed to leanprover-community/mathlib-at-ICERM26 (no commit info)
2026-05-12 15:21:49 | ⭐️ cxt888 starred deepseek-ai/DeepSeek-R1
2026-05-12 15:21:22 | ⭐️ Viyyy starred deepseek-ai/awesome-deepseek-agent
2026-05-12 15:18:39 | 🚀 teorth pushed to leanprover-community/mathlib-at-ICERM26 (no commit info)
2026-05-12 15:18:35 | ⭐️ wzy-study starred deepseek-ai/DeepSeek-V3
2026-05-12 15:18:12 | ⭐️ zhjurz starred deepseek-ai/3FS
2026-05-12 15:17:35 | ⭐️ yuewucl starred deepseek-ai/awesome-deepseek-agent
2026-05-12 15:16:19 | 🔹 sdvillal performed IssueCommentEvent on aqlaboratory/openfold-3
2026-05-12 15:06:36 | 🚀 teorth pushed to leanprover-community/mathlib-at-ICERM26 (no commit info)
2026-05-12 15:03:06 | 🚀 teorth pushed to leanprover-community/mathlib-at-ICERM26 (no commit info)
2026-05-12 15:01:44 | ⭐️ mlkgrnt starred deepseek-ai/awesome-deepseek-agent
2026-05-12 14:57:35 | 🍴 wrrgit forked deepseek-ai/awesome-deepseek-agent
2026-05-12 14:53:47 | ⭐️ kunalsinghdadhwal starred agentclientprotocol/agent-client-protocol
2026-05-12 14:49:24 | ⭐️ abluefan starred deepseek-ai/awesome-deepseek-agent
2026-05-12 14:47:24 | ⭐️ lithuak starred deepseek-ai/DeepEP
2026-05-12 14:44:10 | 🚀 teorth pushed to leanprover-community/mathlib-at-ICERM26 (no commit info)
2026-05-12 14:38:46 | 🚀 teorth pushed to leanprover-community/mathlib-at-ICERM26 (no commit info)
2026-05-12 14:38:08 | ⭐️ elias-mthreads starred deepseek-ai/awesome-deepseek-agent
2026-05-12 14:37:45 | ⭐️ Taiowaz starred deepseek-ai/awesome-deepseek-agent
2026-05-12 14:37:43 | ⭐️ BeeChat starred deepseek-ai/awesome-deepseek-agent
2026-05-12 14:31:56 | ⭐️ spring-quan starred deepseek-ai/DeepSeek-VL2
```

### 2. Scraper 模块 / Scraper Module (`scrape`)

**功能概述 / Functionality**
- `scrape_repository(repo_name, output_file="Context.md")` 会使用 `gh repo view` 获取仓库的描述/README（通过 `gh` CLI），并进行一次浅克隆（`git clone --depth 1`）用于生成仓库的目录结构（ASCII tree），最终把这些内容合并写入一个 Markdown 文件。

**实现细节 / Implementation details**
- 入口函数: `ghresearcher/ghresearcher/scraper.py::scrape_repository`。
- 步骤:
   1. 调用 `get_repo_view(repo_name)`，内部使用 `run_gh_command(["repo", "view", repo_name], capture_output=True)` 获取 `gh repo view` 的文本输出（未使用 `--json` 取得结构化数据）。
   2. 在临时目录中执行 `git clone --depth 1 https://github.com/{repo_name}.git`，然后用 `generate_tree()` 遍历仓库顶层生成简单的 ASCII 目录树（忽略 `.git`, `__pycache__` 等预设目录）。
   3. 将 repo view、分隔符、以及目录树写入到用户指定的 `output_file`（默认 `Context.md`）。

**参数与可配置项**
- `repo_name` (必需): 仓库标识，格式 `owner/repo`。
- `output_file` (可选): 输出 Markdown 文件路径。默认 `Context.md`。
- `ignore_dirs` (内部可配置): `generate_tree` 支持可传入忽略目录集合，当前默认过滤 `('.git','build','vendor','__pycache__','node_modules')`。

**硬限制与风险 / Hard limits & Risks**
- 当前实现依赖本机可用的 `git` 与 `gh` CLI；在无 `gh` 或无网络环境下会失败并写入错误信息。
- 使用 `git clone --depth 1` 做浅克隆：节省带宽与时间，但不能读取仓库的历史（例如无法列出所有分支/历史文件状态）。这是设计决策以优先速度与低成本。
- 对于非常大的仓库（上万文件），`generate_tree` 在内存中构建完整树可能显著占用时间和内存；目前没有递归深度或文件数上限保护。
- `get_repo_view` 使用的是 `gh repo view` 的纯文本输出（未请求 JSON 字段），因此 README 与描述的结构化提取有限，解析能力依赖 `gh` 的输出格式。

**可扩展性建议 / Extensibility**
- 支持结构化 `gh repo view --json name,description,readme`：替换文本解析为 JSON，使 README 与描述更可靠地提取并可选插入 README 的原始 Markdown 内容。
- 可选参数 `--depth` 或 `--no-clone`：允许用户选择是否克隆仓库、克隆深度，或仅使用 `gh` 返回的 README/description 来生成上下文。
- 添加目录树截断/分页与最大深度限制（如 `--max-depth`, `--max-entries`），以保护在超大仓库上的资源消耗。
- 将 `generate_tree` 输出改为带文件大小/类型的结构化表格，或导出为 JSON，以便后续工具自动化处理。

**实用建议**
- 若目标只是快速获取 README/项目描述，推荐使用 `scrape_repository(repo, output_file)` 的 `--no-clone`（可扩展实现）或直接调用 `gh repo view --json`，避开克隆开销。
- 对于需要深入分析代码（比如查找特定文件、依赖、或统计），应在浅克隆后再用更专门的分析脚本（避免一次性在 `scrape` 中承担过多职责）。
