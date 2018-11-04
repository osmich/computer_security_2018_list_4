from utils import text_to_bits
import string

def find_key(text, crypts):
    decrypt1 = text.split()
    cryptograms = crypts
    for i in range(len(cryptograms)):
        cryptograms[i] = cryptograms[i].split()

    size = len(decrypt1)
    key = [None] * size
    characters = set(string.ascii_letters + " ")
    characters_list = list(characters)

    for i in range(len(key)):
        c1 = int(decrypt1[i],2)

        for j in range(len(characters_list)):
            char = characters_list[j]
            char1 = ord(char)

            b = False
            for k in range(len(cryptograms)):
                if i >= len(cryptograms[k]):
                    # b = True
                    break

                char2 = c1 ^ int(cryptograms[k][i], 2) ^ char1
                if chr(char2) not in characters:
                    b = True
                    break

            if(b == False):
                key[i] = char
                break

        # c2 = int(crypt2[i],2)
        # # char1 = int(char, 2)
        # char1 = ord(char)
        # m1xm2 = c1 ^ c2
        # char2 = char1 ^ m1xm2
        # # print(str(chr(m1xm2)))  
        # # print(c1, char1,' : ',c2, char2,'..',m1xm2 ,' | ',c1^char1, "  ", c2 ^ char2)
        # # if(c1 ^ char1 == c2 ^ char2):
        # #     # print('if',i)
        # #     key[i] = c1^char1
        # # elif(c1 ^ char2 == c2 ^ char1):
        # #     # print('else',i)            
        # #     key[i] = c1^char2
        # key[i] = m1xm2^char1
        # print(c1^key[i])

    # print('\n',str(chr(ord(" ")^int(decrypt1[12],2))))
    # print(key)
    # for i in range(len(key)):
        # print(str(chr(key[i])))
        # print(key[i])

    return key

