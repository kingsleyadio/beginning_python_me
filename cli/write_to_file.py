poem='''programin is fun!

Usin d world leadin lang>>
PYTHON...'''

f=file('e:poem.txt', 'w')
f.write(poem)
f.close()

f=file('e:poem.txt')
while True:
    line=f.readline()
    if len(line)==0:
        break
    print line
f.close()
