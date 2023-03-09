from collections import Counter

with open('/home/peter/Code/AoC2016/Day04/input', 'r') as reader:
    lines = reader.readlines()

finished = 0
real_room_sector_id_count = 0

alphabet = "abcdefghijklmnopqrstuvwxyz"
def decrypt(ciphertext, key):
    plaintext = ""
    for letter in ciphertext:
        if letter == "-":
            plaintext = plaintext + " "
        else:
            index = alphabet.find(letter)
            new_index = (index + key) % 26
            plaintext = plaintext + alphabet[new_index]
    return plaintext

for line in lines:
    #print(line.strip())
    finished_with_line = 0
    for pos, next_char in enumerate(line):
        if next_char.isdigit() and finished_with_line == 0:
            name = line[0:pos-1]
            sector_ID = line[pos:pos+3]
            checksum = line[pos+4:pos+9]
        
            finished_with_line = 1
    
    decrypted_name = decrypt(name, int(sector_ID))
    if "north" in decrypted_name:
        print(decrypted_name)
        print(sector_ID)

#print("Plaintext:", decrypt("abc-def", 1))