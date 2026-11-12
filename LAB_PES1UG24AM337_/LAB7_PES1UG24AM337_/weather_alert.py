import math


def parse_reading(text):
    """Parse 'temperature/humidity' (e.g. '35.5/80'). Returns None if invalid."""
    if not isinstance(text, str):
        return None
    parts = text.strip().split('/')
    if len(parts) != 2:
        return None
    try:
        temp = float(parts[0].strip())
        humidity = int(parts[1].strip())
    except ValueError:
        return None
    if not math.isfinite(temp) or not 0 <= humidity <= 100:
        return None
    return temp, humidity


def wind_category(speed_text):
    """Grade wind speed in km/h. Returns 'invalid' for bad input."""
    if not isinstance(speed_text, str):
        return 'invalid'
    try:
        speed = int(speed_text.strip())
    except ValueError:
        return 'invalid'
    if speed < 0:
        return 'invalid'
    if speed >= 89:
        return 'warning'
    if speed >= 39:
        return 'advisory'
    return 'none'


def rainfall_spread(readings_csv):
    """Max - min of comma-separated rainfall values. Returns None if invalid."""
    if not isinstance(readings_csv, str):
        return None
    readings = []
    for r in readings_csv.split(','):
        r = r.strip()
        if not r:
            continue
        try:
            value = float(r)
        except ValueError:
            return None
        if not math.isfinite(value) or value < 0:
            return None
        readings.append(value)
    if not readings:
        return None
    return max(readings) - min(readings)


def main():
    print("==== Running parse_reading ====")
    user_input = input("Enter temperature/humidity (e.g. 35.5/80): ")
    result = parse_reading(user_input)
    print("Temperature and Humidity:", result if result is not None else "Invalid reading")

    print("\n==== Running wind_category ====")
    user_input = input("Enter a wind speed in km/h (e.g. 45): ")
    result = wind_category(user_input)
    print("Wind Category:", result)

    print("\n==== Running rainfall_spread ====")
    user_input = input("Enter hourly rainfall in mm as CSV (e.g. 2,5.5,10): ")
    result = rainfall_spread(user_input)
    print("Rainfall Spread:", result if result is not None else "Invalid rainfall data")


if __name__ == "__main__":
    main()