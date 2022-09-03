x,y,z = input().split()
a,b,c = input().split()

p = (int(y)*float(z))+(int(b)*float(c))
print("VALOR A PAGAR: R$ {0:.2f}".format(p))