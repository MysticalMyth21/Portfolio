# Networking Protocols & HTTP Response Status Analysis

This document compiles core networking theory concepts, protocol definitions, and HTTP status code classifications.

---

## 1. Network Protocols
* **Definition:** A protocol is a standardized set of rules and formats that allows two or more network entities to communicate and exchange data reliably (comparable to social conversational norms and shared language).
* **Core Example:** Web browsers and web servers rely on HTTP/HTTPS protocols to structure requests and responses.
* **Transport Layer Core:** Transmission Control Protocol (`TCP`) ensures reliable, connection-oriented packet delivery.

---

## 2. HTTP Status Code Classifications
HTTP responses are grouped into standardized status classes indicating request outcomes:
* **`200s` (Success):** Indicates that the client's request was successfully received, understood, and accepted (e.g., `200 OK`).
* **`400s` (Client Error):** Indicates that the request contains bad syntax or cannot be fulfilled due to client-side errors (e.g., `400 Bad Request`, `404 Not Found`).

---

## 3. Stateless Architecture & Secure Shell Behavior
* **Stateless Protocols:** Communication methods (like standard HTTP) where each request is treated as an independent transaction; the server retains no conversational context or memory of previous requests from the same client.
* **SSH Security Reaction:** If an SSH connection encounters host key mismatch anomalies or handshake failures, the SSH client immediately blocks and terminates the connection attempt to prevent man-in-the-middle (MitM) attacks.
