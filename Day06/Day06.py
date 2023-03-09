from collections import Counter

with open('/home/peter/Code/AoC2016/Day06/input', 'r') as reader:
    lines = reader.readlines()

print(lines[0])
columns = [""]*len(lines[0].strip())
print(columns[3])

for line in lines:
    line = line.strip()
    for i in range(len(line)):
        columns[i] = columns[i] + line[i]

print(columns)

corrected_message = ""

for i in range(len(columns)):
    counts = Counter(columns[i])
    corrected_message += counts.most_common()[0][0]

print("Corrected message:", corrected_message)