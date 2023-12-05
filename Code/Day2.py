import numpy as np
with open("test.txt", "r") as file:
    content = file.read()

word_to_digit = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}

lines = content.split("\n")
result = []

for line in lines:
    if not line:
        continue

    digits = [int(char) for char in line if char.isdigit()]
    indexDigit = [line.index(char) for char in line if char.isdigit()]

    words = []
    index_word = []

    for word, value in word_to_digit.items():
        index = line.find(word)
        while index != -1:
            words.append(value)
            index_word.append(index)
            index = line.find(word, index + 1)

    if index_word and indexDigit:
        if indexDigit[0] < index_word[0] and indexDigit[-1] < index_word[-1]:
            ab = int(str(digits[0]) + str(words[-1]))
            result.append(ab)
        elif index_word[0] < indexDigit[0] and index_word[-1] < indexDigit[-1]:
            ab = int(str(words[0]) + str(digits[-1]))
            result.append(ab)
        elif indexDigit[0] < index_word[0] and indexDigit[-1] > index_word[-1]:
            ab = int(str(digits[0]) + str(digits[-1]))
            result.append(ab)
        elif indexDigit[0] > index_word[0] and indexDigit[-1] < index_word[-1]:
            ab = int(str(words[0]) + str(words[-1]))
            result.append(ab)
    elif not index_word and indexDigit:
        ab = int(str(digits[0]) + str(digits[-1]))
        result.append(ab)
    elif index_word and not indexDigit:
        ab = int(str(words[-1]) + str(words[1]))
        result.append(ab)
    else:
        result.append(0)
print(result)
result = np.sum(result)
print(result)
 