# Study Notes Repository

This repository contains comprehensive study notes for multiple subjects, organized by topic.

---

## 📁 Repository Structure

```
notes---cod/
├── Cloud_Foundation_Deployment/
│   ├── Unit_III/                 # Cloud Security, Monitoring & Cost Management
│   ├── Unit_IV/                  # Containerization and Orchestration
│   └── Assignment_2/             # Term Assessment-II Exam Answers & Pattern Analysis
├── Data_Engineering/
│   ├── Unit_III/                 # Big Data Technologies and Distributed Computing
│   └── Unit_IV/                  # Data Services on Azure and AWS
├── IoT_Notes/
│   ├── Unit_III/                 # IoT Communication Protocols
│   └── Unit_IV/                  # End Nodes & Gateways for IoT
├── FastAPI_Mastery/              # FastAPI Mastery Course Lessons
│   └── fastapi-mastery/
├── Python_Crash_Course/          # Complete book notes (Eric Matthes, 3rd Ed.)
├── Aptitude_Notes/
│   ├── Reasoning/                # Blood Relations, Syllogism, Fact/Inference/Judgement
│   ├── Quantitative/             # Number System, Time & Work, Pipe & Cistern, TSD, Trains/Boats/Streams
│   └── Verbal/                   # Para Summary
├── Siri_Safari/                  # Siri → Safari Search Shortcut
└── README.md
```

---

## ☁️ Cloud Foundation & Deployment (23CSE3014)

**Institution:** MIT Art Design and Technology University, MIT School of Computing, Pune  
**Professor:** Rupesh Hushangabade  
**Academic Year:** 2026-2027 SEM-I

### Unit III — Cloud Security, Monitoring & Cost Management (8 Hours)
- [Study Guide](./Cloud_Foundation_Deployment/Unit_III/Unit_III_Study_Guide.md) | [PDF](./Cloud_Foundation_Deployment/Unit_III/Unit_III_Study_Guide.pdf)
- [Cheat Sheet](./Cloud_Foundation_Deployment/Unit_III/Cheat_Sheet_Unit_III.md) | [PDF](./Cloud_Foundation_Deployment/Unit_III/Cheat_Sheet_Unit_III.pdf)

**Topics:** Authentication vs Authorization, CIA Triad, Infrastructure Security, Data Security, IAM, Cloud Service Agreements, Cost Management, CloudWatch, SNS, CloudTrail

### Unit IV — Containerization and Orchestration (9 Hours)
- [Study Guide](./Cloud_Foundation_Deployment/Unit_IV/Unit_IV_Study_Guide.md) | [PDF](./Cloud_Foundation_Deployment/Unit_IV/Unit_IV_Study_Guide.pdf)
- [Cheat Sheet](./Cloud_Foundation_Deployment/Unit_IV/Cheat_Sheet_Unit_IV.md) | [PDF](./Cloud_Foundation_Deployment/Unit_IV/Cheat_Sheet_Unit_IV.pdf)

**Topics:** Containers, Containers vs VMs, Kubernetes, Autoscaling (HPA/VPA/Cluster), Microservices, Serverless (BaaS/FaaS)

### Assignment 2 — Term Assessment-II (Cloud Foundation 23CSE3014)
- [Exam Answers](./Cloud_Foundation_Deployment/Assignment_2/Assignment_2_Exam_Answers.md) | [PDF](./Cloud_Foundation_Deployment/Assignment_2/Assignment_2_Exam_Answers.pdf)
- [Exam Pattern & Prediction](./Cloud_Foundation_Deployment/Assignment_2/Exam_Pattern_Analysis_Prediction.md) | [PDF](./Cloud_Foundation_Deployment/Assignment_2/Exam_Pattern_Analysis_Prediction.pdf)

### Exam Answers — Data Engineering Term Assessment-II (23CSE3017)
- [Model Answers Q1–Q4](./Data_Engineering/Assignment_2/Exam_Answers_Term_Assessment_II.md) | [PDF](./Data_Engineering/Assignment_2/Exam_Answers_Term_Assessment_II.pdf)

**Pattern:** Attempt Q1 OR Q2 AND Q3 OR Q4 (each part = 5 marks, total 20 marks)

**Topics Covered:**
- Q1: Spark ETL pipeline (extract/transform/load) + AWS/Azure benefits for data engineering
- Q2: Azure Blob Storage / AWS S3 security + Hadoop batch & Spark Streaming hybrid dashboard
- Q3: Amazon Redshift data warehouse + Amazon S3 scalability/security/durability
- Q4: AWS Glue serverless ETL/ELT + Azure ADF vs AWS Glue comparison
- Quick 5-mark answer writing template

---

## 📊 Data Engineering (23CSE3017)

**Institution:** MIT Art, Design and Technology University, MIT School of Computing, Pune  
**Professor:** Dr. Aditya Pai H  
**Academic Year:** 2025-2026 SEM-I (NEP)

### Unit III — Big Data Technologies and Distributed Computing (Detailed)
- [Detailed Study Guide](./Data_Engineering/Unit_III/Unit_III_DE_Notes_Detailed.md) | [PDF](./Data_Engineering/Unit_III/Unit_III_DE_Notes_Detailed.pdf)
- [Concise Study Guide](./Data_Engineering/Unit_III/Unit_III_DE_Notes.md) | [PDF](./Data_Engineering/Unit_III/Unit_III_DE_Notes.pdf)

**Topics:** Big Data 3Vs & extended characteristics, Big Data Processing Pipeline (5 stages), Distributed Computing Frameworks need & use cases, Apache Hadoop Ecosystem deep dive (HDFS Name Node/Data Node, MapReduce Map/Reduce/shuffle/word count, YARN RM/NM/AM, PIG/HIVE/HBase/Mahout/Solr/Lucene/Zookeeper/Oozie), Apache Spark architecture (RDDs/DataFrames/Datasets, Transformations/Actions lazy vs eager), Spark vs Hadoop MapReduce, Cloud Platforms (IaaS/PaaS/SaaS, deployment models), Azure vs AWS detailed comparison, 10 exam questions with model answers, quick revision cheat sheet

### Unit IV — Data Services on Azure and AWS (Detailed)
- [Detailed Study Guide](./Data_Engineering/Unit_IV/Unit_IV_DE_Notes_Detailed.md) | [PDF](./Data_Engineering/Unit_IV/Unit_IV_DE_Notes_Detailed.pdf)
- [Concise Study Guide](./Data_Engineering/Unit_IV/Unit_IV_DE_Notes.md) | [PDF](./Data_Engineering/Unit_IV/Unit_IV_DE_Notes.pdf)

**Topics:** Azure Data Services (5 categories with supermarket analogy), Azure Data Factory deep dive (ETL vs ELT, Linked Services/Datasets/Pipelines/Activities/Triggers/Integration Runtime, pipeline creation steps, trigger types, monitoring), Azure Synapse Analytics (unified platform, SQL/Spark pools, benefits, use cases), Azure Blob Storage (block/page/append blobs, Hot/Cool/Archive tiers, containers, use cases), Azure Databricks (control plane vs data plane, capabilities, Azure ecosystem integration), AWS Data Services (databases & analytics categories), Amazon S3 (benefits, 11 nines durability, storage classes, data lake), Amazon Redshift (MPP, serverless, AQUA, security, vs traditional DW), AWS Glue (serverless ETL, Data Catalog, crawlers, Glue Studio, DataBrew, strengths/limitations), Azure vs AWS data services comparison matrix, 10 exam questions with model answers, quick revision cheat sheet

### Assignment-2 — Theory Assignment-2, Data Engineering (23CSE3017)
- [Model Answers Q1–Q5](./Data_Engineering/Assignment_2/Assignment_2_Term_Assessment.md) | [PDF](./Data_Engineering/Assignment_2/Assignment_2_Term_Assessment.pdf)

**Pattern:** 5 questions × 2 parts each, mapped to L4/CO3 and L4/CO4

**Topics Covered:**
- Q1: Spark vs Hadoop MapReduce (video-streaming low-latency); Spark RDDs vs DataFrames (telecom CDR batch)
- Q2: Azure/AWS roles in scalable distributed data engineering (insurance); Spark vs Hadoop for real-time/iterative (stock-market)
- Q3: Spark transformations & actions for social-media pipeline; Azure Data Factory vs AWS Glue comparison
- Q4: Azure Blob Storage for media metadata archiving; Amazon Redshift vs Azure Synapse for bank regulatory reports
- Q5: ADF/Glue pipeline tuning for slow Power BI dashboard; S3 → Glue → Redshift ETL flow for social-media analytics
- Quick 5-mark answer writing template

---

## 📶 IoT Notes (23CSE3013 — Internet of Things)

**Institution:** MIT Art, Design and Technology University, MIT School of Computing, Pune  
**Professor:** Prof. Ujjwala N. Salunkhe  
**Academic Year:** 2025-2026 SEM-I

### Unit III — IoT Communication Protocols (Detailed)
- [Detailed Study Guide](./IoT_Notes/Unit_III/IoT_Unit_III_Notes.md) | [PDF](./IoT_Notes/Unit_III/IoT_Unit_III_Notes.pdf)

**Topics:** IoT protocols (3Vs & characteristics), 6 protocol categories (Infrastructure, Discovery, Data, Identification, Device Management, Semantic), IPv6 (128-bit, auto-config, IPSec), RPL (DODAG, objective function), 6LoWPAN (2.4 GHz, 200 kbps, mesh), CCN (content-centric, uniquely named data), Discovery (Physical Web, mDNS, UPnP), Data (MQTT pub/sub, QoS 0/1/2, CoAP, AMQP, XMPP, WebSocket, HTTP), Identification (EPC, URI), Device Management (TR-069, OMA-DM), Semantic (JSON-LD, WoT), 10 exam questions with model answers, quick revision cheat sheet

### Unit IV — End Nodes & Gateways for IoT (Detailed)
- [Detailed Study Guide](./IoT_Notes/Unit_IV/IoT_Unit_IV_Notes.md) | [PDF](./IoT_Notes/Unit_IV/IoT_Unit_IV_Notes.pdf)

**Topics:** ESP32 (dual-core Xtensa LX6 @ 240MHz, Wi-Fi + Bluetooth, 520KB RAM), ESP8266 (single-core LX106 @ 160MHz, Wi-Fi only, 160KB RAM), comparison table, pinouts (power, ADC, DAC, touchpads, SPI, I2C, UART, GPIO, PWM), modes (STA, AP, STA+AP with code), Raspberry Pi (SBC, 40-pin GPIO header, 28 GPIO, BCM vs BOARD numbering), Python GPIO programming (RPi.GPIO), WiringPi library (C), SPI (master-slave, full-duplex, 4 modes), I2C (SDA/SCL, 7-bit/10-bit addressing, pull-up resistors), UART (serial communication), sensors (ultrasonic, PWM servo), 10 exam questions with model answers, quick revision cheat sheet

---

## 🚀 FastAPI Mastery

- [Course Repository](./FastAPI_Mastery/fastapi-mastery/)

**Lessons:** Lifecycle & Architecture, Routing & Parameters, Pydantic v2, Dependency Injection, Async & Concurrency, Errors & Middleware, Databases, Auth & Security, Testing, Architecture, Production, Advanced

---

## 🐍 Python Crash Course — Complete Notes

- [Complete Detailed Notes](./Python_Crash_Course/Python_Crash_Course_Complete_Notes.md)

**Book:** *Python Crash Course, 3rd Edition* — Eric Matthes (No Starch Press)

**Contents:** Part I — Basics (Ch. 1–11: setup, variables, lists, conditionals, dictionaries, loops, functions, classes, files, exceptions, testing) · Part II — Projects (Ch. 12–14 Alien Invasion, Ch. 15–17 Data Visualization, Ch. 18–20 Django web app) · Appendices A–E (installation, editors, getting help, Git, deployment) · master cheat sheets, top 40 mistakes, and a 30-day study plan.

---

## 📊 Aptitude Notes

### Reasoning
- [Blood Relations, Syllogism, Fact Inference Judgement](./Aptitude_Notes/Reasoning/Aptitude_Notes_Reasoning.md) | [PDF](./Aptitude_Notes/Reasoning/Aptitude_Notes_Reasoning.pdf)

### Quantitative
- [Number System, Time & Work, Pipe & Cistern, Time Speed Distance, Trains Boats Streams](./Aptitude_Notes/Quantitative/Aptitude_Notes_Quantitative.md) | [PDF](./Aptitude_Notes/Quantitative/Aptitude_Notes_Quantitative.pdf)

### Verbal
- [Para Summary Basics & Practice](./Aptitude_Notes/Verbal/Aptitude_Notes_Verbal.md) | [PDF](./Aptitude_Notes/Verbal/Aptitude_Notes_Verbal.pdf)

---

## 🎤 Siri → Safari Search Shortcut

- [Instructions](./Siri_Safari/README_Siri_Safari.md)
- [AppleScript](./Siri_Safari/Siri_Safari_Search.applescript)

---

## How to Use

1. Read the `.md` files for detailed, searchable content.
2. Download the `.pdf` files for offline reading and printing.
3. Each subject area is organized in its own folder with both markdown and PDF versions.
