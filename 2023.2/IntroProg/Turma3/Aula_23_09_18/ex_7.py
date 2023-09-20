# Calculadora de Gorjeta: Solicite ao usuário o valor da conta
# em um restaurante e a porcentagem de gorjeta que eles desejam
# deixar. Calcule a quantia da gorjeta e o valor total da
# conta, em seguida, imprima ambos.

valor_conta = float(input("Valor da conta: "))
gorjeta = float(input("% de gorjeta: "))

valor_gorjeta = gorjeta / 100 * valor_conta
valor_conta_total = valor_conta + valor_gorjeta

print(f"Gorjeta: R${valor_gorjeta}")
print(f"Valor total da conta: R${valor_conta_total}")
