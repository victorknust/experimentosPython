""" COMENTÁRIO DA FUNCAO print_lol
    Livro Use a Cabeça Python """

def print_lol(the_list):
    for each_item in the_list:
        if isinstance(each_item, list):
            print_lol(each_item)
        else:
            print(each_item)

""" EXECUÇÃO DA FUNCAO ACIMA """
the_list = [
    'Item 1',
    123,
    ['Item 1.1', 12.3]]

print_lol(the_list)
