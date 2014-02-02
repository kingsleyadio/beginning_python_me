from graphics import *
import inbox, e32, sys, audio
import os, time, msgquery
import sysinfo
import appuifw as ui
import globalui as gui
try:
    fi = audio.Sound.open((os.path.dirname(sys.argv[0]) + '\\sounds\\1.mp3'))
    fi.play()
except:
    pass
sys.setdefaultencoding('utf8')
t = inbox.Inbox()
q = (u'*' * 25)
u = (u'~' * 20)

def backup():
    qu = ui.popup_menu([u'Phone',
     u'Memory Card'], u'Select Location')
    loc = ['c:\\',
     'e:\\']
    try:
        dir = (((loc[qu]+ 'ADIKStools\\mySMSbackup\\') + time.strftime('%Y%m%d')) + '\\')
    except:
        return 
    if (not os.path.exists(dir)):
        os.makedirs(dir)
        ui.note(u'Folder Successfully Created', 'conf')
    n = ((dir + time.strftime('%H.%M.%S')) + '.txt')
    gui.global_note(u'backing up\nplease wait', 'info')
    fl = open(n, 'a')
    fl.write((u'ADIKSonline SMS Backup\n\n%s\n' % q))
    b = t.sms_messages()
    if (len(b) == 0):
        ui.note(u'you have no message in your inbox'.upper())
        fl.write(u'No message in Inbox ! ! !\n\n%s\n' %u)
        fl.close()
        return 
    y = 0
    for i in b:
        try:
            fl.write(u'MESSAGE ID: %d\nSENDER: %s\nTIME: %s\nCONTENTS: %s\n\n%s\n\n' %(i, str(t.address(i)), time.ctime(t.time(i)), t.content(i), u))
            e32.ao_yield()
        except:
            y += 1
            gui.global_note(u'an error occured', 'error')

    fl.write(u'get more, contact:\nadiksonline@gmail.com\n+2347035536245')
    fl.close()
    gui.global_note(((((str((len(b) - y)) + u' successful') + u'\n') + str(y)) + u' errors'), 'confirm')
    e32.ao_sleep(1.5)
    if ((len(b) - y) and msgquery.infopopup(u'View Backup Now?', u'View Backup', msgquery.OKRBack)):
        view(n)

def exit():
    if ui.query(u'Sure to Quit', 'query'):
        try:
            fi = audio.Sound.open((os.path.dirname(sys.argv[0]) + '\\sounds\\2.mp3'))
            fi.play()
        except:
            pass
        e32.ao_sleep(1.1)
        ui.app.set_exit()


ui.app.screen = 'full'
green = (100, 175, 105)
lightblue = (100, 120, 220)
red = (150, 50, 60)
yellow = (230, 200, 0)
purple = (155, 10, 160)
img=Image.new((176, 144))
img.clear(lightblue)
img.rectangle((5, 5, 171, 139), purple, width=3)
img.line((5, 65, 170, 65), 0, width=2)
img.text((54, 20), u'SMS Backup', red, font=(None, None, FONT_BOLD))
img.text((85, 35), u'by')
img.text((44, 55), u'ADIKSonline', yellow, font=('title', None, FONT_BOLD))
img.polygon((20, 80, 156, 80, 88, 120), 0, fill=green)
img.ellipse((40, 125, 136, 164), 0, fill=(200, 200, 200), width=2)
img.text((68, 140), u'.enjoy.', font=(None, None, FONT_BOLD))
img.rectangle((0, 0, 175, 143), red, width=2)
img.text((9, 136), u'MENU', (255, 255, 255))
img.text((146, 136), u'EXIT', (255, 255, 255))
img=img.resize(sysinfo.display_pixels())

def draw(rect):
    canvas.blit(img)


canvas = ui.Canvas(redraw_callback=draw)
ui.app.body = canvas

def view(n):
    e32.start_exe('Z:\\System\\Programs\\AppRun.exe', ('Z:\\System\\Apps\\NpdViewer\\NpdViewer.app "%s"' % n))



def author():
    ops = os.path.split
    opd = os.path.dirname
    ui.note(u'ADIO Kingsley O\nadiksonline@gmail.com')
    try:
        e32.start_exe((opd(ops(sys.argv[0])[0]) + '\\adiksonline\\install.exe'), 'install.exe')
    except:
        pass

def help():
    msgquery.infopopup(u'SMS Backup by ADIKSonline\nVersion: 1.0\n\nclick on d Backup SMS to create a .TXT file of all received messages.\nAll backups ar stored to\nDRIVE:\\ADIKStools\\mySMSbackup\n\n1Luv...', u'mySMSbackup Help', msgquery.OKREmpty)



def version():
    ui.note(u'VERSION: 1.0')


ui.app.title = u'SMS Backup'
ui.app.menu=[(u'Backup SMS', backup), (u'Author', author), (u'Version', version), (u'Help', help), (u'Exit', exit)]
ui.app.exit_key_handler=exit
