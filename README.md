# 🗃️ Log Archive Tool

A simple command-line tool to archive logs by compressing them into `.tar.gz` files and organizing them with timestamps. Ideal for system maintenance, backups, or log rotation.

---

## 🚀 Features

- Run from CLI with a log directory as an argument
- Compresses logs into a `.tar.gz` archive
- Archives named like: `logs_archive_YYYYMMDD_HHMMSS.tar.gz`
- Stores archives in an `archives/` directory
- Logs each archive action with timestamp in `archive_log.txt`
- Optional handling of permission errors (skip unreadable files)

---

## 📦 Requirements

- Python 3.6+

---

## 🛠️ Installation

Clone the repository or copy the script:

```bash
git clone https://github.com/Code-Breaking-on/log-archive-tool.git
cd log-archive-tool
```

Make it executable:

```bash
chmod +x log_archive.py
```

Run the tool:

```bash
sudo ./log_archive.py /var/log

```



# Reference
```bash
https://roadmap.sh/projects/log-archive-tool
