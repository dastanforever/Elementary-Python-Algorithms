__author__ = 'Pranav Sharma'

def gcd(a,b):
    if a == 0:
        print b
        return
    if b == 0:
        print a
        return
    gcd( b%a , a)


print 'Gcd is'
gcd(24,6)
