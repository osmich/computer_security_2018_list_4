from find_key import find_key


def find_cryptograms(cryptograms):
    decrypted = []

    for i in range(len(cryptograms)):
        crypts = cryptograms[:]
        decrypt = crypts.pop(i)

        key = find_key(decrypt, crypts)
        decrypted.append(key)

    return decrypted