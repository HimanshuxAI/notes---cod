# EXAM PATTERN ANALYSIS & QUESTION PREDICTION

**Course:** 23CSE3014 — Cloud Foundation & Deployment  
**Institution:** MIT School of Computing, MIT-ADT University, Pune  
**Professor:** Rupesh Hushangabade  
**Academic Year:** 2026-27  

---

## 1. EXAM PATTERN ANALYSIS

Based on patterns observed across **Unit III slides**, **Unit IV slides**, and **Assignment 2 (Term Assessment-II)**, here is the consistent exam structure:

### 1.1 Paper Structure (Consistent Pattern)

| Element | Pattern Observed |
|---------|-----------------|
| **Total Marks** | 20 marks |
| **Duration** | 1 hour (60 minutes) |
| **Question Format** | Q1/Q2 pair AND Q3/Q4 pair (attempt one from each pair) |
| **Sub-question split** | Each question has Part A (5 marks) + Part B (5 marks) |
| **Total sub-questions to answer** | 4 (2 from Q1/Q2 + 2 from Q3/Q4) |
| **Marks per sub-question** | 5 marks each |
| **CO mapping** | Each sub-question tagged with Course Outcome code (CO3, CO4, etc.) |
| **Diagram requirement** | "Neat diagrams must be drawn wherever necessary" |
| **Figure marks** | "Figures to right indicate the marks allotted" |

### 1.2 Question Type Distribution (Observed)

| Question Type | Frequency | Examples from Assignment 2 |
|--------------|-----------|---------------------------|
| **Definition / Concept** | High | Q1.A "Explain the difference between..." |
| **Comparison / Contrast Table** | High | Q3.A "Compare and contrast containers with VMs" |
| **Factors / List (3 items)** | High | Q1.B "Three main factors for MFA", Q3.B "Three scenarios" |
| **Challenges & Considerations** | Medium | Q2.A "Discuss challenges in implementing 2FA" |
| **Concept Elaboration with Benefits** | Medium | Q2.B "Federated authentication and its benefits" |
| **Scenario-based** | Medium | Q3.B "Scenarios where containerization preferred" |
| **Role / Analysis** | Medium | Q4.A "Analyse the role of container orchestration" |
| **Diagram + Explanation** | Medium | Q4.B "Draw and explain HPA" |

### 1.3 Time Allocation Pattern

| Task | Suggested Time |
|------|---------------|
| Q1 or Q2 (2 sub-questions × 5 marks) | ~25 minutes |
| Q3 or Q4 (2 sub-questions × 5 marks) | ~25 minutes |
| Review / buffer | ~10 minutes |
| **Total** | **60 minutes** |

---

## 2. TOPIC-WISE QUESTION PREDICTION

Based on the recurrence of topics across Unit III, Unit IV, and Assignment 2, here is the predicted likelihood of question types for upcoming exams:

### 2.1 HIGH PROBABILITY (Almost Certain to Appear)

These topics have appeared in both slides AND the assignment:

| Topic | Likely Question Type | Marks | Preparation |
|-------|---------------------|-------|-------------|
| **Authentication vs Authorization** | Definition + Comparison table | 5 | Memorize the comparison table (order, tokens, visibility, user control) |
| **MFA Three Factors** | List + brief explanation | 5 | Know: Something you know/have/are with examples |
| **Containers vs VMs** | Comparison table | 5 | Memorize: size, boot time, kernel, isolation, overhead |
| **Containerization Scenarios** | List 3 scenarios | 5 | Microservices, CI/CD, hybrid cloud, spiky workloads, dev/test |
| **HPA Diagram + Explanation** | Draw diagram + explain | 5 | Draw Metrics Server → HPA Controller → Deployment → Pods flow |
| **Federated Authentication** | Concept + benefits | 5 | SAML/OIDC, IdP → SP flow, benefits list |
| **CIA Triad** | Definition + examples | 5 | Confidentiality (encryption), Integrity (hashing H1=H2), Availability (anti-DoS) |
| **IAM Best Practices** | List best practices | 5 | No root, one user per person, MFA, no shared credentials |

### 2.2 MEDIUM PROBABILity (Likely to Appear)

| Topic | Likely Question Type | Marks | Preparation |
|-------|---------------------|-------|-------------|
| **2FA Challenges** | Discussion / list | 5 | Friction, device dependency, backup, cost, SMS vulnerability |
| **Container Orchestration Role** | Analysis / roles table | 5 | Deployment, scaling, load balancing, self-healing, rolling updates |
| **Token-based Authentication** | How it works + advantages | 5 | JWT flow, stateless, scalability, cross-domain |
| **SSO Concept** | Definition + benefits | 5 | One login → multiple apps, centralized control |
| **Biometric Authentication** | Concept + examples | 5 | Fingerprint, face, retina; pros/cons |
| **VPA / Cluster Autoscaler** | Definition + comparison | 5 | VPA scales resources/pod; Cluster Autoscaler scales nodes |
| **Microservices Pros/Cons** | Table | 5 | Polyglot, scalability vs complexity, network overhead |
| **Serverless BaaS vs FaaS** | Comparison | 5 | Backend focus vs event-driven functions |
| **Strong Password Policies** | Significance discussion | 5 | Length, complexity, history, expiration, lockout |
| **CloudWatch Alarms** | States + actions | 5 | OK / INSUFFICIENT_DATA / ALARM → SNS, Auto Scaling |
| **CloudTrail Audit** | Purpose + features | 5 | API calls, 90-day history, trails to S3 |

### 2.3 LOW PROBABILITY (Possible but less likely)

| Topic | Likely Question Type | Marks |
|-------|---------------------|-------|
| **CSA Problems** | List problems | 5 |
| **Jurisdictional Issues** | Explanation | 5 |
| **Cost Estimation / Billing** | Concept | 5 |
| **SNS Publish Models** | Topic vs Direct publish | 5 |
| **Data Privacy vs Security** | Difference | 5 |
| **Availability / DoS-DDoS** | Threats + prevention | 5 |

---

## 3. QUESTION PATTERN TEMPLATES

Based on the observed patterns, future questions will likely follow these templates:

### Template A: Definition + Difference (5 marks)
> "Explain the difference between **X** and **Y**."

**Answer structure:**
1. Definition of X (2 lines)
2. Definition of Y (2 lines)
3. Comparison table (4-5 rows: basis, X, Y)
4. One-line summary

**Examples seen:** Authentication vs Authorization, Containers vs VMs, Data Privacy vs Data Security

### Template B: Three Factors / Items List (5 marks)
> "What are the **three** main **X** commonly used for **Y**?"

**Answer structure:**
1. Brief intro (1 line)
2. Numbered list: Item 1, Item 2, Item 3 (each with 1-line explanation)
3. Why it matters (1 line)

**Examples seen:** MFA factors, containerization scenarios

### Template C: Challenges & Considerations (5 marks)
> "Discuss the challenges and considerations in implementing **X**."

**Answer structure:**
1. Intro (1 line)
2. 5-6 bullet points with brief explanation
3. Mitigation/considerations (2-3 points)

**Examples seen:** 2FA implementation challenges

### Template D: Concept + Benefits (5 marks)
> "Elaborate the concept of **X** and its benefits."

**Answer structure:**
1. Definition (2 lines)
2. How it works (2-3 lines / flow)
3. Benefits (4-5 bullet points)
4. Example (1 line)

**Examples seen:** Federated authentication, SSO

### Template E: Role / Analysis (5 marks)
> "Analyse the role of **X** in managing **Y**."

**Answer structure:**
1. Definition (1 line)
2. Roles table (5-6 rows: role, explanation)
3. Concluding analysis (2 lines)

**Examples seen:** Container orchestration, IAM

### Template F: Draw + Explain (5 marks)
> "Draw and explain **X**."

**Answer structure:**
1. Neat labeled diagram (major component of marks)
2. Step-by-step explanation (4-5 steps)
3. Example scenario (1 line)

**Examples seen:** HPA, CI/CD pipeline, CloudWatch alarm flow

---

## 4. PREDICTED QUESTIONS FOR NEXT EXAM

Based on all patterns, here are the **most likely questions** with suggested answers:

### Prediction 1: Authentication vs Authorization (5 marks)
**Likely phrasing:** "Differentiate between authentication and authorization in cloud security."

**Key points to include:**
- Order: AuthN first, AuthZ second
- Tokens: ID Token vs Access Token
- Visibility: Visible vs invisible to user
- Changeability: User-changeable vs owner-controlled
- Example scenario

### Prediction 2: Containers vs Virtual Machines (5 marks)
**Likely phrasing:** "Compare and contrast containerization with traditional virtualization."

**Key points to include:**
- Guest OS: None vs full OS
- Size: MB vs GB
- Boot: Seconds vs minutes
- Overhead: Low vs high
- Isolation: OS-level vs hardware-level

### Prediction 3: Kubernetes Autoscaling (5 marks)
**Likely phrasing:** "Explain Horizontal Pod Autoscaler with a diagram" OR "What are the three types of autoscaling in Kubernetes?"

**Key points to include:**
- HPA: Scales pod replicas
- VPA: Scales CPU/memory per pod
- Cluster Autoscaler: Scales cluster nodes
- HPA diagram with Metrics Server → Controller → Deployment → Pods

### Prediction 4: Microservices Stateless vs Stateful (5 marks)
**Likely phrasing:** "Differentiate between stateless and stateful microservices."

**Key points to include:**
- Stateless: No data between requests, easier to scale
- Stateful: Maintains state in external DB (RDBMS/NoSQL)
- Examples: Calculator vs shopping cart

### Prediction 5: Serverless BaaS vs FaaS (5 marks)
**Likely phrasing:** "Explain BaaS and FaaS with examples."

**Key points to include:**
- BaaS: Backend services, focus on frontend (AWS Lambda per slides)
- FaaS: Event-driven functions, modular (Cloudflare Workers)
- Developer doesn't manage servers

---

## 5. REVISION STRATEGY BY PRIORITY

### Priority 1 — Memorize These Tables (Highest ROI)
1. Authentication vs Authorization comparison
2. Containers vs VMs comparison
3. Three MFA factors (know/have/are)
4. Three autoscalers (HPA/VPA/Cluster)
5. Stateless vs Stateful microservices

### Priority 2 — Practice Drawing Diagrams
1. HPA flow: Metrics Server → HPA Controller → Deployment → Pods
2. CIA Triad: Confidentiality → Integrity → Availability
3. Container vs VM architecture (guest OS vs shared kernel)
4. SNS Pub/Sub: One topic → multiple subscribers

### Priority 3 — Prepare List-Based Answers
1. Three containerization scenarios
2. Three microservices advantages + three disadvantages
3. Five IAM best practices
4. Five 2FA challenges
5. Five CloudWatch alarm states/actions

### Priority 4 — Concept Definitions (2-3 lines each)
1. Container, Pod, Deployment, Namespace
2. Authentication, Authorization, Federation
3. Confidentiality, Integrity, Availability
4. BaaS, FaaS, Serverless
5. CloudWatch, CloudTrail, SNS

---

## 6. MARKS DISTRIBUTION GUIDE

For 5-mark questions, aim for:

| Component | Marks | Content |
|-----------|-------|---------|
| Definition / Intro | 1 mark | Clear 1-2 line definition |
| Main body (table/list/explanation) | 3 marks | Core content with proper structure |
| Example / Conclusion | 1 mark | Real-world example or summary line |

**Diagram questions (5 marks):**
| Component | Marks |
|-----------|-------|
| Correct diagram with labels | 3 marks |
| Explanation of components | 2 marks |

---

## 7. FINAL EXAM CHECKLIST

Before the exam, ensure you can:

- [ ] Draw the AuthN vs AuthZ table from memory
- [ ] List the 3 MFA factors with examples
- [ ] Draw the Containers vs VMs comparison table
- [ ] Sketch the HPA diagram and explain each component
- [ ] List 3 containerization scenarios with reasons
- [ ] Explain federated auth flow (IdP → SP → SAML assertion)
- [ ] Define stateless vs stateful microservices with examples
- [ ] Compare BaaS vs FaaS with examples
- [ ] List 3 advantages + 3 disadvantages of microservices
- [ ] Explain CIA triad with hashing example (H1=H2)

---

**Good luck! Focus on the high-probability topics first, then cover medium-probability areas.**