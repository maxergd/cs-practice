import sys

def parse_record(value_):
    for lines_ in value_:
        line_ = lines_.split(';')
        if len(line_) != 3:
            raise ValueError("Полей не три")
        
        city, temp, date = line_.split(";")
        
        if len(city) == 0 or len(date) == 0:
            raise ValueError('Пустая дата или город')
        try:
            temp = float(temp) 
        except ValueError:
            raise ValueError("Температура не число")
        
    return city, temp, date


lines = sys.stdin.read().splitlines()


print(parse_record(lines))

# total = {}
# count = {}
# for line in lines:
#     city, temp, date = line.split(";")
#     total[city] = total.get(city, 0) + float(temp)
#     count[city] = count.get(city, 0) + 1


# best = ""
# for city in total:
#     if best == "" or total[city] / count[city] > total[best] / count[best]:
#         best = city
# print(len(lines))
# print(0)
# print(total[best] / count[best])
# print(parse_record(lines))