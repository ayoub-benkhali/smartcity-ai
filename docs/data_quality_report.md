# SmartCity AI — Data Quality Report

## Scope

Dataset period: January 2025
Platform: Databricks / PySpark / Delta Lake

## 1. Taxi Trips

| Metric | Result |
|---|---:|
| Bronze records | 3,475,226 |
| Invalid records | 119,215 |
| Exact duplicates removed | 0 |
| Silver records | 3,356,011 |
| Retention rate | 96.57% |
| Records excluded | 3.43% |

Validated cleaning conditions:
- Positive trip duration within configured limits
- Trip distance within configured limits
- January 2025 pickup timestamp
- Valid pickup and drop-off IDs
- Non-null essential values

## 2. Geographic Reference

Taxi zone IDs are unique.

No unmatched pickup or drop-off identifiers
were detected in the geographic join test.

Special non-geographic locations require
separate handling in map visualizations.

## 3. Traffic Speed Quality

Silver traffic_speeds was successfully created.

Validation passed for:
- Essential fields
- Timestamp and speed validity
- Road-link identifiers
- Duplicate measurement groups
- Nonnegative travel times when available

The exact verified Silver row count should
be added from the Databricks quality report.

The initial sample is limited and is not
representative of citywide traffic.

## 4. Road Collisions

| Metric | Result |
|---|---:|
| Original misparsed Bronze rows | 19,290 |
| Correctly reparsed records | 6,482 |
| Silver collision records | 6,482 |
| Mappable collisions | 6,266 |
| Map coverage | 96.67% |
| Unspecified borough | 1,326 |

Collision ID data type: STRING

Important: The initial 19,290 rows resulted
from incorrect CSV parsing and are not a
reliable count of distinct collisions.

## 5. Collision Distribution

| Borough | Collisions | Mappable |
|---|---:|---:|
| Brooklyn | 1,870 | 1,810 |
| Queens | 1,361 | 1,329 |
| Unspecified | 1,326 | 1,266 |
| Manhattan | 879 | 846 |
| Bronx | 814 | 785 |
| Staten Island | 232 | 230 |
| Total | 6,482 | 6,266 |

These are observed counts, not normalized
accident risk rates. No population, exposure
or road-traffic denominator has been applied.

## 6. Engineering Limitations

- Current datasets cover limited periods.
- Traffic-speed sample has limited coverage.
- Some collision borough labels are missing.
- Coordinate plausibility does not guarantee
  accurate geographic placement.
- Cleaning thresholds are project assumptions.
- Incremental pipeline automation is pending.

## 7. Next Improvements

- Detailed rejection-reason logging
- Automated data quality tests
- Dataset completeness monitoring
- Incremental processing
- Additional historical months
- ML evaluation using temporal splits
