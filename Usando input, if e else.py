#Usando input para armazenar os valores, alem de especificar o tipo.

A = int(input('Digite o primeiro valor: '))
B = int(input('Digite o segundo valor: '))

#Usando "if else" para imprimir cada mensagem. O "elif" eh como se eu usasse o "if else" de novo.
if A > B:
    print('O primeiro valor  e maior')
elif A == B:
    print('Os valores sao iguais')
else:
    print('O segundo valor e maior')