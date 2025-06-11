# Escreva um programa que pede ao usuário o nome de um aluno e as notas de 3 provas que este aluno realizou.
# No fim o programa deve mostrar na tela a média das 3 provas
# Dica:
# Para calcular a média das provas você deve dividir a soma das notas das provas pela quantidade de provas realizadas
# media = soma / 3

# OUTPUT ESPERADO:

# | ______________________________ |
# | SISTEMA DE PROVAS
# | ______________________________ |
# | Nome do aluno: Fulano
# | Nota da primeira prova: 9.8
# | Nota da segunda prova: 7
# | Nota da terceira prova: 8.5
# | ______________________________ |
# | Aluno: Fulano 
# | Média: 8.43
# | Aluno aprovado
# | ______________________________ |

# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------

print('|',30*'_','|')
print('| SISTEMA DE PROVAS')
print('|',30*'_','|')

nome = input('| Nome do Aluno: ')
n1 = float(input('| Nota da primeira prova: '))
n2 = float(input('| Nota da segunda prova: '))
n3 = float(input('| Nota da terceira prova: '))
print('|',30*'_','|')

soma = n1+n2+n3
media = soma/3
# media = round(media, 2)
print(f'| Aluno: {nome}')
print(f'| Média: {media:.2f}')
if media >=5:
    print('| Aluno Aprovado')
else:
    print('| Aluno Reprovado')
print('|',30*'_','|')