import hashlib

letters_found = 0
i = 0
letters = ""

while letters_found < 8:
    next_door_id = "ugkcyxxp" + str(i)
    next_hash = hashlib.md5(next_door_id.encode()).hexdigest()

    if next_hash[0:5] == "00000":
        print("Found!")
        print(next_door_id)
        letters_found += 1
        letters = letters + next_hash[5]
    i += 1

print("Password:", letters)

#print(hashlib.md5(door_id))
#print(hashlib.md5(door_id_3.encode()).hexdigest())