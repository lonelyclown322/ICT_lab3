#335106 % 6 = 0

#Создаем функцию для проверки файла на хайку
def checkIfHaiku (filename):
    vowels = ['а','о','э','е','и','ы','у','ё','ю','я']
    fileToCheck = open(filename,'r', encoding='utf-8-sig')
    wholeTextInOnestring = ''
    #разберем текст и заключим его в одну строку
    for string in fileToCheck:
        wholeTextInOnestring += string.strip().lower()
    #создадим массив строк на основе деления через /
    arrayOfHaikuStrings = wholeTextInOnestring.split('/')
    #Проверяем является ли хайку, для этого сначала проверяем количество строк в массиве ?= 3
    if len(arrayOfHaikuStrings) != 3:
        return('Не хайку. Должно быть 3 строки.')
    else: #иначе проходимся по каждой строке и проверяем количество согласных, если строка подоходит,
        #  то прибавляем к счетчику 1. Если текст является хайку, то счетчик в конце цикла должен быть равен 3
        #  иначе текст не является хайку
        check3strings = 0
        for i in range (len(arrayOfHaikuStrings)):
            countVowels = 0
            for elem in arrayOfHaikuStrings[i]:
                if elem in vowels:
                    countVowels += 1
            if (i == 0 or i == 2) and countVowels == 5:
                check3strings += 1
            if i == 1 and countVowels == 7:
                check3strings += 1
        if check3strings == 3:
            return('Хайку!')
        else:
            return('Не хайку.')

#Запускам пять тестов для проверки написанной функциий
for i in range(1,6):
    currentTest = 'test' + str(i) + '.txt'
    print(checkIfHaiku(currentTest))