from utils import text_to_bits, text_from_bits
import binascii

cryptogram = "00001000 01010101 10101101 11100011 01001111 10001101 10110000 01100010 11111100 01100011 00110111 10000111 00111101 11100100 00011100 00001111 01010100 01001010 01111100 01011000 01110110 00000111 11100101 10000010 01000001 10110110 11010110 00101000 10011000 10000001 10111111 00000000 01101000 01111011 00110100 00110011 11010011 11110100 11001100 11111010 10111111 00000010 00110101 10110110 10010001 11100011 00100000 10010111 01011111 10000101 01111101 11100110 01111000 10110101 01101100 10001100 01000001 00010010 10010110 10111110 00010000 10000100 11101111 01001110"
cryptogram = cryptogram.split()
key = "c211ef71"
key = list(key)

decrypted = []

for i in range(len(cryptogram)):
    j = i % len(key)
    char1 = text_to_bits(key[j])
    char2 = cryptogram[i]
    # print(char1, char2)
    char1 = int(char1, 2)
    char2 = int(char2, 2)
    # print(char1, char2)
    char3 = char1^char2
    # char3 = ''.join(chr(ord(a) ^ ord(b)) for a,b in zip(char1,char2))
    # print(char3)
    # char3 = str(char3).encode('utf-8').decode('utf-8') 
    # decrypted.append(str(chr((char3))))
    decrypted.append(chr(char3))
    # decrypted.append(str(chr(char3).encode('/ISO-8859-2'), 'ISO-8859-2'))

print(decrypted)
