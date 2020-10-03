b = str(input()).split()

d = int(b[0])
c= int(b[1])
e = '.|.'
for i in range(1,d,2):
    print((e*i).center(c,'-'))
print(('WELCOME').center(c,'-'))
for i in range(d-2,-1,-2):
    print((e * i).center(c, '-'))
