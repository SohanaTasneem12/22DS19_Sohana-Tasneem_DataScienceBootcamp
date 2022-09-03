a,b,c = map(int,input().split())

x = (a+b+abs(a-b))/2
y = int((x+c+abs(x-c))/2)
print("{} eh o maior".format(y))