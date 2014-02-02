#! filename: mycontacts1_1.py

AUTHOR='''\nAdio Kingsley O
adiksonline@gmail.com\n'''
VERSION='\nVERSION 1.1 with minor bug fixes\nProd. Date: 10-01-2011 09:09:00\n'
COPYRIGHT='''\n(c) 2011 ADIKSonline
all rights reserved\n'''
__doc__='check help'

try:
    import os
    import pickle
    from odbchelper import buildConnectionString as div
except ImportError:
    global z
    z='\nUNABLE TO IMPORT MODULES\n'
    print z
    
def open():
    try:
        if z=='\nUNABLE TO IMPORT MODULES\n':
            return
    except:
        pass
    try:
        a=raw_input("""WELCOME TO MyCONTACTs\n\ntype 'ADD', 'BROWSE', 'SEARCH', 'MODIFY', 'DELETE', 'AUTHOR', 'VERSION', 'COPYRIGHT', 'HELP' or 'QUIT'\nto get going : """)
    except:
        print '\ne x i t i n g . . .\n'.upper()
        return 
    a=a.lower()
    if a=='add':
        addc()
    elif a=='quit':
        print '\ne x i t i n g . . .\n'.upper()
        return
    elif a=='browse':
        browsec()
    elif a=='search':
        searchc()
    elif a=='modify':
        modifyc()
    elif a=='delete':
        deletec()
    elif a=='author':
        print AUTHOR
        open()
        return
    elif a=='version':
        print VERSION
        open()
        return
    elif a=='copyright':
        print COPYRIGHT
        open()
        return
    elif a=='help':
        helpc()
    else:
        print '\nplease, enter a valid command !\n'.upper()
        open()
        
def addc():
    relation=('family', 'friend', 'colleague')
    try:
        b=raw_input('enter name: ')
        if b=='':
            print '\nenter a real name!\n'.upper()
            addc()
            return
        c=raw_input('enter phone no: ')
        if not c:
            c='None'
        d=raw_input('enter email: ')
        if not d:
            d='None'
        ok=1
        while ok:
            e=raw_input("enter relation\n('family', 'friend', 'colleague'): ")
            if e not in relation:
                print '\nyou entered an invalid relation\n'.upper()
            else:
                ok=0
    except:
        print '\nr e t u r n i n g . . .\n'.upper()
        open()
        return
    f={'NAME':b, 'PHONE_NUMBER':c, 'EMAIL':d, 'RELATION':e}
    print '\nYOU ENTERED:'; print div(f), '\n'
    try:
        h=pickle.load(file('e:\\adikstools\\myCONTACTS\\mycontacts.info'))
    except (IOError, EOFError):
        print '\nmy first contact info>>>\n'.upper()
        h=[]
    h.append(f)
    for i in h:
        i['SERIAL_NUMBER']=h.index(i)+1
    cd='e:'+os.sep+'ADIKStools'+os.sep+'myCONTACTS'
    if not os.path.exists(cd):
        os.makedirs(cd)
    g=file(cd+os.sep+'mycontacts.info', 'w')
    pickle.dump(h, g)
    g.close()
    open()

def browsec():
    try:
        g=file('e:\\adikstools\\mycontacts\\mycontacts.info')
        h=pickle.load(g)
        if h==[]:
            print '\nno contact info yet !\n'.upper()
            open()
            return
        for i in h:
            print '\n', div(i), '\n'
        
        g.close()
        open()
    except IOError:
        print '\nNO CONTACT INFO YET !\n'
        open()
    except:
        print '\nr e t u r n i n g . . .\n'.upper()
        open()
        return

def searchc():
    relation=('family', 'friend', 'colleague')
    try:
        w=raw_input("""\nSEARCH WITH RELATION\nenter preferred relation group\n('family', 'friend', 'colleague'): """)
        if w not in relation:
            print '\nentered relation does not exist !\n'.upper()
            searchc()
            return
        try:
            g=file('e:\\adikstools\\myCONTACTS\\mycontacts.info')
            h=pickle.load(g)
        except:
            print '\nno contact info yet !\n'.upper()
            open()
            return
        if h==[]:
            print '\nno contact info yet !\n'.upper()
            open()
            return
        count=0
        for i in h:
            if i['RELATION']=='%s' %w:
                count+=1
                print '\n', div(i), '\n'
                g.close()
        if not count:
            print '\nno contact with this relation yet !\n'.upper()
            open()
        open()
    except EOFError:
        print '\nr e t u r n i n g . . .\n'.upper()
        open()
        return
    except IOError:
        print '\nno contact info yet\n'.upper()
        open()
    except:
        print '\nan error occured !\n'.upper()
        open()
    
def modifyc():
    try:
        y=raw_input('\nenter the s/n of the contact you which to modify: '.upper())
        if not y:
            print '\na valid s/n is required !\n'.upper()
            open()
            return
        h=pickle.load(file('e:\\adikstools\\mycontacts\\mycontacts.info'))
    except IOError:
        print '\nno contact info yet !\n'.upper
        open()
        return
    except:
        print '\nr e t u r n i n g . . .\n'.upper()
        open()
        return
    count=0
    for i in h:
        if str(i['SERIAL_NUMBER'])==y:
            count+=1
            print '\n', div(i), '\n'
            try:
                relation=('family', 'friend', 'colleague')
                ok=1
                while ok:
                    b=raw_input('enter name: ')
                    if b=='':
                        print '\nenter a real name!\n'.upper()
                    else:
                        ok=0
                c=raw_input('enter phone no: ')
                if not c:
                    c='None'
                d=raw_input('enter email: ')
                if not d:
                    d='None'
                ok=1
                while ok:
                    e=raw_input("enter relation\n('family', 'friend', 'colleague'): ")
                    if e not in relation:
                        print '\nyou entered an invalid relation\n'.upper()
                    else:
                        ok=0
                i['NAME']=b
                i['PHONE_NUMBER']=c
                i['EMAIL']=d
                i['RELATION']=e
                print '\nu entered:'.upper(), div(i), '\n'
                g=file('e:\\adikstools\\mycontacts\\mycontacts.info', 'w')
                pickle.dump(h, g)
                g.close()
            except:
                print '\nan error occured!\n'.upper()
                open()
                return
    if not count:
        print '\ns/n out of range !!!\n'.upper()
    open()
    
def deletec():
    try:
        y=raw_input('\nenter the s/n of the contact you want to delete: '.upper())
        if not y:
            print '\na valid s/n is required !\n'.upper()
            open()
            return
        h=pickle.load(file('e:\\adikstools\\mycontacts\\mycontacts.info'))
    except IOError:
        print '\nno contact info yet !\n'.upper
        open()
        return
    except:
        print '\nan error occurred !\n'.upper()
        open()
        return
    count=0
    for i in h:
        if str(i['SERIAL_NUMBER'])==y:
            count+=1
            if count==1:
                print '\n', div(i), '\n'
                del h[h.index(i)]
                print '\ncontact successfully deleted>>>\n'.upper()
            elif count>1:
                break
    if not count:
        print '\nout of range !\n'.upper()
    for i in h:
        i['SERIAL_NUMBER']=h.index(i)+1
    g=file('e:\\adikstools\\mycontacts\\mycontacts.info', 'w')
    pickle.dump(h, g)
    g.close()
    open()

def helpc():
    help="""\nA PERSONAL ADDRESS-BOOK FOR CONTACTS INFO STORAGE.\n\ntype the defined keywords for corresponding actions>>>\n\nADD :- add new contact\nBROWSE :- surf existing contacts\nSEARCH :- search for tag-specific contacts\nMODIFY :- edit an existing contact\nDELETE :- shred unwanted contact\nAUTHOR :- get the program developer info\nVERSION :- get current software version and date\nCOPYRIGHT :- get copyright details\nHELP :- to bring you here\nQUIT :- to quit from the program\n\nyou will definitely enjoy it...\n%s\n""" %COPYRIGHT
    print help
    open()

            
            
if __name__=='__main__':
    open()
