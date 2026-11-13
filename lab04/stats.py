def parse_record(line):
    parts = line.split(';')
    if len(parts) != 3:
        raise ValueError("Полей не три")

    city, temp, date = parts
    city = city.strip()
    date = date.strip()

    if len(city) == 0 or len(date) == 0:
        raise ValueError('Пустая дата или город')

    try:
        temp = float(temp)
    except ValueError:
        raise ValueError("Температура не число")

    return {"city": city, "temp": temp, "date": date}


def read_valid(lines):
    valid_records = []
    for line in lines:
        if line.strip() == "":
            continue
        try:
            record = parse_record(line)
            valid_records.append(record)
        except ValueError:
            pass
    return valid_records

def average_by_city(records):
    totals = {}
    counts = {}

    for record in records:
        city = record["city"]
        temp = record["temp"]
        totals[city] = totals.get(city, 0) + temp
        counts[city] = counts.get(city, 0) + 1

    averages = {}
    for city in totals:
        averages[city] = round(totals[city] / counts[city], 1)

    return averages


def warmest_city(records):
    averages = average_by_city(records)
    best_city = ""
    best_temp = 0

    for city in sorted(averages):
        if best_city == "" or averages[city] > best_temp:
            best_city = city
            best_temp = averages[city]

    return best_city
