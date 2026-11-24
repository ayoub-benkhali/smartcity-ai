# SmartCity AI - Bronze Data Lake

## Objective

Build the raw data foundation for an intelligent
urban mobility analytics platform.

## Technologies

- Databricks Free Edition
- Apache Spark / PySpark
- Delta Lake
- Unity Catalog
- Python

## Data Architecture

Raw CSV / Parquet files
|
v
Unity Catalog Volume
|
v
PySpark DataFrames
|
v
Bronze Delta Tables

## Unity Catalog

Catalog: workspace
Schema: smartcity_bronze
Volume: smartcity_raw

## Bronze Tables

| Table           |      Rows | Columns | Format |
| --------------- | --------: | ------: | ------ |
| taxi_trips      | 3,475,226 |      22 | delta  |
| taxi_zones      |       265 |       6 | delta  |
| traffic_speeds  |     5,000 |      15 | delta  |
| road_collisions |    19,290 |      31 | delta  |

## Validation

- All four tables exist.
- Every table contains records.
- Every table uses Delta format.
- Original uploaded files are preserved.

## Engineering Decisions

Original source columns are preserved in Bronze.
Data cleaning and deduplication will occur in Silver.

The data model will later support transportation
analytics, AI forecasting and Power BI reporting.

## Limitations

The first traffic-speed sample contains only
5,000 selected observations and is not representative
of all NYC traffic.

## Next Phase

Silver layer:

- Data cleaning
- Timestamp standardization
- Duplicate detection
- Data quality checks
- Enriched analytical datasets
