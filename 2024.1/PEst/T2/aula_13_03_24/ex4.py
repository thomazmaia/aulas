def fatorial(num : int):
    # 5! = 5 x 4 x 3 x 2 x 1 = 120
    fat = 1
    for i in range(1, num+1):
        fat = fat*i
    return fat

def comb(n : int, p : int):
    return fatorial(n) / (fatorial(p) * fatorial (n-p))


N = int(input("Digite N: "))
P = int(input("Digite P: "))

print(comb(N, P))