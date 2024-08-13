lista: list[int] = []

while len(lista) < 6:
    valor: int = int(input(f'Informe o valor {len(lista) + 1}/6: '))
    lista.append(valor)


for valor in lista:
    print(valor)
