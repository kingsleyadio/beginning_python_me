# filename: myJAReditor.py

import sys, os, unzip, zipfile
import walkfile
import powlite_fm, e32
import appuifw as ui
sys.setdefaultencoding('u8')

ui.app.screen='normal'
ui.app.title=u'myJAReditor'
ui.app.body=ui.Canvas()
lock=e32.Ao_lock()

import progressbartw
pbar = progressbartw.ProgressBarTW()
pbar.set_fonts(text_font = 'dense',text_color=0x0,percent_font = 'normal',percent_color=0xef0000)
pbar.set_colors(rect_color=0x0, back_color=0xffffff)
pbar.set_window_size((130,36))

def unjar(file):
    if unzip.unzip().extract(file, os.path.splitext(file)[0]):
        ui.note(u'JAR successfully unpacked', 'conf')
    else:
        ui.note(u'an error occured', 'error')
    
def do_jar(folder):
    wal=walkfile.Walk()
    li=wal.walk(folder)
    #pbar.begin_progress(len(li))
    al=zipfile.ZipFile(folder+os.path.basename(folder[:-1])+'.jar', 'w', zipfile.ZIP_DEFLATED)
    #j=1
    for i in li:
        #pbar.do_progress(j)
        #j+=1
        al.write(i)
        #e32.ao_yield()
    al.close()
    #pbar.end_progress()
    ui.note(u'JAR successfully created', 'conf')
    
def jar():
    return do_jar(powlite_fm.manager().AskUser(find='dir'))

def start():
    return unjar(powlite_fm.manager().AskUser(ext=['.jar', '.zip']))
    
def exit():
    lock.signal()
    
ui.app.menu=[(u'unjar', start), (u'jar', jar), (u'exit', exit)]
ui.app.exit_key_handler=exit
lock.wait()