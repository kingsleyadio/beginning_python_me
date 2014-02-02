#whao, i cant believe this
#I m actually loving this code

import appuifw2 as ui

def static():
    noc=ui.query(u'total no of courses taken:', 'number')
    if not noc:
        ui.note(u'no course taken')
        return 1
    iter=0
    tnu=0
    tcp=float(0)
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
    GPA=tcp/tnu
    if not ui.query(u'ur GPA is: %.3f'%GPA, 'query', None, u'ok', u'comments'):
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
        else:
            ui.note(u'u are advised to WITHDRAW')
                

static()