n = []
while True:
    valor = (int(input('Digite um valor: ')))
    if valor not in n:
        n.append(valor)
        print('Valor adicionado com sucesso!')
    else:
        print('Valor duplicado! Não posso adicionar...')
    r = ' '
    while r not in 'SN':
        r = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if r in 'N':
        break
n.sort()
print(n)