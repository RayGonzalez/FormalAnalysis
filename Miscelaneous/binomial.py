
def NchooseK(n,k):
    return factorial(n)/(factorial(k)*factorial(n-k))

def BinomDistribution(n,p,k):
    return NchooseK(n,k)*(p**k)*((1-p)**(n-k))

def factorial(a):
    r=1
    if a==0:
        return 1
    while(a!=1):
        r=r*a
        a=a-1
    return r

print BinomDistribution(100,.1,3)
print BinomDistribution(100,.1,5)
print BinomDistribution(100,.1,99)
print NchooseK(5,2)
print factorial(3)
print 1-BinomDistribution(10,.07,0)