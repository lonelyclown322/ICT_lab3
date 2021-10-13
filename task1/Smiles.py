import re
#ISU = 335106
# eyes = 1   nose = 2  mouth = 2

#создаем функцию проверки текста на смайлики
def checkForSmiles(filename):
    pattern = re.compile(r';-{O')
    fileToCheck = open(filename)
    fileInString = fileToCheck.read()
    return len(pattern.findall(fileInString))

#Запускам пять тестов для проверки написанной функциий
for i in range(1,6):
    currentTest = 'test' + str(i) + '.txt'
    print(checkForSmiles(currentTest))