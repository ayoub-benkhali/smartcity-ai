from pathlib import Path
import csv
import pyarrow.parquet as pq

ROOT = Path(__file__).resolve().parents[2]
RAW = ROOT / "data" / "raw"

taxi = RAW / "yellow_tripdata_2025-01.parquet"

assert taxi.exists(), "Taxi Parquet file missing"

parquet = pq.ParquetFile(taxi)
columns = set(parquet.schema_arrow.names)

required = {
    "tpep_pickup_datetime",
    "tpep_dropoff_datetime",
    "PULocationID",
    "DOLocationID",
    "trip_distance"
}

assert required.issubset(columns), (
    f"Missing taxi columns: {required - columns}"
)

assert parquet.metadata.num_rows > 0

print("TAXI DATA: OK")
print("Rows:", parquet.metadata.num_rows)
print("Columns:", len(columns))

datasets = {
    "taxi_zone_lookup.csv": [
        "LocationID", "Borough", "Zone"
    ],
    "dot_traffic_speeds_2025-01_sample.csv": [
        "data_as_of", "speed", "link_id"
    ],
    "nyc_crashes_2025-01.csv": [
        "crash_date", "collision_id"
    ]
}

for filename, required_cols in datasets.items():
    path = RAW / filename
    assert path.exists(), f"Missing: {filename}"

    with path.open(
        encoding="utf-8-sig", newline=""
    ) as file:
        reader = csv.DictReader(file)
        headers = set(reader.fieldnames or [])

        assert set(required_cols).issubset(headers), (
            f"Missing columns in {filename}: "
            f"{set(required_cols) - headers}"
        )

        count = sum(1 for row in reader)

    assert count > 0, f"Empty dataset: {filename}"

    if filename == "nyc_crashes_2025-01.csv":
        assert count < 50000, (
            "Collision download hit the API row cap; "
            "pagination is required."
        )

    print(f"{filename}: OK - {count:,} rows")

print("\nSMARTCITY AI - ALL DATA CHECKS PASSED")
