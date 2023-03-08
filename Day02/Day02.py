with open('/home/peter/Code/AoC2016/Day02/input', 'r') as reader:
    lines = reader.readlines()

inputs = []
for line in lines:
    if line:
        inputs.append(line.strip())

start_pos = 5
current_pos = start_pos

bathroom_code = ""

for input in inputs:
    for next_letter in input:
        if next_letter == "U":
            if current_pos >= 4:
                current_pos -= 3
        if next_letter == "D":
            if current_pos <= 6:
                current_pos += 3
        if next_letter == "L":
            if current_pos % 3 != 1:
                current_pos -= 1
        if next_letter == "R":
            if current_pos % 3 != 0:
                current_pos += 1
    bathroom_code = bathroom_code + str(current_pos)

print("Bathroom code:", bathroom_code)