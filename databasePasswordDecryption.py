import requests

rawResponse = requests.get("https://pastebin.com/raw/fSvkbar7").text
passData = rawResponse.replace('\r', "").split('\n')

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
           "w", "x", "y", "z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29,
           30, 31, 32, 33, 34, 35]


def convert(x):
    if x in letters:
        return numbers[letters.index(x)]
    return letters[numbers.index(x)]


def increment_key_index(key, index):
    if index < len(key) - 1:
        return index + 1
    return 0


def encrypt(plaintext, key):
    plaintext = plaintext.replace(" ", "")
    plaintext = plaintext.lower()
    result = ""
    key_index = 0
    for char in plaintext:
        num = (convert(char) + convert(key[key_index])) % 36
        result += convert(num)
        key_index = increment_key_index(key, key_index)
    return result


def decrypt(ciphertext, key):
    ciphertext = ciphertext.replace(" ", "")
    ciphertext = ciphertext.lower()
    result = ""
    key_index = 0
    for char in ciphertext:
        num = (convert(char) - convert(key[key_index])) % 36
        result += convert(num)
        key_index = increment_key_index(key, key_index)
    return result


def getDBPassword():
    return decrypt(passData[0], passData[1])
