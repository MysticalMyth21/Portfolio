# Network Reconnaissance & Footprinting Lab Report

This document records the step-by-step execution, observations, and learnings from conducting passive and active network reconnaissance and footprinting exercises.

---

## Lab Objectives
* Differentiate between passive reconnaissance (non-intrusive information gathering) and active reconnaissance (direct target engagement).
* Utilize standard Linux networking utilities for local and remote enumeration.
* Perform port scanning, banner grabbing, and service header analysis.

---

## Step-by-Step Execution & Findings

### Step 1: Local Network & Interface Identification
* **Commands Executed:** `ip a` and `hostname -I`
* **Observed Output:** Displayed loopback interface (`127.0.0.1`) and local private network addressing (`172.23.218.46` on `eth0`).
* **Analysis:** This represents **passive reconnaissance** as it involves querying local system configurations without interacting with or alerting external systems.
* **Verification:** Local IP and loopback addresses successfully identified.

### Step 2: Domain Footprinting & DNS Enumeration
* **Commands Executed:** `sudo apt install whois`, `whois kali.org`, `dig kali.org ANY`, and `dig +short kali.org`
* **Observed Output:** `whois` returned registration details, creation dates, and authoritative name servers (`cloudflare.com`), while `dig` resolved the domain to specific target IP addresses (`104.18.4.159`, `104.18.5.159`).
* **Analysis:** Demonstrates how publicly available DNS and registrar records expose target infrastructure layout without direct network tampering.
* **Verification:** Public IP addresses and registrar nameservers successfully queried and displayed.

### Step 3: Port Scanning & Service Discovery
* **Commands Executed:** `sudo nmap -sS 127.0.0.1` and `sudo nmap -sV 127.0.0.1`
* **Observed Output:** Scanned 1000 common TCP ports on localhost, returning closed states across default configurations.
* **Analysis:** Highlights that fresh operating system installations minimize attack surfaces by leaving non-essential ports closed by default.
* **Verification:** Nmap completed port state evaluation and version detection metrics.

### Step 4: Banner Grabbing via Netcat
* **Commands Executed:** `nc -lvp 4444` and `nc 127.0.0.1 4444`
* **Observed Output:** Established an interactive listener on a high port (`4444`) to bypass root permission requirements on privileged ports (like port `22`), allowing successful transmission of banner test strings.
* **Analysis:** Illustrates how service banners and raw socket connections reveal active application identifiers.
* **Verification:** Bi-directional text transmission confirmed across connected terminal sockets.

### Step 5: Web Header Analysis
* **Commands Executed:** `curl -I https://127.0.0.1` and `curl -I http://example.com`
* **Observed Output:** Localhost HTTPS failed due to an inactive local server, while `example.com` returned active HTTP/1.1 headers (`200 OK`, Server type `cloudflare`, Content-Type, and cache tracking).
* **Analysis:** Shows how HTTP response headers passively leak technology stacks and server configurations to external observers.
* **Verification:** HTTP response headers successfully retrieved and inspected.

---

## Overall Conclusion
This lab successfully demonstrated the operational contrast between silent passive footprinting (`ip`, `whois`, `dig`) and intrusive active engagement (`nmap`, `nc`, `curl`). Adapting techniques to match available system services is a core requirement in practical security assessments.
