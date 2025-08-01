import random

secret_number = random.randint(1, 60)

print('Jogo do Número Secreto')

for i in range(1, 6):

    tentativas = int(input('Digite o Número Secreto: '))

    if tentativas > secret_number:
        print('Tentativa está acima do Número Secreto.')
    elif tentativas < secret_number:
        print('Tentatica está abaixo do Número Secreto.')
    else:
        break 

if tentativas == secret_number:
    print(f'Parabéns, você acertou o Número Secreto.: {secret_number}.')
else:
    print(f'Game Over. Tentativas expiraram, o Número Secreto era {secret_number}.')               