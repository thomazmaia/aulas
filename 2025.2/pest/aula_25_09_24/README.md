# Exercícios sobre funções

1. **Calculadora Simples:** Crie uma função chamada **`calculadora`** que recebe dois números e o nome de uma operação (por exemplo, "soma", "subtracao", "multiplicacao", "divisao") como argumentos e retorna o resultado da operação. Peça ao usuário para inserir os números e a operação e exiba o resultado.
2. **Mensagem Personalizada:** Crie uma função chamada **`mensagem_personalizada`** que recebe o nome de uma pessoa como argumento e retorna uma mensagem de saudação personalizada, como "Olá, [Nome]! Como você está?". Peça ao usuário para inserir seu nome e exiba a mensagem.
3. **Verificador de Número Par:** Crie uma função chamada **`eh_par`** que recebe um número como argumento e retorna True se o número for par e False se for ímpar. Peça ao usuário para inserir um número e informe se é par ou ímpar.
4. **Calculadora de Fatorial/Binomial:** Crie uma função chamada **`fatorial`** que calcula o fatorial de um número inteiro não negativo. Em seguida, crie outra função chamada **`comb`** que calcula o coeficiente binomial ${n}\choose{p}$ usando a função **`fatorial`**. Peça ao usuário para inserir dois números inteiros n e p e calcule o coeficiente binomial.
OBS: O coeficiente binomial é dado por:
    
    $$ {{n}\choose{p}} = \frac{n!}{p!(n-p)!} $$
    
5. **Conversor de Moedas:** Crie uma função chamada **`conversor_moeda`** que recebe um valor em real brasileiro (BRL) e uma taxa de câmbio como argumentos e retorna o valor equivalente em dólares americanos (USD). Peça ao usuário para inserir o valor em BRL e a taxa de câmbio e exiba o valor correspondente em USD.
6. **Contador de Dígitos:** Crie uma função chamada **`contar_digitos`** que recebe um número inteiro como argumento e retorna a quantidade de dígitos no número. Peça ao usuário para inserir um número e exiba a quantidade de dígitos.
7. **Jogo de Adivinhação:** Crie uma função chamada **`jogo_adivinhacao`** que gera aleatoriamente um número inteiro entre 1 e 100 e permite que o jogador tente adivinhar o número. A função deve dar dicas se o palpite do jogador estiver muito alto ou muito baixo. Conte o número de tentativas e, no final, informe quantas tentativas foram necessárias para acertar o número.
    
    OBS: para gerar um número aleatório entre 0 e N use:
    
    ```python
    from random import randint
    
    numero_aleatorio = randint(0, N)
    ```
    
8. **Gerador de Sequência de Fibonacci:** Crie uma função chamada **`fibonacci`** que gera a sequência de Fibonacci até o enésimo termo especificado pelo usuário. A sequência de Fibonacci começa com 0 e 1, e cada termo subsequente é a soma dos dois termos anteriores. Peça ao usuário para inserir o número de termos que deseja na sequência e exiba a sequência resultante.
9. **Simulador de Jogo de Dados:** Crie uma função chamada **`simulador_jogo_dados`** que simule um jogo de dados (dados de seis faces) entre dois jogadores. Os jogadores lançam os dados e o jogador com a maior soma vence. A função deve aceitar o número de rodadas e determinar o vencedor geral após todas as rodadas.
10. **Simulador de Caminhada Aleatória:** Crie uma função chamada **`caminhada_aleatoria`** que simula uma caminhada aleatória em uma grade bidimensional. O jogador começa no centro da grade (0, 0) e a cada passo, ele move-se aleatoriamente uma unidade para cima, para baixo, para a esquerda ou para a direita. A função deve rastrear a posição do jogador após um número especificado de passos e calcular a distância total percorrida.
    
    OBS: para gerar um número aleatório use a biblioteca `random`