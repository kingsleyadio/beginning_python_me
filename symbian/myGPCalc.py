#! filename: myGPCalc.py
# must be run directly not imported

import types

print '\nWELCOME TO my GPA Calculator\n\nAuthor: ADIO KINGSLEY O\n(c) 2011 ADIKSonline\nall rights reserved\nVERSION: 1.0 Final\n\nLETS GET STARTED>>>\n\n'

tnu=0
tcp=0
tcp=float(tcp)

while True:
    try:
        x=raw_input('enter course unit: ')
        y=raw_input('enter score: ')
    except EOFError:
        if not tnu:
            print '\nTotal GPA is: 0.0\n'
            print 'E X I T I N G . . .\n'
            break
        else:
            GPA=tcp/tnu
            print '\nTotal GPA is: %.3f\n' %GPA
            print 'E X I T I N G . . .\n'
            break
    except:
        print '\nAN ERROR OCCURRED !\n'
        print 'E X I T I N G . . .\n'
        break
        
    try:
        x=int(x)
    except:
        print '\nunit must be an integer !\n'.upper()
    try:
        if type(x)==types.IntType:
            if int(y) in range(70, 101):
                tnu+=x
                tcp+=5*x
                print '\nGPA is: ', tcp/tnu, '\n'
            elif int(y) in range(60, 70):
                tnu+=x
                tcp+=4*x
                print '\nGPA is: ', tcp/tnu, '\n'
            elif int(y) in range(50, 60):
                tnu+=x
                tcp+=3*x
                print '\nGPA is: ', tcp/tnu, '\n'
            elif int(y) in range(46, 50):
                tnu+=x
                tcp+=2*x
                print '\nGPA is: ', tcp/tnu, '\n'
            elif int(y) in range(40, 46):
                tnu+=x
                tcp+=1*x
                print '\nGPA is: ', tcp/tnu, '\n'
            elif int(y) in range(0, 40):
                tnu+=x
                tcp+=0*x
                if tnu==0:
                    print '\nGPA is: 0.0\n'
                else:
                    print '\nGPA is: ', tcp/tnu, '\n'
            else:
                print '\nscore is out of range !\n'.upper()
                
    except ValueError:
        if type(x)==types.IntType:
            if y in ('a', 'A'):
                tnu+=x
                tcp+=5*x
                print '\nGPA is: ', tcp/tnu, '\n'
            elif y in ('b', 'B'):
                tnu+=x
                tcp+=4*x
                print '\nGPA is: ', tcp/tnu, '\n'
            elif y in ('c', 'C'):
                tnu+=x
                tcp+=3*x
                print '\nGPA is: ', tcp/tnu, '\n'
            elif y in ('d', 'D'):
                tnu+=x
                tcp+=2*x
                print '\nGPA is: ', tcp/tnu, '\n'
            elif y in ('e', 'E'):
                tnu+=x
                tcp+=1*x
                print '\nGPA is: ', tcp/tnu, '\n'
            elif y in ('f', 'F'):
                tnu+=x
                tcp+=0*x
                if tnu==0:
                    print '\nGPA is: 0.0\n'
                else:
                    print '\nGPA is: ', tcp/tnu, '\n'
            elif y=='':
                print '\nenter a valid score !\n'.upper()
            else:
                print '\nscore is out of range !\n'.upper()
    except:
        print '\nan error occurred !\n'.upper()
        print 'E X I T I N G . . .\n'
        break