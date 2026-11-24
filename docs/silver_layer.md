# SmartCity AI — Silver Data Engineering

## 1. Project Overview

SmartCity AI is an end-to-end BI and AI platform
for analyzing urban mobility in New York City.

The Silver layer transforms raw NYC transport
datasets into validated Delta Lake tables.

## 2. Technology Stack

- Databricks Free Edition
- Apache Spark / PySpark
- Delta Lake
- Unity Catalog
- Python
- Git and GitHub

## 3. Medallion Architecture

NYC Open Data / TLC
        |
        v
Unity Catalog Volumes
        |
        v
BRONZE — Raw Delta Tables
        |
        v
SILVER — Cleaned Delta Tables
        |
        v
GOLD — Dimensional Analytics (planned)
        |
        v
Microsoft Fabric + Power BI (planned)

## 4. Unity Catalog Configuration

Catalog: workspace

Bronze schema: smartcity_bronze

Silver schema: smartcity_silver

## 5. Silver Tables

### taxi_trips

3,475,226 raw records processed.

3,356,011 cleaned records retained.

Transformations:
- Timestamp validation
- January 2025 date filtering
- Trip duration calculation
- Distance validation
- Pickup/drop-off ID validation
- Exact duplicate removal
- Pickup hour and weekday enrichment

Retention rate: 96.57%.

### taxi_zones

Geographic reference table.

Transformations:
- Location ID type conversion
- Borough and zone normalization
- Duplicate checking
- Unique key validation
- Special zone identification

Validated relationship with taxi pickup
and drop-off identifiers.

### traffic_speeds

NYC DOT traffic observation dataset.

Transformations:
- Timestamp parsing
- Numeric speed conversion
- Road-link ID standardization
- Invalid speed filtering
- Duplicate measurement removal
- Hourly traffic feature generation

Important: Initial traffic observations are
a limited chronological development sample.

They must not be presented as representative
of NYC-wide traffic conditions.

### road_collisions

6,482 cleaned collision records.

Transformations:
- Correct multiline CSV parsing
- String collision ID preservation
- Collision date validation
- Injury and fatality type conversion
- GPS coordinate plausibility checks
- Mappable-record classification
- Borough normalization
- Collision hour extraction

6,266 collisions have plausible map coordinates.

## 6. Collision CSV Recovery

During the first Bronze ingestion, the collision
CSV was incorrectly interpreted.

Initial Bronze row count: 19,290.

Reparsing the original CSV with multiline
support produced 6,482 records.

Collision identifiers were hexadecimal strings,
not numeric IDs. Numeric conversion returned
null and rejected every collision.

Resolution:
- Re-read the source CSV with multiline support
- Preserve collision IDs as strings
- Store a separate reparsed Bronze table
- Build Silver from correctly parsed records
- Preserve the original Bronze table

## 7. Data Quality Strategy

Validation includes:
- Required columns and data types
- Valid dates and timestamps
- Numeric range checks
- Unique identifiers
- Duplicate detection
- Geographic reference validation
- Delta storage verification
- Post-write record-count verification

## 8. Reproducibility

Notebook: notebooks/02_silver_cleaning.ipynb

The current notebook contains initial table-creation
steps with existing-table protection.

It is not yet an automated incremental ETL pipeline.

A future iteration will add repeatable ingestion,
quality reporting, orchestration and refresh logic.

## 9. Next Phase

- Microsoft Fabric Lakehouse integration
- Curated analytical datasets
- Dimensional Data Warehouse
- AI demand forecasting
- Power BI command center
