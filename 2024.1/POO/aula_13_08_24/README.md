# Exercícios - Métodos de instância/classe/estático

1. Crie uma classe chamada `Ponto`. Essa classe deve receber dois valores X, Y (float) no seu construtor. Faça os getters e setters para esses atributos serem
chamados pelo main abaixo:

```python
P = Ponto(50, 50)
print(f"Coordenadas: {P.getX()}, {P.getY()}")

P.setX(20)
print(f"Coordenadas: {P.getX()}, {P.getY()}")
```

2. Adicione um método de instância à classe Ponto chamado `get_info()`. Esse método deve retornar as coordenadas e o quadrante daquele ponto.

3. Adicione uma proteção ao setter da classe para permitir apenas coordenadas nos quadrantes 1 e 2 (incluindo os eixos).

4. Crie um método de classe chamado `por_tamanho_e_quadrante(t, q)` para que o usuário consiga criar uma ponto com um determinado tamanho em um determinado quadrante. Exemplo:

```python
P = Ponto.por_tamanho_e_quadrante(5, 2)
print(f"Coordenadas: {P.getX()}, {P.getY()}")  # Coordenadas: -3.53, 3.53
```

5. Adicione um método estático à classe Ponto chamado `calc_dist_entre_pontos(p1, p2)` que retornará a distância entre duas instâncias da classe Ponto.

```python
P1 = Ponto(50, 50)
P2 = Ponto(10, 15)

print(f"Distância entre os pontos: {P.calc_dist_entre_pontos(P1, P2)}")
```
