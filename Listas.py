# Lista é uma coleção de dados ordenada e mutável.
# Pode ter zero ou mais elementos do mesmo tipo e tipos diferentes
a = ['b', 'c', 'd']
print(a)

a.append('e')
print(a)

a.insert(0, 'a' )
print(a)

print("---------------------------------------------------")

A = []
for x in range(10):
    y = input("Digite:")
    A.append(y)

print(A)

print("---------------------------------------------------")

a = [3, 4, 1]
b = a
b[0] = 9

print("B: %s" % b)
print("A: %s" % a)