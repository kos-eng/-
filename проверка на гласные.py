word = input('Введите слово из маленьких латинских букв:')
vow = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
cons = 0
for letter in word:
    if letter in vow:
        vow[letter] += 1
    elif letter.isalpha():
        cons += 1
print(f'Колличество согласных букв: {cons}')
for vow, count in vow.items():
    if count == 0:
        print(f'{vow}: False')
    else:
        print(f'{vow}: {count}')