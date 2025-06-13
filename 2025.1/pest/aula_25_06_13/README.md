# Exercícios - Dicionários
1. Crie um dicionário em Python com as seguintes chaves e valores:
- "nome": "João da Silva"
- "idade": 30
- "cidade": "Maranguape"

2. Crie um dicionário em Python que represente uma lista de compras. As chaves do dicionário devem ser os nomes dos produtos e os valores devem ser as quantidades desses produtos a serem compradas. 
    
    Ex: 
    
    ```python
    {'arroz': 2, 'feijão': 1, 'óleo': 1, 'açúcar': 1, 'sal': 1}
    ```
    
3. Crie um dicionário em Python para ler e armazenar as notas de um aluno em uma disciplina. O dicionário deve ter como chaves os nomes das disciplinas (por exemplo, "matemática", "português", "história") e como valores as notas do aluno nessas disciplinas.
    
    Ex: 
    
    ```python
    {'matemática': 8.5, 'português': 7.2, 'história': 9.0}
    ```
    
4. Crie um dicionário com o nome e a idade de três pessoas diferentes. Em seguida, use um loop para imprimir o nome e a idade de cada pessoa separadamente.
5. Crie um dicionário com o nome e a idade de três pessoas diferentes. Em seguida, calcule a média de idade dessas pessoas.
6. Crie um dicionário com o nome e a pontuação de cinco jogadores diferentes. Em seguida, use um loop para calcular a média das pontuações e imprimir o resultado na tela.
7. Crie um programa que armazene a quantidade de letras em cada palavra de uma lista de palavras. A lista deve conter as palavras "casa", "carro" e "bicicleta". O programa deve imprimir um dicionário contendo cada palavra como chave e a quantidade de letras como valor.
    
    Ex: 
    Entrada: `["casa", "carro", "bicicleta"]`
    Saída: `{'casa': 4, 'carro': 5, 'bicicleta': 9}`
    
8. Suponha que você esteja trabalhando com um sistema de votação e precisa contar a quantidade de votos de cada candidato. Você tem uma lista com os números correspondentes aos candidatos votados. Crie um programa que calcule a quantidade de votos para cada candidato e armazene essa informação em um dicionário. Ao final, imprima o dicionário contendo cada candidato como chave e a quantidade de votos como valor.
    
    Ex: 
    Entrada: `[1, 2, 3, 1, 2, 1, 3, 3, 1, 2]`
    Saída: `{1: 4, 2: 3, 3: 3}`
    
9. Escreva um programa que conte o número de ocorrências de cada palavra em uma frase. O programa deve ler uma frase do usuário, separar as palavras, armazená-las em um dicionário e imprimir o número de ocorrências para cada palavra.
    
    Ex: “Um elefante incomoda muita gente, dois elefantes incomodam, incomodam muito mais!”
    `[chave] - [valor]
    um - 1
    elefante - 1
    incomoda - 1
    muita - 1
    gente - 1
    dois - 1
    elefantes - 1
    incomodam - 2
    muito - 1
    mais -1`
    
10. Escreva um programa que conte o número de ocorrências de cada letra em uma frase. O programa deve ler uma frase do usuário, separar suas letras, armazená-las em um dicionário e imprimir o número de ocorrências para cada letra.
    
    Ex: “Parabens pra voce”
    `[chave] - [valor]
    p - 2
    a - 3
    r - 2
    b - 1
    e - 2
    n - 1
    s - 1
    v - 1
    o - 1
    c - 1`
    
11. Escreva um programa que crie um dicionário de produtos e seus preços. O programa deve permitir ao usuário adicionar novos produtos e preços, atualizar preços existentes e excluir produtos do dicionário. Cada produto deve estar relacionado a uma categoria. Considere as categorias: Bebida, Comida, Limpeza e Frutas.
    
    Ex:
    
    ```python
    produtos = {
        'Coca-Cola': {'categoria': 'Bebida', 'preco': 4.5},
        'Pizza': {'categoria': 'Comida', 'preco': 35},
        'Detergente': {'categoria': 'Limpeza', 'preco': 2},
        'Laranja': {'categoria': 'Frutas', 'preco': 5.2}
    }
    ```
    
12. Escreva um programa que crie um dicionário de nomes de alunos e suas notas em disciplinas. Cada aluno deve estar associado a duas disciplinas (Português e Matemática) e cada disciplina deve ter uma ou mais notas. O programa deve permitir ao usuário adicionar novos alunos e notas, atualizar notas existentes e excluir alunos do dicionário. O programa também deve calcular a média de notas do aluno por disciplina.
    
    Ex:
    
    ```python
    alunos = {
        'Artur': {'Matemática': [8.5, 7.2, 6.9], 'Português': [9.0, 8.5, 9.5]},
        'Julia': {'Matemática': [7.5, 6.0, 8.0], 'Português': [9.0, 9.0, 9.5]},
        'Pedro': {'Matemática': [8.0, 7.5, 9.0], 'Português': [9.0, 8.5, 9.5]}
    }
    ```