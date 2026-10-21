# UNIT III — CLOUD SECURITY, MONITORING & COST MANAGEMENT

**Course:** 23CSE3014 – Cloud Foundation & Deployment  
**Class:** T.Y. AIEC (SEM-I)  
**Institution:** MIT Art Design and Technology University, MIT School of Computing, Pune  
**Academic Year:** 2026-2027 SEM-I  
**Professor:** Rupesh Hushangabade  
**Unit Duration:** 8 Hours  

---

# TABLE OF CONTENTS

1. [Authentication & Authorization](#1-authentication--authorization)
2. [CIA Triad — Confidentiality, Integrity, Availability](#2-cia-triad)
3. [Infrastructure Security](#3-infrastructure-security)
4. [Data Security & Storage](#4-data-security--storage)
5. [Identity & Access Management (IAM)](#5-identity--access-management-iam)
6. [Cloud Service Agreements (CSAs)](#6-cloud-service-agreements-csas)
7. [Commercial & Cost Management](#7-commercial--cost-management)
8. [Monitoring & Troubleshooting](#8-monitoring--troubleshooting)
9. [CloudWatch — Deep Dive](#9-cloudwatch---deep-dive)
10. [Amazon SNS & CloudTrail](#10-amazon-sns--cloudtrail)
11. [Exam Questions — Detailed Model Answers](#11-exam-questions---detailed-model-answers)
12. [Quick Revision Cheat Sheet](#12-quick-revision-cheat-sheet)

---

# 1. AUTHENTICATION & AUTHORIZATION

## 1.1 What is Authentication?

**Authentication** is the security process of verifying the identity of a user, system, or service before granting access to a system or resource. It answers the fundamental question: **"Who are you?"**

In cloud security, authentication is the **first gatekeeper**. Without successful authentication, no authorization can occur.

### How Authentication Works (Step-by-Step)

1. **Claim:** User presents credentials (username/password, biometric, token, certificate).
2. **Verification:** System checks these credentials against a stored identity store (Active Directory, LDAP, IAM user database, etc.).
3. **Validation:** If credentials match, the system issues a proof of identity — typically an **ID Token** (via OpenID Connect) or creates a session.
4. **Access Granted:** The user is now "authenticated" and can proceed to the authorization step.

### Popular Authentication Techniques

| Technique | How It Works | Example |
|-----------|--------------|---------|
| **Password-Based** | User enters username + password; system compares hash with stored value. | Logging into AWS Console with IAM user credentials |
| **Passwordless** | No password; uses magic links, email codes, or push notifications. | Slack magic link login |
| **2FA / MFA** | Requires two or more independent factors (see Section 1.3). | AWS Console login with password + Google Authenticator code |
| **Single Sign-On (SSO)** | One login gives access to multiple related applications. | Logging into Okta once, then accessing Gmail, Salesforce, AWS |
| **Social Authentication** | Uses a third-party identity provider (Google, Facebook, GitHub). | "Sign in with Google" on a third-party website |

### Authentication Protocols

- **OpenID Connect (OIDC):** An authentication layer on top of OAuth 2.0. Used to confirm user identity and obtain profile information. Issues an **ID Token**.
- **SAML (Security Assertion Markup Language):** XML-based standard for exchanging authentication/authorization data between identity providers and service providers. Common in enterprise SSO.

---

## 1.2 What is Authorization?

**Authorization** is the process of determining what an authenticated user is allowed to do or access. It answers the question: **"What permissions do you have?"**

### How Authorization Works (Step-by-Step)

1. User has already authenticated (identity proven).
2. System looks up the user's roles, groups, and policies.
3. System evaluates whether the requested action (read, write, delete, admin) is permitted.
4. Access is granted or denied based on pre-defined rules — usually enforced via roles and an **Access Token** (via OAuth 2.0).

### Popular Authorization Techniques

| Technique | How It Works | Example |
|-----------|--------------|---------|
| **RBAC (Role-Based Access Control)** | Permissions are assigned to roles; users are assigned to roles. | "Developer" role can start EC2 but not terminate it; "Admin" can do everything |
| **JWT (JSON Web Token)** | A signed token containing claims about the user; presented on each request. | API calls where frontend sends `Authorization: Bearer <JWT>` |
| **SAML Authorization** | Uses SAML assertions to convey authorization decisions alongside authentication. | Enterprise app accessing AWS via corporate AD |
| **OpenID Authorization** | Built on OIDC; combines identity and access scopes. | "Log in with Google" granting app access to your email scope |
| **OAuth 2.0 Authorization** | Industry-standard protocol for delegated authorization; issues an **Access Token**. | Letting a third-party app post to your account without giving it your password |

---

## 1.3 Authentication vs Authorization — Detailed Comparison

| Feature | Authentication | Authorization |
|---------|---------------|---------------|
| **Core Question** | "Who are you?" | "What are you allowed to do?" |
| **Order** | Happens **first** | Happens **second** (after authentication) |
| **Verifies** | Identity is genuine | Permission level is sufficient |
| **Input Needed** | Login details (username/password, biometric, token) | User's privilege, security level, role, policy |
| **Output Token** | ID Token (OIDC) | Access Token (OAuth 2.0) |
| **Can user change it?** | Yes — user can change password, reset MFA | No — only system/resource owner can change permissions |
| **Visibility** | Visible to user (login screens, MFA prompts) | Invisible to user (happens in backend) |
| **Determines** | Whether the person is a valid user | What permission the user has |

### Real-World Example

- **Authentication:** An employee enters their company badge and PIN at the office entrance turnstile. The system verifies they are a valid employee.
- **Authorization:** Once inside, the same employee tries to enter the CEO's office. The system checks their role — they are not authorized, so access is denied.

**Key Exam Point:** Authentication determines **whether** the person is a valid user. Authorization determines **what permission** the user has.

---

## 1.4 Popular Authentication Techniques (Expanded)

- Password-Based Authentication
- Passwordless Authentication
- 2FA/MFA (Two-Factor Authentication / Multi-Factor Authentication)
- Single Sign-On (SSO)
- Social authentication

### Popular Authorization Techniques (Expanded)

- Role-Based Access Controls (RBAC)
- JSON web token (JWT) Authorization
- SAML Authorization
- OpenID Authorization
- OAuth 2.0 Authorization

---

# 2. CIA TRIAD — CONFIDENTIALITY, INTEGRITY, AVAILABILITY

The **CIA Triad** is the foundational model for designing information security policies within an organization.

## 2.1 Confidentiality

**Definition:** Confidentiality ensures that only authorized individuals or systems can view sensitive or classified information. Unauthorized parties must not be able to read the data.

### The Threat
An attacker may try to capture data in transit over the network using packet sniffers, man-in-the-middle attacks, or eavesdropping tools available on the internet.

### How to Protect Confidentiality

| Method | How It Works |
|--------|--------------|
| **Encryption** | Converts plaintext into ciphertext using an algorithm and key. Even if captured, attacker cannot decrypt without the key. |
| **AES (Advanced Encryption Standard)** | Symmetric encryption standard widely used today. Strong and efficient. |
| **DES (Data Encryption Standard)** | Older symmetric encryption standard (56-bit key). Now considered weak/obsolete, replaced by AES. |
| **VPN (Virtual Private Network)** | Creates an encrypted tunnel over a public network. Data moves securely between two points as if on a private network. |

**Exam Tip:** Confidentiality is primarily achieved through **encryption**. AES and DES are encryption standards. VPNs protect data in transit.

---

## 2.2 Integrity

**Definition:** Integrity ensures that data has **not been modified, altered, or corrupted** during storage or transmission. Corruption of data = failure of integrity.

### How Integrity is Verified: Hash Functions

A **hash function** takes input data of any size and produces a fixed-length output called a **hash value** or **digest**.

#### Key Properties of Cryptographic Hashes:
- Deterministic: Same input always produces same hash.
- Fast to compute.
- One-way: Cannot reverse-engineer original data from hash.
- Avalanche effect: Tiny change in input produces completely different hash.

### The Integrity Process (Host A → Host B)

1. Host A wants to send data to Host B while maintaining integrity.
2. Host A runs a hash function over the data → produces hash **H1**.
3. Host A attaches H1 to the data and sends both.
4. Host B receives the data + H1.
5. Host B runs the **same** hash function over received data → produces hash **H2**.
6. **Comparison:** If **H1 == H2**, integrity is maintained (data was not modified). If **H1 != H2**, data was tampered with or corrupted.

### Common Hash Algorithms

| Algorithm | Bit Length | Status |
|-----------|------------|--------|
| **MD5** (Message Digest 5) | 128-bit | Considered cryptographically broken / weak; avoid for security |
| **SHA** (Secure Hash Algorithm) | 160-bit (SHA-1) | Better than MD5, but SHA-2/SHA-3 recommended today |

**Exam Tip:** To check integrity, compare hash values before and after transmission. H1 = H2 means no modification.

---

## 2.3 Availability

**Definition:** Availability means the network, systems, and data should be readily accessible to authorized users when needed.

### Ensuring Availability

- Maintain hardware (replace failing disks, servers).
- Regular upgrades and patches.
- **Fail-over plan:** If one server goes down, another takes over automatically (redundancy).
- Prevent bottlenecks (load balancing, sufficient bandwidth).

### Threats to Availability

- **DoS (Denial of Service):** Attacker floods target with traffic to exhaust resources, making it unavailable to legitimate users.
- **DDoS (Distributed Denial of Service):** Multiple compromised systems (botnet) attack a single target simultaneously — much harder to block.

### Business Impact
When a network goes down, companies and users who rely on it for business operations suffer significant financial and reputational loss.

**Exam Tip:** Availability is about **uptime and access**. Protect against DoS/DDoS with redundancy, fail-over, and traffic filtering.

---

# 3. INFRASTRUCTURE SECURITY

Cloud infrastructure security is a framework for safeguarding cloud resources against internal and external threats. It protects computing environments, applications, and sensitive data from unauthorized access by **centralizing authentication** and **limiting authorized users' access to resources**.

There are **three levels** of protection:

## 3.1 Network Level Protection

Protects against malicious activity by enforcing security policies on traffic flowing **in and out of your virtual networks**.

| AWS Service | What It Does |
|-------------|--------------|
| **Security Groups** | Host-based **stateful** firewall for EC2 instances. Controls inbound/outbound traffic at instance level. (Stateful = remembers connection state; if you allow inbound, response is automatically allowed out.) |
| **Network ACLs (NACLs)** | **Stateless** firewall for VPC subnets. Controls traffic at subnet level. Must explicitly define both inbound AND outbound rules. |
| **AWS Network Firewall** | Stateful inspection, intrusion prevention, and web filtering for your VPC. Managed firewall service. |
| **Amazon Route 53 Resolver DNS Firewall** | Blocks malicious DNS queries when using Route 53 Resolver for DNS resolution. Stops malware from calling home via DNS. |
| **AWS Shield Standard** | Always-on detection and automatic inline mitigation for common network and transport layer DDoS attacks. Free for all AWS customers. |
| **AWS WAF (Web Application Firewall)** | Protects against common web exploits (SQL injection, cross-site scripting/XSS) that may affect availability, compromise security, or consume excessive resources. |

**Exam Tip:** Security Groups = instance-level, stateful. NACLs = subnet-level, stateless. WAF = application layer (HTTP/HTTPS). Shield = network/transport layer DDoS.

---

## 3.2 Host Level Protection

Secures the **virtual server / host itself** (the operating system and running services).

### Key Practices for Cloud Host Security

| Practice | Description |
|----------|-------------|
| **Host Hardening** | Turn off unused services, close default ports, remove unnecessary software. Reduces possible entry points for attackers (smaller attack surface). |
| **Patch Management** | Install regular security updates and software fixes for OS and applications. Stops hackers from exploiting known vulnerabilities (CVEs). |
| **Access Controls** | Require Multi-Factor Authentication (MFA), use strong SSH keys instead of simple passwords, apply **least privilege** (limit user permissions to only what they need). |
| **Intrusion Detection Systems (IDS)** | Monitoring tools that watch host activities and detect strange behaviors or signs of a break-in. |
| **Antivirus & Endpoint Protection** | Advanced security software to scan, block, and remove malicious files or ransomware on the virtual server. |

**Exam Tip:** Host hardening = reduce attack surface by disabling unused services and closing ports.

---

## 3.3 Application Level Protection

Protects against **web-based attacks targeted at your applications**.

Common application attacks:
- SQL Injection
- Cross-Site Scripting (XSS)
- Cross-Site Request Forgery (CSRF)
- Broken authentication
- Insecure direct object references

Protection methods:
- Input validation and sanitization
- Web Application Firewall (WAF)
- Secure coding practices
- Regular penetration testing

---

# 4. DATA SECURITY & STORAGE

## 4.1 Data Privacy vs Data Security

| | **Data Privacy** | **Data Security** |
|---|------------------|-------------------|
| **Focus** | Proper handling, processing, storage, and usage of personal information | Protecting personal data from unauthorized access, malicious attacks, exploitation |
| **Core Question** | What are individuals' rights over their data? | How do we technically protect the data? |
| **Goal** | Uphold rights of individuals concerning their personal information | Ensure data privacy through methods and techniques |

**Simplified:** Privacy = the **right/policy**; Security = the **technical enforcement**.

---

## 4.2 Jurisdictional Issues Raised by Data Location

**Concept:** Cloud service providers locate their data centers in various geographic regions to:
- Reduce operational costs
- Optimally serve customers on a global scale (low latency, local presence)

**The Problem:** The physical location of data determines which country's laws apply to it. This creates **jurisdictional issues**:
- Data stored in the EU is subject to GDPR.
- Data stored in the US may be subject to CLOUD Act, Patriot Act, etc.
- Data stored in India may be subject to the Digital Personal Data Protection Act.

**Implications:**
- Compliance becomes complex when data crosses borders.
- A company in India storing EU citizens' data on a US server must comply with both Indian and EU laws.
- Legal disputes may arise about which courts have jurisdiction.

---

# 5. IDENTITY & ACCESS MANAGEMENT (IAM)

## 5.1 What is IAM?

**Definition:** IAM enables you to securely control access to AWS services and resources for your users. You control **who can do what, and from where.**

### IAM Components
- **IAM Users:** Individual identities with credentials (password, access keys).
- **IAM Groups:** Collections of users; permissions applied to the group apply to all members.
- **IAM Roles:** Identities with permissions that can be assumed by users, services, or applications (no long-term credentials).
- **Policies:** JSON documents that define what each user, group, or role can and cannot do.

## 5.2 IAM Best Practices (The "IAM Brain Dump")

1. **Never use ROOT IAM credentials** except for initial account setup.
   - The Root account has unrestricted access to everything (like root/admin in Windows/Linux).
   - If compromised, attacker owns your entire AWS account.
2. **One IAM User per PHYSICAL PERSON.** Do not share accounts.
3. **One IAM Role per Application.** Don't reuse roles across unrelated apps.
4. **IAM credentials should NEVER BE SHARED.**
5. **Never write IAM credentials in code.** Use IAM Roles for EC2, Lambda, etc., instead of hardcoding access keys.

### IAM Features
- Shared access to your AWS account
- Granular permissions (allow/deny specific actions on specific resources)
- Multi-Factor Authentication (MFA) support
- **Free to use** (pay for underlying services, not IAM itself)
- Global view (IAM is global, not region-specific)
- Predefined "managed policies" (e.g., `ReadOnlyAccess`, `AdministratorAccess`)
- Password policies and access key management
- Fine-grained control over users, groups, roles, and permissions

## 5.3 IAM Federation

Big enterprises usually already have their own repository of users (e.g., Microsoft Active Directory, LDAP). Instead of creating separate IAM users, they **federate** their existing directory with AWS IAM.

- Employees log in to AWS using their **company credentials**.
- Uses the **SAML standard** (Security Assertion Markup Language).
- Benefits: Single corporate login, centralized user management, no duplicate IAM users.

## 5.4 Access Control (Roles and Policies)

Access control defines who can access which resources and perform which actions.

- **Policies are JSON documents.** Example structure:
```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": "ec2:DescribeInstances",
      "Resource": "*"
    }
  ]
}
```
- **Roles vs Policies:** Policies are the rules. Roles are identities that assume those rules temporarily (e.g., an EC2 instance assuming a role to access S3).

---

# 6. CLOUD SERVICE AGREEMENTS (CSAs)

A **Cloud Service Agreement (CSA)** is the contract between an organization and its cloud service provider.

## Why CSAs Matter
They are at the **front line of protecting privacy and security of personal data.**

### Key Scenarios
1. Organizations use cloud services to store personal data.
2. The individuals whose data is stored are **not direct parties** to the CSA — they have no say in the agreement.
3. If an organization has an **inadequate CSA**, customer data will not be sufficiently protected.
4. Cloud provider negligence or wrongdoing can lead to **law violations and data breaches**.
5. The **organization is liable** for the failings of its cloud service providers.

### Therefore, Adequate CSAs Are Essential For:
- Protecting personal data
- Complying with privacy and security laws
- Meeting regulatory obligations

### Common Problems With CSAs
1. **Lack of Knowledge:** Organizations don't fully understand what they're signing.
2. **Lack of Bargaining Power:** Large providers offer take-it-or-leave-it contracts; small organizations can't negotiate.
3. **Lack of Internal Coordination:** Legal, security, and procurement teams don't align on requirements.

---

# 7. COMMERCIAL & COST MANAGEMENT

## The Cloud Economic Model

| Traditional (On-Premise) | Cloud Computing |
|--------------------------|-----------------|
| Fixed expenses (data centers, physical servers, upfront CapEx) | Variable expenses — pay only for IT as you consume it (OpEx) |
| You pay for peak capacity whether you use it or not | You pay only for what you actually use |
| Economies of scale favor large enterprises only | Economies of scale from cloud providers make variable costs lower than doing it yourself |

**Key Point:** The cloud lets you trade **fixed expenses** for **variable expenses**. Because cloud providers operate at massive scale, their variable expenses are much lower than what you'd pay to build and maintain your own data center.

### Cost Management Topics
- **Strategies:** Right-sizing instances, choosing appropriate pricing models (On-Demand, Reserved, Spot), tagging resources for cost allocation.
- **Budgeting:** Setting spending limits and alerts.
- **Optimization:** Continuously reviewing usage to eliminate waste (unused volumes, idle load balancers, over-provisioned instances).
- **Cost Estimations:** Using pricing calculators to forecast monthly bills.
- **Billing & Accounting:** Detailed invoices, cost explorer, consolidated billing for organizations with multiple accounts.

---

# 8. MONITORING & TROUBLESHOOTING

This section focuses on **Amazon CloudWatch**, **Amazon SNS**, and **AWS CloudTrail**.

---

# 9. CLOUDWATCH — DEEP DIVE

**CloudWatch** provides metrics for **every service in AWS**. It is AWS's native monitoring and observability service.

## Core Concepts

| Concept | Definition |
|---------|------------|
| **Metric** | A variable to monitor. Examples: `CPUUtilization`, `DiskReadBytes`, `NetworkIn`. |
| **Namespace** | A container for metrics. Isolates metrics from different services (e.g., `AWS/EC2`, `AWS/S3`). |
| **Dimension** | An attribute of a metric used to segment/filter it. Example: `InstanceId`, `Environment`, `AutoScalingGroupName`. |
| **Timestamp** | Every metric data point has a time associated with it. |

**Rule:** Up to 10 dimensions per metric.

## Basic vs Detailed Monitoring

| Feature | Basic Monitoring | Detailed Monitoring |
|---------|------------------|---------------------|
| Frequency | Every **5 minutes** | Every **1 minute** |
| Cost | Free | Extra cost |
| Free Tier | N/A | AWS Free Tier allows **10 detailed monitoring metrics** at no charge |

## CloudWatch Features

### 1. CloudWatch Custom Metrics
- You can define and send your own metrics to CloudWatch.
- Use dimensions to segment metrics (e.g., by `Instance.id`, `Environment.name`).
- API call used: `PutMetricData`.

### 2. CloudWatch Dashboards
- Customizable visual dashboards for quick access to key metrics.
- **Global** — not tied to one region.
- Can include graphs from **different regions**.
- You can change time zone and time range.
- Automatic refresh options: 10s, 1m, 2m, 5m, 15m.

### 3. CloudWatch Logs
Applications can send logs to CloudWatch using the SDK. CloudWatch collects logs from:
- **VPC Flow Logs** — VPC-specific network traffic logs.
- **CloudTrail** — API call logs.
- **CloudWatch Log Agents** — installed on EC2 machines to send OS/application logs.
- **AWS Lambda** — function execution logs.

### 4. Log Groups and Log Streams
- **Log Group:** An arbitrary name, usually representing an application (e.g., `/aws/lambda/my-function`).
- **Log Stream:** Instances within an application, log files, or containers. A stream must exist in **only one log group**.

### 5. CloudWatch Alarms
Alarms trigger notifications or actions when a metric crosses a threshold.

| Alarm State | Meaning |
|-------------|---------|
| **OK** | The metric is within the defined threshold. |
| **INSUFFICIENT_DATA** | Alarm just started, metric unavailable, or not enough data. |
| **ALARM** | The metric is outside the defined threshold (problem detected). |

Alarms can send notifications to:
- **SNS** (Simple Notification Service)
- **Auto Scaling** (scale up/down)
- **EC2 Actions** (stop, reboot, terminate)

### 6. CloudWatch Events
Event-driven automation using the pattern: **Source + Rule → Target**

- **Schedule:** Cron jobs (e.g., "run Lambda every night at 2 AM").
- **Event Pattern:** React to a service doing something (e.g., "when an EC2 instance state changes to stopped").
- **Targets:** Lambda functions, SQS queues, SNS topics, etc.
- CloudWatch Events creates a small **JSON document** describing what changed.

---

# 10. AMAZON SNS & CLOUDTRAIL

## 10.1 Amazon SNS (Simple Notification Service)

**SNS** is a **pub/sub** (publish/subscribe) messaging service.

### The Problem It Solves
"What if you want to send **one message to many receivers**?"

### Architecture
```
Event Producer
       |
       v
   SNS Topic  <--- Only ONE topic
       |
   +---+---+---+---+---+
   |   |   |   |   |   |
 Subscribers (up to 10,000,000 per topic)
```

### Subscriber Types
- SQS queues
- HTTP / HTTPS endpoints
- Lambda functions
- Email addresses
- SMS messages
- Mobile push notifications

### Limits
- Up to **10,000,000 subscriptions per topic**
- Up to **100,000 topics** limit

### Publish Models
1. **Topic Publish (AWS server, using SDK):**
   - Create a topic → Create subscription(s) → Publish to topic.
2. **Direct Publish (for mobile apps SDK):**
   - Create platform application → Create platform endpoint → Publish to endpoint.

### SNS Integrations
Services that can send data directly to SNS:
- CloudWatch (for alarm notifications)
- Auto Scaling Groups (instance launch/termination notifications)
- Amazon S3 (bucket events like object creation/deletion)
- CloudFormation (stack state changes — e.g., failed to build)

---

## 10.2 AWS CloudTrail

**CloudTrail** is a web service that records AWS API calls for your account and delivers log files to you.

### What Is Recorded
- Identity of the API caller
- Time of the API call
- Source IP address of the caller
- Request parameters
- Response elements returned by the AWS service

### CloudTrail Features

| Feature | Details |
|---------|---------|
| **Event History** | View and search the last **90 days** of events in CloudTrail console or AWS CLI. |
| **Download Events** | Download CSV or JSON file of up to past 90 days of CloudTrail events. |
| **Create a Trail** | Enables CloudTrail to deliver log files to your Amazon S3 bucket. By default applies to all regions; logs all regions in the AWS partition. |
| **SNS Notifications** | Subscribe to an SNS topic to receive notifications about log file delivery to your bucket. |
| **IAM Permissions** | Use IAM to manage who can create/configure/delete trails, start/stop logging, and access S3 buckets with logs. |

**Exam Tip:** CloudTrail = audit trail of **who did what, when, and from where** in your AWS account. Critical for security auditing and compliance.

---

# 11. EXAM QUESTIONS — DETAILED MODEL ANSWERS

Your slide deck lists these 10 questions. Here are detailed answers for each.

---

### Q1. Define authentication in the context of computer security.

**Answer:**
Authentication is the security process of verifying the identity of a user, system, or service before granting access to a system or resource. It ensures that the entity attempting access is who it claims to be. In computer security, authentication typically involves validating credentials such as usernames and passwords, biometric data, security tokens, or digital certificates against a trusted identity store. Once authentication succeeds, the system establishes a trusted session for that identity. It answers the fundamental question: **"Who are you?"**

---

### Q2. Explain the difference between authentication and authorization.

**Answer:**

| Basis | Authentication | Authorization |
|-------|---------------|---------------|
| Definition | Verifies identity ("Who are you?") | Verifies permissions ("What can you access?") |
| Sequence | Occurs first | Occurs after authentication |
| What it checks | Login credentials are valid | User has rights to perform requested action |
| Tokens | ID Token (e.g., via OpenID Connect) | Access Token (e.g., via OAuth 2.0) |
| User control | User can change credentials (password, MFA) | User cannot change permissions; only owner/admin can |
| Visibility | Visible to user (login screens, prompts) | Invisible to user (backend enforcement) |
| Example | Employee enters badge and PIN at office door | System checks if employee is allowed into server room |

**Summary:** Authentication determines **whether** a person is a valid user. Authorization determines **what permission** that authenticated user has.

---

### Q3. What are the three main factors commonly used for multi-factor authentication?

**Answer:**
Multi-Factor Authentication (MFA) requires two or more independent credentials from different categories. The three main factors are:

1. **Something you KNOW** — A password, PIN, or answer to a security question.
2. **Something you HAVE** — A physical item like a smartphone (for OTP apps), security token, smart card, or hardware key (e.g., YubiKey).
3. **Something you ARE** — A biometric characteristic such as fingerprint, face recognition, iris/retina scan, or voice recognition.

Using two or more of these factors together significantly reduces the risk of unauthorized access, because an attacker would need to compromise multiple independent factors.

---

### Q4. Discuss the significance of strong password policies in authentication.

**Answer:**
Strong password policies are critical because passwords remain the most common authentication factor and are frequently targeted by attackers. A strong password policy typically enforces:

- **Minimum length** (e.g., 12+ characters) to resist brute-force attacks.
- **Complexity requirements** — mix of uppercase, lowercase, numbers, and special characters to resist dictionary attacks.
- **Password history** — prevents reuse of previous passwords.
- **Password expiration** — forces periodic changes to limit the window of exposure if a password is compromised.
- **Account lockout** — locks the account after a defined number of failed login attempts, preventing automated brute-force or credential-stuffing attacks.

**Significance:** Weak or reused passwords are a leading cause of data breaches. Strong policies reduce the likelihood of credential guessing, spraying, and stuffing attacks, thereby strengthening the authentication layer of the CIA triad (specifically confidentiality and integrity).

---

### Q5. Explain the concept of biometric authentication and provide examples.

**Answer:**
Biometric authentication is a method of verifying identity based on unique biological or behavioral characteristics of an individual. Instead of something you know (password) or have (token), it uses **something you are**.

Because biometric traits are difficult to forge or steal compared to passwords, they provide strong authentication. However, they raise privacy concerns and cannot be changed if compromised (unlike a password).

**Examples:**
- **Fingerprint scanning** — used in smartphones, laptops, and access control systems.
- **Face recognition / facial ID** — used in modern smartphones (Face ID), airport border control.
- **Retina / iris scan** — used in high-security government and research facilities.
- **Voice recognition** — used in telephone banking and voice assistants.
- **Hand geometry / vein pattern** — used in some physical access systems.

---

### Q6. What is Single Sign-On (SSO), and how does it enhance user authentication?

**Answer:**
Single Sign-On (SSO) is an authentication scheme that allows a user to log in once with a single set of credentials and gain access to multiple related but independent software systems or applications without being prompted to log in again at each one.

**How it works:** The user authenticates with an Identity Provider (IdP). The IdP issues a token or assertion that service applications trust, granting access based on that token.

**How SSO enhances authentication:**
- **Improved user experience:** Users remember only one set of credentials.
- **Reduced password fatigue:** Less likelihood of users writing down passwords or reusing weak passwords across apps.
- **Centralized access control:** IT can grant/revoke access to all connected applications from one place (e.g., when an employee leaves the company).
- **Stronger security posture:** Enables enforcement of MFA and strong password policies at a single point.
- **Faster access:** Reduces time spent logging into multiple systems.

---

### Q7. Discuss the challenges and considerations in implementing two-factor authentication.

**Answer:**
While 2FA/MFA significantly improves security, implementing it presents several challenges:

1. **User resistance and friction:** Users may find the extra step inconvenient, leading to poor adoption or workarounds.
2. **Device dependency:** If the second factor is a smartphone (SMS or authenticator app), losing or damaging the phone can lock the user out.
3. **Backup and recovery:** Organizations must have secure processes to help users who lose their second factor (e.g., backup codes, identity verification).
4. **Cost:** Hardware tokens, SMS gateways, and MFA infrastructure incur licensing and operational costs.
5. **Integration with legacy systems:** Older applications may not support modern MFA protocols (OIDC, SAML, FIDO2), requiring custom adapters.
6. **Security of the second factor itself:** SMS-based OTPs are vulnerable to SIM-swapping attacks; authenticator apps are more secure but still require device security.
7. **Accessibility:** Some users with disabilities may find certain biometric or hardware factors difficult to use.

**Considerations:** Choose phishing-resistant factors (authenticator apps, hardware keys over SMS), provide backup methods, train users, and enforce MFA for privileged accounts first.

---

### Q8. How does token-based authentication work, and what are its advantages?

**Answer:**
Token-based authentication is a stateless authentication mechanism where the server issues a signed token to the client after successful login. The client then sends this token with every subsequent request to prove its identity.

**How it works (step-by-step):**
1. Client sends credentials (username/password) to the authentication server.
2. Server validates the credentials.
3. If valid, server generates a token (commonly a **JSON Web Token — JWT**) containing claims (user ID, roles, expiry) and signs it with a secret key.
4. Server sends the token to the client.
5. Client stores the token (typically in local storage or a cookie) and includes it in the `Authorization: Bearer <token>` header of every request.
6. The receiving server validates the token's signature and extracts claims without needing to query a database or session store.

**Advantages:**
- **Stateless:** The server does not need to store session data, making it highly scalable.
- **Decoupled:** Authentication can happen in one service, and tokens can be validated by many different services (microservices architecture).
- **Cross-domain / mobile friendly:** Tokens work well with APIs, SPAs, and mobile apps where cookies are difficult to use.
- **Performance:** No server-side session lookup on every request — just token verification.
- **Expiry control:** Tokens have built-in expiration times, limiting exposure if stolen.

---

### Q9. Explain the concept of federated authentication and its benefits.

**Answer:**
Federated authentication is a trust relationship between two or more identity systems that allows a user to authenticate once with their home identity provider (IdP) and access services in another domain or organization without creating a separate account.

**How it works:** The user's home organization (e.g., a company using Active Directory) acts as the IdP. When the user tries to access a cloud service (Service Provider, e.g., AWS), the SP redirects them to the IdP. The IdP authenticates the user and sends a signed assertion (commonly using **SAML** or **OIDC**) back to the SP, which grants access based on that assertion.

**Benefits:**
- **Single identity across organizations:** Users don't need separate accounts for every cloud service.
- **Centralized user management:** When an employee joins or leaves, access is managed in one directory (e.g., AD), not dozens of cloud consoles.
- **Improved security:** Enforces the corporate password policy and MFA at the IdP level.
- **Better user experience:** Seamless access using existing corporate credentials (SSO across trust boundaries).
- **Compliance:** Easier to audit access because all authentication flows through a central IdP.

**Example:** Big enterprises integrate their own user repository with AWS IAM using SAML (Active Directory federation), so employees log into AWS using company credentials.

---

### Q10. Discuss common threats and vulnerabilities related to authentication mechanisms.

**Answer:**
Authentication mechanisms face numerous threats:

1. **Phishing:** Attackers trick users into entering credentials on fake login pages, stealing usernames and passwords.
2. **Credential Stuffing:** Using leaked username/password pairs from one breach to attempt login on other services (exploits password reuse).
3. **Brute-force / Dictionary Attacks:** Automated guessing of passwords, especially weak or common ones.
4. **Session Hijacking:** Stealing session cookies or tokens after authentication to impersonate the user without needing credentials.
5. **Man-in-the-Middle (MitM):** Intercepting credentials or tokens in transit if communication is not encrypted (no HTTPS/TLS).
6. **Weak or Default Passwords:** Factory-default credentials (e.g., admin/admin) that are never changed.
7. **Token Theft:** Stealing JWTs, access tokens, or API keys from client-side storage or logs.
8. **MFA Bypass / SIM Swapping:** Attackers hijack a user's phone number to receive SMS-based OTPs.
9. **Credential Reuse:** Using the same password across multiple services means one breach compromises all.
10. **Insufficient Logging/Monitoring:** Failed login attempts not detected or alerted, allowing brute-force attacks to continue undetected.

---

# 12. QUICK REVISION CHEAT SHEET

Print this mentally before the exam:

| Topic | One-Liner to Remember |
|-------|----------------------|
| **Authentication** | Verifies identity — "Who are you?" — happens first, uses ID Token/OIDC, visible, user-changeable. |
| **Authorization** | Checks permissions — "What can you do?" — happens after, uses Access Token/OAuth 2.0/RBAC/JWT, invisible, owner-controlled. |
| **CIA** | Confidentiality = encryption (AES/DES/VPN). Integrity = hashing (SHA/MD5, H1=H2). Availability = uptime, anti-DoS. |
| **MD5 vs SHA** | MD5 = 128-bit (weak). SHA = 160-bit. Hash verifies integrity. |
| **Security Groups** | Instance-level, **stateful** firewall (EC2). |
| **NACLs** | Subnet-level, **stateless** firewall (VPC). |
| **AWS WAF** | Stops web exploits (SQLi, XSS). |
| **AWS Shield** | Always-on DDoS protection (network/transport layer). |
| **IAM Root** | Never use daily; like admin/root; one person = one IAM user. |
| **IAM Federation** | SAML-based; company AD → AWS; employees use corporate credentials. |
| **IAM Policies** | JSON documents defining what users/roles can/cannot do. |
| **CloudWatch Metric** | Variable to monitor; Namespace = container; Dimension = attribute (max 10). |
| **Basic vs Detailed Monitoring** | Basic = 5 min, free. Detailed = 1 min, paid (10 free in Free Tier). |
| **CloudWatch Alarms** | States: OK / INSUFFICIENT_DATA / ALARM. Actions: SNS, Auto Scaling, EC2. |
| **CloudWatch Logs** | Log Group = app name; Log Stream = instance/file inside group (one group only). |
| **CloudWatch Events** | Source + Rule → Target (cron or event pattern). |
| **SNS** | Pub/Sub: one topic → up to 10M subscribers (SQS, Email, SMS, Lambda, HTTP). |
| **CloudTrail** | API audit log; last 90 days event history; trails deliver logs to S3; IAM controls access. |
| **CSA** | Cloud Service Agreement — protects data privacy; org is liable for provider failings. |
| **Jurisdiction** | Laws of the country where data physically resides apply to that data. |

---

# 13. SELF-TEST / PRACTICE QUESTIONS

Try answering these before checking the key:

1. **True/False:** Authorization happens before authentication.
2. **True/False:** H1 = H2 means data integrity is maintained.
3. **Multiple choice:** Which AWS service is a **stateless** firewall for VPC subnets? (A) Security Groups (B) NACLs (C) WAF (D) Shield
4. **Multiple choice:** Which hash is 128-bit and considered weak? (A) SHA-1 (B) MD5 (C) AES (D) RSA
5. **Short answer:** What is the maximum number of dimensions per CloudWatch metric?
6. **Short answer:** How many days of CloudTrail event history can you view without creating a trail?
7. **Short answer:** Name two subscriber types for SNS.
8. **Scenario:** An employee logs into AWS using their corporate Active Directory password. What IAM feature is this?

**Answer Key:**
1. False (authentication is first)
2. True
3. B (NACLs)
4. B (MD5)
5. 10 dimensions
6. 90 days
7. SQS, Email, SMS, Lambda, HTTP/HTTPS (any two)
8. IAM Federation (SAML)

---

# 14. FINAL EXAM STRATEGY

1. **Memorize the Authentication vs Authorization table** — this is almost certainly a 5-10 mark question.
2. **Know the CIA triad with examples** — especially hashing for integrity (H1=H2) and encryption for confidentiality.
3. **Know Security Groups vs NACLs** — stateful vs stateless, instance vs subnet.
4. **Know IAM best practices** — no root, one user per person, MFA, federation via SAML.
5. **Know CloudWatch basics** — metrics, namespaces, dimensions, Basic vs Detailed, Alarm states.
6. **Know SNS pub/sub** and **CloudTrail audit** purpose.
7. **Practice writing out the 10 slide questions** as full answers — they are likely the actual exam questions.

---

**Good luck with your exam!** If you need any section explained with more examples or want to be quizzed, just ask.