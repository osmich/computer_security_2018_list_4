import string

# print(4^7)
# print(set(string.ascii_letters + " "))

s1 = "00111010"
s2 = "00101111"
char = "A"
char2 = ord(char)

c1 = int(s1, 2)
c2 = int(s2, 2)

print(chr(char2^c1^c2))

