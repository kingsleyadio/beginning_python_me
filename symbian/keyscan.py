import e32
import appuifw as ui
from graphics import Image
lock=e32.Ao_lock()
b='None'
def rec(arg):
    global b
    red(1)
    a=unicode(arg['scancode'])
    b=unicode(arg['keycode'])
    can.text((10, 50), a, font='legend')
    can.text((35, 50), u'('+hex(int(a))+u')', font='symbol')
    can.text((10, 115), b, font='legend')
    can.text((45, 115), u'('+hex(int(b))+u')', font='symbol')
    if arg['type']==ui.EEventKeyUp:
        red(1)
        
def red(rect):
    global a
    if  b!='0':
        a=b
    can.blit(img)
    can.text((5, 165), u'last keycode is %s' %a, font='title')
    
img=Image.new((176, 144))
img.clear(0xb08080)
img.text((5, 20), u'scancode of pressed keys', font='title')
img.text((5, 67), u'keycode of pressed keys', font='title')
img=img.resize((176, 208))
can=ui.Canvas(redraw_callback=red, event_callback=rec)
ui.app.screen='full'
ui.app.body=can
ui.app.exit_key_handler=lock.signal
lock.wait()