M = int(input("M = "))
N = int(input("N = "))

if M > N:
    while N <= M:
        if N % 2 == 1:
            print(N)    
        N = N + 1 
else:
    while M <= N:
        if M % 2 == 1:
            print(M)    
        M = M + 1     