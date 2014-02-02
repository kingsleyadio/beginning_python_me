def even(start, end):
    return [i for i in range(start, end+1) if i%2==0]
        
def odd(start, end):
    return [i for i in range(start, end+1) if i%2!=0]