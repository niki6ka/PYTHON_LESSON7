
chant = input("Наберите кричалку Винни Пуха (слова через дефис, строки через пробел) : ")
rhyme = chant.split()
vowel = ['а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я']
result = list()

def winnythepooh(chant):
    for item in rhyme:
        vow = 0
        for letter in item:
            if letter in vowel:
                vow += 1
        result.append(vow)
    print("Количество слогов в каждой строке: ", result)

    if len(set(result)) == 1:
        print('Парам пам-пам')
    else:
        print('Пам парам')
i = 0
for item in rhyme:
    print(rhyme[i])
    i = i + 1

winnythepooh(chant)











