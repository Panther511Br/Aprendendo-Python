lista = ['a', 'b', 'd']
lista2 = ['A']
print(lista)
print(lista2)

lista.append('e')
# Adiciona 'e' ao fim da lista.
print("lista depois do .append:", lista)

lista.insert(2, 'c')
# Insere 'c' na posição 3, deslocando os demais elementos.
print("lista depois do .insert:", lista)

lista.extend('A')
# Prolonga a lista. Adiciona um elemento de uma lista no fim de outra lista.
print("lista depois do .extend:", lista)

lista.remove('A')
# Remove o primeiro elemento encontrado cujo valor é igual a 'A'.
print("lista depois do .remove:", lista)

lista.pop()
# Remove o último elemento(ou um na posição específica) e o retorna.
print("lista depois do .pop:", lista)

print("Usando .index para dizer o indice de 'c':", lista.index('c'))
# Retorna o ídice do primeiro item cujo valor é igual a 'c'.

print("Usando .count para contar quantas vezes tem 'c':", lista.count('c'))
# Retorna o numero de vezes que 'c' aparece na lista.

lista.reverse()
# Inverte a ordem dos elementos.
print("lista depois do .reverse:", lista)

lista.sort()
# Ordena os itens da lista.
print("lista depois do .sort:", lista)

lista2 = lista.copy()
# Faz uma cópia da lista e a retorna.
print("lista2 depois de copiar a lista1 com .copy:", lista2)

lista.clear()
# Limpa a lista.
print("lista depois do .clear:", lista)