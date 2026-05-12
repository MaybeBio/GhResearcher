# GhResearcher 🔬

专为科研人员、开发者与技术爱好者打造的 GitHub 代码与仓库分析终端工具（CLI）。让你**无需离开终端（Terminal）**，即可追踪学术大牛动态、抓取仓库上下文文件、并进行高级搜索。

---

## 📖 简介 / Introduction

**GhResearcher** 是一个极简而强大的终端工具集。它基于 GitHub REST API 和 GitHub CLI (`gh`) 开发，旨在将 GitHub 的海量信息流、仓库结构以及代码搜索带入命令行中。

无论你是想追踪某位领域专家的“朋友圈”、监控某个实验室（组织）的代码产出，还是想快速将一个庞大仓库的结构导出为供大语言模型（LLM）阅读的上下文 Markdown 文件，GhResearcher 都能通过 `Rich` 和 `Typer` 提供优美、直观且高效的终端交互体验。

## 🧠 设计哲学 / Design Philosophy

- **告别“放养”状态 (Curing Free-Range Research):** 很多研究生（特别是计算方向）常处于“放养”状态，缺乏日常指导。GhResearcher 让你像刷推特、刷“代码朋友圈”一样，时刻追踪领域内学者和大牛们的最新动向。它不仅能为你提供极佳的参考和目标，让你在科研和写代码时更有干劲，更能让你保持极强的学术参与感，确保你的精力始终跟紧主流前沿而不偏离方向。
- **终端优先 (Terminal First):** 保持心流，无需频繁切换回浏览器。
- **高信息密度 (Data Density):** 紧凑输出。长哈希值自动截断，分页无缝处理，过滤冗余信息。
- **AI 友好 (LLM-Friendly):** 诸如 `scrape` 命令，专为生成供 ChatGPT/Claude 阅读的 `.md` 上下文文件而设计。
- **隐私与安全 (Privacy & Security):** 完全依赖你本地的 `gh` CLI 凭证，无需第三方代理，不收集任何使用数据。

---

## ✨ 核心特性 / Features

- **动态追踪 (`monitor`)**: 
  - 支持追踪指定 用户 (User)、组织 (`--org`) 或特定仓库 (`--repo`) 的动态事件。
  - 支持“信息流”追踪 (`--received`)：看看大牛关注的人和仓库最近在干什么。
  - 自动处理分页，突破单次 API 拉取上限，并能对 PR/Issue/Release 生成富文本标题。
- **仓库上下文抓取 (`scrape`)**:
  - 自动浅克隆仓库并生成一个包含项目 README、描述及全景 ASCII 目录树的 Markdown 文件。
- **多领域搜索 (`search`)**:
  - 支持在终端内直接检索仓库、代码片段、Issue 以及 Pull Request。

---

## ⚙️ 安装说明 / Installation

### 环境依赖
1. **Python 3.8+**
2. **GitHub CLI (`gh`)**: 必须在本地安装 [gh](https://github.com/cli/cli) 命令行工具，并完成账号授权。
   ```bash
   # 1. 安装 gh (以 Ubuntu/Debian 为例)
   # 参考: https://github.com/cli/cli/blob/trunk/docs/install_linux.md#debian
   (type -p wget >/dev/null || (sudo apt update && sudo apt install wget -y)) \
	&& sudo mkdir -p -m 755 /etc/apt/keyrings \
	&& out=$(mktemp) && wget -nv -O$out https://cli.github.com/packages/githubcli-archive-keyring.gpg \
	&& cat $out | sudo tee /etc/apt/keyrings/githubcli-archive-keyring.gpg > /dev/null \
	&& sudo chmod go+r /etc/apt/keyrings/githubcli-archive-keyring.gpg \
	&& sudo mkdir -p -m 755 /etc/apt/sources.list.d \
	&& echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/githubcli-archive-keyring.gpg] https://cli.github.com/packages stable main" | sudo tee /etc/apt/sources.list.d/github-cli.list > /dev/null \
	&& sudo apt update \
	&& sudo apt install gh -y

   # 2. 登录并授权你的 GitHub 账号
   gh auth login
   ```

### 安装 GhResearcher
克隆此仓库并使用 `pip` 进行本地安装：
```bash
git clone https://github.com/MaybeBio/GhResearcher.git
cd GhResearcher
pip install -e .
```
验证安装是否成功：
```bash
ghresearcher --help
```

---

## 🚀 使用指南 / Usage Guide

### 1. 动态监控 (`monitor`)

`monitor` 命令提供了一个统一的 GitHub 动态时间轴，就像浏览代码的朋友圈一样。

**语法:** `ghresearcher monitor [选项] [目标]`

#### 监控单个用户
追踪特定开发者的公开行为（例如：推送代码、Star 仓库、Fork 等）。
```bash
ghresearcher monitor MaybeBio -l 5
```

执行后你将看到类似如下的输出（What you get is）：
```python
Fetching events for target(s): MaybeBio...

2026-05-12 23:12:28 | ⭐️ MaybeBio starred alchaincyf/huashu-design
2026-05-12 20:07:14 | 🚀 MaybeBio pushed to MaybeBio/GhResearcher (no commit info)
2026-05-12 19:10:24 | 🚀 MaybeBio pushed to MaybeBio/bioinfor_script_modules (no commit info)
2026-05-12 19:02:18 | 🚀 MaybeBio pushed to MaybeBio/GhResearcher (no commit info)
2026-05-12 18:59:39 | 🆕 MaybeBio created branch 'main' at MaybeBio/GhResearcher
```

#### 监控组织 / 实验室 (`--org`)
将目标解释为组织（Organization）。非常适合用于跟踪某个大学实验室或开源团队的整体产出动态（Release 追踪、大规模 Push）。
```bash
ghresearcher monitor GENTEL-lab --org
```

执行后你将看到类似如下的输出（What you get is）：
```python 
Fetching events for target(s): GENTEL-lab...

2026-05-12 01:33:27 | ⭐️ justiniao starred GENTEL-lab/EVA
2026-05-11 10:59:50 | ⭐️ linjing-lab starred GENTEL-lab/VCWorld
2026-05-10 16:57:58 | ⭐️ NoahQue starred GENTEL-lab/VCWorld
2026-05-10 16:27:29 | ⭐️ Stern-612 starred GENTEL-lab/EnzymeCAGE
2026-05-09 21:31:27 | ⭐️ homandp starred GENTEL-lab/EVA
2026-05-09 15:54:25 | ⭐️ evacia starred GENTEL-lab/EVA
2026-05-09 08:40:08 | ⭐️ 7psusanpruitt40 starred GENTEL-lab/EVA
2026-05-09 00:21:22 | ⭐️ ardonw20 starred GENTEL-lab/EVA
2026-05-08 20:00:48 | ⭐️ CourageSiame starred GENTEL-lab/VCWorld
2026-05-08 16:44:58 | ⭐️ Aspectin starred GENTEL-lab/EnzymeCAGE
2026-05-08 08:24:37 | ⭐️ danserjeunjoline starred GENTEL-lab/EVA
2026-05-08 07:54:05 | ⭐️ inoue0426 starred GENTEL-lab/VCWorld
2026-05-08 07:11:21 | ⭐️ jpetchez starred GENTEL-lab/EVA
2026-05-08 06:25:01 | ⭐️ sb8587-a starred GENTEL-lab/EVA
2026-05-08 04:56:58 | ⭐️ evakagmadrit starred GENTEL-lab/EVA
2026-05-08 00:22:04 | ⭐️ Namkyeong starred GENTEL-lab/VCWorld
2026-05-07 21:13:59 | ⭐️ alexdebelka starred GENTEL-lab/VCWorld
2026-05-07 15:10:20 | 🐛 liwenqi-BGI opened issue in GENTEL-lab/EnzymeCAGE: 'FileNotFound'
2026-05-07 11:17:52 | 🍴 yishutu forked GENTEL-lab/GerNA-Bind
2026-05-06 14:46:47 | ⭐️ yifanfeng97 starred GENTEL-lab/EnzymeCAGE
2026-05-06 12:30:08 | ⭐️ bbyun28 starred GENTEL-lab/OriGene
2026-05-05 16:44:04 | ⭐️ heidban starred GENTEL-lab/EVA
2026-05-05 15:15:19 | ⭐️ FengxuSysbio starred GENTEL-lab/VCWorld
2026-05-05 15:06:26 | ⭐️ dingrenjie12 starred GENTEL-lab/EVA
2026-05-05 03:37:59 | ⭐️ stottlemartinsth starred GENTEL-lab/EVA
2026-05-05 02:58:17 | ⭐️ WaveoffBioMed starred GENTEL-lab/OriGene
2026-05-04 10:42:04 | ⭐️ shayeedew44d starred GENTEL-lab/EVA
2026-05-02 20:01:46 | ⭐️ ron5428-blantonl starred GENTEL-lab/EVA
2026-05-02 18:47:23 | ⭐️ william2014-jw starred GENTEL-lab/EVA
2026-05-02 18:09:32 | ⭐️ 81davejohnson80 starred GENTEL-lab/EVA
```

#### 监控特定仓库 (`--repo`)
仅专注于某个单一仓库的事件流。这可以帮助你密切关注自己或他人重点项目的 Issue 变动、PR 提交和 Release 发布。
```bash
ghresearcher monitor isblab/disobind --repo -l 20
```

执行后你将看到类似如下的输出（What you get is）：
```python
Fetching events for target(s): isblab/disobind...

2026-05-01 18:18:10 | ⭐️ Raghav0573 starred isblab/disobind
2026-04-29 16:40:05 | 🍴 ipcamit forked isblab/disobind
2026-04-23 13:41:51 | 🍴 paolellopotanovic-ctrlxiaoke forked isblab/disobind
```



#### 窥探大牛的视野 / 信息流 (`--received`)
不看他做了什么，而是看他关注了什么。获取该用户的“接收事件”，相当于查看他的 GitHub 主页信息流。这是发现前沿好工具的绝佳途径。
```bash
ghresearcher monitor teorth --received
```
执行后你将看到类似如下的输出（What you get is）：

```python
Fetching events for target(s): teorth...

2026-05-12 21:48:31 | 🍴 benediktjohannes forked teorth/estimates
2026-05-12 21:48:20 | 🍴 benediktjohannes forked teorth/equational_theories
2026-05-12 21:22:02 | 🍴 benediktjohannes forked AlexKontorovich/PrimeNumberTheoremAnd
2026-05-12 20:36:01 | 🔀 Milian0402 opened PR in teorth/erdos-guy-selfridge
2026-05-12 20:14:06 | ⭐️ jonahinthewhale starred AlexKontorovich/PrimeNumberTheoremAnd
2026-05-12 14:35:22 | 🍴 nachose forked teorth/erdos-guy-selfridge
2026-05-12 12:04:37 | 🔹 teorth performed GollumEvent on AlexKontorovich/PrimeNumberTheoremAnd
2026-05-12 12:00:33 | 🚀 teorth pushed to AlexKontorovich/PrimeNumberTheoremAnd (no commit info)
2026-05-12 12:00:33 | 🐛 teorth closed issue in AlexKontorovich/PrimeNumberTheoremAnd: '[CH2]: Limiting integral formula for smoothly 
truncated Dirichlet series (Proposition 2.3)'
2026-05-12 12:00:31 | 🔀 anhhuyalex merged PR in AlexKontorovich/PrimeNumberTheoremAnd
2026-05-12 12:00:26 | 🔹 teorth performed PullRequestReviewEvent on AlexKontorovich/PrimeNumberTheoremAnd
2026-05-12 11:59:56 | 🔹 teorth performed GollumEvent on AlexKontorovich/PrimeNumberTheoremAnd
2026-05-12 11:40:39 | 🐛 github-actions assigned issue in AlexKontorovich/PrimeNumberTheoremAnd: '[BKLNW]: Uniform medium size bound on 
theta (Corollary 8.1b)'
2026-05-12 11:40:23 | 💬 Yu-Misaka created issue '[BKLNW]: Uniform medium size bound on theta (Corollary 8.1b)' in 
AlexKontorovich/PrimeNumberTheoremAnd
2026-05-12 09:17:18 | 🐛 github-actions assigned issue in AlexKontorovich/PrimeNumberTheoremAnd: '[CH2]: Limiting integral formula for 
smoothly truncated Dirichlet series (Proposition 2.3)'
2026-05-12 09:17:14 | 💬 anhhuyalex created issue '[CH2]: Limiting integral formula for smoothly truncated Dirichlet series (Proposition 
2.3)' in AlexKontorovich/PrimeNumberTheoremAnd
2026-05-12 09:17:10 | 💬 anhhuyalex created issue '[CH2]: Limiting integral formula for smoothly truncated Dirichlet series (Proposition 
2.3)' in AlexKontorovich/PrimeNumberTheoremAnd
2026-05-12 09:15:31 | 🔀 anhhuyalex opened PR in AlexKontorovich/PrimeNumberTheoremAnd
2026-05-12 09:10:35 | 🐛 github-actions assigned issue in AlexKontorovich/PrimeNumberTheoremAnd: '[FKS2]: Converting bounds for theta into
bounds for pi (Theorem 6)'
2026-05-12 09:10:24 | 💬 Osalotioman created issue '[FKS2]: Converting bounds for theta into bounds for pi (Theorem 6)' in 
AlexKontorovich/PrimeNumberTheoremAnd
2026-05-12 08:45:29 | 🐛 teorth closed issue in AlexKontorovich/PrimeNumberTheoremAnd: '[FKS2]: Matching lower bound on E_π (Theorem 6, 
substep 2), cowritten with Grok'
2026-05-12 08:44:44 | 🚀 teorth pushed to AlexKontorovich/PrimeNumberTheoremAnd (no commit info)
2026-05-12 08:44:44 | 🐛 teorth closed issue in AlexKontorovich/PrimeNumberTheoremAnd: '[FKS2]: Upper bound on E_pi (Theorem 6, substep 
1)'
2026-05-12 08:44:43 | 🔀 Osalotioman merged PR in AlexKontorovich/PrimeNumberTheoremAnd
2026-05-12 08:44:38 | 🔹 teorth performed PullRequestReviewEvent on AlexKontorovich/PrimeNumberTheoremAnd
2026-05-12 06:11:25 | 🐛 illdreamt opened issue in AlexKontorovich/PrimeNumberTheoremAnd: '[FKS2]: Matching lower bound on E_π (Theorem 6,
substep 2), cowritten with Grok'
2026-05-12 03:10:59 | ⭐️ orfyus starred teorth/symmetric_project
2026-05-12 02:14:48 | 🔀 Milian0402 opened PR in teorth/erdos-guy-selfridge
2026-05-12 00:31:13 | ⭐️ orfyus starred AlexKontorovich/PrimeNumberTheoremAnd
2026-05-12 00:00:59 | 💬 Osalotioman created issue '[FKS2]: Upper bound on E_pi (Theorem 6, substep 1)' in 
AlexKontorovich/PrimeNumberTheoremAnd
```

#### 批量订阅监控
针对一个写满用户名的纯文本文件（每行一个目标），GhResearcher 会并发抓取所有人动态，并按时间戳降序融合成一个全局时间线。
```bash
ghresearcher monitor -f experts.txt --since 2026-05-01 --until 2026-05-12
```

#### 详尽的 Commit 展示 (`--expand-commits`)
默认情况下，冗长的 `PushEvent` 只显示精简信息。如果你想额外发起 API 请求去获取详细的 Commit message，可以开启此选项。
```bash
ghresearcher monitor teorth --expand-commits
```

---

### 2. 抓取仓库上下文 (`scrape`)

将目标仓库的基础元数据、README 以及完整目录树打包成单个 `Context.md` 文件。遇到大型代码库无从下手时，把这个文件直接扔给 LLM 帮你梳理架构。

**语法:** `ghresearcher scrape [REPO]`

```bash
ghresearcher scrape isblab/disobind -o Disobind_Context.md
```
*注：此命令会在系统临时目录执行浅克隆 (`git clone --depth 1`) 以提高目录树生成效率，不会拉取历史冗余数据。*

---

### 3. 多维度搜索 (`search`)

在终端内发起高度定制化的检索。

**语法:** `ghresearcher search [搜索类型] [关键词]`

```bash
# 搜索和 "Deep Learning" 相关的 Python 仓库，最多返回 10 条
ghresearcher search repos "Deep Learning" -L Python -l 10
```

---

## ⚠️ 注意事项与限制 / Limits & Caveats

- **GitHub 原生 API 限制:** 无论是普通用户、组织还是仓库的 Events 接口，受 GitHub 官方限制，最多只能追溯最近 90 天内或最近的 300 条动态。
- **克隆与解析开销 (`scrape`):** 面对拥有数万个文件（如超级巨石型仓库）的项目，在内存中构建 ASCII 目录树会占用一定的时间和资源。
- **速率限制 (Rate Limit):** 频繁开启 `--expand-commits` 进行海量并发查询，或极高频率地调用搜索接口，可能导致你的 GitHub CLI 授权触发访问速率限制。请根据实际需求合理设定抓取极限 (`-l`) 与起止日期 (`--since` / `--until`)。