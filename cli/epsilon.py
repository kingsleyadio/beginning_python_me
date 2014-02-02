print 'to get d smallest number computable on ds device'
d=1.0
y=1.0E-3
e=d-y
print '%f'.ljust(10) %e, y
while e!=1:
    y=y/1.0E1
    e=d-y
    print '%f'.ljust(10) %e, y
print 'this device\'s epsilon is:',y
