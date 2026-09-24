# Collect readings from the station sensor
# In the real project, this script would query the sensor API.
# Here it only confirms that the data file is in place.

from pathlib import Path

DATA_FILE = Path("data") / "sensor-readings.csv"


def main():
    if DATA_FILE.exists():
        print(f"Found {DATA_FILE}")
    else:
        print(f"Missing {DATA_FILE}: run the collection routine first")


if __name__ == "__main__":
    main()
