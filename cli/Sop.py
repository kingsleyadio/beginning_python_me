def psum(power, *args):
    total=0
    for i in args:
        total+=pow(i, power)
    return total
    
print psum(2, 3, 4)