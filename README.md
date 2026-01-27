# End‑to‑End Data Engineering Pipeline  
Azure SQL DB → ADF → ADLS → Auto Loader → Delta Live Tables (SCD Type‑2)

## Overview
This project implements a complete, production‑grade Lakehouse ingestion and transformation pipeline using Azure and Databricks.  
It ingests data from Azure SQL Database, lands it in ADLS (Bronze), processes it into Silver Delta tables using Auto Loader, and models it into Gold SCD Type‑2 dimensions using Delta Live Tables (DLT).

The pipeline includes:

- Incremental ingestion using a watermark column  
- Parameterized ADF datasets for multi‑table ingestion  
- Backfilling support  
- Schema evolution handling  
- SCD Type‑2 dimensional modeling  

---

## Architecture

```text
Azure SQL DB
     │
     ▼
Azure Data Factory (Incremental Copy)
     │
     ▼
ADLS Gen2 (Bronze - Parquet Files)
     │
     ▼
Databricks Auto Loader (Streaming Ingestion)
     │
     ▼
Silver Layer (Cleaned Delta Tables)
     │
     ▼
Delta Live Tables (DLT)
     │
     ▼
Gold Layer (SCD Type‑2 Dimensions)
```


---

## Components

### Source: Azure SQL Database
Operational data stored in Azure SQL DB.  
Each table includes a **watermark column** (e.g., `updated_at`) used for incremental extraction.

---

### Ingestion: Azure Data Factory (ADF)
ADF extracts data from Azure SQL DB and lands it in ADLS as Parquet files.

**Features**

- **Incremental Load using Watermark**  
- **Parameterized Datasets** for reusability  
- **Backfill Support** for historical loads  
- Data lands in **ADLS Bronze** as Parquet files  

---

### Bronze → Silver: Databricks Auto Loader
Auto Loader incrementally processes new files from ADLS and loads them into Delta tables.

- Handles schema drift  
- Provides exactly‑once ingestion  
- Scales automatically  

---

### Silver → Gold: Delta Live Tables (DLT)
DLT builds business‑ready Gold tables.

**Features**

#### 1. SCD Type‑2 Dimensions
- Tracks historical changes  
- Maintains `__START_AT`, `__END_AT`, `__IS_CURRENT`  

#### 2. Declarative Pipeline
DLT handles:
- Dependency resolution  
- Incremental processing  
- Monitoring & lineage  

