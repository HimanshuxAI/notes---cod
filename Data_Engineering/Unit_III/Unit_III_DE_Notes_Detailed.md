# UNIT III — BIG DATA TECHNOLOGIES AND DISTRIBUTED COMPUTING

**Course:** 23CSE3017 – Data Engineering  
**Class:** T.Y. (SEM-I), AIEC  
**Institution:** MIT Art, Design and Technology University, MIT School of Computing, Pune  
**Academic Year:** 2025-2026 SEM-I (NEP)  
**Professor:** Dr. Aditya Pai H  
**Unit Duration:** 8 Hours  

---

# TABLE OF CONTENTS

1. [Big Data — Introduction & Characteristics](#1-big-data-introduction--characteristics)
2. [Big Data Technologies — Categories & Ecosystem](#2-big-data-technologies-categories--ecosystem)
3. [Big Data Processing Pipeline](#3-big-data-processing-pipeline)
4. [Need for Distributed Computing Frameworks](#4-need-for-distributed-computing-frameworks)
5. [Apache Hadoop Ecosystem — Deep Dive](#5-apache-hadoop-ecosystem--deep-dive)
   - [HDFS Architecture](#hdfs-architecture)
   - [MapReduce Framework](#mapreduce-framework)
   - [YARN Architecture](#yarn-architecture)
   - [Other Hadoop Ecosystem Components](#other-hadoop-ecosystem-components)
6. [Apache Spark — Architecture & Basics](#6-apache-spark--architecture--basics)
   - [Spark Core Components](#spark-core-components)
   - [RDDs, DataFrames, Datasets](#rdds-dataframes-datasets)
   - [Transformations & Actions](#transformations--actions)
   - [Spark vs Hadoop MapReduce](#spark-vs-hadoop-mapreduce)
7. [Cloud Platforms — Models & Benefits](#7-cloud-platforms--models--benefits)
8. [Azure vs AWS — Detailed Comparison](#8-azure-vs-aws--detailed-comparison)
9. [Exam Questions — Detailed Model Answers](#9-exam-questions--detailed-model-answers)
10. [Quick Revision Cheat Sheet](#10-quick-revision-cheat-sheet)

---

# 1. BIG DATA — INTRODUCTION & CHARACTERISTICS

## 1.1 What is Big Data?

**Big Data** refers to datasets that are too large, complex, or fast-moving for traditional data-processing software (like RDBMS) to handle efficiently. Traditional systems fail because they are designed for structured data on a single machine with limited storage and compute capacity.

**Big Data Engineering** involves collecting, storing, processing, analyzing, and visualizing these massive datasets in a scalable, timely, and cost-effective manner.

---

## 1.2 Characteristics of Big Data (The Vs)

Big Data is commonly described by the **3Vs**, but modern definitions include up to **7Vs**.

### The Core 3Vs

| V | Meaning | Example |
|---|---------|---------|
| **Volume** | Massive scale of data — terabytes to petabytes and beyond | Social media posts, sensor data, log files |
| **Velocity** | Speed at which data is generated, collected, and processed | Real-time stock ticks, clickstreams, IoT telemetry |
| **Variety** | Different types and formats of data | Structured (SQL tables), Semi-structured (JSON, XML), Unstructured (images, videos, text) |

### Extended Vs

| V | Meaning | Example |
|---|---------|---------|
| **Veracity** | Quality, accuracy, and trustworthiness of data | Noisy sensor readings, biased survey data |
| **Value** | Ability to extract useful insights and business value | Converting raw data into actionable decisions |
| **Variability** | Inconsistency in data flow (peak loads, seasonal spikes) | Black Friday traffic, holiday booking surges |
| **Visualization** | Presenting complex data in understandable formats | Dashboards, heatmaps, geospatial maps |

**Exam Tip:** Memorize the 3Vs with examples — this is a classic 5-mark definition question.

---

## 1.3 Types of Data

| Type | Structure | Examples | Storage |
|------|-----------|----------|---------|
| **Structured** | Fixed schema, tabular | SQL databases, CSV, Excel | RDBMS, Data Warehouse |
| **Semi-structured** | Partial structure, self-describing | JSON, XML, log files, NoSQL documents | NoSQL, Data Lake |
| **Unstructured** | No predefined format | Images, videos, audio, emails, PDFs | Object Storage (S3, Blob), Data Lake |

---

# 2. BIG DATA TECHNOLOGIES — CATEGORIES & ECOSYSTEM

Big Data technologies are a suite of software tools used to manage, process, and analyze massive, complex datasets. They are classified into four major categories:

## 2.1 Category 1: Data Storage

| Technology | Description | Key Features | Best For |
|------------|-------------|--------------|----------|
| **HDFS** (Hadoop Distributed File System) | Distributed file system storing large datasets across multiple nodes | Fault tolerance, rack awareness, block replication, commodity hardware | Raw data lakes, batch processing |
| **NoSQL Databases** (Cassandra, MongoDB, HBase) | Non-relational, horizontally scalable databases | Flexible schema, high availability, auto-sharding | Unstructured/semi-structured data, high-write workloads |
| **Cloud Object Storage** (Amazon S3, Azure Blob) | Scalable object storage for unstructured data | Durability, versioning, lifecycle policies, HTTP access | Data lakes, backups, media files |

---

## 2.2 Category 2: Data Processing & Analytics

| Technology | Description | Key Features | Best For |
|------------|-------------|--------------|----------|
| **Apache Spark** | In-memory distributed processing engine | 100x faster than MapReduce, in-memory computation, unified engine | Iterative algorithms, ML, real-time streaming |
| **Apache Kafka** | Distributed streaming platform | High-throughput, fault-tolerant, publish-subscribe messaging | Real-time data pipelines, event streaming |
| **Apache Flink** | Stream processing framework | Low latency, exactly-once semantics, event-time processing | Real-time analytics, fraud detection |
| **Cloud Data Warehouses** (BigQuery, Redshift, Snowflake) | Managed cloud analytics warehouses | SQL interface, columnar storage, auto-scaling | Business intelligence, ad-hoc analytics |

---

## 2.3 Category 3: Data Mining & Analytics

| Technology | Description | Use Case |
|------------|-------------|----------|
| **Machine Learning** | Algorithms that identify patterns and make predictions | Recommendation systems, fraud detection, churn prediction |
| **Data Mining Tools** | Software for discovering hidden patterns and anomalies | Market basket analysis, anomaly detection |

---

## 2.4 Category 4: Data Visualization

| Tool | Description | Use Case |
|------|-------------|----------|
| **Tableau** | Interactive dashboards and visual analytics | Business dashboards, executive reporting |
| **Power BI** | Microsoft business analytics tool | Self-service BI, Microsoft ecosystem integration |
| **Kibana** | Visualization for Elasticsearch data | Log analysis, operational dashboards |

---

## 2.5 Popular Big Data Technologies — Summary Table

| # | Technology | Type | Key Strength | Example Use Case |
|---|------------|------|--------------|------------------|
| 1 | **Apache Cassandra** | NoSQL DB | High availability, multi-data center replication | Messaging systems, IoT sensor data |
| 2 | **Apache Hadoop** | Batch Processing | HDFS + MapReduce, scalable, cost-effective | Log processing, ETL, data warehousing |
| 3 | **Apache Hive** | Data Warehousing | HiveQL (SQL-like), built on Hadoop | Ad-hoc querying, OLAP on Big Data |
| 4 | **Apache Flume** | Data Ingestion | Collects and aggregates log data | Log collection from web servers |
| 5 | **Apache Spark** | In-Memory Processing | Speed, unified engine, MLlib | Real-time analytics, machine learning |
| 6 | **Apache Kafka** | Streaming | High-throughput messaging, replication | Event-driven architectures, log aggregation |
| 7 | **MongoDB** | NoSQL DB | Document-oriented, JSON storage, auto-sharding | Content management, catalogs |
| 8 | **ElasticSearch** | Search & Analytics | Full-text search, scalable to petabytes | Log search, enterprise search (Wikipedia, GitHub) |

---

# 3. BIG DATA PROCESSING PIPELINE

The Big Data processing pipeline consists of five sequential stages:

## 3.1 Stage 1: Data Ingestion

**Definition:** Collecting data from various sources and bringing it into the processing system.

| Source | Examples |
|--------|----------|
| IoT Devices | Sensors, wearables, industrial controllers |
| Logs | Web server logs, application logs, system logs |
| Sensors | Temperature, pressure, GPS, motion sensors |
| Web APIs | REST APIs, GraphQL, third-party services |
| Databases | Relational databases, NoSQL stores |

| Ingestion Tool | Description |
|---------------|-------------|
| **Apache Kafka** | Distributed streaming platform for high-volume data ingestion |
| **Apache Flume** | Distributed, reliable system for collecting log data |
| **Apache Sqoop** | Tool for transferring data between Hadoop and structured datastores (RDBMS) |

---

## 3.2 Stage 2: Data Storage

**Definition:** Storing ingested data in distributed storage systems for durability and scalability.

| Storage System | Description | Best For |
|---------------|-------------|----------|
| **HDFS** | Hadoop Distributed File System — blocks replicated across nodes | Raw data, batch workloads |
| **Amazon S3** | Scalable object storage with 11 nines durability | Data lakes, backups, media |
| **Azure Blob Storage** | Microsoft's object storage for unstructured data | Backups, data lakes, media serving |

---

## 3.3 Stage 3: Data Processing

**Definition:** Transforming raw data into usable formats through batch or real-time processing.

| Processing Type | Description | Tools |
|----------------|-------------|-------|
| **Batch Processing** | Processing large volumes of data at scheduled intervals | Apache Hadoop MapReduce |
| **Real-Time Processing** | Processing data as it arrives (streaming) | Apache Spark, Apache Storm, Apache Flink |

---

## 3.4 Stage 4: Data Analysis

**Definition:** Applying machine learning, statistical analysis, and analytics frameworks to extract insights.

| Tool | Description |
|------|-------------|
| **Spark MLlib** | Machine learning library for distributed ML on Spark |
| **Apache Hive** | SQL-like querying (HiveQL) on top of Hadoop |
| **Apache Pig** | Script-based data flow language (Pig Latin) |

---

## 3.5 Stage 5: Data Visualization

**Definition:** Presenting analyzed data through dashboards, charts, and visual storytelling.

| Tool | Description |
|------|-------------|
| **Tableau** | Interactive visual analytics and dashboards |
| **Power BI** | Microsoft business intelligence and visualization |
| **Kibana** | Visualization layer for Elasticsearch (log analysis) |

---

## 3.6 Pipeline Example

```
Data Sources (IoT, Logs, APIs)
       ↓
Data Ingestion (Kafka, Flume, Sqoop)
       ↓
Data Storage (HDFS, S3, Azure Blob)
       ↓
Data Processing (MapReduce / Spark / Flink)
       ↓
Data Analysis (Hive, MLlib, Pig)
       ↓
Data Visualization (Tableau, Power BI, Kibana)
```

---

# 4. NEED FOR DISTRIBUTED COMPUTING FRAMEWORKS

## 4.1 Limitations of Traditional Centralized Systems

| Limitation | Detailed Explanation |
|------------|---------------------|
| **Memory Bottlenecks** | A single machine's RAM is limited (typically up to a few TB). Datasets in the petabyte range cannot fit in memory. |
| **Processing Speed** | Sequential processing on one CPU/core becomes too slow for time-sensitive analysis. Jobs that take days on one machine can finish in minutes on a cluster. |
| **Scalability Issues** | Vertical scaling (buying a bigger machine) is expensive and has a physical ceiling. You cannot keep adding RAM/CPU indefinitely. |
| **Single Point of Failure** | If the central machine crashes (hardware failure, power outage), the entire system goes down. All data and processing are lost or interrupted. |

---

## 4.2 What Are Distributed Computing Frameworks?

**Definition:** Systems that split large computational tasks into smaller chunks and distribute them across multiple nodes (computers) in a cluster to work in parallel.

**Popular Examples:**
- Apache Hadoop (MapReduce)
- Apache Spark
- Apache Flink
- Google Dataflow

---

## 4.3 Why Are Distributed Frameworks Needed?

| Reason | Explanation |
|--------|-------------|
| **Volume Handling** | Petabytes of data can be processed efficiently by distributing the load across many machines. No single machine needs to hold all the data. |
| **Faster Computation (Parallelism)** | Tasks run simultaneously on multiple nodes. Spark can be up to **100x faster** than Hadoop MapReduce for in-memory operations because it avoids disk I/O between iterations. |
| **Fault Tolerance** | Data is replicated across nodes (e.g., HDFS default replication factor = 3). If one node fails, another node holding a replica can take over without data loss or halting the system. |
| **Cost-Effective Scalability (Horizontal Scaling)** | Instead of buying one expensive supercomputer, you add inexpensive commodity hardware (servers) to the cluster. This is cheaper and more flexible. |
| **Support for Diverse Workloads** | Distributed frameworks handle batch, stream, interactive, and machine learning workloads in a unified environment (e.g., Spark does all four). |

---

## 4.4 Real-World Use Cases

| Domain | Use Case | Framework |
|--------|----------|-----------|
| **Finance** | Real-time fraud detection using Spark Streaming | Spark Streaming |
| **Healthcare** | Distributed EHR (Electronic Health Record) analysis for disease prediction | Hadoop / Spark |
| **E-commerce** | Product recommendation engines processing user behavior | Flink / Spark |
| **Smart Cities** | Sensor data fusion from traffic, pollution, and weather sensors | Hadoop + Spark |

---

# 5. APACHE HADOOP ECOSYSTEM — DEEP DIVE

## 5.1 Overview

**Apache Hadoop** is an open-source framework that enables distributed storage and processing of large datasets across clusters of commodity hardware. It was inspired by Google's MapReduce and Google File System (GFS) papers.

**Core Philosophy:** Store data cheaply on many machines, and move computation to the data (data locality) rather than moving data to computation.

---

## 5.2 Four Major Elements of Hadoop

| Element | Full Name | Role |
|---------|-----------|------|
| **HDFS** | Hadoop Distributed File System | Distributed storage |
| **MapReduce** | — | Distributed batch processing |
| **YARN** | Yet Another Resource Negotiator | Cluster resource management |
| **Hadoop Common** | — | Common libraries and utilities used by other modules |

---

## 5.3 Complete Hadoop Ecosystem Components

| # | Component | Category | Description |
|---|-----------|----------|-------------|
| 1 | **HDFS** | Storage | Distributed file system for large datasets |
| 2 | **YARN** | Resource Management | Schedules and allocates cluster resources |
| 3 | **MapReduce** | Processing | Batch processing using Map() and Reduce() |
| 4 | **Spark** | Processing | In-memory distributed processing |
| 5 | **PIG** | Query/Scripting | Pig Latin — script-based data flow language |
| 6 | **HIVE** | Query/Warehouse | HiveQL — SQL-like interface for data warehousing |
| 7 | **HBase** | Database | NoSQL column-family database on HDFS |
| 8 | **Mahout** | ML | Machine learning libraries (clustering, classification, collaborative filtering) |
| 9 | **Spark MLLib** | ML | Machine learning library for Spark |
| 10 | **Solr / Lucene** | Search | Full-text search and indexing |
| 11 | **Zookeeper** | Coordination | Distributed coordination and synchronization service |
| 12 | **Oozie** | Scheduling | Workflow scheduler for Hadoop jobs |

---

## 5.4 HDFS — Hadoop Distributed File System

### 5.4.1 Architecture

HDFS follows a **master-slave architecture**:

```
┌─────────────────┐      ┌─────────────────┐
│   Name Node     │──────│  Data Node 1    │
│   (Master)      │      │  (Slave/Worker) │
│   Metadata      │──────│  Actual Data    │
└─────────────────┘      └─────────────────┘
         │
         ├── Data Node 2 (Actual Data)
         ├── Data Node 3 (Actual Data)
         └── ... N Data Nodes
```

### 5.4.2 Name Node vs Data Node

| Feature | Name Node | Data Node |
|---------|-----------|-----------|
| **Role** | Master node | Slave/Worker node |
| **Stores** | Metadata (file-to-block mapping, directory structure, permissions) | Actual data blocks |
| **Resources Required** | Comparatively fewer (RAM-intensive for metadata) | More (disk and CPU intensive) |
| **Hardware** | Typically high-quality, reliable hardware | Commodity hardware (cheap, can fail) |
| **Failure Impact** | Single point of failure (mitigated by Secondary Name Node / HA) | Individual failure tolerated (data replicated elsewhere) |
| **Responsibility** | Coordinates cluster, manages namespace, tracks block locations | Stores and retrieves blocks, reports block status to Name Node |

### 5.4.3 HDFS Key Concepts

| Concept | Description |
|---------|-------------|
| **Block** | Files are split into blocks (default 128 MB in HDFS 2.x/3.x). Each block is stored independently. |
| **Replication** | Each block is replicated across multiple nodes (default factor = 3) for fault tolerance. |
| **Rack Awareness** | HDFS tries to place replicas on different racks to survive rack-level failures. |
| **Data Locality** | Computation is scheduled on the node where data resides, minimizing network transfer. |
| **Write Once, Read Many** | HDFS files are immutable after creation — optimized for batch analytical workloads, not frequent updates. |

---

## 5.5 MapReduce Framework

### 5.5.1 Overview

MapReduce is a programming model for distributed batch processing. It allows writing applications that transform large datasets into manageable results using two core functions.

### 5.5.2 The Two Functions

| Function | Input | Output | Purpose |
|----------|-------|--------|---------|
| **Map()** | Key-value pairs | Intermediate key-value pairs | Sorting, filtering, grouping data |
| **Reduce()** | Intermediate key-value pairs | Final key-value pairs | Summarization, aggregation |

### 5.5.3 How MapReduce Works (Step-by-Step)

```
INPUT DATA
     ↓
1. INPUT SPLIT
   - Divide input into logical splits (one per Map task)
     ↓
2. MAPPING (Map phase)
   - Each split processed by a Map task
   - Map() produces <key, value> intermediate pairs
     ↓
3. SHUFFLE & SORT
   - Intermediate pairs shuffled across network
   - Grouped by key, sent to Reducers
     ↓
4. REDUCING (Reduce phase)
   - Reduce() aggregates values for each key
   - Produces final output
     ↓
5. OUTPUT
   - Final results written to HDFS
```

### 5.5.4 Example: Word Count

**Input:** "Hello world, hello Hadoop"

**Map Phase:**
- "Hello" → <"Hello", 1>
- "world," → <"world", 1>
- "hello" → <"hello", 1>
- "Hadoop" → <"Hadoop", 1>

**Shuffle & Sort:** Group by key (case-insensitive):
- "hello" → [1, 1]
- "world" → [1]
- "hadoop" → [1]

**Reduce Phase:**
- "hello" → sum([1, 1]) = 2
- "world" → sum([1]) = 1
- "hadoop" → sum([1]) = 1

**Output:** <"hello", 2>, <"world", 1>, <"hadoop", 1>

---

## 5.6 YARN — Yet Another Resource Negotiator

### 5.6.1 Overview

YARN is the cluster resource management layer of Hadoop. It decouples resource management from job scheduling/execution, allowing multiple data processing engines (MapReduce, Spark, etc.) to run on the same cluster.

### 5.6.2 YARN Components

| Component | Role | Responsibility |
|-----------|------|----------------|
| **Resource Manager (RM)** | Master daemon | Arbitrates all cluster resources; makes scheduling decisions; runs on a master node |
| **Node Manager (NM)** | Slave daemon | Manages resources on individual nodes (CPU, memory, disk, network); reports to RM; launches/monitors containers |
| **Application Master (AM)** | Per-application daemon | Negotiates resources from RM; works with NM to execute tasks; monitors task progress |

### 5.6.3 YARN Workflow

```
1. Client submits application to Resource Manager
     ↓
2. RM allocates a container for Application Master
     ↓
3. AM registers with RM and requests resources for tasks
     ↓
4. RM allocates containers on Node Managers
     ↓
5. AM launches tasks in containers via Node Managers
     ↓
6. Tasks execute and report status to AM
     ↓
7. AM reports application completion to RM
```

---

## 5.7 Other Hadoop Ecosystem Components

### 5.7.1 PIG

- **Developed by:** Yahoo
- **Language:** Pig Latin (script-based, SQL-like)
- **How it works:** You write a data flow script; Pig converts it into MapReduce jobs behind the scenes
- **Analogy:** Like giving a chef a recipe instead of explaining every hand movement
- **Output:** Stored in HDFS

### 5.7.2 HIVE

- **Purpose:** Data warehousing on Hadoop
- **Language:** HiveQL (SQL-like)
- **Processing:** Supports both batch and real-time processing
- **Components:** JDBC/ODBC drivers (connections/permissions), Hive Command Line (query processing)
- **Best for:** OLAP, ad-hoc querying, users who know SQL but not Java

### 5.7.3 HBase

- **Type:** NoSQL column-family database
- **Inspiration:** Google's BigTable
- **Best for:** Fast random read/write access to small amounts of data within huge datasets
- **Use case:** Searching for a specific record in a petabyte-scale table

### 5.7.4 Mahout & Spark MLLib

- **Purpose:** Machine learning on Big Data
- **Capabilities:** Collaborative filtering, clustering, classification, regression

### 5.7.5 Solr & Lucene

- **Lucene:** Java library for full-text search and indexing (includes spell check)
- **Solr:** Search server built on Lucene; provides distributed search, faceting, etc.

### 5.7.6 Zookeeper

- **Purpose:** Distributed coordination and synchronization
- **Solves:** Inconsistency caused by lack of coordination among Hadoop components
- **Functions:** Configuration management, naming, synchronization, group services

### 5.7.7 Oozie

- **Purpose:** Workflow scheduler for Hadoop jobs
- **Job Types:**
  - **Oozie Workflow:** Sequential execution of actions
  - **Oozie Coordinator:** Trigger-based execution (time-based or data-based)

---

# 6. APACHE SPARK — ARCHITECTURE & BASICS

## 6.1 What is Apache Spark?

**Apache Spark** is a unified, open-source, distributed processing engine designed for large-scale data processing and analytics. It was created at UC Berkeley's AMPLab and later donated to the Apache Software Foundation.

**Supported Workloads:**
- Batch processing
- Real-time streaming (Spark Streaming / Structured Streaming)
- SQL queries (Spark SQL)
- Machine learning (MLlib)
- Graph processing (GraphX)

**Key Advantage:** Spark builds on Hadoop MapReduce's limitations by enabling **in-memory computations**, making it significantly faster for iterative algorithms.

---

## 6.2 Key Features of Spark

| Feature | Description |
|---------|-------------|
| **Speed** | In-memory computation makes Spark up to 100x faster than Hadoop MapReduce for iterative algorithms |
| **Ease of Use** | APIs available in Python (PySpark), Java, Scala, and R |
| **Advanced Analytics** | Built-in libraries: MLlib (ML), Spark Streaming, GraphX, Spark SQL |
| **Unified Engine** | Batch + streaming + SQL + ML workloads in one framework — no need to stitch multiple systems |
| **Fault Tolerance** | RDD lineage graph tracks how each dataset was derived, enabling automatic recovery |
| **Scalability** | Scales from a single laptop to thousands of nodes with minimal code changes |

---

## 6.3 Spark Architecture

Spark follows a **master-slave architecture** with three main components:

```
┌─────────────────────────────────────────┐
│         Driver Program                  │
│  (main() function, SparkContext)        │
└─────────────────┬───────────────────────┘
                  │ coordinates
┌─────────────────▼───────────────────────┐
│       Cluster Manager                   │
│  (YARN / Mesos / Kubernetes / Standalone)│
└─────────────────┬───────────────────────┘
                  │ allocates
          ┌───────┴───────┐
          ▼               ▼
    Executor 1        Executor 2  ... Executor N
    (Worker Node)     (Worker Node)   (Worker Node)
    Runs tasks        Runs tasks      Runs tasks
    on partitions     on partitions   on partitions
```

| Component | Role |
|-----------|------|
| **Driver Program** | Runs the main() function, creates SparkContext/SparkSession, converts user code into a logical plan (DAG), schedules tasks |
| **Cluster Manager** | Allocates resources across the cluster. Options: YARN, Apache Mesos, Kubernetes, or Spark Standalone |
| **Executors (Workers)** | Worker nodes that run tasks, store data in memory/disk, and return results to the driver. Each executor runs on a partitioned dataset. |

---

## 6.4 Core Spark Components

| Module | Purpose | Use Case |
|--------|---------|----------|
| **Spark Core** | Base engine — memory management, fault recovery, scheduling, task distribution | All Spark applications |
| **Spark SQL** | Structured data processing using SQL or DataFrames | ETL, reporting, ad-hoc queries |
| **Spark Streaming** | Real-time data stream processing (micro-batch model) | Log monitoring, fraud detection, real-time dashboards |
| **MLlib** | Machine learning library — classification, regression, clustering, collaborative filtering | Recommendation systems, predictive models |
| **GraphX** | Graph computation library | PageRank, social network analysis, shortest path |

---

## 6.5 Spark Basics — RDDs, DataFrames, Datasets

### 6.5.1 RDDs (Resilient Distributed Datasets)

**Definition:** RDDs are the fundamental data structure of Spark — an immutable, distributed collection of objects partitioned across a cluster that can be operated on in parallel.

| Property | Description |
|----------|-------------|
| **Immutability** | Once created, an RDD cannot be changed. Transformations create new RDDs. |
| **Partitioning** | RDDs are split into logical partitions. Each partition can be computed on a different node. |
| **Creation** | From HDFS files, local files, existing RDDs, or parallelizing collections. |
| **Resilience** | Fault-tolerant via lineage graph — if a partition is lost, Spark can recompute it from its parents. |

**Example:** Think of an RDD as a large dataset split into smaller chunks distributed across the cluster.

### 6.5.2 DataFrames

**Definition:** A DataFrame is a distributed collection of data organized into named columns (like a table in a relational database or a Pandas DataFrame). It is a higher-level abstraction built on top of RDDs.

| Property | Description |
|----------|-------------|
| **Structure** | Data organized into named columns with specific data types (schema) |
| **Schema** | Each DataFrame has a defined schema specifying column names and types |
| **Advantages** | Better performance than RDDs (Catalyst optimizer, Tungsten execution), easier API, SQL integration |
| **Best for** | Structured and semi-structured data (JSON, Parquet, CSV, database tables) |

### 6.5.3 Datasets

**Definition:** A strongly-typed data structure available primarily in Scala and Java. Combines the benefits of RDDs (strong typing, powerful functional transformations) and DataFrames (optimized execution engine).

| Property | Description |
|----------|-------------|
| **Strong Typing** | Compile-time type safety — type errors caught during development |
| **Flexibility** | Supports both functional (map, filter) and relational (SQL) operations |
| **Limitation** | Not available in Python or R (dynamic languages) |

---

## 6.6 Transformations & Actions

### 6.6.1 Transformations (Lazy Evaluation)

**Definition:** Transformations are operations that take an RDD/DataFrame as input and produce a new one. They are **lazily evaluated** — Spark does not execute them immediately. Instead, it records the transformation in a lineage graph (DAG). Execution only happens when an action is called.

| Transformation | Description |
|---------------|-------------|
| **map(func)** | Applies a function to each element; returns a new RDD |
| **filter(func)** | Returns a new RDD with elements that satisfy the condition |
| **flatMap(func)** | Like map, but each input can produce zero or more outputs |
| **groupByKey()** | Groups values by key |
| **reduceByKey(func)** | Combines values for each key using a function (e.g., sum) |
| **join(other)** | Joins two datasets on a key |
| **union(other)** | Returns union of two RDDs |
| **distinct()** | Returns distinct elements |

### 6.6.2 Actions (Eager Evaluation)

**Definition:** Actions trigger the execution of all preceding transformations. They return a result to the driver program or write data to external storage. Actions are **eagerly evaluated** — they force computation of the entire DAG.

| Action | Description |
|--------|-------------|
| **count()** | Returns the number of elements in the RDD |
| **collect()** | Returns all elements as an array to the driver program |
| **take(n)** | Returns the first n elements |
| **saveAsTextFile(path)** | Saves the RDD as a text file in HDFS/S3 |
| **foreach(func)** | Applies a function to each element (used for side effects like writing to a DB) |
| **reduce(func)** | Aggregates all elements using a binary function |
| **first()** | Returns the first element |

---

## 6.7 Spark vs Hadoop MapReduce

| Feature | Apache Spark | Hadoop MapReduce |
|---------|-------------|------------------|
| **Processing Model** | In-memory (keeps data in RAM between iterations) | Disk-based (writes intermediate data to disk) |
| **Speed** | Up to 100x faster for iterative algorithms; ~10x faster for batch | Slower due to disk I/O |
| **Ease of Use** | Rich APIs in Python, Java, Scala, R; interactive shell (REPL) | Java-heavy; verbose code |
| **Workload Support** | Batch, streaming, SQL, ML, graph (unified) | Primarily batch |
| **Fault Tolerance** | RDD lineage (recompute lost partitions) | Task re-execution on failure |
| **Latency** | Low (suitable for near real-time) | High (suitable for batch) |
| **Best For** | Machine learning, streaming, interactive queries | Massive ETL jobs where memory is limited |

---

# 7. CLOUD PLATFORMS — MODELS & BENEFITS

## 7.1 What is a Cloud Platform?

A cloud platform provides on-demand access to computing resources (servers, storage, databases, networking, software) over the internet, eliminating the need for organizations to own and maintain physical infrastructure.

| Feature | Description |
|---------|-------------|
| **On-demand access** | Resources available whenever needed; rent instead of buy |
| **Pay-as-you-go** | Pay only for resources consumed (hourly/secondly billing) |
| **Centralized management** | Cloud provider manages hardware, updates, security patches |
| **Scalability and flexibility** | Scale resources up or down instantly based on demand |

---

## 7.2 Cloud Service Models

| Model | Full Name | What It Provides | Examples | User Responsibility |
|-------|-----------|------------------|----------|---------------------|
| **IaaS** | Infrastructure as a Service | Virtual machines, storage, networks, load balancers | AWS EC2, Azure VMs, Google Compute Engine | OS, middleware, runtime, applications |
| **PaaS** | Platform as a Service | Development platform — OS, middleware, runtime | AWS Elastic Beanstalk, Azure App Service, Google App Engine | Applications and data |
| **SaaS** | Software as a Service | Complete software applications over the internet | Gmail, Salesforce, Office 365, Dropbox | Nothing (just use it) |

**Simple Analogy:**
- **IaaS:** Renting a plot of land — you build the house (install OS, software)
- **PaaS:** Renting a furnished apartment — you bring your furniture (applications)
- **SaaS:** Staying in a hotel — everything is provided, you just use it

---

## 7.3 Cloud Deployment Models

| Model | Description | Example |
|-------|-------------|---------|
| **Public Cloud** | Resources owned and operated by a third-party provider, shared among multiple organizations over the public internet | AWS, Azure, Google Cloud |
| **Private Cloud** | Resources dedicated to a single organization; can be on-premises or hosted by a third party | VMware on-prem, Azure Stack |
| **Hybrid Cloud** | Combines public and private clouds, allowing data and applications to be shared between them | Azure Arc, AWS Outposts |

---

## 7.4 Benefits of Cloud Platforms

| Benefit | Explanation |
|---------|-------------|
| **Reduced Capital Expenditure (CapEx)** | No large upfront investment in hardware, data centers, or software licenses |
| **Increased Agility and Innovation** | Developers can provision resources in minutes, enabling rapid experimentation and deployment |
| **Improved Scalability** | Auto-scaling handles traffic spikes automatically; scale down during low demand to save costs |
| **Cost Efficiency** | Pay-as-you-go pricing; no over-provisioning; turn off resources when not in use |
| **Enhanced Security** | Cloud providers invest heavily in physical security, encryption, threat detection, and compliance |
| **Global Reach** | Deploy applications close to users in multiple geographic regions for low latency |

---

# 8. AZURE VS AWS — DETAILED COMPARISON

## 8.1 Overview

| Factor | Amazon Web Services (AWS) | Microsoft Azure |
|--------|---------------------------|-----------------|
| **Launch Year** | 2006 | 2010 |
| **Market Share** | Market leader (largest cloud provider) | Close second, strong enterprise presence |
| **Core Philosophy** | Developer-first, vast service catalog | Enterprise-first, strong Microsoft ecosystem integration |

---

## 8.2 Service Comparison

| Category | AWS Service | Azure Service | Notes |
|----------|-------------|---------------|-------|
| **Compute** | EC2 (Elastic Compute Cloud) | Azure Virtual Machines | Both offer VMs with various instance types |
| **Container Service** | EKS (Elastic Kubernetes Service) | AKS (Azure Kubernetes Service) | Managed Kubernetes |
| **Serverless** | AWS Lambda | Azure Functions | Event-driven, pay-per-execution |
| **Object Storage** | Amazon S3 | Azure Blob Storage | Both highly durable, scalable |
| **Block Storage** | Amazon EBS | Azure Managed Disks | Attached to VMs |
| **Data Warehouse** | Amazon Redshift | Azure Synapse Analytics | Columnar, MPP architecture |
| **Data Lake** | Amazon S3 + Lake Formation | Azure Data Lake Storage Gen2 | Hierarchical namespace, analytics-ready |
| **Database (Relational)** | Amazon RDS | Azure SQL Database | Managed SQL databases |
| **Database (NoSQL)** | Amazon DynamoDB | Azure Cosmos DB | Globally distributed, multi-model |
| **Data Integration** | AWS Glue | Azure Data Factory | ETL/ELT orchestration |
| **Analytics** | Amazon EMR, Kinesis | Azure HDInsight, Stream Analytics | Big data and streaming |
| **BI & Visualization** | Amazon QuickSight | Power BI | Power BI deeply integrated with Azure |
| **Identity** | AWS IAM | Azure Active Directory (Entra ID) | User and access management |

---

## 8.3 Key Differences

| Dimension | AWS | Azure |
|-----------|-----|-------|
| **Hybrid Cloud** | Strong, but primarily cloud-native | Stronger hybrid focus — Azure Arc, Azure Stack extend cloud to on-premises |
| **Enterprise Integration** | Broad third-party integrations | Deep integration with Microsoft ecosystem (Windows Server, Office 365, Active Directory, .NET) |
| **Resource Organization** | **Accounts** are the primary logical boundary | **Subscriptions** and **Resource Groups** organize resources |
| **Pricing** | Pay-as-you-go, Reserved Instances, Spot Instances | Pay-as-you-go, Reserved VM Instances, Spot VMs |
| **Global Infrastructure** | More Availability Zones and Regions historically | Vast global network, strong in enterprise regions |
| **Certifications** | Large number of specialized certifications | Strong enterprise compliance (ISO, SOC, HIPAA, GDPR) |

---

## 8.4 Choosing Between AWS and Azure

**Choose AWS if:**
- You need the broadest service catalog and newest features first
- You want the largest community and third-party tooling
- You are building cloud-native applications from scratch

**Choose Azure if:**
- Your organization is heavily invested in Microsoft products (Windows, Office 365, Active Directory, .NET, SQL Server)
- You need strong hybrid cloud capabilities (extending on-premises to cloud)
- You want tight integration with Power BI and Microsoft 365

---

# 9. EXAM QUESTIONS — DETAILED MODEL ANSWERS

Based on the syllabus, here are detailed answers to likely exam questions.

---

### Q1. What are the characteristics of Big Data? Explain the 3Vs with examples.

**Answer:**

Big Data is characterized by the **3Vs** (Volume, Velocity, Variety), with extended characteristics including Veracity, Value, Variability, and Visualization.

| Characteristic | Explanation | Real-World Example |
|---------------|-------------|-------------------|
| **Volume** | Massive scale of data — from terabytes to petabytes and exabytes | Facebook generates over 4 petabytes of data per day from user posts, photos, and videos |
| **Velocity** | High speed at which data is generated, collected, and processed | Stock exchange tick data, Twitter tweets, IoT sensor readings every second |
| **Variety** | Different formats — structured, semi-structured, and unstructured | SQL tables (structured), JSON/XML logs (semi-structured), images/videos/emails (unstructured) |

**Extended Vs:**
- **Veracity:** Uncertainty/reliability of data (e.g., noisy sensor readings)
- **Value:** Extracting business insights from raw data
- **Variability:** Inconsistent data flow (e.g., Black Friday traffic spikes)
- **Visualization:** Presenting insights via dashboards (Tableau, Power BI)

---

### Q2. Explain HDFS architecture with Name Node and Data Node.

**Answer:**

**HDFS (Hadoop Distributed File System)** is the primary storage component of the Hadoop ecosystem. It uses a **master-slave architecture** to store large files across multiple machines.

**Architecture Diagram:**

```
┌─────────────────────┐
│   Client            │
└──────────┬──────────┘
           │
     ┌─────▼─────────┐
     │  Name Node    │  ← Master (Metadata)
     │  (Single)     │
     └─────┬─────────┘
           │ coordinates
   ┌───────┴───────┬───────┐
   ▼               ▼       ▼
Data Node   Data Node   Data Node
(Slave)     (Slave)     (Slave)
Actual Data Actual Data Actual Data
Blocks      Blocks      Blocks
```

**Name Node (Master):**
- Stores **metadata** — file-to-block mapping, directory structure, permissions, replication factor
- Requires fewer resources but is memory-intensive (keeps metadata in RAM)
- Single point of failure (mitigated by High Availability setup with Secondary Name Node)
- Makes decisions about block placement and replication

**Data Node (Slave/Worker):**
- Stores **actual data blocks** on commodity hardware
- Requires more disk and CPU resources
- Sends heartbeat and block reports to Name Node
- Individual failures are tolerated because data is replicated across multiple nodes

**Key HDFS Concepts:**
- **Block Size:** Default 128 MB (HDFS 2.x/3.x). Files are split into blocks.
- **Replication Factor:** Default = 3. Each block stored on 3 nodes (typically 2 on same rack, 1 on different rack).
- **Data Locality:** Computation is moved to the node where data resides, minimizing network traffic.
- **Write Once, Read Many:** Files are immutable after creation — optimized for analytical batch workloads.

---

### Q3. Compare Hadoop MapReduce and Apache Spark.

**Answer:**

| Basis | Hadoop MapReduce | Apache Spark |
|-------|-----------------|--------------|
| **Processing Speed** | Disk-based — intermediate data written to disk between map and reduce | In-memory — keeps data in RAM between operations |
| **Performance** | Slower (~10x slower than Spark for iterative jobs) | Up to 100x faster than MapReduce for in-memory computations |
| **Ease of Programming** | Verbose Java code; steep learning curve | Rich APIs in Python (PySpark), Java, Scala, R; interactive shell |
| **Workload Types** | Primarily batch processing | Batch, streaming, SQL, ML, graph — unified engine |
| **Fault Tolerance** | Task re-execution on node failure | RDD lineage — recompute lost partitions from lineage graph |
| **Latency** | High latency (minutes to hours) | Low latency (seconds to minutes) |
| **Best Use Case** | Massive ETL jobs on disk-limited clusters | Machine learning, real-time analytics, interactive queries |
| **Ecosystem** | Mature, stable, widely adopted | Modern, rapidly evolving, preferred for new Big Data projects |

**Key Difference:** MapReduce writes intermediate results to disk after every map/reduce stage, causing heavy disk I/O. Spark keeps intermediate data in memory (RDDs), making it ideal for iterative algorithms like machine learning.

---

### Q4. Explain MapReduce with Map() and Reduce() functions.

**Answer:**

**MapReduce** is a programming model for distributed batch processing on large clusters. It processes data in two main phases.

**Map() Function:**
- Input: A set of key-value pairs
- Output: Intermediate key-value pairs
- Task: Filters, sorts, and groups data; applies a user-defined function to each input record

**Reduce() Function:**
- Input: Intermediate key-value pairs grouped by key
- Output: Final key-value pairs
- Task: Aggregates/summarizes values associated with each intermediate key

**Word Count Example:**

**Input:** "Hello world, hello Hadoop"

**Map Phase:**
- "Hello" → <"Hello", 1>
- "world" → <"world", 1>
- "hello" → <"hello", 1>
- "Hadoop" → <"Hadoop", 1>

**Shuffle & Sort:** Intermediate pairs are grouped by key across the network:
- "hello" → [1, 1]
- "world" → [1]
- "hadoop" → [1]

**Reduce Phase:**
- "hello" → sum([1, 1]) = **2**
- "world" → sum([1]) = **1**
- "hadoop" → sum([1]) = **1**

**Final Output:** <"hello", 2>, <"world", 1>, <"hadoop", 1>

**Additional Stages (Internal to Hadoop):**
- **InputSplit:** Divides input into logical chunks (one per Map task)
- **Shuffle:** Transfers map outputs to reducers
- **Sort:** Sorts intermediate keys before sending to reducers

---

### Q5. What is YARN? Explain its components.

**Answer:**

**YARN (Yet Another Resource Negotiator)** is the cluster resource management layer of Apache Hadoop (introduced in Hadoop 2.x). It decouples resource management from job scheduling, allowing multiple processing engines (MapReduce, Spark, Tez, Flink) to share the same cluster.

**YARN Components:**

| Component | Type | Responsibility |
|-----------|------|----------------|
| **Resource Manager (RM)** | Master daemon (one per cluster) | Arbitrates all cluster resources; makes scheduling decisions; runs on a dedicated master node |
| **Node Manager (NM)** | Slave daemon (one per node) | Manages resources on individual nodes (CPU, memory, disk, network); launches and monitors containers; sends heartbeats to RM |
| **Application Master (AM)** | Per-application daemon | Negotiates resources from RM; coordinates task execution with NMs; monitors application progress |

**YARN Workflow:**
1. Client submits an application to the Resource Manager.
2. RM allocates a container to launch the Application Master.
3. AM registers with RM and requests containers for its tasks.
4. RM allocates containers on Node Managers based on resource availability.
5. AM launches tasks inside containers on Node Managers.
6. Tasks execute and send status/heartbeats to AM.
7. Upon completion, AM unregisters and RM reclaims resources.

**Significance:** Before YARN (Hadoop 1.x), MapReduce handled both resource management and job scheduling, limiting the cluster to MapReduce jobs only. YARN made Hadoop a general-purpose data operating system.

---

### Q6. Compare IaaS, PaaS, and SaaS.

**Answer:**

| Basis | IaaS (Infrastructure as a Service) | PaaS (Platform as a Service) | SaaS (Software as a Service) |
|-------|-----------------------------------|------------------------------|------------------------------|
| **What It Provides** | Virtual machines, storage, networks | Development platform (OS, middleware, runtime) | Complete software applications |
| **Examples** | AWS EC2, Azure VMs, Google Compute Engine | AWS Elastic Beanstalk, Azure App Service, Google App Engine | Gmail, Salesforce, Office 365, Dropbox |
| **User Manages** | OS, middleware, runtime, applications, data | Applications and data | Nothing (just uses the software) |
| **Provider Manages** | Physical hardware, virtualization | Physical hardware, virtualization, OS, middleware, runtime | Everything |
| **Analogy** | Renting an empty plot of land — you build the house | Renting a furnished apartment — you bring your furniture | Staying in a hotel — everything is provided |
| **Best For** | Organizations wanting full control over infrastructure | Developers who want to focus on code, not infrastructure | End-users who want ready-to-use software |

---

### Q7. Differentiate between AWS and Azure.

**Answer:**

| Basis | Amazon Web Services (AWS) | Microsoft Azure |
|-------|---------------------------|-----------------|
| **Market Position** | Market leader, largest cloud provider | Strong second, dominant in enterprise |
| **Primary Strength** | Broadest service catalog, cloud-native innovation | Enterprise integration, hybrid cloud |
| **Key Compute Service** | EC2 (Elastic Compute Cloud) | Azure Virtual Machines |
| **Key Storage Service** | Amazon S3 (Object Storage) | Azure Blob Storage |
| **Key Data Warehouse** | Amazon Redshift | Azure Synapse Analytics |
| **Key ETL Service** | AWS Glue | Azure Data Factory |
| **Hybrid Cloud** | Available but cloud-native focus | Strong hybrid focus (Azure Arc, Azure Stack) |
| **Enterprise Integration** | Broad third-party ecosystem | Deep integration with Microsoft products (Windows Server, Office 365, AD, .NET) |
| **Resource Organization** | AWS Accounts | Azure Subscriptions and Resource Groups |
| **Serverless** | AWS Lambda | Azure Functions |
| **Kubernetes** | Amazon EKS | Azure AKS |

**Choosing Between Them:**
- Choose **AWS** if you need the broadest service catalog, want cloud-native innovation, or are building greenfield cloud applications.
- Choose **Azure** if your organization uses Microsoft products heavily, needs strong hybrid cloud capabilities, or wants tight integration with Power BI and Office 365.

---

### Q8. What are the stages of the Big Data processing pipeline? Explain each with tools.

**Answer:**

The Big Data processing pipeline consists of five stages:

| Stage | Description | Tools | Example |
|-------|-------------|-------|---------|
| **1. Data Ingestion** | Collecting data from various sources into the system | Apache Kafka, Flume, Sqoop | Ingesting web server logs via Flume |
| **2. Data Storage** | Storing data durably in distributed storage | HDFS, Amazon S3, Azure Blob Storage | Storing raw logs in HDFS |
| **3. Data Processing** | Transforming raw data via batch or stream processing | Hadoop MapReduce (batch), Spark/Flink (streaming) | Running word count on MapReduce |
| **4. Data Analysis** | Extracting insights using ML and analytics | Spark MLlib, Hive, Pig | Running SQL queries via Hive |
| **5. Data Visualization** | Presenting insights through dashboards | Tableau, Power BI, Kibana | Building a sales dashboard in Power BI |

**End-to-End Example:**
IoT sensors → Kafka (ingestion) → HDFS (storage) → Spark Streaming (processing) → MLlib (analysis: anomaly detection) → Power BI (visualization: alert dashboard)

---

### Q9. What are the key components of the Apache Hadoop ecosystem? Explain any five.

**Answer:**

The Hadoop ecosystem consists of HDFS, YARN, MapReduce, Spark, HBase, Hive, Pig, Mahout, Solr/Lucene, Zookeeper, and Oozie.

**Five Components Explained:**

1. **HDFS (Hadoop Distributed File System):** Distributed storage layer. Stores large files as blocks across commodity hardware with replication (default 3x) for fault tolerance. Consists of Name Node (metadata) and Data Nodes (actual data).

2. **MapReduce:** Distributed batch processing framework. Uses Map() (filter/sort/group) and Reduce() (aggregate) functions. Writes intermediate data to disk.

3. **YARN (Yet Another Resource Negotiator):** Cluster resource manager. Decouples resource management from processing. Components: Resource Manager (master), Node Manager (slave), Application Master (per-app coordinator).

4. **Apache Hive:** Data warehousing tool built on Hadoop. Provides HiveQL (SQL-like language) for querying large datasets. Converts SQL-like queries into MapReduce jobs. Best for OLAP and users who know SQL.

5. **Apache Spark:** In-memory distributed processing engine. Up to 100x faster than MapReduce for iterative workloads. Supports batch, streaming, SQL, ML (MLlib), and graph processing (GraphX) in one unified engine.

---

### Q10. Explain the benefits of cloud platforms for data engineering.

**Answer:**

Cloud platforms provide significant advantages for data engineering:

1. **Scalability and Flexibility:** On-demand access to compute and storage. Auto-scaling handles fluctuating data volumes without manual intervention. Eliminates hardware procurement delays.

2. **Cost Efficiency:** Pay-as-you-go pricing eliminates large upfront capital expenditure. You pay only for resources consumed (storage GB, compute hours). Avoids over-provisioning.

3. **Agility and Speed:** Pre-configured services and automation enable rapid pipeline development. Data engineers can provision clusters, test ideas, and deploy solutions quickly. Serverless architectures reduce operational overhead.

4. **Enhanced Collaboration:** Centralized data lakes and shared workspaces allow data engineers, analysts, and scientists to collaborate. Version control and shared notebooks (e.g., Azure Databricks, AWS SageMaker Studio) improve team productivity.

5. **Improved Security and Compliance:** Cloud providers offer encryption (at rest and in transit), IAM, VPC isolation, and compliance certifications (ISO, SOC2, HIPAA, GDPR). Easier to implement data governance policies.

6. **Streamlined Data Integration:** Managed services (AWS Glue, Azure Data Factory) connect to hundreds of data sources. Simplifies building ETL/ELT pipelines that consolidate data into data warehouses or data lakes.

7. **Access to Advanced Analytics and ML:** Integrated machine learning services (Amazon SageMaker, Azure ML) and analytics tools (Redshift, Synapse) can be directly connected to data pipelines for intelligent insights.

---

# 10. QUICK REVISION CHEAT SHEET

| Topic | Key Point to Remember |
|-------|----------------------|
| **3Vs of Big Data** | Volume (size), Velocity (speed), Variety (types) |
| **Extended Vs** | Veracity, Value, Variability, Visualization |
| **HDFS** | Master-slave; Name Node = metadata, Data Node = actual data; blocks replicated 3x |
| **MapReduce** | Map() = filter/sort/group; Reduce() = aggregate; disk-based, slower |
| **YARN** | Resource manager; RM + NM + AM; enables multi-engine cluster |
| **Spark** | In-memory, 100x faster than MapReduce; unified for batch/streaming/SQL/ML |
| **RDD** | Immutable, distributed, fault-tolerant via lineage; transformations are lazy |
| **DataFrame** | Structured, schema-based, optimized via Catalyst/Tungsten |
| **Transformations** | Lazy: map, filter, reduceByKey, join |
| **Actions** | Eager: count, collect, take, saveAsTextFile |
| **IaaS** | Rent infrastructure (VMs, storage); you manage OS+apps |
| **PaaS** | Rent platform (OS+runtime); you manage apps |
| **SaaS** | Rent software; provider manages everything |
| **Public Cloud** | Shared, third-party (AWS, Azure) |
| **Private Cloud** | Dedicated to one org |
| **Hybrid Cloud** | Public + Private combined |
| **Azure vs AWS** | AWS = market leader, cloud-native; Azure = enterprise, hybrid, Microsoft integration |
| **ADF** | Azure Data Factory — ETL/ELT orchestration, low-code, triggers |
| **Synapse** | Unified analytics — warehousing + big data + Spark |
| **Blob Storage** | Object storage; block/page/append blobs; unstructured data |
| **Databricks** | Managed Spark on Azure; integrates with Azure services |
| **S3** | Object storage; 11 nines durability; data lake foundation |
| **Redshift** | MPP data warehouse; serverless option; AQUA acceleration |
| **Glue** | Serverless ETL; Data Catalog, crawlers, Glue Studio, DataBrew |

**Good luck with your Data Engineering exam!** Focus on memorizing the comparison tables and understanding Hadoop/Spark architecture — these are the highest-yield topics.