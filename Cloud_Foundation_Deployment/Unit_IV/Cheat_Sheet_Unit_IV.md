# UNIT IV CHEAT SHEET — Containerization and Orchestration

**Course:** 23CSE3014 — Cloud Foundation & Deployment  
**Class:** T.Y. AIEC (SEM-I) | MIT School of Computing, Pune | AY 2026-27  
**Professor:** Rupesh Hushangabade  

---

## 1. INTRODUCTION TO CONTAINERS

**Container:** Unit of software packaging code + required dependencies, running in an isolated, controlled environment.

**Key traits:**
- Predictable — runs same way every time
- Repeatable — same across dev/test/prod
- Portable — same on any machine (laptop, server, cloud)
- Solves "works on my machine" problem

---

## 2. CONTAINERS vs VIRTUAL MACHINES (VMs)

| Feature | Containers | Traditional VMs |
|---------|-----------|-----------------|
| Virtualization | OS-level (shares host kernel) | Hardware-level (hypervisor) |
| Guest OS | None | Full guest OS per VM |
| Size | Megabytes (MB) | Gigabytes (GB) |
| Boot time | Seconds | Minutes |
| Resource overhead | Low | High |
| Density | Many per host | Few per host |
| Isolation | Namespaces/cgroups | Separate kernel (stronger) |

**Key:** Containers share host OS kernel → lightweight, fast. VMs run full guest OS → heavy, slow.

---

## 3. BENEFITS OF CONTAINERIZATION

- **Cost efficiency:** Higher density, lower infrastructure cost
- **Agility:** Fast startup/shutdown, rapid deployment
- **Scalability:** Easy to replicate, horizontal scaling
- **Reliability:** Consistent behavior across environments, isolated failures
- **Resource efficiency:** Lower CPU/memory consumption than VMs

---

## 4. CONTAINER ECOSYSTEM

- **Container images:** Read-only template built from Dockerfile
- **Registry/Repository:** Stores images (e.g., Docker Hub, Amazon ECR)
- **Data volumes:** Persistent storage outliving the container
- **Networking:** Integrated virtual networks, container-to-container communication

---

## 5. CREATING & MANAGING CONTAINERS (Docker)

**Lifecycle:** Build → Ship → Run → Manage → Destroy

**Common commands:**
- `docker build -t my-app:1.0 .` — build image
- `docker run -d -p 5000:5000 my-app:1.0` — run container
- `docker ps` — list containers
- `docker stop / rm` — stop/remove container
- `docker push` — upload to registry

**Dockerfile instructions:** FROM, COPY, RUN, CMD/ENTRYPOINT, EXPOSE

---

## 6. KUBERNETES (K8s)

**Kubernetes:** Open-source system for automating deployment, scaling, and management of containerized applications.

**Run K8s Anywhere:** On-premises, hybrid, public cloud — effortless workload movement.

**Core concepts:**
- **Pod:** Smallest deployable unit; 1+ containers sharing storage/network
- **Node:** Worker machine running pods
- **Cluster:** Set of nodes managed by Kubernetes
- **Deployment:** Manages pod replicas, rollouts, rollbacks
- **Replication Controller:** Group of pods treated as single unit
- **Service:** Exposes application on pods as network service
- **Namespace:** Virtual cluster for multi-tenancy

---

## 7. AUTOSCALING IN KUBERNETES

**Autoscaling:** Automatically adjusts pod count based on demand/resource availability.

| Autoscaler | Scales What | Use Case |
|------------|-------------|----------|
| **HPA** | Number of pod replicas | More/fewer instances based on load |
| **VPA** | CPU/memory per pod | Individual pods need more/fewer resources |
| **Cluster Autoscaler** | Cluster nodes/pods | Whole cluster grows/shrinks |

### HPA (Horizontal Pod Autoscaler)
- Scales number of pods in Deployment/Replication Controller
- Configured as K8s resource; target metric (e.g., CPU 50%)
- Metrics Server collects usage; HPA controller compares vs target
- Scale out if above target, scale in if below

### VPA (Vertical Pod Autoscaler)
- Scales CPU/memory limits of a pod type
- Scale field = max pods; Target utilization = % of resource limit

---

## 8. MICROSERVICES ARCHITECTURE

**Definition:** Software architecture structuring app as collection of single-function, independent services.

**Traits:**
- Single-function focus
- Independent environment & deployment
- Loose coupling via APIs/communication protocols
- Follows SOA (Service-Oriented Architecture) principles

---

## 9. STATELESS vs STATEFUL MICROSERVICES

| Aspect | Stateless | Stateful |
|--------|-----------|----------|
| Data between requests | None kept | Maintained in external DB |
| Remembers past requests | No | Yes |
| Scalability | Easier (any instance handles any request) | Harder (state must be synced) |
| Complexity | Simpler | More complex (needs external store) |
| Example | Calculator API | Shopping cart |

**Stateful stores state externally:** RDBMS (MySQL, PostgreSQL) or NoSQL (MongoDB, DynamoDB)

---

## 10. MICROSERVICES — PROS & CONS

**Advantages:**
- Polyglot development (different languages/platforms per service)
- Better scalability (scale only needed services)
- Faster time to market, faster CI/CD
- Easier deployment and debugging
- Platform and language agnostic

**Disadvantages:**
- More collaboration needed (full lifecycle per team)
- Difficult to test and monitor (complex architecture)
- Poorer performance (network communication overhead)
- Harder network maintenance (load balancing, fault tolerance)

---

## 11. SERVERLESS COMPUTING

**Definition:** Cloud model providing backend services on pay-as-you-go basis; developer writes code without managing servers.

**Provider manages:** Machine/container management, hardware assignment, backend tasks.

**Two types:**

| Type | Description | Example (per slides) |
|------|-------------|---------------------|
| **BaaS** (Backend-as-a-Service) | Third-party backend; focus on frontend | AWS Lambda |
| **FaaS** (Function-as-a-Service) | Event-driven functions, modular architecture | Cloudflare Workers |

> *Note: "Serverless" ≠ no servers; it means developer doesn't manage them.*

---

## 12. EXAM QUESTIONS — QUICK ANSWERS

1. **Containers** = unit of software packaging code + dependencies, isolated environment, OS-level virtualization.
2. **Containers vs VMs:** Containers share host kernel (light, seconds, MBs). VMs have guest OS (heavy, minutes, GBs).
3. **Creating/managing containers:** Dockerfile → build → registry → run → manage → destroy.
4. **Containerization vs VM:** OS-level vs hardware-level virtualization; shared kernel vs separate kernel.
5. **Docker container:** Dockerfile → `docker build` → `docker run` → `docker ps/stop/rm`.
6. **Deploying in containerized env:** Containerize → store image → provision host → deploy → network → storage → monitor → scale.
7. **Containerization scenarios:** Microservices, CI/CD, hybrid/multi-cloud, spiky workloads, dev/test, cost optimization.
8. **Scalability benefits:** Rapid scaling, high density, granular scaling, autoscaling integration, resource efficiency, cost-effective.
9. **Container orchestration:** Automated management of containers across cluster; deployment, scaling, load balancing, self-healing, rolling updates, service discovery, resource mgmt.
10. **Security: containers vs VMs:** VMs stronger isolation (separate kernel). Containers share kernel → container-escape risk; need image scanning, non-root users, network policies.

---

*Print this before the exam. Good luck!*