# DevSecOps Pipeline & Security Scanning Reflection

## 1. Static Analysis (SAST)
* **Observed:** The tool scanned source code without executing it, flagging issues by file and line number (such as insecure functions, hardcoded values, and missing input validation), demonstrating how vulnerabilities enter code during development.
* **Actions:** Refactor flagged sections, enforce secure coding standards, add input validation/parameterized queries, and integrate SAST into the CI/CD pipeline to execute automatically on every commit[cite: 35].

## 2. Dependency Scanning (SCA)
* **Observed:** The scanner cross-referenced third-party libraries against CVE databases, discovering outdated dependencies with known high and medium vulnerabilities, highlighting risks from external code dependencies[cite: 35].
* **Actions:** Update packages to patched versions, remove unused libraries, enable automated update tools like Dependabot, and maintain an SBOM (Software Bill of Materials)[cite: 35].

## 3. Secret Detection / YARA
* **Observed:** YARA scanned for secret patterns like API keys, passwords, and tokens, outputting rule matches and file paths to prevent credential leakage before pushing code to GitHub[cite: 35].
* **Actions:** Remove hard-coded secrets immediately, rotate/revoke exposed keys, move secrets to environment variables or a vault (such as HashiCorp Vault or AWS Secrets Manager), and add pre-commit secret scanning via tools like `gitleaks`[cite: 35].

## Conclusion
This workflow illustrates the core DevSecOps concept of **"shifting left"**—detecting code flaws, dependency vulnerabilities, and exposed secrets early in the development lifecycle before reaching production[cite: 35].
