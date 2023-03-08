with open('/home/peter/Code/AoC2016/Day03/input', 'r') as reader:
    lines = reader.readlines()

lengths = []
for line in lines:
    lengths.append([int(line[2:5].strip()), int(line[7:10].strip()), int(line[12:15].strip())])

possible_triangles = 0
for next_lengths in lengths:
    triangle_possible = 1
    if next_lengths[0] + next_lengths[1] <= next_lengths[2]:
        triangle_possible = 0
    if next_lengths[0] + next_lengths[2] <= next_lengths[1]:
        triangle_possible = 0
    if next_lengths[1] + next_lengths[2] <= next_lengths[0]:
        triangle_possible = 0
    possible_triangles += triangle_possible

print("Possible triangles:", possible_triangles)
