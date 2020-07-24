def addnumber(a,b):
    return a+b
X=addnumber(1,2)
print(X)

def subtrac(c,d):
    return c-d
Y=subtrac(5,1)
print(Y)

def divide(e,f):
    return e/f
Z=divide(10,5)
print(Z)

def floor_divide(g,h):
    return g//h
P=floor_divide(100,3)
print(P)

def modulus(l,k):
    return l%k
M=modulus(100,9)
print(M)


for i in range(2,51):
    print(i)
    for j in range(50,1,-1):
        print(j)
        if i%j==0:
            print(i)
