def main(text):
    lists = []
    count = 0
    i = 0

    while i < len(text) and count < 100:
        letter = text[i]
        if letter.lower() not in ('m', 'n'):
            lists.append(letter)
            count += 1
        i += 1

    return lists


text = input()
result = main(text)
print(result)

