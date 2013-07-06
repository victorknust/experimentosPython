class Atleta(object):
    def __init__(self, nomeArquivo=None):
        self.nome = ''
        self.dataNascimento = None
        self.tempos = self.carregarDadosDeArquivo(nomeArquivo)

    def __len__(self):
        if isinstance(self.tempos, list) or isinstance(self.tempos, set):
            return len(self.tempos)
        else:
            return 0

    def __str__(self):
        return ('Nome: ' + self.nome +
            ' | Data Nascimento: ' + str(self.dataNascimento) +
            ' | Tempos: ' + str(self.tempos))

    def top3(self):
        return self.tempos[0:3]

    def carregarDadosDeArquivo(self, fileName):
        self.tempos = set()
        try:
            with open(fileName) as file:
                for line in file:
                    for data in line.strip().split(','):
                        valor = self.sanitize(data)
                        self.tempos.add(valor)
                        
            self.tempos = sorted(self.tempos)
            return self.tempos

        except IOError as error:
            print('IOError: ' + str(error))
        except ValueError as error:
            print('ValueError: ' + str(error))

    def sanitize(self, dataStr):
        if '-' in dataStr:
            min, seg = dataStr.split('-')
            dataStr = min + '.' + seg
        elif ':' in dataStr:
            min, seg = dataStr.split(':')
            dataStr = min + '.' + seg

        return float(dataStr)

""" FIM CLASSE """
