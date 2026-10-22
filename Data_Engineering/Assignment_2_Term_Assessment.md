# DATA ENGINEERING (23CSE3017) — THEORY ASSIGNMENT-2 MODEL ANSWERS

**Institution:** MIT Art Design and Technology University, MIT School of Computing, Pune  
**Department:** Computer Science and Engineering  
**Class:** Third Year B. Tech  
**Academic Year:** 2026-2027 (SEM-I)  
**Subject:** Data Engineering (23CSE3017)  
**Assignment:** Theory Assignment-2  
**Max Marks:** 10  

---

# TABLE OF CONTENTS

1. [Q.1 — MapReduce vs Spark & RDD vs DataFrame](#q1--mapreduce-vs-spark--rdd-vs-dataframe)
   - [Q.1.a — Hadoop MapReduce vs Apache Spark (Video-Streaming, Low-Latency)](#q1a--hadoop-mapreduce-vs-apache-spark-video-streaming-low-latency)
   - [Q.1.b — Spark RDDs vs DataFrames (Telecom CDR Batch Processing)](#q1b--spark-rdds-vs-dataframes-telecom-cdr-batch-processing)
2. [Q.2 — Azure/AWS Cloud Roles & Spark vs Hadoop Real-Time](#q2--azureaws-cloud-roles--spark-vs-hadoop-real-time)
   - [Q.2.a — Azure & AWS for Scalable Distributed Data Engineering (Insurance Firm)](#q2a--azure--aws-for-scalable-distributed-data-engineering-insurance-firm)
   - [Q.2.b — Spark vs Hadoop for Real-Time & Iterative Processing (Stock-Market Analytics)](#q2b--spark-vs-hadoop-for-real-time--iterative-processing-stock-market-analytics)
3. [Q.3 — Spark Transformations/Actions & ADF vs Glue](#q3--spark-transformationsactions--adf-vs-glue)
   - [Q.3.a — Spark Transformations & Actions for Social-Media Pipeline](#q3a--spark-transformations--actions-for-social-media-pipeline)
   - [Q.3.b — Azure Data Factory vs AWS Glue (Retail Chain Cloud ETL)](#q3b--azure-data-factory-vs-aws-glue-retail-chain-cloud-etl)
4. [Q.4 — Azure Blob Storage Archiving & Redshift/Synapse Reporting](#q4--azure-blob-storage-archiving--redshiftsynapse-reporting)
   - [Q.4.a — Azure Blob Storage for Media Metadata Archiving](#q4a--azure-blob-storage-for-media-metadata-archiving)
   - [Q4.b — Amazon Redshift or Azure Synapse for Bank Regulatory Reports](#q4b--amazon-redshift-or-azure-synapse-for-bank-regulatory-reports)
5. [Q.5 — Pipeline Tuning for Power BI & S3-Glue-Redshift ETL Flow](#q5--pipeline-tuning-for-power-bi--s3-glue-redshift-etl-flow)
   - [Q.5.a — ADF / Glue Pipeline Tuning for Slow Power BI Dashboard](#q5a--adf--glue-pipeline-tuning-for-slow-power-bi-dashboard)
   - [Q.5.b — S3 → Glue → Redshift ETL Flow for Social-Media Analytics](#q5b--s3--glue--redshift-etl-flow-for-social-media-analytics)
6. [Quick Revision Cheat Sheet](#quick-revision-cheat-sheet)

---

# Q.1 — MAPREDUCE VS SPARK & RDD VS DATAFRAME

## Q.1.a) Hadoop MapReduce vs Apache Spark for Video-Streaming Workload [Low-Latency Analysis]

**Scenario:** A video-streaming service must process **billions of daily viewing events**. Compare Hadoop MapReduce and Apache Spark and analyze which better meets low-latency needs.

### Comparison Table

| Basis | Hadoop MapReduce | Apache Spark |
|-------|-----------------|--------------|
| **Processing Model** | Disk-based (intermediate data written to disk between map and reduce stages) | In-memory (keeps data in RAM across operations) |
| **Speed** | Slower — high disk I/O overhead | Up to 100x faster for iterative and in-memory workloads |
| **Latency** | High latency (minutes to hours) — suitable for batch | Low latency (seconds) — suitable for near real-time |
| **Execution Model** | Two-stage: Map → Reduce (with shuffle & sort to disk in between) | DAG-based execution engine with in-memory RDDs/DataFrames |
| **Iterative Algorithms** | Poor — re-reads data from disk in every iteration | Excellent — caches data in memory for repeated access |
| **Streaming Support** | Not native (batch only) | Native via Spark Streaming / Structured Streaming (micro-batch) |
| **Ease of Programming** | Verbose Java code; steep learning curve | Rich APIs in Python (PySpark), Java, Scala, R; interactive shell |
| **Fault Tolerance** | Task re-execution on node failure | RDD lineage graph — recompute lost partitions from lineage |
| **Best Use Case** | Massive batch ETL where cost matters more than latency | Real-time analytics, ML, streaming, interactive queries |

### Analysis — Which Better Meets Low-Latency Needs?

**Apache Spark is the clear choice** for a video-streaming service processing billions of daily viewing events with low-latency requirements.

**Reasons:**

1. **In-Memory Computation:** Spark keeps intermediate results in RAM (RDDs/DataFrames) instead of writing them to disk after every stage. This eliminates the disk I/O bottleneck that makes MapReduce slow.

2. **Streaming Capability:** Viewing events arrive continuously. Spark Streaming / Structured Streaming can ingest these events in micro-batches (e.g., every 1 second) and update dashboards in near real time. MapReduce is strictly batch-oriented and cannot process streaming data natively.

3. **DAG Optimization:** Spark builds a Directed Acyclic Graph (DAG) of transformations and optimizes the execution plan before running. MapReduce executes rigid map-then-reduce stages without global optimization.

4. **Iterative Processing:** If the service runs recommendation algorithms (e.g., "users who watched this also watched..."), Spark’s in-memory caching makes repeated iterations over the same dataset extremely fast. MapReduce would reload data from HDFS in every iteration, causing prohibitive latency.

5. **Scalability:** Spark scales across thousands of nodes and integrates with Kafka for event ingestion — essential for billions of daily events.

**When MapReduce Might Still Be Used:** If the workload is strictly massive batch ETL (e.g., monthly log aggregation) where data is too large to fit in cluster memory and cost is prioritized over speed, MapReduce on HDFS remains viable. But for **low-latency video-streaming analytics, Spark is superior.**

---

## Q.1.b) Spark RDDs vs DataFrames for Nightly Call-Detail Records (CDR) Batch Processing

**Scenario:** A telecom operator processes nightly call-detail records. Analyze how Spark’s RDDs and DataFrames differ and when each is appropriate.

### Comparison Table

| Basis | RDD (Resilient Distributed Dataset) | DataFrame |
|-------|-------------------------------------|-----------|
| **Abstraction Level** | Low-level, foundational data structure | High-level abstraction built on top of RDDs |
| **Structure** | Unstructured / distributed collection of objects | Structured / tabular data with named columns and types (like a SQL table) |
| **Schema** | No schema — elements are arbitrary objects | Defined schema specifying column names and data types |
| **API Languages** | Java, Scala, Python, R | Python, Scala, Java, R (via Spark SQL) |
| **Optimization** | No automatic optimization — developer controls everything | Catalyst Optimizer (logical plan optimization) + Tungsten (physical execution) |
| **Performance** | Lower — serialization overhead, no columnar optimization | Higher — columnar storage, code generation, memory efficiency |
| **Immutability** | Immutable | Immutable |
| **Partitioning** | Manual partitioning control | Automatic and manual partitioning |
| **Best For** | Unstructured data, custom low-level transformations, fine-grained control | Structured/semi-structured data, SQL-like analytics, ETL pipelines |

### When Each Is Appropriate for Batch Processing (Nightly CDRs)

**Call-Detail Records (CDRs)** are inherently **structured** records containing fields such as:
- `caller_id`, `callee_id`, `call_duration`, `call_timestamp`, `cell_tower_id`, `call_type`, `roaming_flag`

#### Use **DataFrames** when:
- The CDR data has a well-defined schema (as it does here).
- You need to run SQL queries (`SELECT`, `GROUP BY`, `JOIN`) on the records.
- Performance matters — DataFrames use the Catalyst Optimizer and Tungsten execution, making them significantly faster for aggregations (e.g., total call duration per subscriber, peak-hour analysis).
- You want concise, readable code (e.g., `df.groupBy("caller_id").sum("duration")`).

**Recommendation:** For nightly CDR batch processing, **DataFrames are appropriate** because CDRs are structured, the operations are typical ETL/aggregations, and Spark SQL optimization reduces runtime.

**Use **RDDs** when:**
- The data is unstructured or semi-structured (e.g., raw log lines, binary records) and does not fit a fixed schema.
- You need custom, low-level transformations that are difficult to express in DataFrame API.
- You are working in a legacy codebase already built around RDDs.

**Example Contrast:**

```python
# RDD approach (verbose, manual)
cdr_rdd = sc.textFile("hdfs://cdr/nightly/*.log")
cleaned = cdr_rdd.filter(lambda line: len(line.split(",")) == 7)
pairs = cleaned.map(lambda line: (line.split(",")[0], int(line.split(",")[3])))
total_duration = pairs.reduceByKey(lambda a, b: a + b)
total_duration.saveAsTextFile("hdfs://cdr/output/")

# DataFrame approach (concise, optimized)
from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("CDR_Batch").getOrCreate()
df = spark.read.option("header", "true").csv("hdfs://cdr/nightly/*.csv")
result = df.groupBy("caller_id").agg({"duration": "sum"})
result.write.mode("overwrite").parquet("hdfs://cdr/output/")
```

**Conclusion:** Use **DataFrames** for structured CDR batch jobs (performance, readability, optimization); reserve **RDDs** for unstructured data or when low-level control is required.

---

# Q.2 — AZURE/AWS CLOUD ROLES & SPARK VS HADOOP REAL-TIME

## Q.2.a) Azure and AWS Roles in Supporting Scalable, Distributed Data Engineering (Insurance Firm)

**Scenario:** An insurance firm plans a distributed data platform on the cloud. Analyze the role of Azure and AWS in supporting scalable, distributed data engineering.

### Role of Cloud Platforms in Distributed Data Engineering

Cloud platforms provide the foundational infrastructure and managed services that allow an insurance firm to build a scalable, distributed data platform without procuring and maintaining physical hardware.

| Role | Azure Offerings | AWS Offerings | Purpose in Insurance Data Engineering |
|------|----------------|---------------|---------------------------------------|
| **Object Storage / Data Lake** | Azure Blob Storage, Azure Data Lake Storage Gen2 | Amazon S3, AWS Lake Formation | Store raw policy documents, claims images, telematics data, historical records at petabyte scale |
| **Relational / NoSQL Databases** | Azure SQL Database, Azure Cosmos DB | Amazon RDS, Amazon DynamoDB | Store structured policyholder data, customer profiles, claims metadata |
| **Data Integration / ETL** | Azure Data Factory (ADF) | AWS Glue | Ingest, transform, and orchestrate data from on-premises legacy systems, third-party feeds, and IoT devices |
| **Data Warehousing / Analytics** | Azure Synapse Analytics | Amazon Redshift | Run SQL analytics on aggregated claims, risk models, actuarial reports |
| **Distributed Compute (Spark/Hadoop)** | Azure Databricks, Azure HDInsight | Amazon EMR, Amazon SageMaker | Run distributed Spark jobs for risk scoring, fraud detection, and large-scale actuarial computations |
| **Streaming / Real-Time** | Azure Stream Analytics, Azure Event Hubs | Amazon Kinesis, Amazon MSK | Process real-time events (e.g., telematics from connected cars, claim submissions) |
| **BI & Visualization** | Power BI | Amazon QuickSight | Dashboards for underwriters, claims adjusters, and executives |

### How Azure and AWS Support Scalability

1. **Elastic Scalability:** Both platforms allow the insurance firm to add or remove compute nodes (Spark workers, Redshift nodes) automatically based on workload — e.g., scaling up during month-end claims processing and scaling down afterward.
2. **Pay-As-You-Go Pricing:** No large upfront capital expenditure. The firm pays only for storage (GB) and compute (hours) consumed.
3. **Global Regions & Availability Zones:** Data can be replicated across regions for disaster recovery and low-latency access to regional offices.
4. **Managed Services:** The cloud provider handles patching, backups, scaling, and security patching, freeing the firm’s data engineers to focus on pipelines and analytics.
5. **Security & Compliance:** Encryption at rest/in transit, IAM, VPC/private endpoints, and compliance certifications (HIPAA, GDPR, ISO) are critical for sensitive insurance data.

**Conclusion:** Azure and AWS provide the complete stack — storage, compute, orchestration, warehousing, and security — enabling the insurance firm to build a scalable, distributed, and compliant data engineering platform without managing physical data centers.

---

## Q.2.b) Spark Preferred Over Hadoop for Real-Time & Iterative Processing (Stock-Market Analytics)

**Scenario:** A stock-market analytics team needs sub-second insights. Analyze the reasons Spark is preferred over Hadoop for real-time and iterative processing.

### Reasons Spark Is Preferred Over Hadoop MapReduce

| Reason | Apache Spark | Hadoop MapReduce |
|--------|--------------|------------------|
| **Computation Model** | **In-memory** — keeps intermediate results in RAM | **Disk-based** — writes intermediate data to disk between map and reduce |
| **Latency** | **Sub-second to seconds** — suitable for real-time | **Minutes to hours** — batch-only, high latency |
| **Iterative Processing** | Excellent — caches datasets in memory across iterations (ideal for ML, PageRank, risk models) | Poor — reloads data from HDFS in every iteration, causing prohibitive overhead |
| **Streaming** | Native **Spark Streaming / Structured Streaming** (micro-batch or continuous processing) | Not native — batch only |
| **Execution Engine** | DAG-based optimizer — optimizes the entire computation graph before execution | Rigid two-stage Map → Reduce with shuffle to disk |
| **Fault Tolerance** | RDD/DataFrame lineage — recompute lost partitions without full checkpointing | Task re-execution; relies on disk persistence |

### Detailed Analysis for Stock-Market Analytics

**1. Sub-Second Latency Requirement**
Stock prices change every millisecond. A stock-market analytics team needs to detect arbitrage opportunities, compute moving averages, or trigger alerts within seconds. Spark Streaming ingests tick data from Kafka/Kinesis, processes it in micro-batches (e.g., 1-second windows), and pushes insights to dashboards almost instantly. Hadoop MapReduce cannot meet sub-second needs because it materializes intermediate data to HDFS after every map and reduce stage.

**2. Iterative Processing (Risk Models, Machine Learning)**
Stock-market analytics often involves iterative algorithms:
- Monte Carlo simulations for option pricing
- Iterative regression or time-series forecasting
- Graph-based fraud detection (e.g., detecting pump-and-dump schemes)

Spark keeps the dataset in memory across iterations via RDD/DataFrame caching, so each iteration is fast. MapReduce would read the full dataset from disk in every iteration, making it impractical for real-time stock analytics.

**3. Unified Engine**
Spark combines batch, streaming, SQL, and ML in one engine. The stock team can run batch ETL on historical trades, stream live ticks, run SQL queries on order books, and train ML models — all in Spark. Hadoop would require stitching together MapReduce, Hive, Mahout, and separate streaming tools.

**Conclusion:** For sub-second stock-market insights, **Spark’s in-memory processing, native streaming, and iterative efficiency make it far superior to Hadoop MapReduce**, which is designed for high-latency batch ETL, not real-time analytics.

---

# Q.3 — SPARK TRANSFORMATIONS/ACTIONS & ADF VS GLUE

## Q.3.a) Spark Transformations and Actions for Social-Media Pipeline [Filter, Group, Aggregate]

**Scenario:** A social-media analytics team builds a processing pipeline to filter, group, and aggregate raw event data (likes, shares, comments, posts).

### Spark Transformations (Lazy — build the DAG, not executed immediately)

| Transformation | Purpose in Social-Media Pipeline |
|---------------|----------------------------------|
| **`filter()`** | Keep only relevant events (e.g., `event_type == "share"` or posts from the last 24 hours) |
| **`map()` / `select()`** | Extract needed fields from raw JSON (e.g., `user_id`, `post_id`, `timestamp`, `sentiment_score`) |
| **`flatMap()`** | Expand one event into multiple (e.g., one post → multiple hashtags) |
| **`groupBy()` / `groupByKey()`** | Group events by `user_id`, `hashtag`, or `region` |
| **`reduceByKey()` / `agg()`** | Aggregate metrics: count likes per post, sum shares per region, average sentiment per campaign |
| **`join()`** | Join event data with user-profile reference data |
| **`distinct()`** | Remove duplicate events (e.g., double-clicked likes) |
| **`sortBy()`** | Sort by engagement count for trending-topics list |

### Spark Actions (Eager — trigger execution of the DAG)

| Action | Purpose |
|--------|---------|
| **`count()`** | Return total number of filtered events |
| **`collect()`** | Bring aggregated results to driver for small result sets |
| **`take(n)`** | Preview top-n trending posts |
| **`saveAsTextFile()` / `write.parquet()`** | Persist aggregated results to data lake (S3/Blob/HDFS) |
| **`reduce()`** | Compute global sum (e.g., total platform likes today) |
| **`foreach()`** | Write results to an external dashboard or alerting system |

### Example Pipeline (PySpark)

```python
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, count, avg, sum as sql_sum

spark = SparkSession.builder.appName("SocialMediaAnalytics").getOrCreate()

# 1. Load raw event data (JSON) from data lake
raw = spark.read.json("s3://social-raw/events/")

# 2. Transformation: filter only engagement events
engagement = raw.filter(col("event_type").isin(["like", "share", "comment"]))

# 3. Transformation: extract relevant columns
cleaned = engagement.select("user_id", "post_id", "event_type", "timestamp", "region")

# 4. Transformation: group by region and event type, aggregate counts
aggregated = cleaned.groupBy("region", "event_type").agg(
    count("*").alias("event_count")
)

# 5. Action: trigger execution and save to processed zone
aggregated.write.mode("overwrite").parquet("s3://social-processed/daily_aggregates/")

# 6. Action: show top regions for dashboard preview
aggregated.orderBy(col("event_count").desc()).show(10)
```

**Key Concept for Exam:** Transformations are **lazy** — Spark records them in a lineage graph (DAG) but does not compute until an **action** is called. Actions **trigger execution** and return results to the driver or write to storage. This lazy evaluation enables Spark to optimize the entire pipeline before running it (e.g., combining filters, reordering joins).

---

## Q.3.b) Azure Data Factory vs AWS Glue (Orchestration, Scalability, Ease of Maintenance)

**Scenario:** A retail chain builds cloud ETL workflows. Compare Azure Data Factory and AWS Glue.

### Comparison Table

| Feature | Azure Data Factory (ADF) | AWS Glue |
|---------|-------------------------|----------|
| **Orchestration Model** | Pipelines with Activities (Copy, Data Flow, Lookup, ForEach, If Condition) connected by dependencies | Glue Jobs (ETL scripts) triggered by Triggers or Workflows; job chaining supported |
| **Trigger Types** | Schedule, Tumbling Window, Event-based (e.g., new file in Blob), Manual | Schedule, Event-based (new S3 object), On-demand |
| **Integration Runtime** | Azure IR (cloud), Self-hosted IR (on-premises), Azure SSIS IR | Glue provides serverless compute; VPC endpoints for on-premises |
| **Scalability** | Serverless; auto-scales Data Integration Units (DIUs); handles petabytes | Serverless; scales via Data Processing Units (DPUs); auto-scales based on job size |
| **Ease of Maintenance** | Visual ADF Studio (drag-and-drop); rich monitoring UI; alerts on failure | Glue Studio (visual); auto-generated code; serverless (no cluster management); Data Catalog centralizes metadata |
| **Schema Discovery** | Manual dataset definition or schema inference in Mapping Data Flows | Glue Crawlers automatically scan data sources and infer schemas |
| **Code Support** | Mapping Data Flows (low-code), custom code via Azure Functions/Databricks notebooks | Auto-generates Python/Scala (Spark) code; Glue DataBrew for no-code cleaning |
| **Metadata Governance** | Azure Purview integration | AWS Glue Data Catalog + AWS Lake Formation |
| **Best Ecosystem** | Azure/Microsoft-native (Synapse, Power BI, Azure ML) | AWS-native (S3, Redshift, Athena, SageMaker) |

### Detailed Analysis

**1. Orchestration**
- **Azure ADF:** Excels at complex orchestration. Pipelines can contain branching logic (If Condition), loops (ForEach), and dependencies between activities. Triggers can react to Azure Blob events, making it ideal for event-driven retail pipelines (e.g., process sales data as soon as a new POS file lands in Blob Storage).
- **AWS Glue:** Orchestrates ETL jobs via triggers and workflows. Simpler model — good for linear ETL chains (extract → transform → load), but less granular than ADF for complex dependency graphs.

**2. Scalability**
- **ADF:** Scales by increasing Data Integration Units (DIUs) for copy activities and by leveraging Azure Databricks/Synapse Spark clusters for heavy transformations. Serverless model means no cluster provisioning.
- **Glue:** Scales by adding DPUs (Data Processing Units). Since Glue is serverless, AWS provisions and manages the underlying Spark clusters automatically.

**3. Ease of Maintenance**
- **ADF:** Visual pipeline designer reduces coding; built-in monitoring shows success/failure of each activity; alerts can be configured via Azure Monitor. Self-hosted Integration Runtime simplifies hybrid connectivity to on-premises retail databases.
- **Glue:** Serverless means no cluster to maintain. Glue Crawlers automatically update the Data Catalog when new data lands in S3, reducing manual schema management. Glue DataBrew allows business analysts to clean data visually without writing code.

**Recommendation:**
- Choose **Azure Data Factory** if the retail chain is already in the Microsoft ecosystem (uses Azure Synapse, Power BI, on-premises SQL Server) or needs complex hybrid orchestration.
- Choose **AWS Glue** if the data lake is on Amazon S3, the warehouse is Redshift, and the team wants a fully serverless ETL experience with automatic schema discovery.

---

# Q.4 — AZURE BLOB STORAGE ARCHIVING & REDSHIFT/SYNAPSE REPORTING

## Q.4.a) Azure Blob Storage for Secure, Scalable, Cost-Effective Archiving (Media Company Metadata)

**Scenario:** A media company archives large volumes of raw footage metadata. Analyze how Azure Blob Storage supports secure, scalable, and cost-effective archiving.

### How Azure Blob Storage Meets These Needs

| Requirement | How Azure Blob Storage Addresses It |
|-------------|-------------------------------------|
| **Scalability** | Object storage designed for virtually unlimited scale (exabytes). Automatically scales as metadata volumes grow; no provisioning required. |
| **Security** | Encryption at rest (Storage Service Encryption) and in transit (HTTPS/TLS) by default. Role-Based Access Control (RBAC) and Shared Access Signatures (SAS) provide granular permissions. Private Endpoints keep traffic off the public internet. Integration with Azure Active Directory for identity management. |
| **Cost-Effectiveness** | Multiple access tiers: **Hot** (frequent access), **Cool** (infrequent access, 30+ days), **Archive** (rare access, 180+ days, lowest cost). Raw footage metadata that is rarely accessed can be moved to Archive tier automatically via lifecycle management policies. |
| **Durability & Availability** | Data is replicated across multiple Availability Zones (LRS/ZRS/GRS options). Versioning and soft delete protect against accidental deletion. |
| **Organization** | Blob containers act like folders; one storage account can hold unlimited containers. Metadata (tags) can be applied to blobs for classification (e.g., by project, date, production house). |
| **Access** | Accessible via HTTP/HTREST API, Azure CLI, SDKs (.NET, Java, Python, etc.), and Azure Storage Explorer. Integrates with Azure Media Services and Azure Data Factory for archiving workflows. |

**Archival Workflow Example:**
1. Raw footage metadata (XML/JSON sidecar files, production logs) is ingested into a **Hot** container for immediate access.
2. After 90 days, an Azure Data Factory pipeline or Azure Blob Storage **lifecycle management policy** automatically moves blobs to the **Cool** tier.
3. After 1 year, rarely accessed metadata is moved to the **Archive** tier for long-term retention at minimal cost.
4. If needed for an audit, archived blobs can be rehydrated (rehydration may take hours).

**Conclusion:** Azure Blob Storage provides **infinite scalability, enterprise-grade security, and tiered cost-efficiency** — ideal for archiving large volumes of raw footage metadata.

---

## Q4.b) Amazon Redshift or Azure Synapse Analytics for Bank Regulatory Reports

**Scenario:** A bank produces quarterly regulatory reports over very large datasets. Analyze how Amazon Redshift or Azure Synapse Analytics meets these analytical reporting needs.

### Amazon Redshift — Data Warehousing for Regulatory Reporting

| Feature | Benefit for Regulatory Reporting |
|---------|-----------------------------------|
| **Petabyte-Scale Columnar Storage** | Stores years of transaction data, customer records, and transaction logs efficiently; columnar storage speeds up aggregations (e.g., total exposure by region) |
| **Massively Parallel Processing (MPP)** | Distributes complex regulatory queries across multiple compute nodes; fast response even on billions of rows |
| **Redshift Serverless** | Automatically scales compute for quarterly report spikes; no need to provision and manage clusters |
| **Zero-ETL / Federated Queries** | Can query data directly in Amazon S3 (Redshift Spectrum) or operational databases without loading into Redshift first — useful when regulatory data spans multiple sources |
| **AQUA (Advanced Query Accelerator)** | Hardware-accelerated cache makes complex analytical queries up to 10x faster |
| **Security** | Encryption, IAM roles, VPC isolation, and compliance certifications (critical for financial regulatory data) |
| **BI Integration** | Connects to Amazon QuickSight, Tableau, or Power BI for regulatory dashboards |

**How a Bank Uses Redshift:** Quarterly regulatory reports (e.g., capital adequacy, transaction monitoring, customer due diligence) require aggregating transaction data across branches, reconciling accounts, and producing audit trails. Redshift’s MPP architecture processes these large joins and aggregations quickly, and results can be visualized in QuickSight for regulators.

---

### Azure Synapse Analytics — Unified Analytics for Regulatory Reporting

| Feature | Benefit for Regulatory Reporting |
|---------|-----------------------------------|
| **Unified Platform** | Combines data integration (Synapse Pipelines like ADF), data warehousing (Dedicated SQL Pools), big data analytics (Apache Spark), and data exploration (Serverless SQL Pools) in one experience |
| **Dedicated SQL Pools** | Provisioned MPP compute for predictable, high-performance quarterly reporting workloads |
| **Serverless SQL Pools** | On-demand query over data in Azure Data Lake Storage without provisioning — cost-effective for ad-hoc regulatory queries |
| **Apache Spark Integration** | Run Spark notebooks for complex transformations before loading into SQL pools for reporting |
| **Synapse Studio** | Single workspace for data engineers, analysts, and compliance officers to build and monitor reporting pipelines |
| **Power BI Integration** | Native integration for publishing regulatory dashboards |
| **Security** | Azure AD authentication, RBAC, column-level security, encryption, and compliance certifications |

**How a Bank Uses Synapse:** The bank ingests transaction data via Synapse Pipelines, transforms it with Spark notebooks, stores it in Dedicated SQL Pools, and generates quarterly regulatory reports. Compliance officers can query data directly from the Data Lake using Serverless SQL Pools for ad-hoc investigations.

### Comparison for Regulatory Reporting

| Criterion | Amazon Redshift | Azure Synapse Analytics |
|-----------|----------------|-------------------------|
| **Primary Strength** | Purpose-built data warehouse, MPP, simple SQL analytics | Unified platform (warehouse + big data + integration) |
| **Serverless Option** | Redshift Serverless | Serverless SQL Pools |
| **BI Integration** | Amazon QuickSight | Power BI (deep integration) |
| **Complex Transformations** | Limited in-warehouse; use Glue/EMR first | Built-in Spark notebooks in Synapse Studio |
| **Best Fit** | AWS-native bank, primarily SQL reporting | Azure-native bank, wants unified analytics + Spark |

**Conclusion:** Both **Amazon Redshift** and **Azure Synapse Analytics** are excellent for quarterly regulatory reporting over very large datasets. The choice depends on the bank’s existing cloud ecosystem: **Redshift** for AWS-native environments, **Synapse Analytics** for Azure-native environments wanting a single platform for warehousing, big data, and integration.

---

# Q.5 — PIPELINE TUNING & S3-GLUE-REDSHIFT ETL FLOW

## Q.5.a) Pipeline-Tuning Strategies for Slow Power BI Dashboard (ADF or AWS Glue)

**Scenario:** A logistics dashboard built on Power BI is loading slowly. Analyze pipeline-tuning strategies in Azure Data Factory or AWS Glue to improve performance.

### Azure Data Factory (ADF) Tuning Strategies

| Strategy | Description |
|----------|-------------|
| **Increase Data Integration Units (DIUs)** | Allocate more DIUs to Copy Activities to parallelize data movement from source to destination |
| **Partition Source Data** | Read from partitioned tables/folders (e.g., by date, region) so ADF reads only relevant partitions instead of full scans |
| **Push Down Transformations** | Perform filtering and aggregation in the source database (via SQL query in Source query) rather than in ADF Data Flows |
| **Use Staging** | Use a staging table in Azure Synapse or SQL Database to load raw data quickly, then transform inside the warehouse |
| **Enable Parallel Copy** | For large datasets, enable parallel copy in Copy Activity to read from multiple source files/partitions simultaneously |
| **Optimize File Format** | Store source data in columnar formats (Parquet/ORC) with compression instead of CSV/JSON |
| **Incremental Loads** | Use watermark columns (e.g., `last_modified`) to load only changed data since the last pipeline run, instead of full refreshes |
| **Monitor & Identify Bottlenecks** | Use ADF Monitoring to identify slow activities (e.g., a slow Copy Activity or Data Flow) and optimize only those steps |

### AWS Glue Tuning Strategies

| Strategy | Description |
|----------|-------------|
| **Increase DPUs** | Allocate more Data Processing Units (DPUs) to the Glue ETL job for greater parallelism |
| **Use Partitioning** | Partition data in Amazon S3 (e.g., `s3://bucket/year=2026/month=10/day=22/`) and use partition filters in Glue jobs to read only relevant partitions |
| **Pushdown Predicates** | Apply filters at the source (e.g., in the Glue connection options) to avoid reading unnecessary data into Spark |
| **Optimize File Format & Size** | Convert raw CSV/JSON to Parquet/ORC with appropriate compression (Snappy/Gzip); avoid the “small files problem” by compacting files before loading |
| **Use Graviton2 DPUs** | Choose AWS Graviton2-based DPUs for better price-performance on Spark workloads |
| **Broadcast Joins** | When joining a large fact table with a small dimension table, use broadcast join to avoid shuffling the large table |
| **Glue Job Bookmarks** | Enable job bookmarks to process only new data since the last successful run (incremental ETL) |
| **Monitor with CloudWatch** | Track Glue job duration, DPU utilization, and skew; optimize skewed joins by salting keys |

**General Dashboard Performance Tips (Power BI Side):**
- Use Import mode instead of DirectQuery for large datasets (with scheduled refreshes)
- Create aggregations and materialized views in the warehouse
- Limit columns imported into Power BI (only what the dashboard needs)

---

## Q5.b) S3 → AWS Glue → Amazon Redshift ETL Flow for Social-Media Analytics

**Scenario:** A marketing team must ingest daily social-media data into analytics.

### ETL Flow Architecture

```
Social Media APIs (Twitter, Instagram, Facebook, TikTok)
           │
           ▼
   ┌───────────────┐
   │   Amazon S3   │  (Bronze Layer - Raw Landing Zone)
   │   (Raw JSON   │
   │    /CSV files)│
   └───────┬───────┘
           │ AWS Glue Crawler
           ▼ (discovers schema)
   ┌───────────────┐
   │ Glue Data     │  (Metadata Catalog: tables, partitions, schemas)
   │   Catalog     │
   └───────┬───────┘
           │ AWS Glue ETL Job (PySpark)
           ▼ (clean, transform, enrich)
   ┌───────────────┐
   │   Amazon S3   │  (Silver/Gold Layer - Processed Data)
   │  (Parquet)    │
   └───────┬───────┘
           │ COPY / Glue Job
           ▼
   ┌───────────────┐
   │ Amazon Redshift│  (Analytical Warehouse - Gold Layer)
   │   Tables      │
   └───────┬───────┘
           │ Marketing Queries
           ▼
   ┌───────────────┐
   │ QuickSight /  │  (Campaign dashboards, sentiment trends)
   │   BI Tool     │
   └───────────────┘
```

### Role of Each Service

| Service | Role in the ETL Flow |
|---------|---------------------|
| **Amazon S3** | **Landing zone and data lake.** Raw social-media posts (JSON from APIs) are deposited daily into S3 buckets (raw/bronze layer). After Glue processing, enriched data is stored as Parquet in processed (silver/gold) buckets. S3 provides durable, scalable, low-cost storage and serves as the intermediate layer between ingestion and warehousing. |
| **AWS Glue** | **ETL orchestration and transformation.** Glue Crawlers scan the S3 raw bucket, infer schemas (hashtags, user IDs, timestamps, sentiment scores), and populate the Glue Data Catalog. Glue ETL jobs (PySpark) read raw data, clean it (remove nulls, standardize date formats), transform it (extract hashtags, compute engagement scores, aggregate by region/campaign), and write processed data back to S3 or directly to Redshift. Glue is serverless — no cluster management. |
| **Amazon Redshift** | **Analytical warehouse.** Processed social-media data is loaded into Redshift tables (e.g., `daily_engagement`, `campaign_performance`, `user_sentiment`). The marketing team runs fast SQL queries to analyze trends, compare campaigns, and measure ROI. Redshift’s MPP architecture handles billions of social-media rows efficiently. Results feed Power BI/QuickSight dashboards for the marketing team. |

### Example Glue ETL Steps (PySpark Pseudocode)

```python
# 1. Read raw social-media data from S3
raw_df = spark.read.json("s3://social-media-raw/daily/")

# 2. Clean and transform
cleaned = raw_df.filter(col("post_id").isNotNull()) \
    .withColumn("engagement_score", col("likes") + col("shares") * 2 + col("comments") * 3) \
    .withColumn("event_date", to_date(col("timestamp")))

# 3. Aggregate by campaign and region
aggregated = cleaned.groupBy("campaign_id", "region", "event_date") \
    .agg(sql_sum("engagement_score").alias("total_engagement"),
         count("*").alias("post_count"))

# 4. Write to processed S3 (Parquet) and load into Redshift
aggregated.write.mode("overwrite").parquet("s3://social-media-processed/daily/")
# Then COPY into Redshift or use Glue JDBC connector
```

**Conclusion:** This S3 → Glue → Redshift pipeline provides a **scalable, serverless, and cost-effective** way to ingest daily social-media data and make it available for fast marketing analytics.

---

# QUICK REVISION CHEAT SHEET

| Topic | Key Exam Point |
|-------|----------------|
| **Spark vs Hadoop MapReduce** | Spark = in-memory, 100x faster, low-latency, streaming, iterative; Hadoop = disk-based, batch, high latency |
| **Spark Streaming** | Micro-batch processing; suitable for real-time video/tick data |
| **RDD vs DataFrame** | RDD = unstructured, low-level, no schema; DataFrame = structured, schema, Catalyst optimizer, faster |
| **Transformations** | Lazy (map, filter, groupBy, reduceByKey); build DAG |
| **Actions** | Eager (count, collect, save, reduce); trigger execution |
| **Azure Data Factory** | Linked Services, Datasets, Pipelines, Activities, Triggers (schedule/event/tumbling); low-code orchestration |
| **AWS Glue** | Serverless ETL; Glue Studio; Crawlers (schema discovery); Data Catalog; DPUs; DataBrew |
| **Azure Blob Storage** | Object storage; Hot/Cool/Archive tiers; encryption, RBAC, SAS; cost-effective archiving |
| **Amazon S3** | Object storage; 11 nines durability; storage classes; data lake landing zone |
| **Amazon Redshift** | MPP data warehouse; columnar; serverless; AQUA; ANSI SQL; BI integration |
| **Azure Synapse** | Unified platform; Dedicated + Serverless SQL pools; Spark integration; Synapse Studio; Power BI |
| **ADF vs Glue** | ADF = rich orchestration, hybrid IR, visual pipelines; Glue = serverless, auto schema via crawlers, AWS-native |
| **Pipeline Tuning** | Increase DIUs/DPUs, partitioning, pushdown predicates, Parquet format, incremental loads, avoid small files |
| **S3 → Glue → Redshift** | S3 = raw/processed storage; Glue = crawlers + ETL jobs; Redshift = analytical warehouse for BI |

---

**Good luck with your Data Engineering Theory Assignment-2!** Focus on understanding the **trade-offs** (Spark vs Hadoop, ADF vs Glue, Redshift vs Synapse, Blob vs S3) — these analytical comparisons score high marks at L4/CO3-CO4 levels.