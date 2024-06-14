H = int(input())
M = int(input())
S = int(input())
T = int(input())

S=S+T
if(S>=60):
    valor = S
    S = S%60
    M=M+(valor/60)
    if(M>=60):
        valor = M 
        M = M%60
        H=H+(valor/60)
        print(H)
        print(M)
        print(S)
    else:
        print(H)
        print(M)
        print(S)
else:
    print(H)
    print(M)
    print(S)