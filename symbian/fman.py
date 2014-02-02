import os
import e32
import appuifw as ui

class Fman:
    def __init__(self):
        self.lock=e32.Ao_lock()
        self.dl=e32.drive_list()
        self.lb=ui.Listbox(self.dl, self.lbox)
        
    def lbox(self):
        ind=self.lb.current()
        return self.opn(self.dl[ind])
        
    def opn(self, dirname):
        self.dirname=obj=dirname
        ui.app.title=obj
        try:
            a=os.listdir(obj)
            b=[]
            c=[]
            for i in a:
                d=obj+os.sep+i
                if os.path.isfile(d):
                    c.append(d)
                else:
                    b.append(d)
            e=b+c
            g=[u'<<<']+map(os.path.basename, e)
            f=ui.selection_list(g, 1)
            if f==0:
                if obj in [u'C:', u'D:', u'E:', u'Z:']:
                    return self.run()
                else:
                    b=os.path.dirname(obj)
                    if b in [u'C:\\', u'D:\\', u'E:\\', u'Z:\\']:
                        self.opn(b[:2])
                        return
                    else:
                        self.opn(b)
                        return
            elif os.path.isfile(e[f-1]):
                try:
                    ui.Content_handler().open_standalone(e[f-1])
                    self.opn(obj)
                    return
                except TypeError:
                    ui.note(u'Exception>>\nunable to open file !', 'error')
                    self.opn(obj)
                    return
            else:
                self.opn(e[f-1])
                return
        except:
            ui.app.title=u'Root'
            pass
        
    def run(self):
        ui.app.body=self.lb
        ui.app.title=u'File Manager'
        self.others()
        self.lock.wait()
        
    def exit(self):
        self.lock.signal()
        
    def others(self):
        e32.ao_sleep(0.2)
        ui.app.menu=[(u'exit', self.exit)]
        ui.app.exit_key_handler=self.exit
            

if __name__=='__main__':
    Fman().run()