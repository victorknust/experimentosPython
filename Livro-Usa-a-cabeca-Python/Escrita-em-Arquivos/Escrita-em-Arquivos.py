def printFileLines(file):
    count = 0;
    with open(fileName) as file:
        for line in file:
            print('#' + str(count) + ': ' + line, end='\n')
            count += 1

try:
    fileName = 'arquivo.txt'
    printFileLines(fileName)
    print('====================================')

    with open(fileName, 'w') as file:
        print('Jefferson H. Stachelski', file=file)
        tab = 1
        for i in range(10):
            print(str(tab) + ' x 10 = ' + str(i * 10), file=file)
            i += 1
    
except IOError as error:
    print('IOError: ' + str(error))
