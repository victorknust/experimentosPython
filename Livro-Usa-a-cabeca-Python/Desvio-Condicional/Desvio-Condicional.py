valor = 0

if valor < 0:
    print('Valor negativo')
elif valor > 0 and valor < 100:
    print('Valor positivo menor que 100')
elif valor > 0:
    print('Valor positivo')
else:
    print('Valor zero')

valor_string = 'string abc'
the_list = [1, 2, 3, 4, 5]

if isinstance(valor, int):
    print('valor é um int')

if isinstance(valor_string, str):
    print('valor_string é uma string')

if isinstance(the_list, list):
    print('the_list é uma list')
