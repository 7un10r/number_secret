# number_secret
1) Importaçã do módulo random
O módulo random permite gerar números aleatórios.
Será usado para definir o número secreto.

2) Sorteio do número secreto
random.randint(1, 60) gera um número inteiro aleatório entre 1 e 60 (inclusive).
Esse valor é armazenado em secret_number, que será o número que o jogador deve
adivinhar.

3) Estrutura de repetição
O for cria um loop que será executado 5 vezes (de 1 a 5).
Cada execução representa uma tentativa do jogador.

4) Entrada do jogador
input() exibe a mensagem e aguarda o jogador digitar um número.
int() converte a entrada (string) em número inteiro.
O valor digitado é armazenado em tentativas.

5) Verifiação das tentativas
Se o número digitado for maior que o número secreto → mensagem de que está acima.
Se for menor → mensagem de que está abaixo.
Se for igual → break interrompe o laço for imediatamente (acertou o número).

6) Verificação final
Se a última tentativa (tentativas) for igual ao número secreto → imprime mensagem
de vitória.
Caso contrário → imprime mensagem de Game Over e revela o número secreto.

