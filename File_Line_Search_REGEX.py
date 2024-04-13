import re

total = 0

with open("regex_sum_1996190.txt") as file:
    for line in file:
        numbers = re.findall(r'\d+', line)

        for number in numbers:
            total += int(number)
            
print(total)
            