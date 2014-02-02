import inbox, msys, sys
import e32, os, audio
from globalui import *

a=inbox.Inbox()
say=audio.Sound(os.path.dirname(sys.argv[0])+u'\\new.mp3')

def cb(recent):
    a=inbox.Inbox()
    tasks=[u'Leave Message', u'Mark as Read', u'Delete']
    try:
        msg=a.content(recent)
        if not msg:
            return
        say.play()
        global_msg_query(msg, u'From: '+a.address(recent))
        do=global_popup_menu(tasks)
        if do==0:
            a.set_unread(recent, 1)
            global_note(u'success', 'confirm')
        elif do==1:
            a.set_unread(recent, 0)
            global_note(u'success', 'confirm')
        else:
            a.delete(recent)
            global_note(u'message succesfully deleted', 'confirm')
    except: pass
    return
    
a.bind(cb)
global_note(u'Waiting for Messages')
e32.ao_sleep(1)
global_note(u'APP will continue running in background')
e32.ao_sleep(1)
#e32.start_server(sys.argv[0])

lock=e32.Ao_lock()
msys.set_system()
msys.send_bg()
msys.set_hidden()
lock.wait()