# SmartCity AI - Data Sources

## Project
NYC Mobility Intelligence Platform

## Acquisition period
January 2025 baseline

## 1. Yellow Taxi Trips
Provider: NYC Taxi and Limousine Commission
URL: https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page
Format: Parquet
Purpose: Taxi demand forecasting

## 2. Taxi Zone Lookup
Provider: NYC TLC
URL: https://d37ci6vzurychx.cloudfront.net/misc/taxi_zone_lookup.csv
Format: CSV
Purpose: Geographic dimensions

## 3. DOT Traffic Speeds
Provider: NYC Department of Transportation
URL: https://data.cityofnewyork.us/d/i4gi-tjb9
Format: CSV via API
Purpose: Traffic slowdown analysis
Scope: 5,000-row January 2025 development sample

## 4. Motor Vehicle Collisions
Provider: NYPD via NYC Open Data
URL: https://data.cityofnewyork.us/d/h9gi-nx95
Format: CSV via API
Purpose: Road safety analytics
Scope: January 2025, maximum 50,000 rows

## Important limitations
- Raw files are excluded from GitHub.
- Taxi demand does not directly measure traffic congestion.
- The speed sample is not representative of the full city.
- The project will expand to additional months.
- Dataset validation does not mean data is fully cleaned.
