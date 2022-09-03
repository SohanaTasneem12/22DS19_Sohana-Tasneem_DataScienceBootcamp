from cmath import sqrt

x1,y1 = map(float,input().split())
x2,y2 = map(float,input().split())

#d = sqrt(((x2-x1)**2)+((y2-y1)**2))
d = sqrt(pow((x2-x1),2)+pow((y2-y1),2))
print("{0:.4f}".format(d))