# Exercícios pós-greve

## Lista de Exercícios - Revisão de Classes e Objetos

💡 **Objetivo:** Relembrar e aplicar os conceitos de Classes, Objetos, Métodos e Atributos.

**Instruções:** Crie um arquivo Python (.py) para cada exercício e salve-os com nomes descritivos (ex: ex1.py, ex2.py). 

**Lembre-se:**

- Utilize nomes de variáveis descritivos.
- Inclua comentários para explicar o que seu código faz.
- Teste seu código com diferentes entradas para garantir que ele funciona corretamente.


1. Crie uma classe chamada `Cachorro` com os atributos `nome`, `raca` e `idade`. Crie um objeto da classe `Cachorro` chamado **rex** com os seguintes valores para os atributos:
- nome: Rex
- raca: Pastor Alemão
- idade: 3

2. Crie uma classe chamada `Carro` com os atributos `marca`, `modelo` e `ano`. Crie um método chamado `mostrar_dados` que imprime os valores dos atributos do objeto. Crie um objeto da classe `Carro` chamado **fusca** com os seguintes valores para os atributos:
- marca: Volkswagen
- modelo: Fusca
- ano: 1970

Chame o método `mostrar_dados` para o objeto **fusca**.

3. Crie uma classe chamada `Pessoa` com os atributos `nome` e `idade`. Crie um método chamado `fazer_aniversario` que incrementa a idade da pessoa em 1 ano. Crie um objeto da classe `Pessoa` chamado **joao** com os seguintes valores para os atributos:
- nome: João
- idade: 25

Chame o método `fazer_aniversario` duas vezes para o objeto **joao** e imprima a idade atual de joao após cada chamada do método.

4. Crie uma classe chamada `Produto` com os atributos `nome`, `preco` e `quantidade`. Crie métodos getters e setters para cada atributo. Crie um objeto da classe `Produto` chamado **produto1** e atribua os seguintes valores aos atributos:
- nome: Televisão
- preco: 2000
- quantidade: 10

Utilize os métodos getters e setters para modificar o preço do produto para R$1800 e a quantidade para 5. Imprima os valores atualizados dos atributos do objeto **produto1**.

5. Crie uma classe chamada `Retangulo` com os atributos `base` e `altura`. Crie métodos para calcular a área e o perímetro do retângulo. Crie um objeto da classe `Retangulo` com os seguintes valores para os atributos:
- base: 10
- altura: 5

Calcule e imprima a área e o perímetro do retângulo utilizando os métodos criados.

6. Crie uma classe chamada `ContaBancaria` com os atributos `numero_conta`, `saldo` e `titular`. Crie métodos para depositar e sacar valores da conta. Implemente o método sacar para que ele só permita sacar valores que não excedam o saldo da conta. Crie um objeto da classe `ContaBancaria` com os seguintes valores para os atributos:
- numero_conta: 123456
- saldo: 1000
- titular: João da Silva

Realize as seguintes operações e imprima o saldo após cada operação:

1. Depositar R$500.
2. Sacar R$300.
3. Sacar R$800 (o método sacar deve impedir a operação e imprimir uma mensagem de erro).

**Dica:** Utilize o conceito de getters e setters para controlar o acesso e a modificação do atributo saldo da classe ContaBancaria.