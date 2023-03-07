with open('/home/peter/Code/AoC2016/Day01/input', 'r') as reader:
    lines = reader.readlines()

position = [0,0]
positions_visited = []
visited_position_twice = 0

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
    distance_to_travel = int(directions[i][1:])
    for i in range(distance_to_travel):
        position = [position[0] + facing[0], position[1] + facing[1]]
        if position in positions_visited:
            if visited_position_twice == 0:
                print("First position visited twice:", position)
                print("Blocks away:", abs(position[0])+ abs(position[1]))
                visited_position_twice = 1
        else:
            positions_visited.append(position)

print("Final position:", position)
print("Blocks away:", abs(position[0])+ abs(position[1]))