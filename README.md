# GhResearcher 🔬

[En](README.md) | [中文](README_zh.md)

A powerful GitHub Code & Repo Analysis CLI for Researchers, designed to track activities, scrape repository contexts, and search intelligently—**without leaving YOUR terminal**.

---

## 📖 Introduction

**GhResearcher** is a terminal-based toolkit built for researchers, developers, and tech enthusiasts who need to keep a close eye on the open-source ecosystem. Instead of navigating through web interfaces, GhResearcher leverages the GitHub REST API and GitHub CLI (`gh`) to bring timelines, repository structures, and multi-domain searches directly to your command line. 

Whether you want to track a specific expert's "feed", monitor the activities of a lab/organization, or quickly dump a repository's structure into an LLM-friendly context file, GhResearcher provides the necessary utilities in a clean, terminal-native format powered by `Rich` and `Typer`.

## 🧠 Design Philosophy

- **Curing "Free-Range" Research:** Many researchers and grad students (especially in computational fields) feel isolated without daily guidance. This tool acts as your academic "social feed" for code. By tracking what experts and labs are actively working on, it keeps you involved, gives you clear targets, and ensures you stay motivated and closely aligned with mainstream developments.
- **Terminal First:** Keep you in the flow. No context switching to a web browser.
- **Data Density:** Present maximum information with minimal clutter. Long commit hashes are truncated; pagination is handled automatically.
- **LLM-Friendly:** Commands like `scrape` are explicitly designed to generate `.md` files that can be directly fed into Language Models for code analysis and project understanding.
- **Privacy & Security:** Relies entirely on your local `gh` authentication. No third-party servers, no telemetry.

---

## ✨ Features

- **Dynamic Tracking (`monitor`)**: 
  - Track events from Users, Organizations (`--org`), or specific Repositories (`--repo`).
  - Read a user's GitHub Feed (`--received`) to see what experts are paying attention to.
  - Seamless pagination handling to bypass standard API constraints.
- **Repository Scraper (`scrape`)**:
  - Automatically clone (shallow) and generate a Markdown file containing the project's README, description, and an ASCII directory tree.
- **Multi-domain Search (`search`)**:
  - Quickly search across repos, code, issues, and pull requests.

---

## ⚙️ Installation

### Prerequisites
1. **Python 3.8+**
2. **GitHub CLI (`gh`)**: You must have the [GitHub CLI](https://github.com/cli/cli) installed and authenticated.
   ```bash
   # 1. Install gh (Ubuntu/Debian example)
   # follow https://github.com/cli/cli/blob/trunk/docs/install_linux.md#debian
   (type -p wget >/dev/null || (sudo apt update && sudo apt install wget -y)) \
	&& sudo mkdir -p -m 755 /etc/apt/keyrings \
	&& out=$(mktemp) && wget -nv -O$out https://cli.github.com/packages/githubcli-archive-keyring.gpg \
	&& cat $out | sudo tee /etc/apt/keyrings/githubcli-archive-keyring.gpg > /dev/null \
	&& sudo chmod go+r /etc/apt/keyrings/githubcli-archive-keyring.gpg \
	&& sudo mkdir -p -m 755 /etc/apt/sources.list.d \
	&& echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/githubcli-archive-keyring.gpg] https://cli.github.com/packages stable main" | sudo tee /etc/apt/sources.list.d/github-cli.list > /dev/null \
	&& sudo apt update \
	&& sudo apt install gh -y



   # 2. Authenticate with your GitHub account
   gh auth login
   ```

### Install GhResearcher
Clone the repository and install it via `pip`:
```bash
git clone https://github.com/MaybeBio/GhResearcher.git
cd GhResearcher
pip install -e .
```
Verify the installation:
```bash
ghresearcher --help
```

---

## 🚀 Usage Guide

### 1. Monitoring Activities (`monitor`)

The `monitor` command provides a unified chronological timeline of GitHub activities.

**Usage:** `ghresearcher monitor [OPTIONS] [TARGET]`

#### Monitor a Single User
Track the public actions of a specific developer (e.g., pushes, stars, forks).
```bash
ghresearcher monitor MaybeBio -l 5
```

what you get is:
```python
Fetching events for target(s): MaybeBio...

2026-05-12 23:12:28 | ⭐️ MaybeBio starred alchaincyf/huashu-design
2026-05-12 20:07:14 | 🚀 MaybeBio pushed to MaybeBio/GhResearcher (no commit info)
2026-05-12 19:10:24 | 🚀 MaybeBio pushed to MaybeBio/bioinfor_script_modules (no commit info)
2026-05-12 19:02:18 | 🚀 MaybeBio pushed to MaybeBio/GhResearcher (no commit info)
2026-05-12 18:59:39 | 🆕 MaybeBio created branch 'main' at MaybeBio/GhResearcher
```


#### Monitor an Organization (`--org`)
Track the collective public events of an entire organization or lab. This is highly useful for following research groups' release updates or code pushes.
```bash
ghresearcher monitor GENTEL-lab --org
```
what you get is
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

#### Monitor a specific Repository (`--repo`)
Focus cleanly on the event stream of a single repository (e.g., releases, issues, PRs, stars).
```bash
ghresearcher monitor isblab/disobind --repo -l 20
```

what you get is
```python
Fetching events for target(s): isblab/disobind...

2026-05-01 18:18:10 | ⭐️ Raghav0573 starred isblab/disobind
2026-04-29 16:40:05 | 🍴 ipcamit forked isblab/disobind
2026-04-23 13:41:51 | 🍴 paolellopotanovic-ctrlxiaoke forked isblab/disobind
```

#### Monitor a User's Feed (`--received`)
Discover new tools by looking at what an expert is watching. This fetches the "received events" feed (similar to the GitHub homepage feed).
```bash
ghresearcher monitor teorth --received
```
what you get is

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


#### Batch Monitoring
Pass a text file with multiple targets (one per line) to merge their activities into a single global timeline.
```bash
ghresearcher monitor -f experts.txt --since 2026-05-01 --until 2026-05-12
```

#### Expanded Commits
By default, long pushes are truncated. Use `--expand-commits` to fetch detailed commit messages via additional API calls.
```bash
ghresearcher monitor teorth --expand-commits
```

---

### 2. Scraping Repository Context (`scrape`)

Dumps a repository's metadata, README, and directory tree into a single `Context.md` file, perfect for sharing context with ChatGPT or Claude.

**Usage:** `ghresearcher scrape [REPO]`

```bash
ghresearcher scrape isblab/disobind -o Disobind_Context.md
```
*Note: This performs a shallow clone (`git clone --depth 1`) in a temporary directory to generate the tree efficiently.*

---

### 3. Searching GitHub (`search`)

Perform tailored searches from the terminal.

**Usage:** `ghresearcher search [item_type] [query]`

```bash
# Search for repositories related to "Deep Learning"
ghresearcher search repos "Deep Learning" -L Python -l 10
```

---

## ⚠️ Limits & Caveats

- **GitHub API Limits:** The `monitor` timeline is restricted to a maximum of 300 recent events or events within the past 90 days due to GitHub API constraints.
- **Scraper Size:** The `scrape` command currently builds the tree in memory and clones the repository. Extremely massive repositories (10,000+ files) may take longer or consume significant memory.
- **Rate Limiting:** Heavy use of `--expand-commits` or batch mapping large lists may quickly consume your GitHub API rate limit. Use with care.
