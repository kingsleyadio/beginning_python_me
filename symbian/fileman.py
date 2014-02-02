import os, e32
import appuifw as ui

ui.app.screen='normal'

def root():
    ui.app.title=u'File Manager'
    try:
        drivelist=e32.drive_list()
        #drivelist=[u'C:', u'D:', u'E:', u'Z:']
        index=ui.selection_list(drivelist)
        opn(drivelist[index])
    except:
        a=ui.query(u'sure to quit?', 'query')
        if not a:
            root()
    
def opn(obj):
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
        #h=map(os.path.basename, g)
        #h=[os.path.basename(i) for i in g]
        f=ui.selection_list(g, 1)
        if f==0:
            if obj in [u'C:', u'D:', u'E:', u'Z:']:
                root()
                return
            else:
                b=os.path.dirname(obj)
                if b in [u'C:\\', u'D:\\', u'E:\\', u'Z:\\']:
                    opn(b[:2])
                    return
                else:
                    opn(b)
                    return
        elif os.path.isfile(e[f-1]):
            try:
                ui.Content_handler().open_standalone(e[f-1])
                opn(obj)
                return
            except TypeError:
                ui.note(u'Exception>>\nunable to open file !', 'error')
                opn(obj)
                return
        else:
            opn(e[f-1])
            return
    except:
        a=ui.query(u'sure to quit?', 'query')
        if not a:
            opn(obj)
            
if __name__=='__main__':
    root()
