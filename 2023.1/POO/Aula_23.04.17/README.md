# Lista encapsupamento

### 01 - Crie uma classe chamada ```Ponto``` e salve em um mesmo arquivo .py esta classe e o arquivo principal indicando o uso de cada uma das questões. Essa classe deve receber dois valores X, Y (float) no seu construtor. Faça os *getters* e *setters* para esses atributos serem chamados conforme código principal abaixo:

```# Questão 1
P = Ponto(50,50)
print(f"Coordenadas: {P.x},{P.y}")

P.x = 20
print(f"Novas coordenadas: {P.x},{P.y}")
     
# Questão 2 
# ...
```

### 02 - Adicione um método de instância à classe Ponto chamado ```get_info()```. Esse método deve retornar as coordenadas e o quadrante daquele ponto.

### 03 - Adicione uma proteção ao *setter* da classe para permitir apenas coordenadas nos quadrantes 1 e 2 (incluindo os eixos).

### 04 - Crie um método de classe chamado ```por_tamanho_e_quadrante(t, q)``` para que o usuário consiga criar uma ponto com um determinado tamanho em um determinado quadrante.

### 05 - Adicione um método estático à classe Ponto chamado ```calc_dist_entre_pontos(p1, p2)``` que retornará a distância entre duas instâncias da classe Ponto.

**NOTA**: a lista deve ser feita em dupla e deve ser anviado pelo SUAP. Envie um único arquivo .py contendo a classe implementada e códigos de teste dessa classe.