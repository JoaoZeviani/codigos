import math

def ButVol(x):
    f=math.exp(alfa*x)-math.exp((alfa-1)*x)-beta
    return f
def ButVolprime(x):
    f=alfa*math.exp(alfa*x)-(alfa-1)*math.exp((alfa-1)*x)
    return f

def bis(f,a,b,t): 
    n=1
    while(n!=200):
        m=(a+b)/2
        if f(a)*f(m)<0:
            b=m
        else:
            a=m
        if n!=1:
            xn_1=xn
            xn=m
            if math.fabs(xn-xn_1)/math.fabs(xn)<t:
                break
        else: xn=m
        n=n+1
    return xn, n

def newton(f,fprime,x0,t):
    n=1
    xn=x0
    while(n!=200):
        xn1=xn-f(xn)/fprime(xn)
        xn_1=xn
        xn=xn1
        if math.fabs(xn-xn_1)/math.fabs(xn)<t:
             break
        n=n+1
    return xn, n

alfa=0.2
beta=2
print(bis(ButVol,3,4,.001))
print(newton(ButVol,ButVolprime,1,.001))