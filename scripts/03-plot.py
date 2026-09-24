# Reviewed for the field season report
# Plot the daily temperature readings
# Prints a simple text chart, one bar per reading.

from pathlib import Path

DATA_FILE = Path("data") / "sensor-readings.csv"


def main():
    lines = DATA_FILE.read_text().strip().split("\n")[1:]
    for line in lines[:10]:
        date, time, temp, _, _ = line.split(",")
        bar = "#" * int(float(temp))
        print(f"{date} {time} {bar} {temp}")


if __name__ == "__main__":
    main()
