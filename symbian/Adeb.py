#! filename: myGPCalc1_3.py
# my first GUI program
#improved !
#now with static and
#dynamic GPA calculators

import e32, os
import appuifw2 as ui
from graphics import *
#from camera import _main_pane_size as pixels

#app_lock=e32.Ao_lock()

#ui.app.title=u'myGPCalc'
#ui.app.screen='normal'
#img=Image.open('e:\\python\\scripts\\me.jpg')
#img=img.resize(pixels())
#ui.note(u'my GPA Calculator\namplified...')

#def handle_redraw(rect):
   # canvas.blit(img)
    
#canvas=ui.Canvas(event_callback=None, redraw_callback=handle_redraw)

#ui.app.body=canvas

def static(tnu=0, tcp=0):
    noc=ui.query(u'total no of courses taken:', 'number')
    if not noc:
        ui.note(u'no course taken')
        return 1
    iter=0
    #tnu=0
    tcp=float(tcp)
    while iter<noc:
        while True:
            unit=ui.query(u'enter course unit:', 'number')
            if unit==0:
                ui.note(u'a value is required')
            elif not unit:
                if ui.query(u'exit GPCalc', 'query', None, u'Yes', u'No'):
                    return 1
            else:
                break
        tnu+=unit
        while True:
            score=ui.query(u'enter score or grade:', 'text')
            if not score:
                if ui.query(u'exit GPCalc', 'query', None, u'Yes', u'No'):
                    return 1
            elif score in (['%d'%x for x in range(70, 101)]+['A', 'a']):
                tcp+=5*unit
                break
            elif score in (['%d'%x for x in range(60, 70)]+['B', 'b']):
                tcp+=4*unit
                break
            elif score in (['%d'%x for x in range(50, 60)]+['C', 'c']):
                tcp+=3*unit
                break
            elif score in (['%d'%x for x in range(46, 50)]+['D', 'd']):
                tcp+=2*unit
                break
            elif score in (['%d'%x for x in range(40, 46)]+['E', 'e']):
                tcp+=unit
                break
            elif score in (['%d'%x for x in range(40)]+['F', 'f']):
                break
            else:
                ui.note(u'invalid score', 'error')
        
        iter+=1
    gpa=tcp/tnu
    if not ui.query(u'ur GPA is: %.3f'%gpa, 'query', None, u'ok', u'comments'):
        __comments(gpa)

def dynamic(tnu=0, tcp=0):
    ui.note(u'lets get started')
    #tnu=0
    tcp=float(tcp)
    while True:
        while True:
            unit=ui.query(u'enter course unit:', 'number')
            if unit==0:
                ui.note(u'a value is required')
            elif not unit:
                if ui.query(u'exit GPCalc', 'query', None, u'Yes', u'No'):
                    return 1
            else:
                break
        tnu+=unit
        while True:
            score=ui.query(u'enter score or grade:', 'text')
            if not score:
                if ui.query(u'exit GPCalc', 'query', None, u'Yes', u'No'):
                    return 1
            elif score in (['%d'%x for x in range(70, 101)]+['A', 'a']):
                tcp+=5*unit
                break
            elif score in (['%d'%x for x in range(60, 70)]+['B', 'b']):
                tcp+=4*unit
                break
            elif score in (['%d'%x for x in range(50, 60)]+['C', 'c']):
                tcp+=3*unit
                break
            elif score in (['%d'%x for x in range(46, 50)]+['D', 'd']):
                tcp+=2*unit
                break
            elif score in (['%d'%x for x in range(40, 46)]+['E', 'e']):
                tcp+=unit
                break
            elif score in (['%d'%x for x in range(40)]+['F', 'f']):
                break
            else:
                ui.note(u'invalid score', 'error')
        gpa=tcp/tnu
        if not ui.query(u'ur GPA is: %.3f'%gpa, 'query', None, u'continue', u'stop'):
            break
    __comments(gpa)

def __comments(GPA):
    if 5.0>=GPA>=4.5:
        ui.note(u'FIRST CLASS\nwhao! keep it up', 'info')
    elif 4.5>GPA>=3.5:
        ui.note(u'SECOND class, UPPER division\nur best is yet to come')
    elif 3.5>GPA>=2.5:
        ui.note(u'SECOND class, LOWER division\nu can do beta')
    elif 2.5>GPA>=1.5:
        ui.note(u'THIRD class\nput in more effort')
    elif 1.5>GPA>=1.0:
        ui.note(u'This is just a PASS result')
    elif 1.0>GPA>=0.0:
        ui.note(u'u are advised to WITHDRAW')
    else:
        ui.note(u'unrecognized gradepoint')
    return 1

def exit_key_handler():
    if ui.query(u'sure to exit', 'query', None, u'Yes', u'No'):
        e32.ao_sleep(0.2)
       # app_lock.signal()
        ui.app.set_exit()
    
def la():
    ui.note(u'ADIO Kingsley O\n(c) 2011 ADIKSonline\nadiksonline@gmail.com')
    
def ma():
    ui.note(u'VERSION: 1.3')
            
#ui.app.menu=[(u'Static Calc', static), (u'Dynamic Calc', dynamic), (u'Author', la), (u'Version', ma), (u'Exit', exit_key_handler)]

#ui.app.exit_key_handler=exit_key_handler
#app_lock.wait()