# É uma coleção de dados não ordenados, mutáveis e indexáveis, que não permite membros repetidos.
# Composto de um conjunto de chaves(keys) e valores(values). Uma chave e está relacionada a um valor específico.
estoque = {"tomate": [1000, 2.3],
           "alface": [500, 0.45],
           "batata": [2001, 1.20],
           "feijao": [100, 1.50]}
print(estoque["batata"])

print("----------------------------------------------------------")

carros = {"marca": "Ford",
          "modelo": "mustang",
          "ano": 1964}
m = carros["marca"]
print(m)

a = carros.get("modelo")
print(a)

c = carros["ano"]
print(c)
carros["ano"] = 1984
print(carros)