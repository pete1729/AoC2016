import re

with open('/home/peter/Code/AoC2016/Day07/input', 'r') as reader:
    lines = reader.readlines()

def test_if_abba(in_str):
    abba_str = 0
    for i in range(len(in_str)-3):
        if in_str[i] == in_str[i+3] and in_str[i+1] == in_str[i+2] and in_str[i] != in_str[i+1]:
            abba_str = 1
    return abba_str

ip_supporting_tls = 0

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

    supports_tls = 0
    for reg_seq in regular_sequences:
        if test_if_abba(reg_seq) == 1:
            supports_tls = 1
    for hyp_seq in hypernet_sequences:
        if test_if_abba(hyp_seq) == 1:
            supports_tls = 0

    ip_supporting_tls += supports_tls
#print(regular_sequences)
#print(hypernet_sequences)

print("IPs supporting TLS:", ip_supporting_tls)