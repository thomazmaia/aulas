# Lista - Módulos e pacotes

1. Crie um arquivo chamado ```Ponto.py``` com a classe ```Ponto``` criada anteriormente.

2. Crie um outro arquivo chamado ```Triangulo.py``` contendo a classe ```Triangulo```. Essa classe será composta por 3 objetos da classe ```Ponto``` e terá os métodos:

    - ```calc_lado(A, B)```: calcula o tamanho de uma aresta definida entre os pontos A e B.
    - ```verifica()```: verifica se o objeto triângulo é, de fato um triângulo e, caso seja, verifique se é escaleno, isósceles ou equilátero.    
    - ```calc_area()```: calcula a área do objeto triângulo.
	
		**Dica**: Procure por "fórmula de Heron de Alexandria"

3. Crie um terceiro arquivo chamado ```Retangulo.py``` contendo a classe ```Retangulo```. Essa classe será comporta por 4 objetos da classe ```Ponto``` e terá os métodos:
	- ```calc_perimetro()```: calcula o perímetro do retângulo.
    - ```calc_area()```: calcula a área do objeto retângulo.		

4. Crie uma classe ```Conta``` contendo agência, número, limite (R$ 1000) e um histórico (extrato) de todas as operações realizadas. Além de criar a conta, o cliente pode verificar saldo, extrato, realizar saques, depósitos, transferências e encerrá-la. Pense em tudo que pode acontecer. 

	Exemplo:
	- Cliente sacar mais do que tem na conta
	- Cliente depositar valores negativos
	- Cliente transferir mais do que seu próprio saldo
	- Cliente poder modificar seu saldo
	- etc...

5. Teste a classe ```Conta``` em um arquivo principal realizando as operações implementadas. Veja se sua abstração foi suficientemente boa. O que pode melhorar?

**NOTA**: a lista deve ser feita em dupla e deve ser anviado pelo SUAP. Envie um único arquivo .py para cada classe implementada com seus códigos de teste da classe.