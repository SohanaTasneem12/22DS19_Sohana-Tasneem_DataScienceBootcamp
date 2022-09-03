
a,b,c = map(float,input().split())

if(a+b>c and b+c>a and c+a>b):
    x = a+b+c
    print("Perimetro = {0:.1f}".format(x))
else:
    y = (0.5)*(a+b)*c
    print("Area = {0:.1f}".format(y))
