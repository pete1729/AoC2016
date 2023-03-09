import re

with open('/home/peter/Code/AoC2016/Day07/input', 'r') as reader:
    lines = reader.readlines()

def get_abas(in_str):
    abas = []
    for i in range(len(in_str)-2):
        if in_str[i] == in_str[i+2] and in_str[i] != in_str[i+1]:
            abas.append(in_str[i:i+3])
    return abas

ips_supporting_SSL = 0

for line in lines:
    line = line.strip()
    regular_sequences = []
    hypernet_sequences = []
    in_hypernet_sequence = 0
    next_sequence = ""
    for i in line:
        if i == "[":
            regular_sequences.append(next_sequence)
            next_sequence = ""
            in_hypernet_sequence = 1
        elif i == "]":     
            hypernet_sequences.append(next_sequence)
            in_hypernet_sequence = 0
            next_sequence = ""
        else:
            next_sequence = next_sequence + i
    regular_sequences.append(next_sequence)

    abas = []
    for reg_seq in regular_sequences:
        abas = abas + get_abas(reg_seq)
    print(abas)

    support_SSL = 0
    babs = []
    for aba in abas:
        babs.append(aba[1] + aba[0] + aba[1])
    for hyp_seq in hypernet_sequences:
        for bab in babs:
            if bab in hyp_seq:
                support_SSL = 1
    ips_supporting_SSL += support_SSL
    print("Supports SSL:", support_SSL)

print("IPs supporting SSL:", ips_supporting_SSL)

#print(regular_sequences)
#print(hypernet_sequences)
