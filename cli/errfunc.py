from math import sqrt
pi=22.0/7.0
x=input('the value of x is: ')
n=input('numba of terms in series is: ')
fac=2.0/sqrt(pi)
prod=1.00
result=0.0
sum=0.0
for i in range(1, n+1):
    y1=((-1.0)**(i))*x**((2*i)+1)
    prod*=i
    y2=prod*(2.0*(i+1))
    sum+=(y1/y2)
result=sum*fac
print 'erf(%0.2f) = %0.5f'%(x, result)
