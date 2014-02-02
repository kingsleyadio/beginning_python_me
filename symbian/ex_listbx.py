import appuifw as ui
import e32

class MyApp:
    def __init__(self):
        self.lock=e32.Ao_lock()
        ui.app.title=u'My App'
        self.lb=ui.Listbox([u'item 1', u'item 2'], self.lb_callback)
        self.activate()
        
    def activate(self):
        ui.app.menu=[(u'help', lambda: None), (u'exit', self.key_exit), ]
        ui.app.exit_key_handler=self.key_exit
        ui.app.body=self.lb
        
    def key_exit(self):
        self.lock.signal()
        
    def lb_callback(self):
        i=self.lb.current()
        ui.note(u'list callback selection: %s' %i, 'info')
        
    def run(self):
        self.lock.wait()
        
if __name__=='__main__':
    global myapp
    e32.ao_yield()
    myapp=MyApp()
    myapp.run()