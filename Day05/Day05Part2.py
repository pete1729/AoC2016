import hashlib

letters_found = 0
i = 0
password = [" "]*8
feasible_outputs = "01234567"

while letters_found < 8:
    #next_door_id = "abc" + str(i)
    next_door_id = "ugkcyxxp" + str(i)
    next_hash = hashlib.md5(next_door_id.encode()).hexdigest()

    if next_hash[0:5] == "00000":
        print("Found!")
        print(next_door_id)
        print(next_hash)

        if next_hash[5] in feasible_outputs:
            if password[int(next_hash[5])] == " ":
                password[int(next_hash[5])] = next_hash[6]
                letters_found += 1
    i += 1

print("Password:", "".join(password))

#print(hashlib.md5(door_id))
#print(hashlib.md5(door_id_3.encode()).hexdigest())