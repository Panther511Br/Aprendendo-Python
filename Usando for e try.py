#Sera repetido dez vezes.
for x in range(10):
    try:
    #Tenta executar os comandos
        a = int(input("Digite um numero: "))
        if(a % 2 == 0):
            print("par")
        else:
            print("impar")
    except ValueError:
        print("digite um numero inteiro.")
    #Em caso de erro, executara esse comando.

print("------------------------------------------------------")

try:
    numero = int(input("Digite um numero entre 1 a 20: "))
    resultado = 1
    
    while(numero < 0 or numero >= 20):
        numero = int(input("Digite um numero entre 1 a 20: "))
    #Se o número estiver fora desse intervalo, o usuário é solicitado a digitar novamente até que um número válido seja fornecido.
    
    if(numero > 1 and numero < 20):
        for i in range(1, numero + 1):
            resultado = resultado * i
        #Multiplicando o 'resultado' pelos numeros de 1 ate 'numero'.
        #Calculando assim, o fatorial.
        print("O fatorial eh:", resultado)

except ValueError:
    x = int(input("Digite um numero inteiro."))
