with open('/home/peter/Code/AoC2016/Day02/input', 'r') as reader:
    lines = reader.readlines()

inputs = []
for line in lines:
    if line:
        inputs.append(line.strip())

start_pos = "5"
current_pos = start_pos

bathroom_code = ""

for input in inputs:
    for next_letter in input:
        if next_letter == "U":
            if current_pos == "3":
                current_pos = "1"
            elif current_pos == "6":
                current_pos = "2"
            elif current_pos == "7":
                current_pos = "3"
            elif current_pos == "8":
                current_pos = "4"
            elif current_pos == "A":
                current_pos = "6"
            elif current_pos == "B":
                current_pos = "7"
            elif current_pos == "C":
                current_pos = "8"
            elif current_pos == "D":
                current_pos = "B"
        elif next_letter == "D":
            if current_pos == "1":
                current_pos = "3"
            elif current_pos == "2":
                current_pos = "6"
            elif current_pos == "3":
                current_pos = "7"
            elif current_pos == "4":
                current_pos = "8"
            elif current_pos == "6":
                current_pos = "A"
            elif current_pos == "7":
                current_pos = "B"
            elif current_pos == "8":
                current_pos = "C"
            elif current_pos == "B":
                current_pos = "D"
        elif next_letter == "L":
            if current_pos == "6":
                current_pos = "5"
            elif current_pos == "3":
                current_pos = "2"
            elif current_pos == "7":
                current_pos = "6"
            elif current_pos == "B":
                current_pos = "A"
            elif current_pos == "4":
                current_pos = "3"
            elif current_pos == "8":
                current_pos = "7"
            elif current_pos == "C":
                current_pos = "B"
            elif current_pos == "9":
                current_pos = "8"
        elif next_letter == "R":
            if current_pos == "8":
                current_pos = "9"
            elif current_pos == "3":
                current_pos = "4"
            elif current_pos == "7":
                current_pos = "8"
            elif current_pos == "B":
                current_pos = "C"
            elif current_pos == "2":
                current_pos = "3"
            elif current_pos == "6":
                current_pos = "7"
            elif current_pos == "A":
                current_pos = "B"
            elif current_pos == "5":
                current_pos = "6"
    bathroom_code = bathroom_code + current_pos

print("Bathroom code:", bathroom_code)