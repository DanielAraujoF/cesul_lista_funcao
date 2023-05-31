def somar(x: int, y: int):
    resultado = x + y
    return resultado


# usando o return, a função vai nos dar o resultado sem mostrá-lo

num1 = int(input("Insira um número: "))
num2 = int(input("Insira um outro número: "))

res = somar(num1, num2)

print(f"A soma dos números é {res}")
