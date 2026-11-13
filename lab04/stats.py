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


