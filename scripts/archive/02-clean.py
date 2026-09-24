# Clean the raw sensor readings
# Removes the header and keeps complete rows only.

from pathlib import Path

DATA_FILE = Path("data") / "sensor-readings.csv"


def main():
    lines = DATA_FILE.read_text().strip().split("\n")
    header, rows = lines[0], lines[1:]
    complete = [r for r in rows if len(r.split(",")) == 5]
    print(f"Columns: {header}")
    print(f"Complete rows: {len(complete)} of {len(rows)}")


if __name__ == "__main__":
    main()
