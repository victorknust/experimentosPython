""" PROGRAMA QUE LIDA COM ARQUIVOS """

def getDataEachLine(line):
    arrData = line.split(',')
    data = {}
    
    if len(arrData) == 3:
        data['nome'] = arrData[0]
        data['idade'] = arrData[1]
        data['sexo'] = arrData[2]

    return data

def printUsuarios(usuarios):
    if isinstance(usuarios, list):
        for usuario in usuarios:
            printUsuarios(usuario)
    else:
        print('Nome: ' + usuarios['nome'], end='\n')
        print('Idade: ' + usuarios['idade'], end='\n')
        print('Sexo: ' + usuarios['sexo'], end=' ==================================================== \n')

file = open('test.txt')

try:
    print(file.readline(), end='============================================= \n\n')

    file.seek(0) #RETROCEDE PARA O INICIO DO ARQUIVO
    usuarios = []
    
    for line in file:
        usuarios.append(getDataEachLine(line))

    printUsuarios(usuarios)
except:
    print('DEU MELECA')
finally:
    file.close()
