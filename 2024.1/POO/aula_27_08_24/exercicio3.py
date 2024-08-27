# Crie uma classe chamada Veiculo que possua um atributo velocidade_maxima e um método acelerar(), que incrementa um valor passado como parâmetro à "velocidade_atual" do veículo. Em seguida, crie duas subclasses chamadas Carro e Moto, que  herdam da classe Veiculo. A classe Carro deve ter um atributo adicional "marca" e a classe Moto deve ter um atributo adicional "cilindradas". Cada subclasse deve sobrescrever o método acelerar() para verificar se a velocidade atual não ultrapassou a sua respectiva velocidade máxima. Se ultrapassou, deve imprimir a mensagem “Velocidade máxima atingida”. Caso contrário, deve chamar o método acelerar() da superclasse.

carro = Carro('Fiat', 120)  # Marca e velocidade maxima
moto = Moto(250, 100) # Cilindradas e velociadde maxima

carro.acelerar(110)
moto.acelerar(120)

print(carro.velocidade_atual)
print(moto.velocidade_atual)