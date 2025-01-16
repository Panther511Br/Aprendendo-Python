# Criando a classe. É um tipo de dado que agrupa um conjunto de variáveis(atributos) e funções(métodos).
# Atributos são as características de uma classe. Descrevem o estado do objeto.
# Métodos são as ações que um objeto pode realizar.
# Cada tipo diferente de dado pode ser um objeto.
class Cachorro(object):
    atributo1 = 'Mamífero'
    # Atributo de classe.

    def __init__(self, nome):
    # Definindo o método especial __init__.
    # 'self' refere-se a instância(objeto) da classe.
        self.nome = nome
        # Atributo de instância.

caramelo = Cachorro("Amarelo")
# Uma instância da classe 'Cachorro' é criada com o nome "Amarelo" e atribuída à variável 'caramelo'.
print("Meu nome eh:", caramelo.nome)

Rodger = Cachorro("Rodger")
Tommy = Cachorro("Tommy")
# Criando mais instâncias.

print("Rodger eh um {}".format(Rodger.__class__.atributo1))
print("Tommy tambem eh um {}".format(Tommy.__class__.atributo1))
# Acessa o atributo de classe 'atributo1' usando '.__class__.atributo1'

print("Meu nome eh:", Rodger.nome)
print("Meu nome eh:", Tommy.nome)

print("-------------------------------------------------------------------------")

class Cachorro(object):
    def __init__(self, nome):
        self.nome = nome

    def falar(self):
    # Python sempre passa o objeto 'self' como primero argumento de todos os métodos.
        print("Meu nome eh {}".format(self.nome))

Scooby = Cachorro("Scooby")
Coragem = Cachorro("Coragem")
# inicialização de objetos.

Scooby.falar()
Coragem.falar()
# Acessando métodos
# Para acessaratributos ou métodos, usa-se 'objeto.nomeAtributo' ou 'objeto.nomeMétodo'