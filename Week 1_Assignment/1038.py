x,y = map(int,input().split())

if (x==1):
    z = y*4.00
    print("Total: R$ {0:.2f}".format(z))
elif (x==2):
    z = y*4.50
    print("Total: R$ {0:.2f}".format(z))
elif (x==3):
    z = y*5.00
    print("Total: R$ {0:.2f}".format(z))
elif (x==4):
    z = y*2.00
    print("Total: R$ {0:.2f}".format(z))
else:
    z = y*1.50
    print("Total: R$ {0:.2f}".format(z))
