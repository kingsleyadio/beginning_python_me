import sys
print 'using taylor\'s series to derive the exponential of (x):\n'
n=input('enter d no of terms: ')
x=input('enter x: ')
result=1.0
ifac=1.0
for i in range(1, n+1):
    ifac*=i
    result+=(x**i)/ifac
    m=i
    sys.stdout.write('.')
m+=1
ifac*=m
errortam=(x**m)/ifac
print '\nvalue of X: %0.2f'%x
print 'RESULT: %0.5f'%result
print 'ERROR: %0.5f'%errortam