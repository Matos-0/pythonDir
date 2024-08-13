A: list[int] = [1, 0, 5, -2, -5, 7]

soma: int = A[0] + A[1] + A[5]
print(f'A soma dos valores é {soma}')

A[5] = 100

for valor in A:
    print(valor)
