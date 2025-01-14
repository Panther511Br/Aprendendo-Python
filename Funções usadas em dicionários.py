dicionario = {'carro': 'corolla',
              'marca': 'toyota',
              'cor': 'preto',
              'ano': 1964}
print(dicionario)

novo_dicionario = dicionario.fromkeys(['marca'], 'toyota')
print("\nnovo dicionario criado com o .fromkeys(k, v): ", novo_dicionario)
# Retorna um dicionario a partir da key 'k' e valor 'v' especificados.

ano = dicionario.get('ano')
print("retornando o valor da key especificada 'ano' com o .get:", ano)
# Retorna o valor do elemento com key 'k' especificada.

items = dicionario.items()
print("\nretornando todas as chave-valor do dicionario com .items:", items)
# Retorna uma lista com todos as tuplas chave-valor do dicionário.

chaves = dicionario.keys()
print("retornando as chaves do dicionário com .keys:", chaves)
# Retorna uma lista com todas as chaves do dicionário.

valores = dicionario.values()
print("\nretornando todos os valores com .values:", valores)
#Retorna uma lista com todos os valores do dicionário.

dicionario.pop('cor')
print("dicionario depois de remover a chave-valor 'cor' com .pop:", dicionario)
# Remove o elemento com a key 'k' especificada.

dicionario.popitem()
print("\ndicionario depois de remover o ultimo par chave-valor com popitem:", dicionario)
# Remove o último par chave-valor inserido no dicionário.

dicionario.setdefault('cor', 'azul')
print("adicionando um novo par chave-valor com .setdefault:", dicionario)
# Adiciona um valor a uma chave em um dicionário, se a chave não existir.

dicionario.update({'cor': 'preto'})
print("\natualizando um par chave-valor com .update:", dicionario)
# Atualiza o dicionário de acordo com um par chave-valor(k e v).

dicionario.clear()
print("dicionario depois do .clear:", dicionario)
# Limpa o dicionário.

dicionario2 = dicionario.copy()
print("dicionario2 depois de copiar o dicionario1 com o .copy:", dicionario2)
# Faz uma cópia do dicionário e o retorna.


