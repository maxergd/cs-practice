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

def count_levels(lines):
    counts = {}
    for line in lines:
        if line.strip() == "":
            continue
        try:
            event = parse_event(line)
            level = event["level"]
            counts[level] = counts.get(level, 0) + 1
        except ValueError:
            counts["BROKEN"] = counts.get("BROKEN", 0) + 1
    return counts


def top_errors(lines, n):
    error_counts = {}
    for line in lines:
        if line.strip() == "":
            continue
        try:
            event = parse_event(line)
            if event["level"] == "ERROR":
                msg = event["message"]
                error_counts[msg] = error_counts.get(msg, 0) + 1
        except ValueError:
            pass

    items = []
    for msg in error_counts:
        items.append([msg, error_counts[msg]])

    items.sort(key=lambda x: (-x[1], x[0]))
    return items[:n]
