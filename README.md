# GhResearcher 🔬

[En](README.md) | [中文](README_zh.md)

A powerful GitHub Code & Repo Analysis CLI for Researchers, designed to track activities, scrape and parse repository contexts, and search intelligently—**without leaving YOUR terminal**.

---
 
## Table of Contents

- [GhResearcher 🔬](#ghresearcher-)
  - [Table of Contents](#table-of-contents)
  - [📖 Introduction](#-introduction)
  - [🧠 Design Philosophy](#-design-philosophy)
  - [✨ Features](#-features)
  - [⚙️ Installation](#️-installation)
    - [Prerequisites](#prerequisites)
    - [Install GhResearcher](#install-ghresearcher)
  - [🚀 Usage Guide](#-usage-guide)
    - [1. Monitoring Activities (`monitor`)](#1-monitoring-activities-monitor)
      - [Monitor a Single User](#monitor-a-single-user)
      - [Monitor an Organization (`--org`)](#monitor-an-organization---org)
      - [Monitor a specific Repository (`--repo`)](#monitor-a-specific-repository---repo)
      - [Monitor a User's Feed (`--received`)](#monitor-a-users-feed---received)
      - [Batch Monitoring](#batch-monitoring)
      - [Expanded Commits](#expanded-commits)
    - [2. Parsing Repository Context (`parse`)](#2-parsing-repository-context-parse)
    - [3. Searching GitHub (`search`)](#3-searching-github-search)
  - [Advanced Search Syntax (GitHub)](#advanced-search-syntax-github)
  - [⚠️ Limits \& Caveats](#️-limits--caveats)


## 📖 Introduction

**GhResearcher** is a terminal-based toolkit built for researchers, developers, and tech enthusiasts who need to keep a close eye on the open-source ecosystem. Instead of navigating through web interfaces, GhResearcher leverages the GitHub REST API and GitHub CLI (`gh`) to bring timelines, repository structures, and multi-domain searches directly to your command line. 

Whether you want to track a specific expert's "feed", monitor the activities of a lab/organization, or quickly dump a repository's structure into an LLM-friendly context file, GhResearcher provides the necessary utilities in a clean, terminal-native format powered by `Rich` and `Typer`.

## 🧠 Design Philosophy

- **Curing "Free-Range" Research:** Many researchers and grad students (especially in computational fields) feel isolated without daily guidance. This tool acts as your academic "social feed" for code. By tracking what experts and labs are actively working on, it keeps you involved, gives you clear targets, and ensures you stay motivated and closely aligned with mainstream developments.
- **Terminal First:** Keep you in the flow. No context switching to a web browser.
- **Data Density:** Present maximum information with minimal clutter. Long commit hashes are truncated; pagination is handled automatically.
- **LLM-Friendly:** Commands like `parse` are explicitly designed to generate `.md` files that can be directly fed into Language Models for code analysis and project understanding.
- **Privacy & Security:** Relies entirely on your local `gh` authentication. No third-party servers, no telemetry.

---

## ✨ Features

- **Dynamic Tracking (`monitor`)**: 
    - Track events from Users, Organizations (`--org`), or specific Repositories (`--repo`).
    - Read a user's GitHub Feed (`--received`) to see what experts are paying attention to.
    - Seamless pagination handling to bypass standard API constraints.
- **Repository Parser (`parse`)**:
    - Default mode exports README + repository tree into a Markdown file(similar to tree command).
    - `--view` opens a pager instead of writing files.
    - `--view-mode readme` uses `gh repo view` directly for README-only paging.
    - `--view-mode tree` shows only the repository tree.
    - `--source` lists saved `Agent Parser(like DeepWiki OR some GitHub LLM-based parsers)` source URLs for the repository.
    - `--sources-file <file>` loads extra or overridden saved `Agent Parser` source URLs from JSON.
    - Single-file targets like `owner/repo/path/to/file` fetch file contents directly without cloning.
    - Supports `direct download of file content` in addition to paginated viewing.
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

Three important commands daily for me:
```python
# you can change the target file to your own file

# yesterday to today activities of my followed experts
ghresearcher monitor -f /data2/GhResearcher/tests/target_user.txt --since $(date -d "1 day ago" +%Y-%m-%d) --expand-commits

```

**Usage:** `ghresearcher monitor [OPTIONS] [TARGET]`

```python
❯ ghresearcher monitor --help
                                                                                                                                                                  
 Usage: ghresearcher monitor [OPTIONS] [TARGET_NAME]                                                                                                              
                                                                                                                                                                  
 Track and view the recent events of specific GitHub user(s), organization(s), or repos. Supports single target directly or batch targets via file. Events from   
 multiple targets are combined into a global chronological timeline.                                                                                              
                                                                                                                                                                  
╭─ Arguments ────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│   target_name      [TARGET_NAME]  The GitHub user, org, or repo to monitor                                                                                     │
╰────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─ Options ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ --file            -f      TEXT     File containing GitHub targets (one per line)                                                                               │
│ --received        -r               Fetch feed instead of user's own events                                                                                     │
│ --org             -O               Treat target as an Organization instead of a User                                                                           │
│ --repo            -R               Treat target as a Repository (owner/repo format)                                                                            │
│ --limit           -l      INTEGER  Number of events to fetch per target [default: 30]                                                                          │
│ --since                   TEXT     Filter events on or after this date (YYYY-MM-DD)                                                                            │
│ --until                   TEXT     Filter events on or before this date (YYYY-MM-DD)                                                                           │
│ --expand-commits                   Make additional API calls to get commit details for PushEvents if missing                                                   │
│ --help                             Show this message and exit.                                                                                                 │
╰────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
```


#### Monitor a Single User
Track the public actions of a specific developer (e.g., pushes, stars, forks).
```bash
# Monitor my activities (single user)
ghresearcher monitor MaybeBio -l 5

# Monitor multiple users (file input)
ghresearcher monitor -f users_to_track.txt 
# ghresearcher monitor -f ./tests/target_user.txt --since 2026-05-11 --expand-commits
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

if multiple, you get is
```python
Fetching events for target(s): alexholehouse, Junjie-Zhu, HFChenLab, sirius777coder, Zuricho, Immortals-33, lujiarui, ChenDdon, AspirinCode, bjing2016, tyang816, prokia, Gonglab-THU...

2026-05-13 08:50:23 | ⭐️ prokia starred yliust/Tactile
2026-05-13 03:04:54 | ⭐️ Zuricho starred jsdoc/jsdoc
2026-05-12 23:14:59 | 🚀 AspirinCode pushed to AspirinCode/awesome-AI4MolConformation-MD
    - [cc88d0d] (expanded) Update README.md
2026-05-12 22:54:36 | 🚀 AspirinCode pushed to AspirinCode/papers-for-molecular-design-using-DL
    - [c062c62] (expanded) Update README.md
2026-05-12 20:29:29 | ⭐️ sirius777coder starred aqlaboratory/genie3
2026-05-12 20:01:38 | ⭐️ Immortals-33 starred obra/superpowers
2026-05-12 19:54:51 | ⭐️ Zuricho starred nicobailon/visual-explainer
2026-05-12 19:48:18 | ⭐️ Zuricho starred RomeroLab/BioDesignBench
2026-05-12 19:17:07 | 🔹 bjing2016 performed MemberEvent on MihirBafna/boltzgen
2026-05-12 19:08:38 | 🚀 AspirinCode pushed to AspirinCode/awesome-AI4MolConformation-MD
    - [042c4c9] (expanded) Update README.md
2026-05-12 18:54:19 | 🚀 AspirinCode pushed to AspirinCode/awesome-AI4MolConformation-MD
    - [6a0bac1] (expanded) Update README.md
2026-05-12 18:50:17 | 🚀 AspirinCode pushed to AspirinCode/awesome-AI4MolConformation-MD
    - [348fb9f] (expanded) Update README.md
2026-05-12 18:24:54 | ⭐️ AspirinCode starred HealthRex/PhysicianBench
2026-05-12 16:23:29 | ⭐️ Zuricho starred yliust/Tactile
2026-05-12 16:19:36 | ⭐️ Zuricho starred smiles724/Proteo-R1
2026-05-12 09:56:57 | ⭐️ AspirinCode starred yaochenr/LLM-TPD-Extraction
2026-05-12 00:07:44 | 💬 tyang816 created issue 'Trouble recreating zero shot results on protein gym' in ai4protein/VenusREM
2026-05-11 23:30:54 | ⭐️ AspirinCode starred Yuan1z0825/nature-skills
2026-05-11 18:08:37 | 💬 Junjie-Zhu created issue 'Availability of pretrained weights' in Vincentx15/atomsurf
2026-05-11 17:51:13 | ⭐️ Immortals-33 starred openai/plugins
```


#### Monitor an Organization (`--org`)
Track the collective public events of an entire organization or lab. This is highly useful for following research groups' release updates or code pushes.
```bash
# Monitor GENTEL-lab's activities (single organization)
ghresearcher monitor GENTEL-lab --org

# Monitor multiple organizations (file input)
ghresearcher monitor -f labs_to_track.txt --org
# ghresearcher monitor -f ./tests/target_org.txt --since 2026-05-11 
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

if multiple, you get is
```python
Fetching events for target(s): kiharalab, honig-lab, ai4protein, GENTEL-lab, steineggerlab, biomed-AI, BioComputingUP, ProteinDesignLab, sparks-lab-org, baker-laboratory, Graylab, isblab, THGLab, idptools, holehouse-lab, 
Pappulab, KULL-Centre...

2026-05-13 09:37:56 | 💬 jmcavanagh created issue 'Getting invalid SMILES string while trying tutorial in T4 Colab' in THGLab/SmileyLlama
2026-05-13 06:29:17 | 🚀 jmcavanagh pushed to THGLab/SmileyLlama (no commit info)
2026-05-13 06:29:16 | 🔀 GbAlteri merged PR in THGLab/SmileyLlama
2026-05-13 06:10:58 | 🏷️  AntiMatter568 published release v1.0.1 in kiharalab/DAQplugin
2026-05-13 06:10:42 | 🚀 AntiMatter568 pushed to kiharalab/DAQplugin (no commit info)
2026-05-13 04:42:31 | 💬 MichaelChungyoun created issue 'Intuition of calculating the ProGen2 likelihood of the reverse sequence' in Graylab/FLAb
2026-05-13 04:42:31 | 🐛 MichaelChungyoun closed issue in Graylab/FLAb: 'Intuition of calculating the ProGen2 likelihood of the reverse sequence'
2026-05-13 04:36:09 | 🐛 MichaelChungyoun closed issue in Graylab/FLAb: 'missing data in immunogenicity data folder'
2026-05-13 04:36:08 | 💬 MichaelChungyoun created issue 'missing data in immunogenicity data folder' in Graylab/FLAb
2026-05-13 04:23:23 | 🔹 AntiMatter568 performed DeleteEvent on kiharalab/DAQplugin
2026-05-13 04:21:16 | 🚀 AntiMatter568 pushed to kiharalab/DAQplugin (no commit info)
2026-05-13 04:16:46 | 🏷️  AntiMatter568 published release v1.0.0 in kiharalab/DAQplugin
2026-05-13 04:16:19 | 🚀 AntiMatter568 pushed to kiharalab/DAQplugin (no commit info)
2026-05-13 03:55:16 | 🍴 BankBro forked biomed-AI/DiffDec
2026-05-13 03:46:31 | 🐛 MichaelChungyoun closed issue in Graylab/FLAb: ''tm' folder is missing'
2026-05-13 03:46:30 | 💬 MichaelChungyoun created issue ''tm' folder is missing' in Graylab/FLAb
2026-05-13 03:44:29 | 🔹 MichaelChungyoun performed DeleteEvent on Graylab/FLAb
2026-05-13 03:44:08 | 🚀 MichaelChungyoun pushed to Graylab/FLAb (no commit info)
2026-05-13 03:43:59 | 🚀 MichaelChungyoun pushed to Graylab/FLAb (no commit info)
2026-05-13 03:33:53 | 🚀 MichaelChungyoun pushed to Graylab/FLAb (no commit info)
2026-05-13 03:33:44 | 🚀 MichaelChungyoun pushed to Graylab/FLAb (no commit info)
2026-05-13 03:30:45 | 🚀 MichaelChungyoun pushed to Graylab/FLAb (no commit info)
2026-05-13 03:30:06 | 🆕 MichaelChungyoun created branch 'flab2-dev' at Graylab/FLAb
2026-05-13 03:27:22 | 🔹 MichaelChungyoun performed DeleteEvent on Graylab/FLAb
2026-05-13 03:26:54 | 🔹 MichaelChungyoun performed DeleteEvent on Graylab/FLAb
2026-05-13 03:24:26 | 🚀 MichaelChungyoun pushed to Graylab/FLAb (no commit info)
2026-05-13 03:22:54 | 🚀 MichaelChungyoun pushed to Graylab/FLAb (no commit info)
2026-05-13 03:20:52 | 🚀 MichaelChungyoun pushed to Graylab/FLAb (no commit info)
2026-05-13 03:20:36 | 🚀 MichaelChungyoun pushed to Graylab/FLAb (no commit info)
2026-05-13 03:06:54 | 🐛 MichaelChungyoun closed issue in Graylab/FLAb: 'When is the article updated'
2026-05-13 03:06:51 | 💬 MichaelChungyoun created issue 'When is the article updated' in Graylab/FLAb
2026-05-13 02:59:37 | 🐛 MichaelChungyoun closed issue in Graylab/FLAb: 'Rosace et al. binding data are likely in M'
2026-05-13 02:59:35 | 💬 MichaelChungyoun created issue 'Rosace et al. binding data are likely in M' in Graylab/FLAb
2026-05-13 02:59:11 | 🚀 MichaelChungyoun pushed to Graylab/FLAb (no commit info)
2026-05-13 02:53:53 | 🚀 MichaelChungyoun pushed to Graylab/FLAb (no commit info)
2026-05-13 02:51:54 | 🚀 MichaelChungyoun pushed to Graylab/FLAb (no commit info)
2026-05-13 02:38:15 | 🐛 MichaelChungyoun closed issue in Graylab/FLAb: 'HCDR3s swapped with trastuzumab HCDR1 in Shanehsazzadeh zero-shot dataset'
2026-05-13 02:38:13 | 💬 MichaelChungyoun created issue 'HCDR3s swapped with trastuzumab HCDR1 in Shanehsazzadeh zero-shot dataset' in Graylab/FLAb
2026-05-13 02:30:27 | 🚀 MichaelChungyoun pushed to Graylab/FLAb (no commit info)
2026-05-13 02:25:12 | 🚀 MichaelChungyoun pushed to Graylab/FLAb (no commit info)
2026-05-13 01:28:10 | ⭐️ alanfwilliams starred baker-laboratory/RoseTTAFold-All-Atom
2026-05-13 01:05:12 | 🚀 zlr-zmm pushed to ai4protein/VenusFactory2 (no commit info)
2026-05-13 01:02:35 | 🚀 zlr-zmm pushed to ai4protein/VenusFactory2 (no commit info)
2026-05-13 01:02:33 | 🔀 Patiskey merged PR in ai4protein/VenusFactory2
2026-05-13 00:40:24 | ⭐️ DSamuelHodge starred ProteinDesignLab/dEVA
2026-05-12 22:46:44 | 🐛 sudhir2016 opened issue in THGLab/SmileyLlama: 'Getting invalid SMILES string while trying tutorial in T4 Colab'
2026-05-12 22:26:19 | ⭐️ qianyhpku starred biomed-AI/DRlinker
2026-05-12 20:27:13 | 🔀 sooyoung-cha opened PR in steineggerlab/foldseek
2026-05-12 20:25:13 | 🚀 sooyoung-cha pushed to steineggerlab/foldseek (no commit info)
2026-05-12 20:14:03 | 🚀 sooyoung-cha pushed to steineggerlab/foldseek (no commit info)
2026-05-12 20:14:01 | 🔀 sooyoung-cha merged PR in steineggerlab/foldseek
2026-05-12 20:13:46 | 🔀 sooyoung-cha opened PR in steineggerlab/foldseek
2026-05-12 18:54:09 | ⭐️ zmzhang starred THGLab/SmileyLlama
2026-05-12 17:03:15 | ⭐️ zhimingzhang275 starred ai4protein/VenusX
2026-05-12 15:16:35 | ⭐️ Abbbbyyyy starred ai4protein/Pro-Prime
2026-05-12 14:40:01 | ⭐️ DrDiscoDao starred THGLab/HiQBind
2026-05-12 12:58:09 | ⭐️ insilicoscientist starred baker-laboratory/RoseTTAFold-All-Atom
2026-05-12 11:39:18 | ⭐️ hajuchan starred steineggerlab/foldseek
2026-05-12 06:05:49 | ⭐️ lorcai starred steineggerlab/StrucTTY
2026-05-12 05:47:44 | 🚀 gterashi pushed to kiharalab/DAQplugin (no commit info)
2026-05-12 05:47:19 | 🚀 AntiMatter568 pushed to kiharalab/DAQplugin (no commit info)
2026-05-12 05:37:45 | 🚀 gterashi pushed to kiharalab/DAQplugin (no commit info)
2026-05-12 03:53:09 | 💬 dmoypal created issue 'Missing Alignment Visualizations in html Output' in steineggerlab/foldseek
2026-05-12 02:38:03 | 🚀 ryanemenecker pushed to idptools/goose (no commit info)
2026-05-12 02:35:14 | 🔀 Patiskey opened PR in ai4protein/VenusFactory2
2026-05-12 02:33:55 | 🚀 ryanemenecker pushed to idptools/goose (no commit info)
2026-05-12 02:31:48 | 🚀 ryanemenecker pushed to idptools/goose (no commit info)
2026-05-12 02:28:56 | 🚀 ryanemenecker pushed to idptools/goose (no commit info)
2026-05-12 02:27:42 | 🏷️  ryanemenecker published release v0.2.5.1 in idptools/goose
2026-05-12 02:14:56 | 🚀 ryanemenecker pushed to idptools/goose (no commit info)
2026-05-12 01:33:27 | ⭐️ justiniao starred GENTEL-lab/EVA
2026-05-12 00:56:26 | ⭐️ rujinlong starred steineggerlab/StrucTTY
2026-05-12 00:27:15 | ⭐️ damrane starred ProteinDesignLab/dEVA
2026-05-12 00:07:44 | 💬 tyang816 created issue 'Trouble recreating zero shot results on protein gym' in ai4protein/VenusREM
2026-05-11 23:36:06 | 🚀 adelbke pushed to BioComputingUP/nest-mongo-acl (no commit info)
2026-05-11 23:35:26 | 🚀 adelbke pushed to BioComputingUP/nest-mongo-acl (no commit info)
2026-05-11 23:01:28 | 🚀 LunaJang pushed to steineggerlab/StrucTTY (no commit info)
2026-05-11 18:42:35 | 🚀 LunaJang pushed to steineggerlab/StrucTTY (no commit info)
2026-05-11 18:21:16 | ⭐️ Hidroxiapatito starred steineggerlab/colabfold-protocol
2026-05-11 13:41:39 | 🔹 gamcil performed DeleteEvent on steineggerlab/foldmason
2026-05-11 13:41:35 | 🚀 gamcil pushed to steineggerlab/foldmason (no commit info)
2026-05-11 13:41:34 | 🔀 gamcil merged PR in steineggerlab/foldmason
2026-05-11 13:40:56 | 🔀 gamcil opened PR in steineggerlab/foldmason
2026-05-11 13:05:16 | 🚀 gamcil pushed to steineggerlab/foldmason (no commit info)
2026-05-11 10:59:50 | ⭐️ linjing-lab starred GENTEL-lab/VCWorld
2026-05-11 10:33:03 | ⭐️ samuelmcurtis starred baker-laboratory/RoseTTAFold-All-Atom
2026-05-11 10:19:35 | ⭐️ chengwilliamlin starred idptools/starling
2026-05-11 09:06:44 | ⭐️ AndyCycle starred steineggerlab/foldseek
2026-05-11 09:02:37 | 🚀 gterashi pushed to kiharalab/DAQplugin (no commit info)
2026-05-11 02:55:34 | ⭐️ wyqmath starred idptools/starling

```


#### Monitor a specific Repository (`--repo`)
Focus cleanly on the event stream of a single repository (e.g., releases, issues, PRs, stars).
```bash
# Monitor a single repository (isblab/disobind)
ghresearcher monitor isblab/disobind --repo -l 20

# Monitor multiple repositories (file input)
ghresearcher monitor -f repos_to_track.txt --repo
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

what you get is
```python
Fetching events for target(s): teorth...

2026-05-13 08:57:32 | 🚀 teorth pushed to teorth/erdos-guy-selfridge
    - [617f9ad] (expanded) Merge pull request #101 from Milian0402/maxiboi/readme-roadmap
2026-05-13 08:57:21 | 🔹 teorth performed PullRequestReviewEvent on teorth/erdos-guy-selfridge
2026-05-13 08:52:04 | 🚀 teorth pushed to teorth/erdos-guy-selfridge
    - [0da591c] (expanded) Merge pull request #102 from Milian0402/maxiboi/c1-constant-docs
2026-05-13 08:51:57 | 🔹 teorth performed PullRequestReviewEvent on teorth/erdos-guy-selfridge
2026-05-13 06:17:43 | 🚀 teorth pushed to leanprover-community/mathlib-at-ICERM26
    - [bcfd513] (expanded) integral form of additivity
2026-05-13 05:37:12 | 🚀 teorth pushed to leanprover-community/mathlib-at-ICERM26
    - [fc850d0] (expanded) trim docstring
2026-05-13 05:35:07 | 🚀 teorth pushed to leanprover-community/mathlib-at-ICERM26
    - [a75fbf5] (expanded) Merge branch 'stieltjes' of https://github.com/leanprover-community/mathlib-at-ICERM26 into stieltjes
2026-05-13 02:10:07 | 🚀 teorth pushed to leanprover-community/mathlib-at-ICERM26
    - [92e6786] (expanded) redefine Stieltjes integral to handle backwards integral
2026-05-12 22:30:35 | 🚀 teorth pushed to leanprover-community/mathlib-at-ICERM26
    - [ad35844] (expanded) some map API
2026-05-12 20:20:08 | 🚀 teorth pushed to leanprover-community/mathlib-at-ICERM26
    - [2bce97a] (expanded) some simple lemmas about intervals
2026-05-12 16:57:47 | 🚀 teorth pushed to leanprover-community/mathlib-at-ICERM26
    - [c025070] (expanded) integration of constants
2026-05-12 15:38:00 | 🚀 teorth pushed to leanprover-community/mathlib-at-ICERM26
    - [3ffc66b] (expanded) remove warning
2026-05-12 15:35:29 | 🚀 teorth pushed to leanprover-community/mathlib-at-ICERM26
    - [e297d8a] (expanded) add connections to standard integrals
2026-05-12 15:28:46 | 🚀 teorth pushed to leanprover-community/mathlib-at-ICERM26
    - [92c1ea3] (expanded) notation for integral
2026-05-12 15:22:09 | 🚀 teorth pushed to leanprover-community/mathlib-at-ICERM26
    - [e7fbac7] (expanded) even more linearity API
2026-05-12 15:18:39 | 🚀 teorth pushed to leanprover-community/mathlib-at-ICERM26
    - [09e1ecb] (expanded) more linearity API
2026-05-12 15:06:36 | 🚀 teorth pushed to leanprover-community/mathlib-at-ICERM26
    - [bcfd5f1] (expanded) sectioning
2026-05-12 15:03:06 | 🚀 teorth pushed to leanprover-community/mathlib-at-ICERM26
    - [98ae4aa] (expanded) Stieltjes integral linearity API
2026-05-12 14:44:10 | 🚀 teorth pushed to leanprover-community/mathlib-at-ICERM26
    - [bedff9f] (expanded) automated style fixes
2026-05-12 14:38:46 | 🚀 teorth pushed to leanprover-community/mathlib-at-ICERM26
    - [0f90350] (expanded) bundle ofDiff as a hom
2026-05-12 13:59:52 | 🚀 teorth pushed to leanprover-community/mathlib-at-ICERM26
    - [18d419b] (expanded) BoxAdditiveMap API
2026-05-12 13:29:05 | 🚀 teorth pushed to leanprover-community/mathlib-at-ICERM26
    - [2a43bd9] (expanded) fix lean
2026-05-12 13:28:23 | 🚀 teorth pushed to leanprover-community/mathlib-at-ICERM26
    - [096a002] (expanded) fix lean
2026-05-12 13:27:31 | 🚀 teorth pushed to leanprover-community/mathlib-at-ICERM26
    - [3425dd1] (expanded) add other predicates for Stieltjes integrability
2026-05-12 13:16:48 | 🚀 teorth pushed to leanprover-community/mathlib-at-ICERM26
    - [6d9643a] (expanded) notational golf
2026-05-12 13:10:50 | 🚀 teorth pushed to leanprover-community/mathlib-at-ICERM26
    - [5198afa] (expanded) change interval to Ioc
2026-05-12 13:08:16 | 🚀 teorth pushed to leanprover-community/mathlib-at-ICERM26
    - [354ba9b] (expanded) generalize integration against summatory function
2026-05-12 13:00:43 | 🚀 teorth pushed to leanprover-community/mathlib-at-ICERM26
    - [44a86ee] (expanded) golf namespaces
2026-05-12 12:54:26 | 🚀 teorth pushed to leanprover-community/mathlib-at-ICERM26
    - [a692262] (expanded) add docstring
2026-05-12 12:49:38 | 🚀 teorth pushed to leanprover-community/mathlib-at-ICERM26
    - [cfc0361] (expanded) change from Unit to Fin 1
```

---

### 2. Parsing Repository Context (`parse`)

Parses a repository, file, or saved source catalog into terminal-friendly text. The default repository path uses GitHub's Trees API first, so it does not need to clone the repository unless the API response is truncated or unavailable.

**Usage:** `ghresearcher parse [TARGET] [--view] [--view-mode readme|tree|both] [--source] [--sources-file FILE]`

```python
❯ ghresearcher parse --help
                                                                                                                                                                  
 Usage: ghresearcher parse [OPTIONS] TARGET                                                                                                                       
                                                                                                                                                                  
 Parse a repository, file, or source URL into Markdown/text.                                                                                                      
                                                                                                                                                                  
╭─ Arguments ────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ *    target      TEXT  The GitHub repo (owner/repo) or file (owner/repo/path/to/file) [required]                                                               │
╰────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─ Options ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ --output        -o      TEXT  Output file path                                                                                                                 │
│ --view                        View in a pager instead of writing to disk                                                                                       │
│ --view-mode             TEXT  View mode for repositories: both, readme, or tree [default: both]                                                                │
│ --source                      List saved source URLs for the repository                                                                                        │
│ --sources-file          TEXT  JSON file containing extra or overridden source URLs                                                                             │
│ --help                        Show this message and exit.                                                                                                      │
╰────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯

```

---

> ⚠️ Parse logic is global, i.e., not adding `--view` option will download the repository content to a file. Adding `--view` option will only view in a pager, without writing to disk.

```bash
# Write README + tree to a file
ghresearcher parse isblab/disobind -o Disobind_Context.md

# View README + tree in a pager
ghresearcher parse isblab/disobind --view

# README-only pager using the native `gh repo view` experience
ghresearcher parse isblab/disobind --view --view-mode readme

# Tree-only pager
ghresearcher parse isblab/disobind --view --view-mode tree

# Single file, e.g., README.md, you can directly append the file path after owner/repo
ghresearcher parse isblab/disobind/README.md --view

# Saved source catalog for the repository (we provide some default urls)
ghresearcher parse isblab/disobind --source --view

# Load extra sources from a JSON file (except default urls, you can also add your own urls in the JSON file, we will merge them together)
ghresearcher parse isblab/disobind --source --sources-file ./sources.json --view
```

Current default sources:
```json
[
    {"name": "deepwiki", "kind": "template", "url": "https://deepwiki.com/{owner}/{repo}"},
    {"name": "zreadai", "kind": "template", "url": "https://zread.ai/{owner}/{repo}"},
    {"name": "readmex", "kind": "template", "url": "https://readmex.com/{owner}/{repo}"},
    {"name": "gitdiagram", "kind": "template", "url": "https://gitdiagram.com/{owner}/{repo}"},
]
```


Implementation notes:
- Repository trees are fetched from the GitHub Trees API first.
- If the Trees API is truncated or fails for a very large repository, GhResearcher falls back to a temporary shallow clone to generate the tree.
- `--view --view-mode readme` uses `gh repo view` directly, so it keeps GitHub CLI's native pager behavior.
- `sources.json` can define both template sources and fixed URLs.
- You can point `--sources-file` at any JSON file containing extra or overridden saved source URLs.
- A ready-to-edit example lives at `sources.example.json` in the repository root.

---

> 🌟 A Simple Example like:

I want to view the README of a repository, I first check the README to quickly understand the project.

```bash
ghresearcher parse Junjie-Zhu/IDPFold --view --view-mode readme
```

![](./figs/1.png)

and then I want to quickly understand the file structure of the repository, so I can check where the main code lives, and where the data lives.

```bash
ghresearcher parse Junjie-Zhu/IDPFold --view --view-mode tree
```

![](./figs/2.png)

e.g., I am pretty interested in script /src/common/pdb_utils.py, I can check it by running the following command:

```bash
ghresearcher parse Junjie-Zhu/IDPFold/src/common/pdb_utils.py --view    
```

![](./figs/3.png)

finally, I want to check if there are any LLM Annotations for this script.

```bash
hresearcher parse Junjie-Zhu/IDPFold --source --view
```

![](./figs/4.png)

I can directly open the default smart reading page in the browser to view the detailed information of the project.



### 3. Searching GitHub (`search`)

Perform tailored searches from the terminal.

**Usage:** `ghresearcher search [item_type] [query]`

```bash
# Search for repositories related to "Deep Learning"
ghresearcher search repos "Deep Learning" -L Python -l 10
```


## Advanced Search Syntax (GitHub)

GhResearcher exposes GitHub's search through `ghresearcher search` (a thin wrapper around `gh search`). This section summarizes the advanced search syntax, common qualifiers, and practical examples you can run directly from the CLI.

Core idea
- GitHub search accepts a free-form query string that can include qualifiers (key:value pairs) and boolean operators. Qualifiers such as `repo:`, `language:`, `path:`, `filename:`, `extension:`, `topic:`, `user:`, `org:`, `stars:`, `size:` narrow results efficiently.

How to use with GhResearcher
- Basic form: `ghresearcher search <item_type> "<query>" [options]` where `<item_type>` is one of `repos`, `code`, `issues`, `prs`, `commits`, `users`.
- The CLI helper flags (`--language`, `--owner`, `--repo`, `--topic`, `--extension`, `--filename`) append equivalent qualifiers to the query.
- `--limit`, `--sort`, and `--order` are passed to `gh` to control result count and ordering.

Useful qualifiers and examples
- `repo:owner/name` — restrict search to a repository. Example: `repo:MaybeBio/GhResearcher`.
- `language:Python` — filter by language for repos/code.
- `path:docs/` — search only inside a path in a repository.
- `filename:README.md` — find files named `README.md`.
- `extension:py` — search files by extension.
- `topic:bioinformatics` — filter repos by topic.
- `user:username` / `org:orgname` — filter by owner or organization.
- `stars:>100` / `stars:10..50` — numeric ranges.

Practical examples
```bash
# Find Python repos mentioning "LLM" with >50 stars
ghresearcher search repos "LLM language:Python stars:>50" -l 20

# Search code for TODO comments inside a specific repo
ghresearcher search code "TODO repo:MaybeBio/GhResearcher" --filename "*.py" -l 50

# Find issues containing "crash" in the MaybeBio organization
ghresearcher search issues "crash org:MaybeBio" -l 100

# Search code by extension and path inside repos (code search)
ghresearcher search code "def my_function extension:py path:src/" -l 50
```

Tips & caveats
- Use quotes for exact phrases: `"memory leak"`.
- Combine conditions with `OR` and exclude terms with `-` (e.g. `bug OR error`, `-wip`).
- `gh search` supports JSON output when needed — for machine parsing prefer `gh`'s `--json` option directly.
- GitHub search semantics and available qualifiers differ slightly by domain (`code` vs `repos` vs `issues`). Refer to the official docs in `docs/` for details.
- Rate limits and result pagination may apply — use `--limit` to bound results.

References
- See the `docs/` folder for harvested GitHub search documentation (`docs_github_com_en_search-github_*`).


---

## ⚠️ Limits & Caveats

- **GitHub API Limits:** The `monitor` timeline is restricted to a maximum of 300 recent events or events within the past 90 days due to GitHub API constraints.
- **Parser Size:** The `parse` command can still be expensive for extremely large repositories because tree rendering and pager output may be large. When the Trees API is truncated, the tool falls back to a temporary shallow clone.
- **Rate Limiting:** Heavy use of `--expand-commits` or batch mapping large lists may quickly consume your GitHub API rate limit. Use with care.
