# Static Application Security Testing (SAST) - Bandit Report

## Overview
This document records the output and findings from running Bandit on the sample Python application codebase (`sample_code.py`).

## Scan Results & Vulnerabilities Flagged
* **High Severity:** 
  * `B602` - Subprocess call with `shell=True` identified on line 23 (`subprocess.run(command, shell=True)`), creating a command injection risk[cite: 34].
* **Medium Severity:** 
  * `B506` - Use of unsafe `yaml.load()` with `yaml.Loader` on line 33, allowing arbitrary object instantiation[cite: 34].
  * `B307` - Use of insecure `eval(user_input)` function on line 54, which executes arbitrary code[cite: 34].
* **Low Severity:** 
  * `B105` - Hardcoded password string (`DB_PASSWORD = "P@ssw0rd123"`) found on line 8[cite: 34].
  * `B404` - Security implications associated with importing the `subprocess` module on line 2[cite: 34].

## Scan Metrics
* **Total Lines of Code Scanned:** 54[cite: 34]
* **Total Issues Found:** 5 (1 High, 2 Medium, 2 Low)[cite: 34]
* **Confidence Breakdown:** 4 High-confidence issues, 1 Medium-confidence issue[cite: 34]
