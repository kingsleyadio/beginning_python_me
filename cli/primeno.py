def testprime(numba):
    if type(numba)!=int:
        raise ValueError, 'integer number required'
    if numba<0:
        n=-(numba)
    else:
        n=numba
    if n in (0, 1):
        return '%d is not a prime number' %numba
    for i in range(2, n):
        if n%i==0:
            return '%d is not a prime number' %numba
    else:
        return '%d is a prime number' %numba

def getprime(start, end):
    if type(start)!=int or type(end)!=int:
        raise ValueError, 'integer numbers expected'
    result=[]
    if start<2: start=2
    for n in range(start, end+1):
        for x in range(2, n):
            if n%x==0:
                break
        else:
            result.append(n)
    return result

while True:
    a=input("enter number to test: ")
    print testprime(a)
