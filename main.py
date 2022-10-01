f = open("books.csv")
a = []
num, num30 = 0, 0

for e in f.readlines():
    stroka = e.split(";")
    if len(stroka[1]) > 30:
        num30 += 1
    a.append(stroka)
    num += 1
a.pop(0)
print("(1) Количество записей: ", num)
print("(2) Количество записей, у которых в поле 'Название' строка длиннее 30 символов: ", num30)
print("(3)----Поиск книг по автору----", "\n", "Введите автора: ", end=" ")
aut = input()

count = 0
for e in a:
    if int(e[0]) != 166276 and int(
            e[0]) != 8703225:  # В названии книг использованна ; из-за которой сдвигается индексация данных в строке
        if e[3] == aut and float(e[6][6:10]) >= 2018:
            count += 1
            print(count, ") ", e[1], sep="")

print("(4) Генератор библиографических ссылок")
ID = []
for i in range(20):
    print('Введите ID искомой книги(введено ', i, "/20", '): ', sep="", end=" ")
    ID.append(input())
ID.sort()
with open('output.txt', 'w') as vivod:
    count = 1
    for e in a:
        if int(e[0]) != 166276 and int(e[
                                           0]) != 8703225:  # В названии книг использованна ; из-за которой сдвигается индексация данных в строке
            if e[0] in ID:
                stroka_4 = str(count) + ") " + e[3] + " " + e[1] + " - " + str(e[6][6:10])
                vivod.write(stroka_4)
                vivod.write("\n")
                count += 1

# Допзадание

Atags = []  # Alltags
for e in a:
    Ltags = e[-1].split("#")[:-2]  # Localtags
    for tag in Ltags:
        if tag not in Atags:
            Atags.append(tag)
Atags.sort()
Atags.pop(0)
print("(Допзадание)Перечень всех тегов без повторений:")
for i in range(len(Atags)):
    print(i + 1, ")", Atags[i])

print("(Допзадание)Самые популярные 20 книг:")
PopBooks = []
for e in a:
    if int(e[0]) != 166276 and int(
            e[0]) != 8703225:  # В названии книг использованна ; из-за которой сдвигается индексация данных в строке
        book = [int(e[8]), e[0], e[1]]
        PopBooks.append(book)
PopBooks.sort(reverse=True)

schetchik = 0
for e in PopBooks:
    if schetchik < 20:
        print(schetchik + 1, ")", *e[::-1])
    schetchik += 1
