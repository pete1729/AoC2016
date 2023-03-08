from collections import Counter

with open('/home/peter/Code/AoC2016/Day04/input', 'r') as reader:
    lines = reader.readlines()

finished = 0
real_room_sector_id_count = 0

for line in lines:
    print(line.strip())
    finished_with_line = 0
    for pos, next_char in enumerate(line):
        if next_char.isdigit() and finished_with_line == 0:
            name = line[0:pos-1]
            sector_ID = line[pos:pos+3]
            checksum = line[pos+4:pos+9]
        
            finished_with_line = 1
        
            name = name.replace("-", "")
            sorted_name = "".join(sorted(name))

            print(name)
            print(sorted_name)
            print(sector_ID)
            print(checksum)

            counts = Counter(sorted_name)
            sorted_counts = counts.most_common()
            print(counts)
            print("Sorted counts:", sorted_counts)
            
            real_room = 1
            for i in range(5):  
                if sorted_counts[i][0] != checksum[i]:
                    real_room = 0
            print("Real room:", real_room)
            real_room_sector_id_count += real_room*int(sector_ID)
    print()

print("Real room sector ID count:", real_room_sector_id_count)