# Trabalho Computacional 1

**Instruções:**
1. O trabalho deve ser feito em dupla e em sala de aula
2. Cada questão deve ser feita em um arquivo próprio .py com o nome `q1.py`, `q2.py`, `q3.py`, `q4.py`.
3. Os quatro arquivos .py devem ser enviados por e-mail (thomaz.maia@ifce.edu.br) até o fim da aula.
4. No e-mail coloque o nome a dupla e da disciplina.

**OBS: Faça as proteções necessárias para as funções!**

******Questão 1 - 2 pontos******

Escreva uma função chamada **`adicionar_elemento`** que aceite três parâmetros: uma lista **`lst`**, um índice **`indice`** e um elemento **`elemento`**. A função deve inserir o **`elemento`** na lista **`lst`** no índice especificado. Lembre-se de que o índice pode ser maior que o tamanho atual da lista.

Exemplo de uso:

```python
minha_lista = [1, 2, 3, 4]
adicionar_elemento(minha_lista, 2, 10)
print(minha_lista)  # Deve imprimir: [1, 2, 10, 3, 4]
```

**Questão 2 - 2 pontos**

Escreva uma função chamada **`remover_elemento`** que aceite uma lista **`lst`** e um elemento **`elemento`**. A função deve remover a primeira ocorrência de **`elemento`** da lista, se existir. Se o elemento não estiver na lista, a função não deve fazer nada.

Exemplo de uso:

```python
minha_lista = [1, 2, 3, 4, 3]
remover_elemento(minha_lista, 3)
print(minha_lista)  # Deve imprimir: [1, 2, 4, 3]
```

**Questão 3 - 2 pontos**

Crie uma função chamada **`media_lista`** que aceita uma lista de números **`numeros`** como parâmetro e retorna a média dos números na lista.

Exemplo de uso:

```python
lista_de_numeros = [1, 2, 3, 4, 5]
media = media_lista(lista_de_numeros)
print(media)  # Deve imprimir: 3.0
```

**Questão 4 - 3 pontos**

Escreva um programa que use as funções **`adicionar_elemento`** e **`remover_elemento`** para transformar a lista **`frutas`** na lista **`frutas_desejadas`** de acordo com as seguintes etapas:

- Inicialmente, **`frutas`** contém **`['maçã', 'banana', 'uva', 'laranja']`**.
- Adicione **`'morango'`** no final da lista.
- Remova **`'uva'`** da lista.
- Adicione **`'abacaxi'`** na posição 1 (índice 1) da lista.

Lembre-se de imprimir **`frutas_desejadas`** no final do seu programa.

**Organização do código, nomenclatura de funções e variáveis: 1 ponto**