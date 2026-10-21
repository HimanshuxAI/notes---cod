# UNIT IV — DATA SERVICES ON AZURE AND AWS

**Course:** 23CSE3017 – Data Engineering  
**Class:** T.Y. (SEM-I), AIEC  
**Institution:** MIT Art, Design and Technology University, MIT School of Computing, Pune  
**Academic Year:** 2025-2026 SEM-I (NEP)  
**Professor:** Dr. Aditya Pai H  

---

# TABLE OF CONTENTS

1. [Azure Data Services](#1-azure-data-services)
2. [Azure Data Factory (ADF) — ETL/ELT Orchestration](#2-azure-data-factory-adf---etlelt-orchestration)
3. [Creating and Scheduling Data Pipelines with ADF](#3-creating-and-scheduling-data-pipelines-with-adf)
4. [Azure Synapse Analytics](#4-azure-synapse-analytics)
5. [Azure Blob Storage](#5-azure-blob-storage)
6. [Azure Databricks](#6-azure-databricks)
7. [AWS Data Services](#7-aws-data-services)
8. [Amazon S3](#8-amazon-s3)
9. [Amazon Redshift](#9-amazon-redshift)
10. [AWS Glue](#10-aws-glue)
11. [Exam Preparation — Key Topics & Questions](#11-exam-preparation-key-topics--questions)

---

# 1. AZURE DATA SERVICES

## 1.1 What are Azure Data Services?

**Azure Data Services** are cloud-based services provided by Microsoft Azure that help organizations:

| Capability | Description |
|------------|-------------|
| **Store data** | Persistent, scalable storage |
| **Move data** | Data ingestion and transfer |
| **Clean and transform data** | Data preparation and ETL/ELT |
| **Analyze data** | Analytics and insights |
| **Process real-time data** | Streaming analytics |
| **Build AI/ML models** | Machine learning workflows |
| **Manage and govern data** | Data governance and compliance |

---

## 1.2 Key Azure Data Services — Categories

### 1. Data Storage and Management

| Service | Description | Best For |
|---------|-------------|----------|
| **Azure SQL Database** | Fully managed, scalable relational database based on SQL Server | Structured/tabular data |
| **Azure Cosmos DB** | Globally distributed, multi-model database for low latency and high availability | Global apps, low-latency needs |
| **Azure Data Lake Storage** | Scalable, cost-effective storage for large volumes of structured and unstructured data | Big data lakes |
| **Azure Blob Storage** | Object storage for unstructured binary data (images, videos, PDFs) | Media files, backups, unstructured data |

### 2. Data Integration and Analytics

| Service | Description |
|---------|-------------|
| **Azure Data Factory** | Cloud-based data integration service for creating data-driven workflows (ETL/ELT) |
| **Azure Synapse Analytics** | Limitless analytics service combining data integration, warehousing, and big data analytics |
| **Azure Databricks** | Fast, collaborative Apache Spark-based analytics service |

### Additional Services

| Service | Description |
|---------|-------------|
| **Azure HDInsight** | Cloud-based analytics supporting Hadoop, Spark, Kafka |
| **Azure Analysis Services** | Enterprise-grade analytics engine for building analytical models |
| **Azure Stream Analytics** | Real-time event processing engine |

### 3. AI and Machine Learning

| Service | Description |
|---------|-------------|
| **Azure Machine Learning** | Cloud platform for building, training, deploying ML models |
| **Azure AI Services** | Pre-built AI capabilities |

### 4. Specialized Data Services

| Service | Description |
|---------|-------------|
| **Azure Health Data Services** | Handling protected health information (PHI) using FHIR and DICOM standards |
| **Azure Time Series Insights** | Managed analytics, storage, visualization for time series data |
| **Azure Purview** | Unified data governance for discovering, understanding, managing data assets |

### 5. Modernization and Hybrid Capabilities

| Service | Description |
|---------|-------------|
| **Azure Arc-enabled data services** | Run Azure data services anywhere (on-premises, edge) |
| **Application and data modernization** | Tools for migrating and modernizing apps and data to cloud |

---

# 2. AZURE DATA FACTORY (ADF) — ETL/ELT ORCHESTRATION

## 2.1 What is ADF?

**Azure Data Factory (ADF)** is a cloud-based ETL and data integration service provided by Azure. It enables building complex ETL processes and scheduled event-driven workflows.

| Approach | Description |
|----------|-------------|
| **ETL** (Extract, Transform, Load) | Data is transformed before loading into storage |
| **ELT** (Extract, Load, Transform) | Raw data is loaded first, then transformed |

---

## 2.2 Core Capabilities of ADF

| Capability | Description |
|------------|-------------|
| **Data Ingestion** | Pull data from 90+ sources (SQL, APIs, Blob, SAP, etc.) |
| **Data Transformation** | Use Data Flow or external compute (Azure Databricks, HDInsight) |
| **Data Movement** | Reliable, secure, scalable data transfers across systems |
| **Orchestration** | Manage complex workflows, dependencies, conditional logic |

---

## 2.3 Benefits of Using ADF

| Benefit | Description |
|---------|-------------|
| **Low-code environment** | Drag-and-drop interface for building data flows |
| **Cost-effective** | Pay-as-you-go model; integrates with other Azure tools |
| **Hybrid support** | Connects on-premise and cloud data sources seamlessly |
| **Scalable & performant** | Handles petabytes using Spark or SSIS engines |

---

## 2.4 Common Use Cases

| Use Case | Objective | ADF Role |
|----------|-----------|----------|
| **Data Warehousing & BI** | Consolidate data into centralized warehouse (Azure Synapse) | Automates ETL workflows; cleansing and transformation before loading |
| **Real-time Data Sync** | Keep data in sync across cloud and on-premises | Event-based triggers; near-real-time pipelines |
| **Legacy Migration** | Migrate on-premise/outdated systems to cloud | Built-in connectors to legacy DBs and mainframes; incremental migration |
| **Predictive Analytics** | Feed clean data into ML models | Automates extraction, feature engineering, loading into data lake/ML workspace |

---

# 3. CREATING AND SCHEDULING DATA PIPELINES WITH ADF

## 3.1 How to Create a Data Pipeline

| Step | Action |
|------|--------|
| **1. Create New Pipeline** | Log into ADF Studio → Author → Add new pipeline |
| **2. Add Activities** | Copy Activity (data transfer), Data Flow (transformations), Web Activity, Stored Procedure Activity |
| **3. Create Linked Services** | Define source/target connection details (Azure Blob, SQL DB, Amazon S3, REST APIs) |
| **4. Define Datasets** | Describe data structure (file format, schema, folder path) — used as inputs/outputs |

---

## 3.2 Trigger Types in ADF

| Trigger Type | Description |
|-------------|-------------|
| **Schedule Trigger** | Runs pipelines at specific time (e.g., daily at midnight) |
| **Tumbling Window Trigger** | Recurring intervals with dependency control |
| **Event-based Trigger** | Reacts to events (e.g., file creation in Blob Storage) |
| **Manual/Debug Run** | For development and testing |

---

## 3.3 Monitoring and Management

Use the ADF Monitoring Interface to:
- View pipeline execution history
- Analyze success/failure status
- Monitor performance metrics
- Set alerts and error thresholds

---

## 3.4 Creating Your First Pipeline — Steps

1. **Setting up ADF Studio** — Launch through Azure Portal; access authoring canvas
2. **Creating Linked Services** — Connect to source (Blob/Data Lake) and destination (SQL Database)
3. **Defining Datasets** — Specify schema, file location, format for source and sink
4. **Configuring a Pipeline** — Drag Copy Data activity; link source + sink through datasets
5. **Testing & Debugging** — Preview data, validate configuration, run debug session
6. **Publishing & Running** — Publish pipeline; trigger manually; observe activity execution

---

# 4. AZURE SYNAPSE ANALYTICS

## 4.1 Overview

**Azure Synapse Analytics** is a powerful analytics service that unifies enterprise data warehousing and big data analytics in a single platform. It bridges the gap between data lakes and data warehouses.

---

## 4.2 Key Concepts and Capabilities

| Capability | Description |
|------------|-------------|
| **1. Unified Platform** | Combines data integration, data warehousing (SQL), big data analytics (Spark), and data exploration |
| **2. Scalable Architecture** | Massively parallel processing (MPP); serverless and dedicated options |
| **3. Data Integration** | Built-in data pipelines (like ADF) and connectors for various sources |
| **4. SQL Analytics** | Dedicated SQL pools (predictable workloads) + Serverless SQL pools (on-demand queries, T-SQL) |
| **5. Apache Spark Integration** | Deep Spark integration for data engineering, preparation, ETL, ML |
| **6. Azure Synapse Studio** | Unified workspace for data integration, analytics, visualization |
| **7. Integration** | Integrates with Azure Data Lake Storage, Power BI, Azure Machine Learning |

---

## 4.3 Benefits

| Benefit | Description |
|---------|-------------|
| **Accelerated time to insight** | Rapid delivery of insights and ML models |
| **Scalability and Flexibility** | Scalable compute and storage; adjust based on workload |
| **Unified Analytics Platform** | Combines integration, warehousing, analytics in one platform |
| **Enhanced Productivity** | Unified experience and integrated tools |
| **Cost Efficiency** | Pay-as-you-go for serverless SQL pools; reserved capacity options |
| **Advanced Security** | Encryption, RBAC, compliance with industry standards |

---

## 4.4 Use Cases

| Use Case | Description |
|----------|-------------|
| **Enterprise Data Warehousing** | Consolidating structured data from multiple sources |
| **Big Data Analytics** | Processing structured/semi-structured/unstructured data using Spark |
| **Real-time Insights** | Analyzing streaming data for fraud detection, equipment monitoring |
| **AI and ML Integration** | Orchestrating data pipelines for model training, evaluation, deployment |

---

# 5. AZURE BLOB STORAGE

## 5.1 What is Blob Storage?

**Blob** = Binary Large Object. Azure Blob Storage is Microsoft's cloud platform for storing large amounts of unstructured data (text, binary data) that doesn't fit into a specific data model.

**Key Features:**
- Scalability
- Cost-effectiveness
- Accessibility
- Integration with Azure services
- Data security and compliance

**Access:** Objects accessible via HTTP/HTTPS through Azure Storage REST API, Azure CLI, Azure PowerShell, or client libraries (.NET, Node.js, Java, Python, PHP, Ruby, Go).

---

## 5.2 Blob Containers

| Feature | Description |
|---------|-------------|
| **Analogy** | Work like drawers for file management |
| **Capacity** | One storage account = unlimited containers; one container = up to 500 TB |
| **Naming rules** | 3–63 characters; start with lowercase letter or number; use dashes only (no spaces) |

---

## 5.3 Types of Blobs

| Type | Description | Max Size | Use Case |
|------|-------------|----------|----------|
| **Block Blobs** | Best for media files, text, documents, binary files | 4000 MiB per blob; 50,000 blocks | Media, documents |
| **Page Blobs** | Collection of 512-byte pages for random read/write | 8 TiB | Random access operations |
| **Append Blobs** | Designed for append operations (log file updating) | 50,000 blocks; 4 MiB per block | Log files, auditing |

> Once a blob is created, its type cannot be changed.

---

## 5.4 Use Cases

| Use Case | Description |
|----------|-------------|
| **Data Lakes** | Foundation for storing and analyzing large volumes of unstructured data |
| **Backup and Disaster Recovery** | Reliable, durable storage for backups |
| **Websites and Applications** | Store website content (images, videos) |
| **High-Performance Computing (HPC)** | Integrates with Azure Managed Lustre for parallel file system |
| **IoT Data** | Handle massive influx of sensor data from IoT devices |

---

# 6. AZURE DATABRICKS

## 6.1 Overview

**Azure Databricks** provides a fully managed, highly scalable, available unified compute platform using the Databricks distribution of open-source Spark.

| Feature | Description |
|---------|-------------|
| **Ease of setup** | Automates setup steps; developers can start in minutes |
| **Languages** | R, Python, Scala, SQL APIs |
| **ML Frameworks** | TensorFlow, PyTorch, ScikitLearn, Spark MLlib |
| **Integrations** | Azure Storage, Cosmos DB, Event Hub, Azure Data Factory, Azure AD |

---

## 6.2 Capabilities

| Capability | Description |
|------------|-------------|
| **Data Warehouse & Analytics** | Collect all data types; process/transform at scale using ADF + Databricks; analyze using Azure SQL DW, Analysis Services, Power BI |
| **Real-time Analytics** | Capture streaming data; process near-real-time using Databricks; serve using Cosmos DB |
| **Machine Learning** | Build, train, test ML models using Spark APIs |

---

## 6.3 Getting Started

1. Create an Azure Databricks workspace
2. Create a cluster (select 5.0 ML Beta Databricks runtime for ML applications)
3. Build data models using R, Python, Scala, SQL

---

# 7. AWS DATA SERVICES

## 7.1 Overview

AWS provides a comprehensive suite of data services encompassing databases, analytics, data lakes, and more.

| Category | Services |
|----------|----------|
| **Databases** | Amazon Aurora, Amazon RDS, Amazon DynamoDB, Amazon DocumentDB, Amazon Neptune, Amazon ElastiCache, Amazon QLDB |
| **Analytics** | Amazon Redshift, Amazon S3, AWS Lake Formation, Amazon Kinesis, Amazon MSK, Amazon EMR, Amazon QuickSight, Amazon OpenSearch Service, Amazon Athena, AWS Glue, AWS Data Pipeline |

---

## 7.2 Key Benefits

| Benefit | Description |
|---------|-------------|
| **Scalability and Flexibility** | Scale up/down based on demand |
| **Cost-Effectiveness** | Pay-as-you-go pricing |
| **Security and Compliance** | Robust security features and compliance certifications |
| **Managed Services** | Fully managed services reduce operational burden |
| **Integration** | Services work seamlessly with each other |
| **Innovation** | Wide range of AI/ML services |

---

# 8. AMAZON S3

## 8.1 Overview

**Amazon S3** (Simple Storage Service) is an object storage service offering industry-leading scalability, data availability, security, and performance.

| Benefit | Description |
|---------|-------------|
| **Scalability** | Store virtually any amount of data (exabytes); fully elastic; pay only for what you use |
| **Durability and Availability** | 99.999999999% (11 nines) durability; 99.99% availability |
| **Security and Data Protection** | Secure, private, encrypted by default; auditing capabilities |
| **Price and Performance** | Multiple storage classes; automated lifecycle management; cost-efficient storage |

---

## 8.2 Data Lake on S3

A **data lake** is a centralized repository that allows storing all structured and unstructured data at any scale. Run analytics, AI, ML, and HPC applications to unlock data value.

---

# 9. AMAZON REDSHIFT

## 9.1 Overview

**Amazon Redshift** is a fully managed, cloud-based data warehouse service designed for fast and cost-effective analysis of large-scale data.

| Feature | Description |
|---------|-------------|
| **Petabyte-Scale Storage** | Handles structured/semi-structured data at petabyte/exabyte scale |
| **Massively Parallel Processing (MPP)** | Distributes query processing across multiple compute nodes |
| **Seamless AWS Integration** | Integrates with S3, AWS Glue, Amazon SageMaker; federated queries |
| **Serverless** | Redshift Serverless — no server management; auto-scales |
| **Zero-ETL** | Near real-time analytics; connects to streaming services, databases, data lakes |
| **AQUA** | Advanced Query Accelerator — hardware-accelerated caching; queries up to 10x faster |
| **Security** | Encryption, IAM, SSL, VPC, granular access controls, dynamic data masking |
| **SQL Compatibility** | Standard ANSI SQL; integrates with Tableau, Looker, MicroStrategy |
| **ML Capabilities** | In-database ML; integrates with Amazon SageMaker |

---

## 9.3 Redshift vs. Traditional Data Warehouse

| Feature | Amazon Redshift | Traditional Data Warehouse |
|---------|-----------------|---------------------------|
| **Deployment** | Fully managed, cloud-based | On-premises, self-managed |
| **Scalability** | Petabyte/exabyte scale, elastic | Limited by hardware |
| **Performance** | MPP, AQUA, hardware acceleration | Single-node or SMP |
| **Integration** | Deep AWS ecosystem, BI tools | Limited, often proprietary |
| **Security** | Built-in, cloud-native | Varies, often manual |
| **Cost** | Pay-as-you-go, serverless | High upfront, fixed capacity |

---

## 9.4 Typical Use Cases

| Use Case | Description |
|----------|-------------|
| **Business Intelligence (BI)** | Powering dashboards and analytics platforms |
| **Operational Analytics** | Real-time analysis of transactional data |
| **Data Lakehouse** | Unifying data warehouses and data lakes |
| **Data Science & ML** | Advanced analytics and AI workloads |

---

# 10. AWS GLUE

## 10.1 Overview

**AWS Glue** is a fully managed, serverless data integration service designed to simplify and automate ETL (Extract, Transform, Load) and ELT (Extract, Load, Transform) jobs at scale.

---

## 10.2 Core Features

| Feature | Description |
|---------|-------------|
| **1. Serverless Architecture** | No infrastructure to provision; AWS handles scaling, resource allocation, maintenance |
| **2. Automatic Code Generation** | Generates ETL code (Python/Scala) based on sources/targets using Apache Spark |
| **3. Glue Studio** | Visual job authoring with drag-and-drop editor for building/monitoring ETL jobs |
| **4. Data Catalog** | Centralized metadata repository (table definitions, job metadata, schema versions) |
| **5. Schema Discovery (Crawlers)** | Automatically scans data sources, infers schemas, populates Data Catalog |
| **6. Job Scheduling & Triggers** | Schedule, event-triggered, or on-demand; chain workflows for complex pipelines |
| **7. Broad Data Source Support** | S3, Redshift, RDS, DynamoDB, DocumentDB, JDBC databases, streaming, external connectors |
| **8. Multiple Workloads** | Batch, streaming, real-time data transformation |
| **9. Data Quality (DataBrew)** | Data profiling, validation, quality checks; no-code data preparation |
| **10. Cost Efficiency** | Pay only for DPUs (Data Processing Units) used; no upfront costs |

---

## 10.3 Strengths and Limitations

| Strengths | Limitations |
|-----------|-------------|
| Fully managed, scalable, serverless | Custom ETL code limited to Python and Scala |
| Automatic schema discovery, code generation | Best for AWS-centric; limited non-AWS integration |
| Visual and code-based development | Some Spark knowledge helpful for advanced customizations |
| Deep integration with AWS analytics ecosystem | |

---

# 11. EXAM PREPARATION — KEY TOPICS & QUESTIONS

## High Probability Topics

### Azure Data Services
1. Azure Data Services categories and key services
2. Azure Data Factory (ADF) — ETL vs ELT, core capabilities
3. ADF pipeline creation steps and trigger types
4. Azure Synapse Analytics — unified platform, capabilities
5. Azure Blob Storage — types of blobs, use cases
6. Azure Databricks — Spark-based analytics, integrations

### AWS Data Services
1. AWS Data Services overview (databases, analytics categories)
2. Amazon S3 — benefits, durability, data lake
3. Amazon Redshift — features, MPP, serverless, comparison with traditional DW
4. AWS Glue — serverless ETL, core features, Data Catalog, crawlers

---

## Suggested Exam Questions

1. What are Azure Data Services? List and explain key categories.
2. Explain Azure Data Factory (ADF) with ETL vs ELT approach.
3. How do you create and schedule a data pipeline in ADF? Describe trigger types.
4. Describe Azure Synapse Analytics and its key capabilities.
5. What is Azure Blob Storage? Explain the three types of blobs.
6. What is Azure Databricks? How does it integrate with other Azure services?
7. List AWS Data Services categories with examples.
8. Explain Amazon S3 benefits and durability features.
9. Describe Amazon Redshift key features and compare with traditional data warehouse.
10. What is AWS Glue? Explain its core features for ETL/ELT jobs.
