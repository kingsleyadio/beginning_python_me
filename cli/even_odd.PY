def even():
    try:
        try:
            a=int(raw_input('enter startin point number: '))
            b=int(raw_input('enter endin point number: '))
            if a<b:
                for x in range(a, b+1):
                    if x%2!=0:
                        continue
                    else:
                        print x,
            else:
                print 'STARTING POINT MUST BE LOWER THAN ENDING POINT !!!'
                even()

        except:
            print 'ERROR'
            even()
    finally:
        print '\nwow, as easy as ABC !!!'
        
def odd():
    try:
        try:
            a=int(raw_input('enter startin point number: '))
            b=int(raw_input('enter endin point number: '))
            if a<b:
                for x in range(a, b+1):
                    if x%2==0:
                        continue
                    else:
                        print x,
        
            else:
                print 'STARTING POINT MUST BE LOWER THAN ENDING POINT !!!'
                odd()

            
        except:
            print 'ERROR'
            even()
        
    finally:
        print '\nwow, this is FANTAstic !!!'