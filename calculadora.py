def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b != 0:
        return a / b
    else:
        return "Não pode dividir por zero"


print("=== Calculadora Python ===")

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

print("Soma:", somar(num1, num2))
print("Subtração:", subtrair(num1, num2))
print("Multiplicação:", multiplicar(num1, num2))
print("Divisão:", dividir(num1, num2))
