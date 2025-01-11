# Tupla é uma coleção de dados ordenada e imutável, que permite elementos duplicados.
tupla = ("maçã", "banana", "cereja")

# Acessando elementos da tupla
primeiro_elemento = tupla[0]
print(f"Primeiro elemento: {primeiro_elemento}")

# Verificando o comprimento da tupla
comprimento_tupla = len(tupla)
print(f"Comprimento da tupla: {comprimento_tupla}")

# Iterando sobre uma tupla
for fruta in tupla:
    print(fruta)

# Desempacotando tuplas
(maçã, banana, cereja) = tupla
print(f"Maçã: {maçã}, Banana: {banana}, Cereja: {cereja}")

# Concatenando duas tuplas
tupla2 = ("uva", "manga")
tupla_concatenada = tupla + tupla2
print(f"Tupla concatenada: {tupla_concatenada}")
