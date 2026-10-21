# UNIT III CHEAT SHEET — Cloud Security, Monitoring & Cost Management

**Course:** 23CSE3014 — Cloud Foundation & Deployment  
**Class:** T.Y. AIEC (SEM-I) | MIT School of Computing, Pune | AY 2026-27  
**Professor:** Rupesh Hushangabade  

---

## 1. AUTHENTICATION vs AUTHORIZATION

| Feature | Authentication | Authorization |
|---------|---------------|---------------|
| Question | "Who are you?" | "What can you do?" |
| Order | First | Second (after authN) |
| Verifies | Identity is genuine | Permission level sufficient |
| Input | Username/password, biometric, token | Role, privilege, security level, policy |
| Token | ID Token (OIDC) | Access Token (OAuth 2.0) |
| User change | Yes | No (owner/admin only) |
| Visibility | Visible to user | Invisible (backend) |

**AuthN determines whether the person is a valid user. AuthZ determines what permission the user has.**

### AuthN Techniques: Password-based, Passwordless, 2FA/MFA, SSO, Social auth
### AuthZ Techniques: RBAC, JWT, SAML, OpenID, OAuth 2.0
### Protocols: OIDC = authentication; OAuth 2.0 = authorization

---

## 2. CIA TRIAD

### Confidentiality — Only authorized can view data
- **Protection:** Encryption (AES, DES), VPN tunnel
- AES = Advanced Encryption Standard; DES = Data Encryption Standard (older, weaker)

### Integrity — Data not modified/corrupted
- **Method:** Hash functions
- **Process:** Host A hashes data → H1, sends data + H1. Host B hashes → H2. If H1 = H2, integrity maintained.
- **Algorithms:** MD5 (128-bit, weak), SHA (160-bit)

### Availability — Network/systems readily accessible
- **Ensured by:** Hardware maintenance, upgrades, fail-over, prevent bottlenecks
- **Threats:** DoS (Denial of Service), DDoS (Distributed DoS)

---

## 3. INFRASTRUCTURE SECURITY

### Network Level Protection
| Service | Type | Purpose |
|---------|------|---------|
| Security Groups | Stateful firewall | EC2 instance level |
| NACLs | Stateless firewall | VPC subnet level |
| AWS WAF | Application layer | Stops SQL injection, XSS |
| AWS Shield | Network/Transport | DDoS protection (always-on) |
| AWS Network Firewall | Stateful | VPC inspection, intrusion prevention |
| Route 53 DNS Firewall | DNS | Blocks malicious DNS queries |

**Key:** Security Groups = instance-level, stateful. NACLs = subnet-level, stateless.

### Host Level Protection
- Host hardening (turn off unused services, close ports, remove software)
- Patch management
- Access controls (MFA, SSH keys, least privilege)
- IDS (Intrusion Detection Systems)
- Antivirus & endpoint protection

### Application Level Protection
- Protects against web-based attacks (WAF, input validation, secure coding)

---

## 4. DATA SECURITY & STORAGE

| Data Privacy | Data Security |
|-------------|---------------|
| Rights of individuals over personal data | Technical protection from unauthorized access |
| Policy/rights | Enforcement/methods |

### Jurisdictional Issues
- Data location determines which country's laws apply (GDPR in EU, CLOUD Act in US, DPDP Act in India)
- Compliance complexity when data crosses borders

---

## 5. IAM (Identity & Access Management)

- Controls **who can do what, and from where** in AWS
- Components: IAM Users, Groups, Roles, Policies (JSON documents)
- **Best Practices (IAM Brain Dump):**
  1. Never use ROOT credentials (except initial setup)
  2. One IAM user per physical person
  3. One IAM role per application
  4. Never share IAM credentials
  5. Never write IAM credentials in code
- **IAM Federation:** SAML standard; enterprise AD → AWS; employees use corporate credentials
- Features: Free, global view, granular permissions, MFA, managed policies

---

## 6. CLOUD SERVICE AGREEMENTS (CSAs)

- Contract between organization and cloud provider
- **Why matters:** Individuals whose data is stored are NOT direct parties to CSA
- Organization is **liable** for cloud provider's failings
- Essential for: protecting personal data, complying with laws, regulatory obligations
- **Common problems:** Lack of knowledge, lack of bargaining power, lack of internal coordination

---

## 7. COST MANAGEMENT

- Cloud = Fixed expenses → Variable expenses (pay only for what you consume)
- Economies of scale make cloud cheaper than self-hosting
- Topics: Strategies, budgeting, optimization, cost estimations, billing & accounting

---

## 8. MONITORING & TROUBLESHOOTING

### CloudWatch
| Concept | Definition |
|---------|------------|
| Metric | Variable to monitor (CPUUtilization, DiskReadBytes) |
| Namespace | Container for metrics (AWS/EC2, AWS/S3) |
| Dimension | Attribute of metric (InstanceId, Environment); max 10 per metric |

- **Basic:** 5 min, free. **Detailed:** 1 min, paid (10 free in Free Tier)
- **Alarms:** OK / INSUFFICIENT_DATA / ALARM → actions: SNS, Auto Scaling, EC2
- **Logs:** Log Group (app name) → Log Stream (instance/file, one group only)
- **Events:** Source + Rule → Target (cron or event pattern)
- **Dashboards:** Global, multi-region, auto-refresh 10s–15m

### SNS (Pub/Sub)
- One topic → up to 10,000,000 subscribers
- Subscribers: SQS, HTTP/HTTPS, Lambda, Email, SMS, Mobile
- 100,000 topics limit

### CloudTrail
- Records AWS API calls (who, when, from where, what)
- Event history: last **90 days**
- Trails deliver logs to S3 bucket
- IAM controls trail access

---

## 9. EXAM QUESTIONS — QUICK ANSWERS

1. **Authentication** = verifying identity ("Who are you?")
2. **Difference:** AuthN = identity (first, ID Token, visible, changeable). AuthZ = permissions (after, Access Token, invisible, owner-controlled).
3. **MFA 3 factors:** Something you know (password), have (phone/token), are (biometrics).
4. **Strong passwords:** Length, complexity, history, expiration, lockout — prevent brute-force/dictionary attacks.
5. **Biometric:** Something you are. Examples: fingerprint, face, retina/iris.
6. **SSO:** One login → multiple apps. Enhances UX, reduces password fatigue, centralizes control.
7. **2FA challenges:** Friction, device dependency, backup/recovery, cost, legacy integration, SMS vulnerability.
8. **Token-based:** Server issues signed token (JWT); client sends with each request. Stateless, scalable, cross-domain.
9. **Federated auth:** Trust between IdP and SP (SAML/OIDC). Single identity, centralized management, SSO across orgs.
10. **Threats:** Phishing, credential stuffing, brute-force, session hijacking, MitM, weak passwords, token theft.

---

*Print this before the exam. Good luck!*