# UNIT III — BIG DATA TECHNOLOGIES AND DISTRIBUTED COMPUTING

**Course:** 23CSE3017 – Data Engineering  
**Class:** T.Y. (SEM-I), AIEC  
**Institution:** MIT Art, Design and Technology University, MIT School of Computing, Pune  
**Academic Year:** 2025-2026 SEM-I (NEP)  
**Professor:** Dr. Aditya Pai H  

---

# TABLE OF CONTENTS

1. [Big Data Technologies](#1-big-data-technologies)
2. [Introduction to Big Data Processing](#2-introduction-to-big-data-processing)
3. [Need for Distributed Computing Frameworks](#3-need-for-distributed-computing-frameworks)
4. [Apache Hadoop Ecosystem](#4-apache-hadoop-ecosystem)
5. [Apache Spark Basics](#5-apache-spark-basics)
6. [Introduction to Cloud Platforms](#6-introduction-to-cloud-platforms)
7. [Benefits of Cloud Platforms for Data Engineering](#7-benefits-of-cloud-platforms-for-data-engineering)
8. [Overview of Microsoft Azure and AWS](#8-overview-of-microsoft-azure-and-aws)
9. [Exam Preparation — Key Topics & Questions](#9-exam-preparation-key-topics--questions)

---

# 1. BIG DATA TECHNOLOGIES

## 1.1 What is Big Data Technology?

**Big Data Technologies** are a suite of software tools used to manage, process, and analyze massive, complex datasets that traditional data processing systems cannot handle. These technologies are crucial for extracting valuable insights from Big Data, which is often characterized by **Volume, Velocity, and Variety.**

---

## 1.2 Key Categories of Big Data Technologies

### 1. Data Storage

| Technology | Description | Use Case |
|------------|-------------|----------|
| **HDFS** (Hadoop Distributed File System) | Distributed file system designed to store large datasets across multiple machines, enabling scalable storage and processing. | Storing petabyte-scale datasets across commodity hardware |
| **NoSQL Databases** (Cassandra, MongoDB) | Flexible data models with horizontal scalability to handle diverse data types and high volumes. | Unstructured/semi-structured data, high-velocity writes |

### 2. Data Processing and Analytics

| Technology | Description | Use Case |
|------------|-------------|----------|
| **Apache Spark** | In-memory processing framework that accelerates data processing tasks, particularly for ML and real-time analytics. | Iterative algorithms, ML, streaming |
| **Apache Kafka** | Distributed streaming platform for building real-time data pipelines and handling high-velocity data streams. | Event streaming, log aggregation |
| **Apache Flink** | Stream processing framework known for low latency and fault tolerance. | Real-time stream processing |
| Cloud Data Warehouses (BigQuery, Redshift, Snowflake) | Scalable, cost-effective cloud solutions for storing and analyzing large datasets. | Enterprise analytics, BI |

### 3. Data Mining and Analytics

| Technology | Description |
|------------|-------------|
| **Machine Learning** | Algorithms to identify patterns, make predictions, and gain insights from Big Data. |
| **Data Mining Tools** | Software and techniques for discovering hidden patterns, relationships, and anomalies within large datasets. |

### 4. Data Visualization

| Tool | Description |
|------|-------------|
| **Tableau** | Interactive dashboards and visualizations to explore Big Data. |
| **Power BI** | Business analytics tool for creating interactive visual reports. |

---

## 1.3 Key Considerations in Big Data

| Consideration | Description |
|---------------|-------------|
| **Volume, Velocity, Variety** | The three Vs of Big Data that impact technology choice. |
| **Real-time vs. Batch Processing** | Technologies chosen based on whether use case needs real-time or batch processing. |
| **Cloud vs. On-premise** | Organizations choose between cloud-based solutions or on-premise infrastructure based on needs and resources. |

---

## 1.4 Popular Big Data Technologies

| # | Technology | Description | Key Features |
|---|------------|-------------|--------------|
| 1 | **Apache Cassandra** | No-SQL database, highly scalable, high availability | Replication across data centers, fault tolerance, no downtime on node failure |
| 2 | **Apache Hadoop** | Handles large-scale data using HDFS and MapReduce | Scalable, processes multi-terabyte datasets (e.g., human genome) |
| 3 | **Apache Hive** | Data summarization and ad-hoc querying on Hadoop | HiveQL (SQL-like), OLAP, fast, scalable, extensible |
| 4 | **Apache Flume** | Collects, aggregates, moves log data from many sources to centralized store | Distributed, reliable log collection |
| 5 | **Apache Spark** | In-memory processing, faster than Hadoop MapReduce | Interactive queries, stream processing, in-memory cluster computing |
| 6 | **Apache Kafka** | Distributed publish-subscribe messaging system | High volume, message replication, integrates Storm and Spark, built on ZooKeeper |
| 7 | **MongoDB** | Document-oriented NoSQL database | JSON storage, auto-sharding, high availability, rich queries |
| 8 | **ElasticSearch** | Real-time distributed full-text search and analytics engine | Scalable to petabytes, used by Wikipedia, GitHub |

---

# 2. INTRODUCTION TO BIG DATA PROCESSING

## 2.1 What is Big Data?

**Big Data** refers to data sets that are too large or complex for traditional data-processing software to handle efficiently.

**Big Data Processing** focuses on collecting, transforming, storing, analyzing, and visualizing these data sets in a scalable and timely manner.

## 2.2 Key Characteristics ("3Vs")

| Characteristic | Description | Example |
|---------------|-------------|---------|
| **Volume** | Large quantities of data | Petabytes of data |
| **Velocity** | High speed of data generation and processing | Real-time data streams |
| **Variety** | Different types of data | Structured, unstructured, semi-structured |

---

## 2.3 Stages in Big Data Processing Pipeline

| Stage | Description | Tools |
|-------|-------------|-------|
| **1. Data Ingestion** | Collecting data from various sources | Apache Kafka, Flume, Sqoop |
| **2. Data Storage** | Storing in distributed storage systems | HDFS, Amazon S3, Azure Blob Storage |
| **3. Data Processing** | Batch or real-time processing | Hadoop MapReduce (batch), Spark/Storm/Flink (real-time) |
| **4. Data Analysis** | Machine learning, analytics frameworks | Spark MLlib, Hive, Pig |
| **5. Data Visualization** | Dashboards and visual storytelling | Tableau, Power BI, Kibana |

---

## 2.4 Applications of Big Data Processing

| Application | Description | Example |
|-------------|-------------|---------|
| **Fraud Detection (Banking)** | Analyzing transaction patterns, cross-referencing data, ML models, real-time alerts | High-value transaction in Singapore after Mumbai spending triggers fraud alert |
| **Predictive Maintenance (Manufacturing)** | IoT sensor monitoring, historical data analysis, reducing downtime | Vibration data from motors predicts bearing wear |
| **Personalized Recommendations (E-commerce)** | Clickstream analysis, product recommendations, A/B testing, dynamic pricing | Amazon recommends based on purchase history and browsing |
| **Health Monitoring (Smart Healthcare)** | Wearable devices, EHRs, predictive diagnostics, resource optimization | Smartwatches detect irregular heartbeats and notify doctors |

---

# 3. NEED FOR DISTRIBUTED COMPUTING FRAMEWORKS

## 3.1 Limitations of Traditional (Centralized) Systems

| Limitation | Description |
|------------|-------------|
| **Memory Bottlenecks** | Single machines can't handle terabytes to petabytes of datasets |
| **Processing Speed** | Sequential processing is too slow for time-sensitive analysis |
| **Scalability Issues** | Vertical scaling (upgrading hardware) is expensive and limited |
| **Single Point of Failure** | System crash = loss of all data and processing |

---

## 3.2 What Are Distributed Computing Frameworks?

Systems that split large tasks into smaller chunks and distribute them across multiple nodes (computers) in a cluster to work in parallel.

**Popular Examples:** Apache Hadoop (MapReduce), Apache Spark, Apache Flink, Google Dataflow

---

## 3.3 Why Are They Needed?

| Reason | Description |
|--------|-------------|
| **Volume Handling** | Process petabytes efficiently by distributing load across many machines |
| **Faster Computation** | Parallelism — tasks run simultaneously; Spark up to 100x faster than Hadoop MapReduce for in-memory ops |
| **Fault Tolerance** | Data replicated across nodes; if one node fails, another takes over without data loss |
| **Cost-Effective Scalability** | Horizontal scaling — add inexpensive commodity hardware |
| **Support for Diverse Workloads** | Handle batch, stream, interactive, and ML workloads in unified environment |

---

## 3.4 Real-World Use Cases

| Domain | Use Case |
|--------|----------|
| Finance | Real-time fraud detection using Spark Streaming |
| Healthcare | Distributed EHR analysis for disease prediction |
| E-commerce | Product recommendation engines using Flink |
| Smart Cities | Sensor data fusion using Hadoop and Spark |

---

# 4. APACHE HADOOP ECOSYSTEM

## 4.1 Overview

**Apache Hadoop** is an open-source framework that makes interaction with Big Data easier. It enables processing of large data sets that reside in clusters.

**Four Major Elements:**
1. HDFS
2. MapReduce
3. YARN
4. Hadoop Common Utilities

**Ecosystem Components:**

| # | Component | Description |
|---|-----------|-------------|
| 1 | **HDFS** | Hadoop Distributed File System |
| 2 | **YARN** | Yet Another Resource Negotiator |
| 3 | **MapReduce** | Programming-based data processing |
| 4 | **Spark** | In-memory data processing |
| 5 | **PIG, HIVE** | Query-based data processing |
| 6 | **HBase** | NoSQL Database |
| 7 | **Mahout, Spark MLLib** | Machine Learning algorithm libraries |
| 8 | **Solr, Lucene** | Searching and Indexing |
| 9 | **Zookeeper** | Managing cluster |
| 10 | **Oozie** | Job Scheduling |

---

## 4.3 HDFS (Hadoop Distributed File System)

HDFS is the primary component of the Hadoop ecosystem, responsible for storing large datasets across various nodes while maintaining metadata.

### Architecture

| Component | Role | Resources |
|-----------|------|-----------|
| **Name Node** | Contains metadata (data about data); prime node | Fewer resources |
| **Data Node** | Stores actual data; commodity hardware | More resources |

The Name Node maintains coordination between clusters and hardware — it works at the heart of the system.

---

## 4.4 YARN (Yet Another Resource Negotiator)

YARN manages resources across clusters and performs scheduling and resource allocation.

### Components

| Component | Role |
|-----------|------|
| **Resource Manager** | Allocates resources for applications |
| **Node Manager** | Allocates resources (CPU, memory, bandwidth) per machine; acknowledges Resource Manager |
| **Application Manager** | Interface between Resource Manager and Node Manager; performs negotiations |

---

## 4.5 MapReduce

MapReduce uses distributed and parallel algorithms to process Big Data. It uses two functions:

| Function | Task |
|----------|------|
| **Map()** | Performs sorting and filtering; organizes data into groups; generates key-value pairs |
| **Reduce()** | Summarization by aggregating mapped data; combines tuples into smaller set |

---

## 4.6 PIG

Developed by Yahoo; works on Pig Latin language (query-based, similar to SQL).

| Feature | Description |
|---------|-------------|
| **Platform** | Structuring data flow, processing, analyzing huge datasets |
| **Execution** | Executes commands; MapReduce activities handled in background |
| **Storage** | Stores results in HDFS |
| **Language** | Pig Latin runs on Pig Runtime (like Java on JVM) |
| **Analogy** | Like giving a chef a recipe instead of explaining every hand movement |

---

## 4.7 HIVE

Performs reading and writing of large datasets using SQL methodology.

| Feature | Description |
|---------|-------------|
| **Query Language** | HQL (Hive Query Language) |
| **Processing** | Real-time and batch processing |
| **Data Types** | All SQL datatypes supported |
| **Components** | JDBC Drivers, HIVE Command Line |
| **Use** | Designed for OLAP |

---

## 4.8 Mahout

Provides Machine Learnability to systems.

| Feature | Description |
|---------|-------------|
| **Capabilities** | Collaborative filtering, clustering, classification |
| **Libraries** | Provides ML algorithm libraries |
| **Usage** | Invoke algorithms as needed via its own libraries |

---

## 4.9 Apache Spark

| Feature | Description |
|---------|-------------|
| **Purpose** | Handles batch processing, interactive/real-time processing, graph conversions, visualization |
| **Memory** | Consumes in-memory resources; faster than Hadoop |
| **Best For** | Real-time data (Hadoop best for structured/batch) |
| **Cluster Mgmt** | Has its own cluster management |

---

## 4.10 Apache HBase

| Feature | Description |
|---------|-------------|
| **Type** | NoSQL database |
| **Capability** | Supports all kinds of data; like Google's BigTable |
| **Use Case** | Fast search/retrieval of small occurrences in huge databases |

---

## 4.11 Solr, Lucene

| Component | Description |
|-----------|-------------|
| **Lucene** | Java-based library for search and indexing; spell check mechanism |
| **Solr** | Driven by Lucene; searching and indexing service |

---

## 4.12 Zookeeper

| Feature | Description |
|---------|-------------|
| **Purpose** | Coordination and synchronization among Hadoop components |
| **Functions** | Synchronization, inter-component communication, grouping, maintenance |

---

## 4.13 Oozie

| Feature | Description |
|---------|-------------|
| **Purpose** | Job scheduler; binds jobs together as a single unit |
| **Job Types** | Oozie Workflow (sequential), Oozie Coordinator (event-triggered) |

---

# 5. APACHE SPARK BASICS

## 5.1 What is Apache Spark?

**Apache Spark** is a unified, open-source, distributed processing engine designed for large-scale data processing and analytics.

**Supported Workloads:**
- Batch processing
- Real-time streaming
- SQL queries
- Machine learning
- Graph processing

Spark builds on Hadoop MapReduce limitations by enabling **in-memory computations** and faster execution of iterative algorithms.

---

## 5.2 Key Features

| Feature | Description |
|---------|-------------|
| **Speed** | In-memory computation; 100x faster than Hadoop MapReduce |
| **Ease of Use** | APIs in Python, Java, Scala, R |
| **Advanced Analytics** | MLlib (ML), Streaming, GraphX libraries |
| **Unified Engine** | Batch + streaming + SQL + ML in one framework |
| **Fault Tolerance** | RDD keeps track of data lineage |
| **Scalability** | Scales across thousands of nodes |

---

## 5.3 Spark Architecture

| Component | Role |
|-----------|------|
| **Driver Program** | Runs main function and coordinates all workers |
| **Cluster Manager** | Allocates resources (YARN, Mesos, Kubernetes) |
| **Executors (Workers)** | Run tasks and return results; operate on partitioned datasets |

---

## 5.4 Core Components

| Module | Purpose |
|--------|---------|
| **Spark Core** | Base engine for memory management, task scheduling |
| **Spark SQL** | Structured data queries using SQL or DataFrames |
| **Spark Streaming** | Real-time data stream processing |
| **MLlib** | Machine learning algorithms and tools |
| **GraphX** | Graph computation library |

---

## 5.5 Spark Basics — RDDs, DataFrames, Transformations, Actions

### 5.5.1 RDDs (Resilient Distributed Datasets)

| Property | Description |
|----------|-------------|
| **Definition** | Fundamental data structure; fault-tolerant, distributed collection processed in parallel |
| **Immutability** | Data cannot be changed after creation |
| **Partitions** | Divided into logical partitions for parallel processing |
| **Creation** | From HDFS, local files, or existing RDDs |

### 5.5.2 DataFrames

| Property | Description |
|----------|-------------|
| **Definition** | Higher-level abstraction on RDDs; optimized for structured/tabular data |
| **Structure** | Named columns with specific data types (like relational table) |
| **Advantages** | Better performance and ease of use vs RDDs |
| **Schema** | Defined schema specifying structure and data types |

### 5.5.3 Datasets

| Property | Description |
|----------|-------------|
| **Definition** | Strongly-typed structure (Scala/Java); combines RDDs + DataFrames |
| **Strong Typing** | Compile-time type safety |
| **Flexibility** | Functional and relational operations |

### 5.5.4 Transformations (Lazy Evaluation)

| Transformation | Description |
|---------------|-------------|
| **map()** | Applies function to each element |
| **filter()** | Creates new RDD with elements satisfying condition |
| **flatMap()** | Each input mapped to multiple outputs |
| **groupByKey()** | Groups elements based on key |
| **reduceByKey()** | Combines values for each key |

> Transformations are **lazily evaluated** — executed only when an action is called.

### 5.5.5 Actions (Eager Evaluation)

| Action | Description |
|--------|-------------|
| **count()** | Returns number of elements |
| **collect()** | Returns all elements as array to driver |
| **take(n)** | Returns first n elements |
| **saveAsTextFile()** | Saves RDD to external storage |
| **foreach()** | Applies function to each element (side effects) |

> Actions trigger execution of all preceding transformations.

---

## 5.6 Common Spark Use Cases

| Use Case | Description | Example |
|----------|-------------|---------|
| **Real-time fraud detection** | Spark Streaming + Kafka + MLlib | Credit card transactions evaluated in milliseconds |
| **Log and Event Stream Analysis** | Processing terabytes of logs near real-time | Netflix/Facebook server log analysis |
| **ML Model Training** | MLlib for parallel model training | E-commerce recommendation model |
| **ETL Pipelines** | Extract, Transform, Load for analytics | Retail chain sales data processing |
| **Social Network Analysis** | GraphX for relationship analysis | LinkedIn "People You May Know" |

---

# 6. INTRODUCTION TO CLOUD PLATFORMS

## 6.1 What is a Cloud Platform?

Cloud platforms offer on-demand access to computing resources (storage, servers, databases) over the internet, replacing on-premises infrastructure.

| Feature | Description |
|---------|-------------|
| **On-demand access** | Access computing resources over internet; rent instead of purchase |
| **Pay-as-you-go** | Charged based on actual consumption |
| **Centralized management** | Provider manages infrastructure; no hardware maintenance |
| **Scalability and flexibility** | Scale resources up/down based on demand |

---

## 6.2 Cloud Service Models

| Model | Description |
|-------|-------------|
| **IaaS** (Infrastructure as a Service) | Fundamental resources: VMs, storage, networking |
| **PaaS** (Platform as a Service) | Platform for developing, running, managing applications |
| **SaaS** (Software as a Service) | Software applications over internet (email, CRM, office apps) |

---

## 6.3 Deployment Models

| Model | Description |
|-------|-------------|
| **Public Cloud** | Third-party owned; shared among multiple users |
| **Private Cloud** | Dedicated to single organization; on-premises or hosted |
| **Hybrid Cloud** | Combines public and private clouds |

---

## 6.4 Benefits

| Benefit | Description |
|---------|-------------|
| **Reduced Capital Expenditure** | No large upfront hardware investments |
| **Increased Agility** | Faster development and deployment cycles |
| **Improved Scalability** | Resources scale up/down easily |
| **Cost Efficiency** | Pay-as-you-go pricing |
| **Enhanced Security** | Providers invest heavily in security infrastructure |

---

# 7. BENEFITS OF CLOUD PLATFORMS FOR DATA ENGINEERING

| Benefit | Description |
|---------|-------------|
| **1. Scalability and Flexibility** | On-demand resources; auto-scaling; handle peak workloads |
| **2. Cost Efficiency** | Pay-as-you-go; no over-provisioning; reduced operational costs |
| **3. Agility and Speed** | Pre-configured services; faster development; serverless architectures |
| **4. Enhanced Collaboration** | Centralized data access; shared workspaces; version control |
| **5. Improved Security & Compliance** | Firewalls, encryption, access controls; governance tools |
| **6. Streamlined Data Integration** | Consolidate data from diverse sources into data warehouse/lake |
| **7. Advanced Analytics & ML** | Access to ML services; integrated with data pipelines |

---

# 8. OVERVIEW OF MICROSOFT AZURE AND AWS

## 8.1 Comparison

| Factor | AWS | Azure |
|--------|-----|-------|
| **Market Share** | Market leader | Close second |
| **Hybrid Cloud** | Scalability, third-party integrations | Stronger hybrid focus; leverages on-premises |
| **Integration** | Vast third-party integrations | Tightly integrated with Microsoft products (Windows Server, Office 365) |
| **Resource Management** | Accounts as logical boundary | Subscriptions and resource groups |
| **Compute Service** | Elastic Compute Cloud (EC2) | Virtual Machines |
| **Pricing** | Pay-as-you-go, reserved, spot instances | Pay-as-you-go, reserved, spot instances |
| **Scalability** | Excellent | Excellent + autoscaling |
| **Global Infrastructure** | More availability zones | Vast global network |

## 8.2 Choosing Between AWS and Azure

Depends on:
- Existing technology investments
- Specific workload requirements
- Desired level of integration with other services

---

# 9. EXAM PREPARATION — KEY TOPICS & QUESTIONS

## High Probability Topics

1. **3Vs of Big Data** (Volume, Velocity, Variety)
2. **Hadoop Ecosystem components** (HDFS, YARN, MapReduce, Hive, Pig, HBase, etc.)
3. **HDFS Architecture** (Name Node vs Data Node)
4. **MapReduce** (Map() and Reduce() functions)
5. **Spark vs Hadoop** (In-memory vs disk-based; 100x faster)
6. **Spark Core Components** (RDD, DataFrame, Dataset, Transformations, Actions)
7. **Cloud Service Models** (IaaS, PaaS, SaaS)
8. **Cloud Deployment Models** (Public, Private, Hybrid)
9. **AWS vs Azure comparison**
10. **Big Data Processing Pipeline** (5 stages)

## Suggested Exam Questions

1. Explain the 3Vs of Big Data with examples.
2. Compare Hadoop and Spark.
3. Describe HDFS architecture with Name Node and Data Node.
4. Explain MapReduce with Map() and Reduce() functions.
5. What are RDDs, DataFrames, and Datasets in Spark?
6. Differentiate between IaaS, PaaS, and SaaS.
7. Compare AWS and Azure cloud platforms.
8. Explain the Big Data processing pipeline stages.
9. What is YARN and its components?
10. List popular Big Data technologies and their use cases.
