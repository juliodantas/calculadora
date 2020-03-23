print("********** Python Calculator **********\n")

print("Selecione uma das seguintes opções\n")

print("1 - Soma")
print("2 - Subtração")
print("3 - Divisão")
print("4 - Multiplicação")

opcao = int(input("Digite sua opção (1,2,3,4): "))

#x = int(input("Digite o primeiro número: "))
#y = int(input("Digite o segundo número: "))

def somar():
    x = int(input("Digite o primeiro número: "))
    y = int(input("Digite o segundo número: "))
    print("O resultado é:",x + y)

def subtrair(x,y):
    return x - y

def multplicar(x,y):
    return x * y

def dividir(x,y):
    return x / y

if opcao == 1:
    #x = int(input("Digite o primeiro número: "))
    #y = int(input("Digite o segundo número: "))
    somar()
    #z = x + y
    #print("O resultado é:",z)

elif opcao == 2:
    x = int(input("Digite o primeiro número: "))
    y = int(input("Digite o segundo número: "))
    z = x - y
    print("O resultado é:",z)

elif opcao == 3:
    x = int(input("Digite o primeiro número: "))
    y = int(input("Digite o segundo número: "))
    z = x / y
    print("O resultado é:",z)

elif opcao == 4:
    x = int(input("Digite o primeiro número: "))
    y = int(input("Digite o segundo número: "))
    z = x * y
    print("O resultado é:",int(z))

else:
    print("Essa opção não existe")
