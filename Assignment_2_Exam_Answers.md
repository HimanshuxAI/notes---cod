# ASSIGNMENT 2 — EXAM ANSWERS (Term Assessment-II, Cloud Foundation & Deployment)

**Institution:** MIT School of Computing, MIT-ADT University, Pune  
**Subject:** 23CSE3014 — Cloud Foundation & Deployment  
**Exam:** Term Assessment–II, Oct-2025 | Max Marks: 20 | Time: 1 hour  
**Instructions:** Attempt Q1 OR Q2 AND Q3 OR Q4. Figures to right indicate marks.

---

## STRATEGY — Pick one from each pair

| Pair | Easier Option | Why |
|------|--------------|-----|
| Q1 OR Q2 | **Q1** | Straight definitions + table (easy to memorize) |
| Q3 OR Q4 | **Q3** | Comparison table + scenarios (no drawing required) |

*Choose Q4 only if you're comfortable drawing the HPA diagram.*

---

## Q1 — AUTHENTICATION & AUTHORIZATION (CO3)

### Q1.A) Difference between authentication and authorization. [5 marks]

**Answer table:**

| Basis | Authentication | Authorization |
|-------|---------------|---------------|
| Question | "Who are you?" | "What can you do?" |
| Sequence | First | After authentication |
| Verifies | Identity genuine | Permission sufficient |
| Input | Username/password, biometric, token | Role, privilege, security level, policy |
| Token | ID Token (OIDC) | Access Token (OAuth 2.0) |
| User change | Yes | No (owner/admin only) |
| Visibility | Visible to user | Invisible (backend) |

**Summary:** Authentication determines **whether** the person is a valid user. Authorization determines **what permission** the user has.

**Example:** Employee logs in (authN) → system decides what they can access (authZ).

---

### Q1.B) Three main factors for multi-factor authentication. [5 marks]

1. **Something you KNOW** — Password, PIN, security question answer.
2. **Something you HAVE** — Smartphone (OTP app), security token, smart card, hardware key (YubiKey).
3. **Something you ARE** — Biometrics: fingerprint, face recognition, iris/retina scan, voice.

**Why MFA:** Attacker must compromise multiple independent factors, drastically reducing unauthorized access risk.

---

## Q2 — AUTHENTICATION CHALLENGES & FEDERATION (CO3)

### Q2.A) Challenges in implementing two-factor authentication. [5 marks]

**Challenges:**
1. User resistance & friction (extra login step)
2. Device dependency (lost phone = lockout)
3. Backup & recovery (need secure process for lost second factor)
4. Cost (hardware tokens, SMS gateways)
5. Legacy integration (older apps may not support OIDC/SAML/FIDO2)
6. SMS vulnerability (SIM-swapping attacks)
7. Accessibility (biometrics/hardware may be difficult for some users)

**Considerations:** Use phishing-resistant factors (authenticator apps, hardware keys over SMS), provide backup codes, enforce MFA for privileged accounts first.

---

### Q2.B) Federated authentication — concept and benefits. [5 marks]

**Concept:** Trust relationship between identity systems. User authenticates once with home Identity Provider (IdP, e.g., Active Directory) and accesses services in another domain (Service Provider, e.g., AWS) without separate accounts.

**How it works:** SP redirects user to IdP → IdP authenticates → sends signed assertion (SAML/OIDC) → SP grants access.

**Benefits:**
- Single identity across organizations (no duplicate accounts)
- Centralized user management (one directory)
- Improved security (corporate password policy + MFA at IdP)
- Better user experience (SSO with corporate credentials)
- Compliance (all auth flows through central IdP, easier to audit)

**Example:** Enterprise AD federated with AWS IAM via SAML; employees log into AWS with company credentials.

---

## Q3 — CONTAINERS vs VIRTUALIZATION (CO4)

### Q3.A) Compare and contrast containers with traditional virtualization. [5 marks]

**Similarities:** Both isolate apps on one host; both provide resource allocation; both enable portability.

**Differences table:**

| Feature | Containers | Traditional VMs |
|---------|-----------|-----------------|
| Virtualization level | OS-level (shares host kernel) | Hardware-level (hypervisor) |
| Guest OS | None | Full guest OS per VM |
| Size | Megabytes (MB) | Gigabytes (GB) |
| Boot time | Seconds | Minutes |
| Resource overhead | Low | High |
| Density per host | Many | Few |
| Isolation | Namespaces/cgroups | Separate kernel (stronger) |

**Key differentiator:** Containers virtualize at OS level (share kernel); VMs virtualize at hardware level (each VM has own kernel). Containers = lighter, faster.

---

### Q3.B) Three scenarios where containerization is preferred. [5 marks]

| Scenario | Why |
|----------|-----|
| **Microservices** | Each service containerized independently, different languages, scaled independently |
| **CI/CD pipelines** | Same image moves dev → test → prod; eliminates "works on my machine" |
| **Hybrid/multi-cloud** | Images run identically on-prem, AWS, Azure, GCP |
| **Spiky workloads** | Start in seconds; rapidly replicated via autoscaling |
| **Dev & testing** | Identical environments; spin up/tear down quickly |
| **Cost optimization** | Higher density per server vs VMs |

*(Write any 3 with 1–2 sentence explanation each.)*

---

## Q4 — CONTAINER ORCHESTRATION & HPA (CO4)

### Q4.A) Role of container orchestration in managing complex containerized apps. [5 marks]

**Definition:** Automated arrangement, coordination, and management of containers across a cluster (e.g., Kubernetes).

**Roles:**

| Role | Explanation |
|------|-------------|
| Automated deployment | Places containers on nodes based on resources |
| Scaling | Auto-scales replicas (HPA, Cluster Autoscaler) |
| Load balancing | Distributes traffic across container instances |
| Self-healing | Restarts failed containers, replaces dead nodes |
| Rolling updates/rollbacks | Zero-downtime updates; roll back if issues |
| Service discovery | Containers find each other via DNS (no hardcoded IPs) |
| Resource management | CPU/memory limits per container |
| Storage & secrets | Mounts volumes; injects passwords/API keys |
| Namespace isolation | Virtual clusters for multi-tenancy |

**Analysis:** Managing 100s of containers across hosts manually is impractical. Orchestration provides automation, resilience, scalability for production apps.

---

### Q4.B) Draw and explain Horizontal Pod Autoscaler (HPA). [5 marks]

**Draw this diagram in your exam:**

```
        Metrics Server
             |
             v
    +------------------+
    |   HPA Controller |
    +------------------+
             |
   (actual vs target utilization)
             |
             v
    +------------------+
    |  Deployment /    |
    |  ReplicaSet      |
    +------------------+
             |
             v
       +-----------+
       |   Pods    |
       +-----------+
```

**Explanation:**
- HPA automatically scales the **number of pod replicas** based on demand.
- Configured as K8s resource with target metric (e.g., CPU 50–70%).
- Metrics Server collects CPU/memory from pods; HPA controller compares actual vs target.
- Above target → scale out (more pods). Below target → scale in (fewer pods).
- Updates state as pods are created/deleted.

**Exam tip:** Label all components clearly in your diagram. Neat diagrams = full marks.

---

## 📊 QUICK MARKS DISTRIBUTION

| Question | Marks | Topic |
|----------|-------|-------|
| Q1.A | 5 | AuthN vs AuthZ table |
| Q1.B | 5 | MFA 3 factors |
| Q2.A | 5 | 2FA challenges |
| Q2.B | 5 | Federated auth |
| Q3.A | 5 | Containers vs VMs |
| Q3.B | 5 | 3 containerization scenarios |
| Q4.A | 5 | Orchestration roles |
| Q4.B | 5 | HPA diagram + explanation |

**Total: 20 marks** (answer 4 sub-questions)

---

*Good luck with your exam!*