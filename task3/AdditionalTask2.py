#335106 % 4 = 2
import re

#описываем функцию для замены найденного числа
def replaceFunction(stringNumber):
    x = int(stringNumber)
    return str(3 * x**2 + 5)

#создаем функцию шифровки
def encryptMessage(filename):
    fileToCheck = open(filename,'r', encoding='utf-8-sig')
    fileToStrings = []
    pattern = re.compile('[0-9]+')#создаем паттерн поиска числа
    #заполняем массив fileToStrings строками из файла
    for string in fileToCheck:
        fileToStrings.append(string.rstrip())
    #проходимся по массиву строк из файла и с помощью регулярного выражения находим все числа и заменяем их при помощи функции
    for i in range(len(fileToStrings)):
        numbersInString = re.findall(pattern, fileToStrings[i])
        for number in numbersInString:
            fileToStrings[i] = fileToStrings[i].replace(number, replaceFunction(number))
    #выводим строки на экран
    for string in fileToStrings:
        print(string)
        
#Запускам пять тестов для проверки написанной функциий
for i in range(1,6):
    print('-----New Test-----')
    currentTest = 'test' + str(i) + '.txt'
    encryptMessage(currentTest)
    