import os, sys, e32
import appuifw as ui
#from key_codes import *

LIBPATH='\\system\\libs'
for i in e32.drive_list():
    if os.path.isfile(i+LIBPATH+'\\usefman.py'):
        LIBPATH=i+LIBPATH+'\\'
        break

class useFman:
    def __init__(self):
        self.LIBPATH=LIBPATH
        self.lock=e32.Ao_lock()
        self.drive_icon=ui.Icon(self.LIBPATH+u'myicons.mbm', 0, 1)
        self.folder_icon=ui.Icon(self.LIBPATH+u'myicons.mbm', 2, 3)
        self.wait_icon=ui.Icon(self.LIBPATH+u'myicons.mbm', 6, 7)
        self.empty_icon=ui.Icon(self.LIBPATH+u'myicons.mbm', 8, 9)
        self.file_icon=ui.Icon(self.LIBPATH+u'myicons.mbm', 36, 37)
        e32.ao_yield()
        entry=[(u'C:', self.drive_icon)]
        self.lb=ui.Listbox(entry, self.ret)
        self.old_body=ui.app.body
        self.old_menu=ui.app.menu
        self.old_exit=ui.app.exit_key_handler
        self.old_screen=ui.app.screen
        self.old_title=ui.app.title
        self.CH=-1
    
    def AskUser(self, path=None, path_item=None, type='file', exts=[]):
        self.type=type.lower()
        self.exts=map(str.lower, exts)
        if self.type not in ('file', 'folder'):
            self.type='file'
        ui.app.screen='normal'
        ui.app.exit_key_handler=self.exit
        e32.ao_yield()
        ui.app.menu=[(u'Select', self.ret), 
            (u'Open', self.rightArrow), 
            (u'Back', self.leftArrow), 
            (u'Edit Filter', ((u'Filter', lambda: self.editFilter('f')), (u'Show All', self.editFilter))), 
            (u'Quit', self.exit)]
        ui.app.title=u'Choose '+self.type
        e32.ao_yield()
        self._run(path, path_item)
        ui.app.title=self.old_title
        ui.app.body=self.old_body
        ui.app.menu=self.old_menu
        ui.app.exit_key_handler=self.old_exit
        ui.app.screen=self.old_screen
        ui.app.focus=None
        if self.CH:
            return self.cur
        else:
            return None
    
    def _run(self, path=None, path_item=None):
        ui.app.focus=self.refresh
        self.CH=0
        if path!=None:
            path=unicode(os.path.normpath(path))
            if os.path.exists(path) or os.path.basename(path)=='(empty)':
                path=path
            else:
                ui.note(u'path does not exist', 'error')
                return self._run()
        e32.ao_yield()
        self.all=[]
        self.allist=[]
        if path==None:
            running=1
            while running:
                self.lb.set_list([(u'please wait...', self.wait_icon), ])
                e32.ao_yield()
                self.allist+=[(i, self.drive_icon) for i in e32.drive_list()]
                e32.ao_yield()
                self.all=self.allist
                if path_item!=None:
                    try: select=e32.drive_list().index(path_item)
                    except: select=0
                else: select=0
                running=0
            return self.__execute(self.allist, select)
        elif os.path.isdir(path):
            running=1
            while running:
                self.lb.set_list([(u'please wait...', self.wait_icon), ])
                e32.ao_yield()
                a=os.listdir(path)
                b=[]
                c=[]
                for i in a:
                    d=path+os.sep+i
                    if os.path.isdir(d):
                        b.append((d, self.folder_icon))
                        e32.ao_yield()
                    else:
                        ext=os.path.splitext(d)[1][1:].lower()
                        if not self.exts or ext in self.exts:
                            c.append((d, self.file_icon))
                            e32.ao_yield()
                if self.type=='folder':
                    self.all=b
                else:
                    self.all=b+c
                if len(self.all)==0:
                    self.all.append((path+'\\(empty)', self.empty_icon))
                self.allist=[(os.path.basename(k), v) for k, v in self.all]
                e32.ao_yield()
                al=[k for k, v in self.allist]
                if path_item != None:
                    try: select=al.index(path_item)
                    except: select=0
                else: select=0
                running=0
            return self.__execute(self.allist, select)
        elif os.path.isfile(path):
            self.CH=1
            self.cur=path
            self.lock.signal()
            return
        else:
            if not os.path.exists(path):
                dir=os.path.dirname(path)
                if dir.endswith('\\'):
                    dir=dir[:-1]
                return self._run(dir, path_item)
                    
    def __execute(self, list, cur):
        self.type=self.type
        self.lb.set_list(list, cur)
        e32.ao_yield()
        ui.app.body=self.lb
        self.lb.bind(63495, self.leftArrow)
        self.lb.bind(63496, self.rightArrow)
        self.lb.bind(42, lambda:self.scroll('u'))
        self.lb.bind(35, self.scroll)
        try: self.lock.wait()
        except: pass
        
    def __previous(self, obj):
        par=os.path.dirname(obj)
        if par.endswith('\\'):
            par=par[:-1]
        pre=os.path.dirname(par)
        if pre.endswith('\\'):
            pre=pre[:-1]
        
        if obj.endswith(':'):
            return 1
        elif par.endswith(':'):
            return self._run(path_item=par)
        else:
            return self._run(pre, os.path.basename(par))
            
    def rightArrow(self):
        ind=self.lb.current()
        current_item=self.all[ind][0]
        return self._run(path=current_item)
        
    def leftArrow(self):
        ind=self.lb.current()
        current_item=self.all[ind][0]
        return self.__previous(current_item)
        
    def scroll(self, mode='d'):
        ind=self.lb.current()
        tot=len(self.allist)
        down=ind+5
        up=ind-5
        if mode=='d' and down<tot:
            self.lb.set_list(self.allist, down)
            e32.ao_yield()
        elif mode=='d' and down>=tot:
            self.lb.set_list(self.allist, tot-1)
            e32.ao_yield()
        elif mode=='u' and up>=0:
            self.lb.set_list(self.allist, up)
            e32.ao_yield()
        elif mode=='u' and up<0:
            self.lb.set_list(self.allist, 0)
            e32.ao_yield()
        else:
            return 1
            
    def refresh(self, var):
        try:
            if var:
                ind=self.lb.current()
                obj=self.all[ind][0]
                base=os.path.basename(obj)
                path=os.path.dirname(obj)
                if path.endswith('\\'):
                    path=path[:-1]
                if obj.endswith(':'):
                    path, base='None', obj
                e32.ao_yield()
                return self._run(path, base)
        except: return 1
    
    def editFilter(self, mode='s'):
        ind=self.lb.current()
        cur=self.all[ind][0]
        if cur.endswith(':'):
            return 1
        path=os.path.dirname(cur)
        if path.endswith('\\'):
            path=path[:-1]
        if mode=='f':
            if len(os.listdir(path))==len(self.all):
                self.hide=self.all
            key=ui.query(u'enter keyword:', 'text')
            if not key: return 1
            if key==u'*':
                self.all=self.hide
            else:
                self.all=self.hide
                result=filter(lambda k: unicode.startswith(os.path.basename(k[0]).lower(), key.lower()), self.all)
                if len(result)==0:
                    result.append((path+'\\(empty)', self.empty_icon))
                self.all=result
            self.allist=[(os.path.basename(k), v) for k, v in self.all]
            self.lb.set_list(self.allist)
        else:
            return self.refresh(1)
    
    def ret(self):
        self.CH=1
        ind=self.lb.current()
        self.cur=self.all[ind][0]
        if (self.type=='file' and os.path.isfile(self.cur)) or (self.type=='folder' and os.path.isdir(self.cur)):
            self.lock.signal()
            return
        
    def exit(self):
        self.lock.signal()
        self.CH=0
        return
        
if __name__=='__main__':
    a=useFman().AskUser()
    print a
    ui.note(u'Selected:\n'+unicode(a), 'conf')
    