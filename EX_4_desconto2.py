# Faça uma atualização no código do exercício anterior, agora o programa deve exibir o nome do produto, o valor do desconto e o valor final do produto.

# OUTPUT ESPERADO:

# Produto: FIAT TORO
# Preço: 200000
# Porcentagem de desconto: 15
# O FIAT TORO com 15.0% de desconto custará R$ 170000.0

# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------

produto = input('Produto: ')
preco = float(input('Preço: '))
porcentagem = float(input('Porcentagem de desconto: '))
desconto = preco * (porcentagem/100)
valor_final = preco - desconto
print(f'O {produto} com {porcentagem}% de desconto custará R$ {valor_final}')