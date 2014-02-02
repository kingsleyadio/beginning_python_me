import e32
import appuifw as ui
lock=e32.Ao_lock()
def newfile():
    name=ui.query(u'input filename', 'text', u'e:/new.txt')
    if not name: return 1
    if os.path.exists(name) and not ui.query(u'file exists! overwrite?', 'query'):
        return newfile()
    old=ui.app.body
    menu=ui.app.menu
    a=ui.Text()
    ui.app.body=a
    
    def save(name):
        new=file(name, 'w')
        new.write(a.get())
        new.close()
        ui.note(u'saved', 'conf')
        exit()
    def exit():
        if not os.path.exists(name) or len(file(name).read())!=len(a.get()):
            ask=ui.query(u'not saved, save now?', 'query')
            if ask: save(name)
        else:
            ui.app.body=old
            ui.app.menu=menu
            lock.signal()
    ui.app.menu=[(u'save', lambda:save(name)), (u'exit', exit)]
    lock.wait()
if __name__=='__main__':
    newfile()