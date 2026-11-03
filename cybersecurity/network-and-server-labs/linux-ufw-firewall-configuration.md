# Linux Firewall Configuration (UFW) & Stateful Inspection Analysis

## 1. Scenario & Hardening Objectives
Configure a host-based Linux firewall using **Uncomplicated Firewall (UFW)** for an enterprise web server (`10.0.0.10`)[cite: 12]. The objective is to enforce a default-deny posture while permitting public HTTPS web traffic, restricting SSH management to a single trusted office IP (`203.0.113.50`), and allowing outbound package updates[cite: 12].

---

## 2. UFW Rule Configuration

| Rule Order | Objective | UFW Command Syntax | Security Rationale |
| :--- | :--- | :--- | :--- |
| **0** | **Default Inbound Policy** | `sudo ufw default deny incoming`[cite: 12] | Establishes a zero-trust baseline by dropping all unsolicited inbound traffic unless explicitly permitted[cite: 12]. |
| **1** | **HTTPS Inbound** | `sudo ufw allow to 10.0.0.10 port 443 proto tcp`[cite: 12] | Allows external users to access the encrypted web server over TCP port 443[cite: 12]. |
| **2** | **Restricted SSH Management** | `sudo ufw allow from 203.0.113.50 to 10.0.0.10 port 22 proto tcp`[cite: 12] | Prevents brute-force SSH attacks from the public internet by restricting port 22 access exclusively to the static office IP[cite: 12]. |
| **3** | **Outbound Server Updates** | `sudo ufw allow from 10.0.0.10 to any port 80 proto tcp`<br>`sudo ufw allow from 10.0.0.10 to any port 443 proto tcp`[cite: 12] | Permits the server to initiate outbound HTTP/HTTPS connections to external repositories for OS and security patching[cite: 12]. |

---

## 3. Architectural Analysis

### Stateful Packet Inspection in Action
Unlike a stateless packet filter that evaluates packets in isolation, a **Stateful Inspection Firewall** maintains an active **State Table** tracking connection states[cite: 12]:
1. **Session Initiation:** When the web server (`10.0.0.10`) initiates an outbound request on TCP port 80 or 443 for system updates, UFW records the session details in its state table and marks the connection as `ESTABLISHED`[cite: 12].
2. **Return Traffic Verification:** When the external update server responds, the firewall inspects its state table, confirms the inbound packets match an existing outbound session initiated by `10.0.0.10`, and automatically permits the traffic back in[cite: 12].
3. **Security Benefit:** This eliminates the need to write an insecure inbound rule (`allow from any to 10.0.0.10`)[cite: 12]. Only return traffic tied to an active, internally initiated session is allowed through the perimeter, while unsolicited inbound connections are dropped[cite: 12].

---

### Defence-in-Depth: Network Firewall vs. Endpoint Antivirus
Network firewalls and endpoint antivirus solutions operate at different defensive layers and inspect distinct aspects of traffic[cite: 12]:

* **Network Firewall (Header & Transport Inspection):** Inspects packet headers, source/destination IP addresses, ports, and protocols (TCP/UDP)[cite: 12]. It governs *who* can communicate with *whom* on *which port*, but remains blind to the actual application payload inside the packet[cite: 12].
* **Endpoint Antivirus / EDR (Payload & Behavioral Inspection):** Inspects the actual file contents, cryptographic signatures, and runtime behavior on the host operating system[cite: 12, 13].

#### Attack Scenario: Malicious Payload Over Permitted Port 443
1. **The Bypass:** An attacker transmits a valid HTTPS request to `10.0.0.10` over TCP port 443 containing an embedded web shell or ransomware payload[cite: 12]. Because the destination IP, port, and protocol match Rule #1 (`allow to 10.0.0.10 port 443 proto tcp`), the firewall permits the packet through—it only verifies the "envelope," not the contents inside[cite: 12, 13].
2. **The Detection:** Once the payload reaches the server and is decrypted/written to disk, the host-based antivirus scans the file content and runtime behavior, matches the malicious signature or heuristic pattern, and immediately blocks and quarantines the threat[cite: 13].
