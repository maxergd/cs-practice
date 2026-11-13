def parse_event(line):
    line = line.strip()
    parts = line.split(" ", 2)
    if len(parts) != 3:
        raise ValueError("В строке меньше трёх частей")

    time_str, level, message = parts
    message = message.strip()

    if time_str == "" or message == "":
        raise ValueError("Пустое время или сообщение")

    valid_levels = ["DEBUG", "INFO", "WARNING", "ERROR"]
    if level not in valid_levels:
        raise ValueError("Незнакомый уровень")

    return {"time": time_str, "level": level, "message": message}

