def saudacoes(y: int, x: str):
    if y == 1:
        print(f"Bom dia, {x}!")
    elif y == 2:
        print(f"Boa tarde, {x}!")
    else:
        print(f"Boa noite, {x}!")


# sempre boa prática ter o tipo da variável (str, int, float) dentro do scopo


nome = input("Qual seu nome? ")
periodo = int(input("Qual o periodo do dia é agora? 1 - manhã; 2 - tarde e 3 - noite. "))

saudacoes(periodo, nome)
