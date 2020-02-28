# Вывести последнюю букву в слове
word = 'Архангельск'
print(word[len(word) - 1])


# Вывести количество букв "а" в слове
word = 'Архангельск'
print(word.lower().count('а'))


# Вывести количество гласных букв в слове
word = 'Архангельск'
word = word.lower()
sum_vowels = 0
vowels = 'ауоыиэяюёе'
for letter in word:
    if letter in vowels:
        sum_vowels +=1
print(sum_vowels)

# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
print(len(sentence.split(' ')))


# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
words = sentence.split(' ')
for word in words:
    print(word[0])


# Вывести усреднённую длину слова.
sentence = 'Мы приехали в гости'
avr_len = 0
words = sentence.split(' ')
for word in words:
    avr_len += len(word)
avr_len = avr_len / len(words)
print(avr_len)