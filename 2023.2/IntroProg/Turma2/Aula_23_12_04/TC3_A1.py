M = int(input("M: "))
N = int(input("N: "))

if M < N:
    while M <= N:
        print(M)
        M += 1    
else:
    while N <= M:
        print(N)
        N += 1