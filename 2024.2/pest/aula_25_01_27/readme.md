# Exercícios sobre Listas   
1. Escreva um programa que peça ao usuário para inserir números inteiros em uma lista até que ele digite '0'. Em seguida, o programa deve imprimir a lista resultante.
```
Exemplo:
    Digite um número (0 para sair): 5
    Digite um número (0 para sair): 10
    Digite um número (0 para sair): -3
    Digite um número (0 para sair): 0
    Lista resultante: [5, 10, -3]
```

2. Dada uma lista de nomes de frutas, crie um programa que peça ao usuário para digitar o nome de uma fruta para remover da lista. Certifique-se de que a fruta exista na lista antes de removê-la e imprima a lista resultante.
```
Exemplo caso a fruta exista:
    Lista de frutas atual: ['maçã', 'banana', 'laranja', 'uva']
    Digite o nome de uma fruta para remover: banana
    Fruta removida. Lista resultante: ['maçã', 'laranja', 'uva']

Exemplo caso a fruta não exista:
    Lista de frutas atual: ['maçã', 'banana', 'laranja', 'uva']
    Digite o nome de uma fruta para remover: melancia
    Fruta não encontrada na lista. Nenhuma alteração feita.
```

3. Crie uma lista de números inteiros e, em seguida, peça ao usuário para inserir um número e uma posição. O programa deve usar o método `insert` para inserir o número na posição especificada e, em seguida, imprimir a lista resultante.
```
Exemplo:
    Lista inicial: [1, 2, 3, 4, 5]
    Digite o número que deseja inserir: 99
    Digite a posição onde deseja inserir: 2
    Lista resultante: [1, 2, 99, 3, 4, 5]
```

4. Dada uma lista de números inteiros, crie um programa que remova todos os números pares da lista usando o método 'remove'. Em seguida, imprima a lista vazia resultante.
```
Exemplo:
    Lista inicial: [1, 2, 3, 4, 5, 6]
    Removendo números pares...
    Lista resultante: [1, 3, 5]
```

5. Crie uma lista de nomes de cidades e peça ao usuário para digitar o nome de uma cidade. O programa deve verificar se a cidade existe na lista usando a operação `in` e informar ao usuário se a cidade existe ou não.
```
Exemplo:
    Lista de cidades: ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte']
    Digite o nome de uma cidade: Salvador
    A cidade Salvador não está na lista.
```

6. Crie um programa que ajude o usuário a gerenciar uma lista de compras. O programa deve permitir que o usuário adicione itens à lista, remova itens existentes, e exiba a lista de compras atual. Certifique-se de usar os métodos de lista apropriados para adicionar, remover e verificar a existência de itens na lista. Crie um menu onde o usuário vai escolher o que fazer.
```
Exemplo:
    Menu:
    1. Adicionar item
    2. Remover item
    3. Exibir lista
    4. Sair

    Escolha uma opção: 1
    Digite o item a adicionar: arroz
    Item adicionado.

    Menu:
    1. Adicionar item
    2. Remover item
    3. Exibir lista
    4. Sair

    Escolha uma opção: 3
    Lista de compras: ['arroz']
```

7. Simule uma fila de espera de atendimento em um consultório médico. Crie uma lista vazia que representará a fila de espera. O programa deve permitir que os pacientes sejam adicionados à fila, removidos quando forem atendidos e exiba a lista de pacientes que ainda estão esperando.
```
Exemplo:
    Fila atual: []
    Digite o nome do paciente para adicionar à fila: João
    Fila atual: ['João']
    Digite o nome do paciente para adicionar à fila: Maria
    Fila atual: ['João', 'Maria']
    Atendendo o paciente: João
    Fila atual: ['Maria']
```

8. Peça ao usuário para inserir uma série de números inteiros em uma lista. Em seguida, ordene a lista em ordem crescente usando o método `insert` para inserir cada número na posição correta. Por fim, imprima a lista ordenada.
```
Exemplo:
    Digite um número (ou 'fim' para terminar): 5
    Digite um número (ou 'fim' para terminar): 3
    Digite um número (ou 'fim' para terminar): 8
    Digite um número (ou 'fim' para terminar): 1
    Digite um número (ou 'fim' para terminar): fim
    Lista ordenada: [1, 3, 5, 8]
```

9. Crie um jogo de adivinhação em que o programa escolhe aleatoriamente um número entre 1 e 100 e o armazena em uma lista. O jogador deve tentar adivinhar o número. O programa deve permitir que o jogador insira palpites, remover o número da lista quando ele acertar e continuar até que o jogador adivinhe corretamente.
```
Exemplo:
    O programa escolheu um número.
    Digite seu palpite: 50
    Número errado! Tente novamente.
    Digite seu palpite: 75
    Número errado! Tente novamente.
    Digite seu palpite: 42
    Parabéns! Você acertou!
```