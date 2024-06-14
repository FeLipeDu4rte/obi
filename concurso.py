n, k = map(int, input().split())
lista = input().split()
numeros = [int(num) for num in lista]
if(k == 1):
    candidatos = max(numeros)
    print(candidatos)
else:
    x=1
    while True:
        candidatos = max(numeros)
        v = numeros.count(candidatos)
        numeros.remove(candidatos)
        if(v==k):
            print(candidatos)
            break
        elif(x==k):
            print(candidatos)
            break
        x+=1
        