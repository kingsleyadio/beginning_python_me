import appuifw as ui
import e32
from graphics import *

lock=e32.Ao_lock()
old=ui.app.body
ui.app.screen='normal'

green=(10, 175, 25)
lightblue=(80, 100, 220)
red=(100, 5, 10)
purple=(155, 10, 160)
img=Image.new((176, 144))
img.clear(lightblue)
img.rectangle((5, 5, 171, 139), 0, width=3)
img.line((5, 65, 170, 65), 0, width=2)
img.text((54, 20), u'SMS Backup', red, font=(None, None, FONT_BOLD))
img.text((85, 35), u'by')
img.text((44, 55), u'ADIKSonline', 0, font=('title', None, FONT_BOLD))
img.polygon((20, 80, 156, 80, 88, 120), 0, fill=0xffffff)
img.ellipse((40, 125, 136, 164), purple, fill=green, width=2)
img.text((71, 140), u'.enjoy.')

def draw(rect):
    canvas.blit(img)
    
canvas=ui.Canvas(redraw_callback=draw)
ui.app.body=canvas
    
def exit():
    ui.app.body=old
    lock.signal()
    
ui.app.exit_key_handler=exit
lock.wait()
