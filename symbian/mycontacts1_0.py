#! filename: mycontacts1_0.py

AUTHOR='''Adio Kingsley O
adiksonline@gmail.com'''
DATE='07-01-2011 16:22:50'
VERSION='version 1.0'
COPYRIGHT='''(c) 2011 ADIKSonline
all rights reserved'''
__doc__='check help'

try:
    import os
    import pickle
    from odbchelper import buildConnectionString as div
except ImportError:
    print 'UNABLE TO IMPORT MODULES'
    
def open():
    try:
        a=raw_input("""WELCOME TO MyCONTACTs\n\ntype 'ADD', 'BROWSE', 'SEARCH', 'MODIFY', 'DELETE',  or 'HELP'\nto get going : """)
    except:
        print '\nan error occured !\n'.upper()
        return 
    a=a.lower()
    if a=='add':
        addc()
    elif a=='browse':
        browsec()
    elif a=='search':
        searchc()
    elif a=='modify':
        modifyc()
    elif a=='delete':
        deletec()
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
        e=raw_input("enter relation\n('family', 'friend', 'colleague'): ")
        if e not in relation:
            print '\nyou entered an invalid relation\n'.upper()
            addc()
            return
    except:
        return
    f={'NAME':b, 'PHONE_NUMBER':c, 'EMAIL':d, 'RELATION':e}
    print 'YOU ENTERED:'; print div(f), '\n'
    try:
        h=pickle.load(file('e:\\CONTACTS\\mycontacts.info'))
    except (IOError, EOFError):
        print '\nmy first contact info>>>\n'.upper()
        h=[]
    h.append(f)
    for i in h:
        i['SERIAL_NUMBER']=h.index(i)+1
    cd='e:'+os.sep+'CONTACTS'
    if not os.path.exists(cd):
        os.mkdir(cd)
    g=file(cd+os.sep+'mycontacts.info', 'w')
    pickle.dump(h, g)
    g.close()
    open()

def browsec():
    try:
        g=file('e:\\contacts\\mycontacts.info')
        h=pickle.load(g)
        if h==[]:
            print '\nno contact info yet !\n'.upper()
            return
        for i in h:
            print '\n', div(i), '\n'
        
        g.close()
    except IOError:
        print '\nNO CONTACT INFO YET !\n'
    except:
        print '\nan error occured!\n'.upper()
        return
    open()
def searchc():
    relation=('family', 'friend', 'colleague')
    try:
        w=raw_input("""\nSEARCH WITH RELATION\nenter preferred relation group\n('family', 'friend', 'colleague'): """)
        if w not in relation:
            print '\nentered relation does not exist !\n'.upper()
            searchc()
            return
        try:
            g=file('e:\\CONTACTS\\mycontacts.info')
            h=pickle.load(g)
        except:
            print '\nno contact info yet !\n'.upper()
            return
        if h==[]:
            print '\nno contact info yet !\n'.upper()
            return
        count=0
        for i in h:
            if i['RELATION']=='%s' %w:
                count+=1
                print '\n', div(i), '\n'
                g.close()
        if not count:
            print '\nno contact with this relation yet !\n'.upper()
    except EOFError:
        return
    except IOError:
        print '\nno contact info yet\n'.upper()
    except:
        print '\nan error occured !\n'.upper()
    open()
    
def modifyc():
    try:
        y=raw_input('\nenter the s/n of the contact you which to modify: '.upper())
        if not y:
            print '\na valid s/n is required !\n'.upper()
        h=pickle.load(file('e:\\contacts\\mycontacts.info'))
    except IOError:
        print '\nno contact info yet !\n'.upper
        return
    except:
        print '\nan error occurred !\n'.upper()
        return
    count=0
    for i in h:
        if str(i['SERIAL_NUMBER'])==y:
            count+=1
            print '\n', div(i), '\n'
            try:
                relation=('family', 'friend', 'colleague')
                b=raw_input('enter name: ')
                if b=='':
                    print '\nenter a real name!\n'.upper()
                    modifyc()
                    return
                c=raw_input('enter phone no: ')
                if not c:
                    c='None'
                d=raw_input('enter email: ')
                if not d:
                    d='None'
                e=raw_input("enter relation\n('family', 'friend', 'colleague'): ")
                if e not in relation:
                    print '\nyou entered an invalid relation\n'.upper()
                    modifyc()
                    return
                i['NAME']=b
                i['PHONE_NUMBER']=c
                i['EMAIL']=d
                i['RELATION']=e
                print '\nu entered:'.upper(), div(i), '\n'
                g=file('e:\\contacts\\mycontacts.info', 'w')
                pickle.dump(h, g)
                g.close()
            except:
                print '\nan error occured!\n'.upper()
    if not count:
        print '\ns/n out of range !!!\n'.upper()
    open()
    
def deletec():
    try:
        y=raw_input('\nenter the s/n of the contact you want to delete: '.upper())
        if not y:
            print '\na valid s/n is required !\n'.upper()
        h=pickle.load(file('e:\\contacts\\mycontacts.info'))
    except IOError:
        print '\nno contact info yet !\n'.upper
        return
    except:
        print '\nan error occurred !\n'.upper()
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
    g=file('e:\\contacts\\mycontacts.info', 'w')
    pickle.dump(h, g)
    g.close()
    open()

def helpc():
    help="""\nA PERSONAL ADDRESS-BOOK FOR CONTACTS INFO STORAGE.\n\ntype the defined keywords for corresponding actions>>>\n\nADD :- add new contact\nBROWSE :- surf existing contacts\nSEARCH :- search for tag-specific contacts\nMODIFY :- edit an existing contact\nDELETE :- shred unwanted contact\nHELP :- to bring you here\n\nyou will definitely enjoy it...\n\n%s\n""" %COPYRIGHT
    print help
    open()

            
            
if __name__=='__main__':
    open()