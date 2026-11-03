# PKI & X.509 SSL/TLS Certificate Chain Analysis

## 1. Objective
Inspect and validate the X.509 SSL/TLS digital certificate and Public Key Infrastructure (PKI) trust hierarchy for `https://www.microsoft.com` to evaluate cryptographic strength, organizational validation, and certificate lifecycle risk.

---

## 2. X.509 Certificate Metadata & Cryptographic Specifications

| Certificate Field | Recorded Value |
| :--- | :--- |
| **Subject Common Name (CN)** | `www.microsoft.com` |
| **Subject Organization (O)** | Microsoft Corporation (Redmond, WA, US)[cite: 33, 35] |
| **Issuer Common Name (CN)** | `Microsoft TLS G2 RSA CA OCSP 04`[cite: 33] |
| **Issuer Organization (O)** | Microsoft Corporation[cite: 33] |
| **Signature Algorithm** | PKCS #1 SHA-384 With RSA Encryption[cite: 34] |
| **Validity Period (Not Before)** | Thursday, January 22, 2026 (21:55:21)[cite: 33] |
| **Validity Period (Not After)** | Sunday, January 17, 2027 (21:55:21)[cite: 33] |
| **SHA-256 Certificate Fingerprint** | `9f17b548f7d24f309dbcaab571576c0ca73b80559ce69f27fe295f6408cc57bf`[cite: 33] |
| **SHA-256 Public Key Fingerprint** | `dfd1a06be3dbe1fea78817bd8a9afdab57829819abf4c2bae78fdb34daae6193`[cite: 33] |

---

## 3. PKI Certificate Chain of Trust

The certificate relies on a three-tier hierarchical chain of trust anchored by a globally trusted Root Certificate Authority (CA)[cite: 34, 35]:

```text
DigiCert Global Root G2 (Root CA)
 └── Microsoft TLS RSA Root G2 (Intermediate CA)
      └── Microsoft TLS G2 RSA CA OCSP 04 (Issuing Intermediate CA)
           └── [www.microsoft.com](https://www.microsoft.com) (End-Entity / Leaf Certificate)
