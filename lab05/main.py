from logstats import count_levels, format_report, top_errors


path = input().strip()

with open(path, encoding="utf-8") as log:
    counts = count_levels(log)

with open(path, encoding="utf-8") as log:
    errors = top_errors(log, 3)

total_valid = 0
for level in counts:
    if level != "BROKEN":
        total_valid += counts[level]

error_count = counts.get("BROKEN", 0)
level_error_count = counts.get("ERROR", 0)

print(total_valid)
print(level_error_count)
print(error_count)

report_text = format_report(counts, errors)
with open("report.txt", "w", encoding="utf-8") as out:
    out.write(report_text)
