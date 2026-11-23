from pathlib import Path
import requests

ROOT = Path(__file__).resolve().parents[2]
RAW = ROOT / "data" / "raw"
RAW.mkdir(parents=True, exist_ok=True)

def download(name, url, params=None):
    path = RAW / name

    if path.exists() and path.stat().st_size > 0:
        print(f"[SKIP] {name} already exists")
        return

    temp = RAW / (name + ".part")
    print(f"[DOWNLOAD] {name}", flush=True)

    try:
        with requests.get(
            url,
            params=params,
            stream=True,
            timeout=(20, 120)
        ) as response:
            response.raise_for_status()

            with temp.open("wb") as file:
                for chunk in response.iter_content(
                    chunk_size=1024 * 1024
                ):
                    if chunk:
                        file.write(chunk)

        if temp.stat().st_size < 100:
            raise ValueError("Downloaded file is too small")

        temp.replace(path)
        print(f"[OK] {name}: {path.stat().st_size:,} bytes")

    except Exception:
        temp.unlink(missing_ok=True)
        raise


download(
    "yellow_tripdata_2025-01.parquet",
    "https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2025-01.parquet"
)

download(
    "taxi_zone_lookup.csv",
    "https://d37ci6vzurychx.cloudfront.net/misc/taxi_zone_lookup.csv"
)

download(
    "dot_traffic_speeds_2025-01_sample.csv",
    "https://data.cityofnewyork.us/resource/i4gi-tjb9.csv",
    {
        "$where": "data_as_of >= '2025-01-01T00:00:00' AND data_as_of < '2025-02-01T00:00:00'",
        "$order": "data_as_of ASC",
        "$limit": 5000
    }
)

download(
    "nyc_crashes_2025-01.csv",
    "https://data.cityofnewyork.us/resource/h9gi-nx95.csv",
    {
        "$where": "crash_date >= '2025-01-01T00:00:00' AND crash_date < '2025-02-01T00:00:00'",
        "$order": "crash_date ASC",
        "$limit": 50000
    }
)

print("\nSMARTCITY AI - DOWNLOADS COMPLETED")
