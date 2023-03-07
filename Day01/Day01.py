with open('/home/peter/Code/AoC2016/Day01/input', 'r') as reader:
    lines = reader.readlines()

position = [0,0]

compass = [[0,1], [1,0], [0,-1], [-1,0]]
facing_index = 0    # start facing North
facing = compass[facing_index]

directions = lines[0].split(",")
for i,direction in enumerate(directions):
    directions[i] = direction.strip()

    if directions[i][0] == "R":
        facing_index += 1
    elif directions[i][0] == "L":
        facing_index -= 1

    facing = compass[facing_index % 4]
    position = [position[0] + facing[0]*int(directions[i][1:]), position[1] + facing[1]*int(directions[i][1:])]

print("Final position:", position)
print("Blocks away:", abs(position[0])+ abs(position[1]))