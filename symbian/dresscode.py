import random, msgquery, e32, thread
import appuifw2 as ui
from graphics import Image

white=(255, 255, 255)
black=0
black_jean=10
grey=(128, 128, 128)
red=(255, 0, 0)
orange=(220, 150, 120)
green=(0, 255, 0)
wine=(100, 0, 0)
blue=255
blue_jean=150
brown=(100, 100, 70)
pink=(255, 128, 128)
yellow=(255, 200, 50)
striped=1

def viewit(top, tro):
    img=Image.new((176, 200))
    img.clear((180, 180, 180))
    img.polygon(((50, 15), (80, 15), (85, 8), (95, 8), (100, 15), (130, 15), (130, 40), (105, 35), (110, 70), (70, 70), (75, 35), (50, 40)), outline=0, fill=top)
    def tr():
        while 1:
            can.text((110, 55), u'short or long')
            e32.ao_sleep(0.5)
            hand(1)
            e32.ao_sleep(0.5)
    img.polygon((95, 8, 90, 18, 85, 8), (25, 25, 25))
    img.line((90, 18, 90, 70), (25, 25, 25))
    img.polygon(((105, 70), (120, 140), (95, 140), (90, 90), (85, 140), (60, 140), (75, 70)), outline=0, fill=tro)
    if tro==1:
        img.text((120, 100), u'striped...')
    def hand(rect):
        can.blit(img)
    lock=e32.Ao_lock()
    can=ui.Canvas(redraw_callback=hand)
    ui.app.screen='full'
    ui.app.body=can
    #thread.start_new_thread(tr, ())
    ui.app.exit_key_handler=lock.signal
    lock.wait()


def dresscode():
    global a, b
    topc=['red', 'yellow', 'green', 'blue', 'black', 'wine', 'brown', 'white', 'grey', 'pink', 'orange']
    troc=['white', 'black', 'striped', 'blue_jean', 'black_jean']
    a=random.choice(topc)
    b=random.choice(troc)
    #c=random.choice(color_list)
    result=u'TOP: %s\nTROUSERS: %s\n\nyou like it?' %(a, b)
    a, b=eval(a), eval(b)
    viewit(a, b)
    ans=msgquery.infopopup(result, u'Dress Code Result:', msgquery.OKRCancel)
    return ans
getting=dresscode()
while not getting:
    getting=dresscode()
else:
    ui.note(u'you made a wonderful selection !', 'conf')
    getting=0
    viewit(a, b)
