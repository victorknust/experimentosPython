from Atleta import Atleta

""" INICIO PROGRAMA """

julie = Atleta('julie.txt')
james = Atleta('james.txt')
mikey = Atleta('mikey.txt')
sarah = Atleta('sarah.txt')

julie.nome = 'Julie'
james.nome = 'James'
mikey.nome = 'Mikey'
sarah.nome = 'Sarah'

""" PRINT DOS OBJETOS DOS ATLETAS """
if True:
    print('julie: ' + str(julie))
    print('james: ' + str(james))
    print('mikey: ' + str(mikey))
    print('sarah: ' + str(sarah))

print('\nMelhores Tempos:')
print('julie: ' + str(julie.top3()))
print('james: ' + str(james.top3()))
print('mikey: ' + str(mikey.top3()))
print('sarah: ' + str(sarah.top3()))
