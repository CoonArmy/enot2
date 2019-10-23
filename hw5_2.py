import sys
fname = sys.argv[0]
# Переменные для подсчета строк, слов .
lines = 0
words = 0

#обращаемся к файлу на чтение
for line in open("hw3.txt", "r"):
    lines += 1
    words += len(line.split())

# Вывод количеств строк, слов.
print("Строк общее:", lines)
print("Слов общее:", words)