# Linux Crontab Automation & Task Scheduling Analysis

This report documents the analysis, auditing, and review of scheduled cron jobs on a Linux (Ubuntu) system, focusing on both regular user-level automation and privileged root-level task scheduling.

---

## 1. Overview of Task Scheduling in Linux
The cron daemon (`cron`) is a time-based job scheduler in Unix-like operating systems. It executes commands or scripts (known as cron jobs) at specified dates and times. Auditing crontabs is a critical component of system administration and security monitoring to ensure that no unauthorized, malicious, or disruptive automation runs in the background.

Cron expressions follow a standard 5-field time format followed by the command to execute:
```text
# ┌───────────── minute (0 - 59)
# │ ┌───────────── hour (0 - 23)
# │ │ ┌───────────── day of the month (1 - 31)
# │ │ │ ┌───────────── month (1 - 12)
# │ │ │ │ ┌───────────── day of the week (0 - 6) (Sunday to Saturday)
# │ │ │ │ │
# * * * * * command to execute
