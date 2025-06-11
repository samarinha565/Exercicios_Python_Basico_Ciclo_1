# Aluguel de carros:
# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado
# Calcule o preço a pagar, sabendo que o carro custa R$ 60 por dia e R$ 0.15 por km rodado

# OUTPUT ESPERADO:

# Por quantos dias o carro foi alugado: 10
# Quantos km o carro rodou: 500
# Você andou 500.0km por 10 dias, então o preço a pagar é R$675.00.

# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------

print('|',30*'-','|')
print('| ALUGUEL DE CARROS')
print('|',30*'-','|')

dias = int(input('| Quantos dias ficou com o carro? '))
km = float(input('| Quantos km percorridos por um carro alugado? '))
valor_dias = dias*60
valor_km = km*0.15
total_pagar = (valor_dias + valor_km)
print('|',30*'-','|')
print(f'| Você percorreu {km}km por {dias} dias, então o preço a pagar é R${total_pagar} ')
