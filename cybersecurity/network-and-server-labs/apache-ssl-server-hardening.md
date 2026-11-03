# Apache HTTP Server SSL/TLS Hardening & Certificate Configuration

This report outlines the process of generating a self-signed RSA certificate, configuring secure virtual hosts in Apache (`httpd.conf`), and verifying HTTPS connectivity.

---

## Lab Objectives
* Generate self-signed cryptographic certificates for local testing.
* Configure Apache HTTP Server (`httpd`) to support secure TLS encrypted connections.
* Review browser security warning mechanics associated with self-signed certificates.

---

## Configuration & Implementation Steps

### 1. Generating a Self-Signed RSA Certificate
* **Certificate Details:**
  * **Issuer / Subject:** `CN=localhost`, `OU=IT`, `O=Hyperion Dev`, `L=Cape Town`, `ST=Western Cape`, `C=ZA`
  * **Public Key:** RSA 2048-bit encryption
  * **Signature Algorithm:** `sha256WithRSAEncryption`
  * **Validity Window:** October 2026 – October 2027
* **Verification:** Certificate file generated and verified with proper Distinguished Name (DN) attributes.

### 2. Apache Server Configuration (`httpd.conf`)
* **Key Modules Enabled:** Loaded essential cryptographic and proxy modules including `mod_ssl.so`, `mod_socache_shmcb.so`, and proxy-related components.
* **Privilege Management:** Configured dedicated user and group directives (`Group javas` / service users) following least-privilege administrative practices rather than running web services directly as root.
* **Virtual Host Setup (`VirtualHost _default_:443`):**
  * Enabled the SSL engine (`SSLEngine on`).
  * Pointed directives to the server certificate file (`SSLCertificateFile`) and private key file (`SSLCertificateKeyFile`).
* **Verification:** Syntax check passed and Apache service initialized successfully with SSL parameters loaded.

### 3. Browser Testing & Security Warnings
* **Observed Behavior:** Navigating to `https://127.0.0.1` initially triggered a browser warning screen (*"Your connection isn't private"* / `NET::ERR_CERT_AUTHORITY_INVALID`).
* **Technical Reason:** The certificate is self-signed by a local test authority (`localhost`) rather than a globally recognized Public Certificate Authority (CA) trusted by the browser store by default.
* **Verification:** Advanced bypass options utilized successfully to inspect certificate details locally in-browser.
