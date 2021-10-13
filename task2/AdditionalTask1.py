import re
#335106 % 6 = 0

#Создаем функцию для проверки файла на хайку
def checkIfHaiku (filename):
    fileToCheck = open(filename,'r', encoding='utf-8-sig')
    arrayOfHaikuStrings = fileToCheck.read().split('/')
    pattern = re.compile('а|о|э|е|и|ы|у|ё|ю|я|А|О|Э|Е|И|Ы|У|Ё|Ю|Я')
    #Проверяем является ли хайку, для этого сначала проверяем количество строк в массиве ?= 3
    if len(arrayOfHaikuStrings) != 3:
        return('Не хайку. Должно быть 3 строки.')
    else: #иначе химичим :)
        check3strings = 0
        for i in range(3):
            if (len(re.findall(pattern, arrayOfHaikuStrings[i])) == 5) and (i == 0 or i == 2):
                check3strings += 1
            elif (len(re.findall(pattern, arrayOfHaikuStrings[i])) == 7) and (i == 1):
                check3strings += 1
        if check3strings == 3:
            return ('Хайку!')
        else:
            return ('Не хайку.')


#Запускам пять тестов для проверки написанной функциий
for i in range(1,6):
    currentTest = 'test' + str(i) + '.txt'
    print(checkIfHaiku(currentTest))