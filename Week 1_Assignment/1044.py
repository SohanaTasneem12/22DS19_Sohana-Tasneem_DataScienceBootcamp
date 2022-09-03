a,b = map(int,input().split())

if(max(a,b) % min(a,b) != 0):
    print("Nao sao Multiplos")
else:
    print("Sao Multiplos")