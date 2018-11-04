import sys
from utils import text_from_bits
from find_cryptograms import find_cryptograms

cryptograms = None

if len(sys.argv) > 1:
    file_name = sys.argv[1]
    with open(file_name, 'r') as my_file:
        temp = my_file.read()    
    cryptograms = temp.split('\n')
else:
    try:
        n=int(input("How many cryptograms you have?\n"))
    except ValueError:
        print("Not a number")


decrypted = find_cryptograms(cryptograms)

for i in range(len(decrypted)):
    print(i,':\n',decrypted[i])


