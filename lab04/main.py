import sys
from stats import average_by_city, read_valid, warmest_city


lines = sys.stdin.read().splitlines()

non_empty = 0
for line in lines:
    if line.strip() != "":
        non_empty += 1

records = read_valid(lines)
skipped = non_empty - len(records)

averages = average_by_city(records)
best = warmest_city(records)
best_temp = averages.get(best, 0.0)

print(len(records))
print(skipped)
print(best_temp)