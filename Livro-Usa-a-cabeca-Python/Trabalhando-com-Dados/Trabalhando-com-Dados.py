def getListAtleta(fileName):
    theList = set()
    try:
        with open(fileName) as file:
            for line in file:
                for data in line.strip().split(','):
                    valor = sanitize(data)
                    theList.add(valor)
                    # if valor not in theList: # se fosse um list, com set nao precisa disso
                        # theList.append(valor)

    except IOError as error:
        print('IOError: ' + str(error))
    except ValueError as error:
        print('ValueError: ' + str(error))
    finally:
        return sorted(theList)

def sanitize(dataStr):
    if '-' in dataStr:
        min, seg = dataStr.split('-')
        dataStr = min + '.' + seg
    elif ':' in dataStr:
        min, seg = dataStr.split(':')
        dataStr = min + '.' + seg

    return float(dataStr)

def melhoresTempos(theList):
    return theList[0:3]

""" INICIO PROGRAMA """

julie = getListAtleta('julie.txt')
james = getListAtleta('james.txt')
mikey = getListAtleta('mikey.txt')
sarah = getListAtleta('sarah.txt')

""" PRINT DOS OBJETOS DOS ATLETAS """
if True:
    print('julie: ' + str(julie))
    print('james: ' + str(james))
    print('mikey: ' + str(mikey))
    print('sarah: ' + str(sarah))

print('\nMelhores Tempos:')
print('julie: ' + str(melhoresTempos(julie)))
print('james: ' + str(melhoresTempos(james)))
print('mikey: ' + str(melhoresTempos(mikey)))
print('sarah: ' + str(melhoresTempos(sarah)))
