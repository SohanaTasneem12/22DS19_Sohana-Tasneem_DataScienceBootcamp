a,b,c = map(float,input().split())

#triangle
p = (0.5)*a*c
#circle
q = 3.14159*c*c
#trapezium
r = (0.5)*(a+b)*c
#square
s = b*b
#rectangle
t = a*b

print("TRIANGULO: {0:.3f}".format(p))
print("CIRCULO: {0:.3f}".format(q))
print("TRAPEZIO: {0:.3f}".format(r))
print("QUADRADO: {0:.3f}".format(s))
print("RETANGULO: {0:.3f}".format(t))

