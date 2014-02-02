#! filename: myGPCalc1_2.py
# my first GUI program

import e32, os, sys
import types
import appuifw as ui
from graphics import *

app_lock=e32.Ao_lock()

ui.app.title=u'myGPCalc'
ui.app.screen='normal'
img=Image.open(os.path.dirname(sys.argv[0])+'\\me.jpg')
ui.note(u'WELCOME TO my GPA Calculator')

def handle_redraw(rect):
    canvas.blit(img)
    
canvas=ui.Canvas(event_callback=None, redraw_callback=handle_redraw)

ui.app.body=canvas

def GPACalc():
    tnu=0
    tcp=0
    tcp=float(tcp)

    ui.note(u'LETS GET STARTED', 'info')

    while True:
        try:
            while True:
                x=ui.query(u'enter course unit: ', 'number')
                if int(x)==0:
                    ui.note(u'you entered an invalid unit'.upper(), 'error')
                else:
                    break
            y=ui.query(u'enter score or grade: ', 'text')
            x=int(x)
        except:
            if not tnu:
                ui.note(u'Total GPA is: 0.0', 'conf')
                break
            else:
                GPA=tcp/tnu
                ui.note(u'Total GPA is: %.3f\n' %GPA, 'conf')
                if 5.0>=GPA>=4.5:
                    ui.note(u'WOW\nA FIRST CLASS RESULT', 'info')
                elif 4.5>GPA>=3.5:
                    ui.note(u'This is SECOND class, UPPER division')
                elif 3.5>GPA>=2.5:
                    ui.note(u'a SECOND class, LOWER division')
                elif 2.5>GPA>=1.5:
                    ui.note(u'THIRD class result')
                elif 1.5>GPA>=1.0:
                    ui.note(u'This is just a PASS result')
                else:
                    ui.note(u'You are ADVISED to WITHDRAW ASAP')
                break
      
        try:
            if type(x)==types.IntType:
                if int(y) in range(70, 101):
                    tnu+=x
                    tcp+=5*x
                    ui.note(u'GPA is: '+str( tcp/tnu), 'conf')
                elif int(y) in range(60, 70):
                    tnu+=x
                    tcp+=4*x
                    ui.note(u'GPA is: '+str(tcp/tnu), 'conf')
                elif int(y) in range(50, 60):
                    tnu+=x
                    tcp+=3*x
                    ui.note(u'GPA is: '+str(tcp/tnu), 'conf')
                elif int(y) in range(46, 50):
                    tnu+=x
                    tcp+=2*x
                    ui.note(u'GPA is: '+str(tcp/tnu), 'conf')
                elif int(y) in range(40, 46):
                    tnu+=x
                    tcp+=1*x
                    ui.note(u'GPA is: '+str(tcp/tnu), 'conf')
                elif int(y) in range(0, 40):
                    tnu+=x
                    tcp+=0*x
                    if tnu==0:
                        ui.note(u'GPA is: 0.0', 'conf')
                    else:
                        ui.note(u'GPA is: '+str(tcp/tnu), 'conf')
                else:
                    ui.note(u'score is out of range !'.upper(), 'error')
            if ui.query(u'continue', 'query'):
                continue
            else:
                if not tnu:
                    ui.note(u'Total GPA is: 0.0', 'conf')
                    break
                else:
                    GPA=tcp/tnu
                    ui.note(u'Total GPA is: %.3f\n' %GPA, 'conf')
                if 5.0>=GPA>=4.5:
                    ui.note(u'WOW\nA FIRST CLASS RESULT', 'info')
                elif 4.5>GPA>=3.5:
                    ui.note(u'This is SECOND class, UPPER division')
                elif 3.5>GPA>=2.5:
                    ui.note(u'a SECOND class, LOWER division')
                elif 2.5>GPA>=1.5:
                    ui.note(u'THIRD class result')
                elif 1.5>GPA>=1.0:
                    ui.note(u'This is just a PASS result')
                else:
                    ui.note(u'You are ADVISED to WITHDRAW ASAP')
                break
                
        except ValueError:
            if type(x)==types.IntType:
                if y in ('a', 'A'):
                    tnu+=x
                    tcp+=5*x
                    ui.note(u'GPA is: '+str(tcp/tnu), 'conf')
                elif y in ('b', 'B'):
                    tnu+=x
                    tcp+=4*x
                    ui.note(u'GPA is: '+str(tcp/tnu), 'conf')
                elif y in ('c', 'C'):
                    tnu+=x
                    tcp+=3*x
                    ui.note(u'GPA is: '+str(tcp/tnu), 'conf')
                elif y in ('d', 'D'):
                    tnu+=x
                    tcp+=2*x
                    ui.note(u'GPA is: '+str(tcp/tnu), 'conf')
                elif y in ('e', 'E'):
                    tnu+=x
                    tcp+=1*x
                    ui.note(u'GPA is: '+str(tcp/tnu), 'conf')
                elif y in ('f', 'F'):
                    tnu+=x
                    tcp+=0*x
                    if tnu==0:
                        ui.note(u'GPA is: 0.0', 'conf')
                    else:
                        ui.note(u'GPA is: '+str(tcp/tnu), 'conf')

                else:
                    ui.note(u'score is out of range !'.upper(), 'error')
            if ui.query(u'continue', 'query'):
                continue
            else:
                if not tnu:
                    ui.note(u'Total GPA is: 0.0', 'conf')
                    break
                else:
                    GPA=tcp/tnu
                    ui.note(u'Total GPA is: %.3f\n' %GPA, 'conf')
                if 5.0>=GPA>=4.5:
                    ui.note(u'WOW\nA FIRST CLASS RESULT', 'info')
                elif 4.5>GPA>=3.5:
                    ui.note(u'This is SECOND class, UPPER division')
                elif 3.5>GPA>=2.5:
                    ui.note(u'a SECOND class, LOWER division')
                elif 2.5>GPA>=1.5:
                    ui.note(u'THIRD class result')
                elif 1.5>GPA>=1.0:
                    ui.note(u'This is just a PASS result')
                else:
                    ui.note(u'You are ADVISED to WITHDRAW ASAP')
                break
        except:
            if not tnu:
                ui.note(u'Total GPA is: 0.0', 'conf')
                break
            else:
                GPA=tcp/tnu
                ui.note(u'Total GPA is: %.3f\n' %GPA, 'conf')
                if 5.0>=GPA>=4.5:
                    ui.note(u'WOW\nA FIRST CLASS RESULT', 'info')
                elif 4.5>GPA>=3.5:
                    ui.note(u'This is SECOND class, UPPER division')
                elif 3.5>GPA>=2.5:
                    ui.note(u'a SECOND class, LOWER division')
                elif 2.5>GPA>=1.5:
                    ui.note(u'THIRD class result')
                elif 1.5>GPA>=1.0:
                    ui.note(u'This is just a PASS result')
                else:
                    ui.note(u'You are ADVISED to WITHDRAW ASAP')
                break

def exit_key_handler():
    e32.ao_sleep(0.2)
    app_lock.signal()
    ui.app.set_exit()
    
def la():
    ui.note(u'ADIO KINGSLEY O\n(c) 2011 ADIKSonline\nadiksonline@gmail.com')
    
def ma():
    ui.note(u'VERSION: 1.2 Beta')
            
ui.app.menu=[(u'GPA Calculator', GPACalc), (u'Author', la), (u'Version', ma), (u'Exit', exit_key_handler)]

ui.app.exit_key_handler=exit_key_handler
app_lock.wait()