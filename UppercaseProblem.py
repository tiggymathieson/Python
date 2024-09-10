word = input("Etera word")
word = word.lower()
word2 = ""
for letter in word:
    word2 = word2 + chr(ord(letter) - 32)
print(word2)