import appuifw as ui
import e32

class TestinClass:
    def __init__(self):
        ui.app.exit_key_handler=self.exit
        self.lock=e32.Ao_lock()
        self.icon1=ui.Icon(u'z:\\system\\data\\avkon.mbm', 150, 151)
        self.icon2=ui.Icon(u'z:\\system\\data\\avkon.mbm', 130, 131)
        self.icon3=ui.Icon(u'z:\\system\\data\\avkon.mbm', 144, 145)
        self.icon4=ui.Icon(u'z:\\system\\data\\avkon.mbm', 124, 125)
        self.icon5=ui.Icon(u'z:\\system\\data\\avkon.mbm', 154, 155)
        self.entries=[(u'test1', u'am damn testin', self.icon1), (u'test2', u'thank God it worked', self.icon2), (u'test3', u'whaooo', self.icon3), (u'test4', u'ooooh shey', self.icon4), (u'test5', u'na God ooo', self.icon5)]
        
    def run(self):
        self.lb=ui.Listbox(self.entries, self.lbox)
        ui.app.body=self.lb
        ui.app.title=u'testin...'
        ui.app.screen='full'
        self.menu()
        self.lock.wait()
        
    def lbox(self):
        ind=self.lb.current()
        this=self.entries[ind][0]
        ui.note(u'%s was selected' %this, 'info')
        if this==self.entries[-1][0]:
            ui.note(u'%s is the last item in d list...' %this, 'conf')
            
    def exit(self):
        self.lock.signal()
            
    def menu(self):
        ui.app.menu=[(u'help', lambda: None), (u'see', ((u'now', self.lbox),)), (u'exit', self.exit)]

if __name__=='__main__':
    TestinClass().run()