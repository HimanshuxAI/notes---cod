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
├── FastAPI_Mastery/              # FastAPI Mastery Course Lessons
│   └── fastapi-mastery/
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
- [Model Answers Q1–Q4](./Data_Engineering/Exam_Answers_Term_Assessment_II.md) | [PDF](./Data_Engineering/Exam_Answers_Term_Assessment_II.pdf)

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
- [Model Answers Q1–Q5](./Data_Engineering/Assignment_2_Term_Assessment.md) | [PDF](./Data_Engineering/Assignment_2_Term_Assessment.pdf)

**Pattern:** 5 questions × 2 parts each, mapped to L4/CO3 and L4/CO4

**Topics Covered:**
- Q1: Spark vs Hadoop MapReduce (video-streaming low-latency); Spark RDDs vs DataFrames (telecom CDR batch)
- Q2: Azure/AWS roles in scalable distributed data engineering (insurance); Spark vs Hadoop for real-time/iterative (stock-market)
- Q3: Spark transformations & actions for social-media pipeline; Azure Data Factory vs AWS Glue comparison
- Q4: Azure Blob Storage for media metadata archiving; Amazon Redshift vs Azure Synapse for bank regulatory reports
- Q5: ADF/Glue pipeline tuning for slow Power BI dashboard; S3 → Glue → Redshift ETL flow for social-media analytics
- Quick 5-mark answer writing template

---

## 🚀 FastAPI Mastery

- [Course Repository](./FastAPI_Mastery/fastapi-mastery/)

**Lessons:** Lifecycle & Architecture, Routing & Parameters, Pydantic v2, Dependency Injection, Async & Concurrency, Errors & Middleware, Databases, Auth & Security, Testing, Architecture, Production, Advanced

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
