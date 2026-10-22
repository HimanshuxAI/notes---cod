# DATA ENGINEERING — TERM ASSESSMENT-II EXAM ANSWERS

**Course:** 23CSE3017 – Data Engineering  
**Examination:** Term Assessment–II, OCT-2025  
**Class:** B. Tech. CSE - AIEC, TY, Semester V  
**Max Marks:** 20 | **Time:** 1 hour  
**Pattern:** Attempt Q1 OR Q2 AND Q3 OR Q4 (each part = 5 marks)  

---

# EXAM PATTERN SUMMARY

| Question Pair | Attempt | Marks per part | Total |
|---------------|---------|----------------|-------|
| Q1 OR Q2 | Any one question (both parts a & b) | 5 + 5 | 10 marks |
| Q3 OR Q4 | Any one question (both parts a & b) | 5 + 5 | 10 marks |
| **Grand Total** | | | **20 marks** |

---

# Q1 — SPARK ETL & CLOUD BENEFITS (CO3)

## Q1.a) Spark ETL Pipeline for Online Shopping Website [5 marks]

**Scenario:** An online shopping website wants to analyze customer clicks and purchases. Explain how Spark ETL pipeline can extract, transform, and load this data for reports.

**Answer:**

**Step 1: Extract (Data Ingestion)**
- Customer clickstream data and purchase transactions are ingested from sources like web servers, mobile app logs, and databases.
- Tools: **Apache Kafka** or **Apache Flume** can stream real-time click events into the system.
- Data is landed in raw format into **HDFS** or **Amazon S3 / Azure Blob Storage** as the data lake landing zone.

**Step 2: Transform (Data Processing using Spark)**
- A **Spark ETL job** reads the raw data using **Spark SQL** or **DataFrame API**.
- Transformations applied:
  - **Cleaning:** Remove nulls, duplicates, and malformed records (e.g., incomplete click sessions).
  - **Enrichment:** Join click data with product catalog and customer profile data to add product category, price, and customer segment.
  - **Aggregation:** Group by customer ID, product ID, and time window (hourly/daily) to compute metrics like total clicks, conversion rate, revenue per user, and top-selling products.
  - **Filtering:** Keep only successful purchases (status = "completed") for revenue reports.
- Spark's **in-memory processing** enables fast iterative transformations on large clickstream volumes.

**Step 3: Load (Data Storage for Reports)**
- Transformed data is written to a structured destination:
  - **Aggregated reports** → Loaded into **Azure Synapse Analytics** or **Amazon Redshift** for BI reporting.
  - **Processed datasets** → Stored in **Parquet/ORC format** in Azure Data Lake or Amazon S3 for downstream analytics.
- Reports are generated using **Power BI** or **Amazon QuickSight** connected to the warehouse.

**Diagram (to draw in exam):**
```
Web Logs & Purchase Events
       ↓
Kafka / Flume (Ingestion)
       ↓
Raw Data in Data Lake (S3 / Blob / HDFS)
       ↓
Spark ETL Job (Extract → Transform → Load)
       ↓
Cleaned & Aggregated Data (Parquet format)
       ↓
Data Warehouse (Synapse / Redshift)
       ↓
BI Reports (Power BI / QuickSight)
```

**Key Spark Concepts to Mention:**
- **RDDs / DataFrames** for distributed processing
- **Transformations** (map, filter, join, groupBy) are lazy
- **Actions** (count, save, collect) trigger execution
- **Spark SQL** for structured querying

---

## Q1.b) Two Main Benefits of Using AWS or Azure for Data Engineering [5 marks]

**Scenario:** A startup plans to move its data from local servers to the cloud.

**Answer:**

When a startup migrates data engineering workloads from local on-premises servers to the cloud (AWS or Azure), it gains two major benefits:

### Benefit 1: Scalability and Cost Efficiency (Pay-as-you-go)

- **Elastic Scalability:** Cloud platforms allow the startup to scale compute and storage resources up or down based on data volume. During peak shopping seasons, they can add more Spark worker nodes or Redshift nodes instantly; during low demand, they scale down to save costs.
- **No Upfront Capital Expenditure:** Unlike local servers that require buying hardware upfront, cloud follows a **pay-as-you-go model**. The startup pays only for the storage (GB) and compute (hours) it actually uses.
- **Managed Services:** AWS Glue, Azure Data Factory, Amazon Redshift, and Azure Synapse are fully managed — the cloud provider handles patching, backups, and infrastructure maintenance, reducing the startup's operational burden.

### Benefit 2: Agility, Speed, and Managed Ecosystem

- **Faster Time to Insight:** The startup can provision a data pipeline in minutes using cloud-native tools (e.g., AWS Glue Studio or Azure Data Factory drag-and-drop interface) instead of weeks required to order, install, and configure on-premises hardware.
- **Integrated Ecosystem:** Both AWS and Azure provide end-to-end data services — storage (S3 / Blob), processing (EMR / Databricks), warehousing (Redshift / Synapse), and BI (QuickSight / Power BI) — that work together seamlessly.
- **Global Reach & Reliability:** Data can be replicated across multiple availability zones and regions, ensuring high availability and disaster recovery without building secondary data centers.

**Summary for exam:** Scalability + Cost Efficiency + Agility + Managed Services = The startup can focus on data insights rather than infrastructure management.

---

# Q2 — CLOUD STORAGE & HYBRID BATCH-STREAMING (CO3)

## Q2.a) Azure Blob Storage or AWS S3 for Secure Big Data Storage [5 marks]

**Scenario:** A retail store wants to store daily sales records on the cloud.

**Answer:**

Both **Azure Blob Storage** and **Amazon S3** are object storage services designed to store massive volumes of unstructured and semi-structured data securely.

### How Azure Blob Storage Helps:

1. **Scalable Storage:** Daily sales records (CSV, JSON, Parquet, images of receipts) can be stored as blobs in containers. The store can start small and grow to petabytes without provisioning hardware.
2. **Security:**
   - Data is **encrypted by default** at rest (Storage Service Encryption) and in transit (HTTPS/TLS).
   - **Role-Based Access Control (RBAC)** and **Shared Access Signatures (SAS)** allow fine-grained permissions — e.g., store managers can read, while analysts can only read specific containers.
   - **Private Endpoints** ensure traffic does not traverse the public internet.
3. **Durability:** High durability with redundant copies (Locally Redundant Storage / Zone-Redundant Storage / Geo-Redundant Storage).
4. **Access Tiers:** Hot (frequent access), Cool (infrequent), Archive (rare access) — optimize cost for daily sales vs. historical records.
5. **Access:** Accessible via REST API, Azure CLI, SDKs (.NET, Java, Python), and Azure Storage Explorer.

### How AWS S3 Helps:

1. **Scalable Object Storage:** S3 buckets can store unlimited sales records with automatic scaling.
2. **Security:**
   - **99.999999999% (11 nines) durability** and 99.99% availability.
   - **Server-side encryption (SSE-S3, SSE-KMS, SSE-C)** and **SSL/TLS** in transit.
   - **S3 Block Public Access** and **Bucket Policies / IAM policies** for fine-grained access control.
   - **S3 Object Lock** for write-once-read-many (WORM) compliance — important for sales audit records.
3. **Storage Classes:** S3 Standard (frequent access), S3 Standard-IA (infrequent), S3 Glacier (archival) — cost-optimized for daily vs. historical sales data.
4. **Access:** Via AWS Console, CLI, SDKs (Boto3 for Python), and REST API.

**Recommendation for Exam:** Either service is acceptable. Mention **encryption, access control, scalability, durability, and cost tiers** as the key security and storage benefits.

---

## Q2.b) Hadoop (Batch) + Spark Streaming (Live) for Real-Time Sales Dashboard [5 marks]

**Scenario:** A company needs a dashboard showing sales data in real time.

**Answer:**

To build a real-time sales dashboard, the company uses a **hybrid batch-streaming architecture** combining Hadoop and Spark Streaming:

### Architecture Overview (Draw this in exam):

```
Sales Transactions (POS, Online, Mobile)
       ↓
┌──────────────┬──────────────────────┐
│  BATCH PATH  │    STREAMING PATH    │
│  (Hadoop)    │   (Spark Streaming)  │
│              │                      │
│  • Daily     │  • Live events       │
│    sales     │    (clicks,          │
│    batch     │     purchases)       │
│  → HDFS      │  → Kafka → Spark     │
│  → MapReduce │    Streaming         │
│  → Aggregates│    → Live Dashboard  │
└──────────────┴──────────────────────┘
       ↓              ↓
   Daily Report   Real-time Dashboard
   (T+1)          (Sub-second latency)
```

### How Hadoop Handles Batch Data:

- **Daily sales batch jobs** run overnight using **Hadoop MapReduce** or **Hive**.
- Raw transaction data from all stores is loaded into **HDFS**.
- Batch processing computes daily totals, store-wise performance, product-category sales, and monthly trends.
- Results are loaded into the data warehouse for **T+1 reporting** (next-day reports).
- Suitable for: End-of-day reconciliation, inventory valuation, financial reporting.

### How Spark Streaming Handles Live Data:

- **Sales events** (each purchase, refund, inventory update) are published to **Apache Kafka** in real time.
- **Spark Streaming** (or Structured Streaming) consumes the Kafka stream in micro-batches (e.g., every 1 second).
- Transformations applied:
  - Filter valid transactions
  - Compute running totals (revenue per hour, per store)
  - Detect anomalies (sudden spike in refunds)
- Results are pushed to a **live dashboard** (Power BI, Grafana, or custom web app) with sub-second to minute-level latency.
- Suitable for: Real-time revenue monitoring, flash-sale tracking, fraud detection, inventory alerts.

### How They Work Together:

| Aspect | Hadoop (Batch) | Spark Streaming (Live) |
|--------|---------------|------------------------|
| **Data** | Historical, daily sales | Real-time event stream |
| **Latency** | Hours (T+1) | Seconds to minutes |
| **Use Case** | Daily/weekly reports | Live dashboard, alerts |
| **Storage** | HDFS | Kafka → Memory → Dashboard |
| **Processing** | MapReduce / Hive | Spark Streaming / Structured Streaming |

**Combined Value:** The company gets **accurate daily reconciliation** from Hadoop batch and **immediate operational visibility** from Spark Streaming — enabling both strategic decisions and real-time responses.

---

# Q3 — AMAZON REDSHIFT & S3 (CO4)

## Q3.a) Amazon Redshift for E-commerce Data Warehouse [5 marks]

**Scenario:** An e-commerce company wants to build a data warehouse on AWS for order analytics.

**Answer:**

**Amazon Redshift** is a fully managed, cloud-based data warehouse service designed for fast, cost-effective analysis of large-scale structured data.

**How Amazon Redshift Stores and Analyzes Structured Sales Data:**

1. **Data Ingestion:**
   - Order data (orders, customers, products, payments) is extracted from operational databases (e.g., Amazon RDS) or application logs.
   - Data is loaded into Redshift using **AWS Glue ETL jobs**, **Redshift COPY command** (from Amazon S3), or **AWS Data Pipeline**.
   - Supports **Zero-ETL** integration with Amazon Aurora and other operational stores for near real-time analytics.

2. **Storage:**
   - Data is stored in a **columnar format** — ideal for analytics queries that scan specific columns (e.g., `order_amount`, `order_date`) rather than entire rows.
   - **Petabyte-scale storage** — scales from hundreds of gigabytes to petabytes.
   - Data is automatically replicated across multiple Availability Zones for high availability.

3. **Processing (MPP Architecture):**
   - Redshift uses **Massively Parallel Processing (MPP)** — the query is distributed across multiple compute nodes (leader node + compute nodes).
   - Each node processes a slice of the data in parallel, dramatically speeding up complex analytics queries (e.g., "top 10 products by revenue last quarter").

4. **Analysis:**
   - Users run standard **ANSI SQL** queries via Redshift Query Editor, JDBC/ODBC clients, or BI tools.
   - Example query:
     ```sql
     SELECT product_category, SUM(order_amount) AS total_revenue
     FROM orders
     WHERE order_date >= '2025-01-01'
     GROUP BY product_category
     ORDER BY total_revenue DESC;
     ```

5. **Performance Enhancements:**
   - **AQUA (Advanced Query Accelerator):** Hardware-accelerated caching makes queries up to 10x faster.
   - **Redshift Serverless:** Automatically scales compute based on workload — no server management.

6. **Integration:**
   - Output connects to **Amazon QuickSight**, **Tableau**, or **Power BI** for dashboards.
   - Integrates with **Amazon SageMaker** for machine learning on sales data (e.g., demand forecasting).

**Summary for exam:** Redshift = Columnar storage + MPP + ANSI SQL + AWS ecosystem integration = Fast analytics on structured e-commerce sales data.

---

## Q3.b) Amazon S3 for Media Company (Videos & Images) [5 marks]

**Scenario:** A media company stores thousands of videos and images online.

**Answer:**

**Amazon S3 (Simple Storage Service)** is an object storage service designed for storing and retrieving any amount of unstructured data like videos and images. It ensures scalability, security, and durability as follows:

### 1. Scalability

- **Elastic Storage:** S3 can store virtually unlimited data — from gigabytes to exabytes. The media company can upload thousands of videos and images without provisioning storage.
- **Automatic Scaling:** S3 automatically grows and shrinks as media files are added or removed. No need to pre-allocate capacity.
- **High Throughput:** S3 supports high request rates for uploading and streaming media files (e.g., video-on-demand, image galleries).

### 2. Security

- **Encryption by Default:** All data is encrypted at rest (SSE-S3, SSE-KMS, or SSE-C) and in transit (SSL/TLS).
- **Access Control:**
  - **S3 Block Public Access** prevents accidental public exposure of media files.
  - **Bucket Policies and IAM Policies** grant fine-grained permissions (e.g., only admin can upload, public can view specific videos).
  - **Signed URLs** allow temporary, secure access to private videos/images.
- **Compliance:** Supports WORM (Write Once Read Many) via **S3 Object Lock** for compliance and ransomware protection.

### 3. Durability

- **11 Nines Durability:** Amazon S3 provides **99.999999999% (11 nines) durability** — data is automatically replicated across multiple Availability Zones within a region.
- **High Availability:** 99.99% availability SLA ensures media files are accessible when users request them.
- **Versioning:** S3 Versioning keeps multiple versions of an object, protecting against accidental deletion or overwrites.
- **Cross-Region Replication (CRR):** Media can be replicated to another AWS region for disaster recovery and lower-latency access globally.

**Summary for exam:** S3 provides **unlimited scalability** for media files, **enterprise-grade security** (encryption, IAM, signed URLs), and **extreme durability** (11 nines, multi-AZ replication, versioning) — making it ideal for video/image storage.

---

# Q4 — AWS GLUE & ADF vs AWS GLUE COMPARISON (CO4)

## Q4.a) AWS Glue for ETL Job from Multiple AWS Sources [5 marks]

**Scenario:** A financial firm wants to create an ETL job to clean and combine data from multiple AWS sources.

**Answer:**

**AWS Glue** is a fully managed, serverless data integration service that automates ETL (Extract, Transform, Load) and ELT jobs at scale.

**How AWS Glue Performs ETL/ELT Operations:**

**Step 1: Extract (Data Discovery & Ingestion)**
- **AWS Glue Crawlers** automatically scan multiple AWS data sources (e.g., Amazon S3 buckets, Amazon RDS, Amazon DynamoDB, Amazon Redshift, JDBC-accessible databases).
- Crawlers infer schemas, detect data formats, and populate the **AWS Glue Data Catalog** — a central metadata repository.
- Example: A crawler scans S3 buckets containing transaction logs, customer profiles, and market data from different financial systems.

**Step 2: Transform (Data Cleaning & Combining)**
- **AWS Glue Studio** provides a visual, drag-and-drop interface to design ETL jobs without writing code (or with minimal code).
- Glue can **automatically generate ETL code** in Python or Scala using Apache Spark under the hood.
- Transformations applied:
  - **Clean:** Remove nulls, standardize date formats, handle missing financial values.
  - **Combine (Join):** Join transaction data with customer master data and reference tables using common keys (e.g., `customer_id`, `account_id`).
  - **Enrich:** Add calculated fields (e.g., risk score, transaction fees).
  - **Filter:** Remove fraudulent or invalid records.

**Step 3: Load (Write to Target)**
- Cleaned and combined data is written to a target such as:
  - **Amazon Redshift** (for financial analytics and reporting)
  - **Amazon S3** (as processed Parquet/ORC files for data lake)
  - **Amazon RDS** (for operational reporting)

**Step 4: Schedule & Automate**
- Glue jobs can be triggered on a schedule (e.g., nightly at 2 AM), by events (new data arrives in S3), or on demand.
- Workflows can chain multiple Glue jobs together for complex ETL pipelines.

**Key Advantages for the Financial Firm:**
- **Serverless:** No infrastructure to provision — AWS manages compute (DPUs), scaling, and maintenance.
- **Visual Interface:** Business analysts can design jobs using Glue Studio without deep coding.
- **Automatic Schema Discovery:** Crawlers reduce manual schema management across multiple sources.
- **Cost:** Pay only for DPUs used during job execution — no upfront costs.

---

## Q4.b) Compare Azure ADF and AWS Glue [5 marks]

**Scenario:** A multinational organization wants to compare Azure ADF and AWS Glue before choosing a cloud ETL service.

**Answer:**

| Comparison Factor | Azure Data Factory (ADF) | AWS Glue |
|-------------------|-------------------------|----------|
| **Ease of Setup** | Low-code, drag-and-drop interface in ADF Studio; visual pipeline builder | Glue Studio provides visual job authoring; auto-generates Python/Scala code |
| **Automation** | Schedule triggers, tumbling window triggers, event-based triggers (e.g., new file in Blob); integrates with Azure Logic Apps | Schedules, event triggers (new S3 object), on-demand; workflow chaining |
| **Cost Efficiency** | Pay-as-you-go for pipeline execution and data movement; integrates with Azure hybrid benefits | Pay only for DPUs used during job execution; no upfront cost |
| **Code Generation** | Mapping Data Flows (visual) or custom code | Auto-generates ETL code (Python/Scala) via Apache Spark |
| **Metadata Catalog** | Dataset metadata + Azure Purview for governance | AWS Glue Data Catalog (central metadata repository) |
| **Schema Discovery** | Manual dataset definition or schema inference | Glue Crawlers auto-scan and infer schemas |
| **Best Ecosystem** | Azure/Microsoft-native (Synapse, Power BI, Azure ML) | AWS-native (S3, Redshift, Athena, SageMaker) |
| **Hybrid Support** | Self-hosted Integration Runtime for on-premises connectivity | Limited hybrid; primarily AWS-native |

### Detailed Comparison:

**1. Ease of Setup:**
- **Azure ADF:** Offers a highly visual, low-code ADF Studio where users drag and drop activities (Copy, Data Flow, Lookup, etc.) to build pipelines. Ideal for teams with mixed technical skills.
- **AWS Glue:** Glue Studio provides a similar visual interface, but Glue's strength is automatic code generation — it writes Spark-based ETL code for you based on source/target selection.

**2. Automation:**
- **ADF:** Rich trigger options — Schedule (time-based), Tumbling Window (recurring intervals with dependencies), and Event-based (react to Azure Blob storage events). Deep integration with Azure Logic Apps for complex workflow automation.
- **AWS Glue:** Supports time-based schedules, event-based triggers (new objects in S3), and on-demand runs. Can chain multiple Glue jobs into workflows.

**3. Cost Efficiency:**
- **ADF:** Pay for pipeline orchestration and data movement activities. Cost-effective for hybrid scenarios using Self-hosted Integration Runtime.
- **AWS Glue:** Pay only for Data Processing Units (DPUs) consumed during job runtime. Very cost-efficient for sporadic or variable ETL workloads.

**4. Code & Customization:**
- **ADF:** Mapping Data Flows allow visual transformations; supports custom activities via Azure Functions or Databricks for complex logic.
- **Glue:** Automatically generates Spark code (Python/Scala); advanced users can customize the generated code. Glue DataBrew offers no-code data cleaning.

**Recommendation for Exam:**
- Choose **Azure ADF** if the organization is already in the Microsoft ecosystem (Azure Synapse, Power BI, on-premises SQL Server) or needs strong hybrid connectivity.
- Choose **AWS Glue** if the organization is AWS-native (data in S3, warehouse in Redshift, analytics in Athena/QuickSight) and wants a fully serverless ETL experience.

---

# QUICK 5-MARK ANSWER TEMPLATE (For Exam)

For every 5-mark question in this paper, structure your answer as:

| Component | Marks | What to Write |
|-----------|-------|---------------|
| **Definition / Overview** | 1 mark | 2–3 line definition of the service/concept |
| **Main Body** | 3 marks | Core explanation with bullet points, features, or step-by-step process |
| **Example / Diagram / Conclusion** | 1 mark | Scenario example, simple diagram, or one-line summary |

**For Diagram Questions (Q2.b):**
- Draw a clear labeled diagram (3 marks)
- Explain each component briefly (2 marks)

**For Comparison Questions (Q4.b):**
- Use a comparison table (3 marks)
- Write 2–3 sentences of analysis/conclusion (2 marks)

---

**Good luck with your Data Engineering Term Assessment-II!** Focus on: Spark ETL steps, cloud benefits, S3/Blob security, Redshift vs S3, AWS Glue vs ADF comparison. These are the high-yield topics for this paper.