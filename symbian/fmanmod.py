# -*- coding: utf-8 -*-
import os, socket, sysinfo
sys=os.sys
default=sys.getdefaultencoding()
sys.setdefaultencoding('utf8')
e32=socket.e32
import time, miso
import envy, walkfile
import appuifw as ui
from usefman import useFman
from key_codes import *
from msgquery import *
import shutil1 as sh

class Fman(object):
    def __init__(self):
        self.pre=os.path.dirname(ui.app.full_name())+'\\'
        self.lock=e32.Ao_lock()
        try:
            ini=file(self.pre+'ini.ini').read().split('\n')
            self.screen, self.system, self.lastpath, self.font_type, self.color_type, self.pw, self.pat, self.cur=ini[0], int(ini[1]), int(ini[2]), ini[3], ini[4], ini[5].decode('base64'), ini[6], ini[7]
            e32.ao_yield()
            if len(self.pw)!=0:
                p=ui.query(u'enter password:', 'code')
                if p != self.pw or not p:
                    ui.note(u'password error', 'error')
                    os.abort()
        except:
            self.screen, self.system, self.lastpath, self.font_type, self.color_type, self.pw, self.pat, self.cur='normal', 0, 0, u'Normal', u'Blue', u'', 'None', 'None'
            ini=file(self.pre+'ini.ini', 'w')
            ini.write('normal\n0\n0\nNormal\nBlue\n\nNone\nNone')
            e32.ao_yield()
            ini.close()
        self.drive_icon=ui.Icon(self.pre+u'myicons.mbm', 0, 1)
        self.folder_icon=ui.Icon(self.pre+u'myicons.mbm', 2, 3)
        self.py=('py', 'pyc', 'pyd', 'dll', 'cc', 'c', 'cpp', 'h')
        self.py_icon=ui.Icon(self.pre+u'myicons.mbm', 4, 5)
        self.wait_icon=ui.Icon(self.pre+u'myicons.mbm', 6, 7)
        self.empty_icon=ui.Icon(self.pre+u'myicons.mbm', 8, 9)
        self.zip=('zip', 'rar', 'tar', 'bz2', '7z', 'gz', 'tgz')
        self.zip_icon=ui.Icon(self.pre+u'myicons.mbm', 10, 11)
        self.img=('jpg', 'jpeg', 'gif', 'png', 'bmp')
        self.img_icon=ui.Icon(self.pre+u'myicons.mbm', 18, 19)
        self.vid=('3gp', 'avi', 'mp4', 'mkv')
        self.vid_icon=ui.Icon(self.pre+u'myicons.mbm', 20, 21)
        self.music=('mp3', 'mid', 'midi', 'aac', 'ogg', 'wma', 'amr', 'wav', 'm4a')
        self.music_icon=ui.Icon(self.pre+u'myicons.mbm', 22, 23)
        self.exe=('exe', 'app')
        self.exe_icon=ui.Icon(self.pre+u'myicons.mbm', 24, 25)
        self.pdf=('pdf',)
        self.pdf_icon=ui.Icon(self.pre+u'myicons.mbm', 28, 29)
        self.web=('html', 'xhtml', 'htm', 'xml', 'wml', 'js', 'php', 'asp', 'aspx')
        self.web_icon=ui.Icon(self.pre+u'myicons.mbm', 14, 15)
        self.doc=('doc', 'docx', 'xls', 'mobi', 'prc')
        self.doc_icon=ui.Icon(self.pre+u'myicons.mbm', 12, 13)
        self.text=('txt', 'css', 'lrc')
        self.text_icon=ui.Icon(self.pre+u'myicons.mbm', 32, 33)
        self.other_icon=ui.Icon(self.pre+u'myicons.mbm', 34, 35)
        self.install=('sis', 'sisx', 'jar', 'jad')
        self.install_icon=ui.Icon(self.pre+u'myicons.mbm', 36, 37)
        entry=[(u'C:', self.drive_icon)]
        self.fonts={u'Small':(u'LatinPlain12', 10), 
            u'Normal':(u'Alp13', 12),
            u'Large':(u'Alp17', 15)}
        self.colors={u'Red':0xaa0000, 
            u'Green':0x00aa00, 
            u'Blue':0x0000aa, 
            u'Black':0x0,
            u'Purple':0xaa00aa, 
            u'Grey':0x808080}
        self.dic={self.music: self.music_icon, 
            self.img: self.img_icon, 
            self.zip: self.zip_icon, 
            self.py: self.py_icon, 
            self.pdf: self.pdf_icon, 
            self.vid: self.vid_icon, 
            self.install: self.install_icon, 
            self.exe: self.exe_icon, 
            self.web: self.web_icon, 
            self.doc: self.doc_icon, 
            self.text: self.text_icon}
        e32.ao_yield()
        self.lb=ui.Listbox(entry, self.rightArrow)
        self.count=0
        ui.app.screen=self.screen
        envy.set_app_system(self.system)
        self.font=self.fonts[self.font_type]
        self.color=self.colors[self.color_type]
        
    def run(self, path='None', path_item='None'):
        if not self.count:
            path, path_item=self.pat, self.cur
            self.count=1
        ui.app.focus=self.refresh
        ui.app.exit_key_handler=self.exit
        ui.app.menu=[
            (u'File', ((u'Open', self.rightArrow), (u'Back', self.leftArrow), (u'Goto Root', self.run), (u'Edit', self.fileEdit), (u'Details [5]', self.__info), (u'Attributes [6]', self.attributes), (u'Rename [7]', self.rename), (u'Delete [C]', self.delete), (u'New Folder [9]', self.newdir), (u'New File', self.newfile))), 
            (u'Find', self.findfile), 
            (u'Edit Filter', ((u'Filter', lambda: self.editFilter('f')), (u'Show All', self.editFilter))), 
            (u'Edit', ((u'Copy [1]', self.do_copy), (u'Move [2]', self.do_move))),
            (u'Send by', ((u'Bluetooth [send]', self.bt_send), )), 
            (u'Tools', ((u'Configurations [0]', self.settings), (u'Compress RAM [4]', self.compress), (u'Phone Info', self.devInfo), (u'Network Info', self.netInfo), (u'Restart Device', self.shutdown), (u'Shutdown Device', lambda: self.shutdown('s')), (u'Tasks [8]', self.tasks), (u'About', self.about))), 
            (u'Exit', self.exit)]
        if path!='None':
            path=unicode(os.path.normpath(path))
            if os.path.exists(path) or os.path.basename(path)=='(empty)':
                path=path
            else:
                ui.note(u'path does not exist', 'error')
                return self.run()
        self.all=[]
        self.allist=[]
        if path=='None':
            running=1
            while running:
                self.lb.set_list([(u'please wait...', self.wait_icon), ])
                ui.app.title=u'myX-plorer'
                self.allist+=[(i, self.drive_icon) for i in e32.drive_list()]
                e32.ao_yield()
                self.all=self.allist
                if path_item!='None':
                    try: select=e32.drive_list().index(path_item)
                    except: select=0
                else: select=0
                running=0
            return self.__execute(self.allist, select)
        elif os.path.isdir(path):
            running=1
            while running:
                self.lb.set_list([(u'please wait...', self.wait_icon), ])
                if path.endswith(':'): ui.app.title=path
                else: ui.app.title=os.path.basename(path)
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
                        for i in self.dic.keys():
                            if ext in i:
                                c.append((d, self.dic[i]))
                                break
                        else:
                            c.append((d, self.other_icon))
                        e32.ao_yield()
                self.all=b+c
                if len(self.all)==0:
                    self.all.append((path+'\\(empty)', self.empty_icon))
                self.allist=[(os.path.basename(k), v) for k, v in self.all]
                e32.ao_yield()
                al=[k for k, v in self.allist]
                if path_item != 'None':
                    try: select=al.index(path_item)
                    except: select=0
                else: select=0
                running=0
            return self.__execute(self.allist, select)
        elif os.path.isfile(path):
            #self.lb.bind(EKeyRightArrow, None)
            running=1
            while running:
                self.lb.set_list([(u'please wait...', self.wait_icon), ])
                ext=os.path.splitext(path)[1][1:].lower()
                exts=self.img+self.music+self.install
                openwith=u'z:\\system\\programs\\apprun.exe'
                try:
                    loc=e32.Ao_lock()
                    if ext in exts:
                        ui.Content_handler(loc.signal).open(path)
                        ui.app.title=os.path.basename(path)
                        loc.wait()
                    elif ext in self.exe:
                        if ext=='app':
                            e32.start_exe(openwith, path)
                        else:
                            e32.start_exe(path, path)
                    elif ext in self.text:
                        self.all=[(path, self.text_icon)]
                        self.lb.set_list([(os.path.basename(k), v) for k, v in self.all])
                        return self.fileEdit()
                    elif ext in self.web:
                        newpath=path.replace('\\', '/')
                        newpath=newpath.replace(' ', '%20')
                        e32.start_exe(openwith, u'z:\\system\\apps\\browser\\browser.app "file://%s"' %newpath)
                    else:
                        ui.Content_handler().open_standalone(path)
                except:
                    ui.note(u'No Viewer Found', 'error')
                dir=os.path.dirname(path)
                if dir.endswith('\\'):
                    dir=dir[:-1]
                cur=os.path.basename(path)
                running=0
            return self.run(dir, cur)
        else:
            if not os.path.exists(path):
                dir=os.path.dirname(path)
                if dir.endswith('\\'):
                    dir=dir[:-1]
                return self.run(dir, path_item) 
                    
    def __execute(self, list, cur=0):
        self.lb.set_list(list, cur)
        ui.app.body=self.lb
        e32.ao_yield()
        self.lb.bind(EKeyLeftArrow, self.leftArrow)
        self.lb.bind(EKeyRightArrow, self.rightArrow)
        self.lb.bind(EKey5, self.__info)
        self.lb.bind(EKeyBackspace, self.delete)
        self.lb.bind(EKeyStar, lambda:self.scroll('u'))
        self.lb.bind(EKeyHash, self.scroll)
        self.lb.bind(EKey0, self.settings)
        self.lb.bind(EKey1, self.do_copy)
        self.lb.bind(EKey2, self.do_move)
        self.lb.bind(EKey7, self.rename)
        self.lb.bind(EKey9, self.newdir)
        self.lb.bind(EKeyYes, self.bt_send)
        self.lb.bind(EKey8, self.tasks)
        self.lb.bind(EKey6, self.attributes)
        self.lb.bind(EKey4, self.compress)
        try:self.lock.wait()
        except:pass
        
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
            return self.run(path_item=par)
        else:
            return self.run(pre, os.path.basename(par))    
    
    def __info(self):
        ind=self.lb.current()
        obj=self.all[ind][0]
        info=os.stat(obj)
        seq=time.localtime(info.st_mtime)
        a=[(u'FullName', obj), (u'Last Modified', time.strftime('%d-%m-%Y at %H:%M:%S', seq))]
        if os.path.isfile(obj):
            size=info.st_size
            if size>1024*1024*1024:
                size='%0.2f GB (%d bytes)' %(size/1024/1024/1024., size)
            elif size>1024*1024:
                size='%0.2f MB (%d bytes)' %(size/1024/1024., size)
            elif size>1024:
                size='%0.2f KB (%d bytes)' %(size/1024., size)
            else:
                size=str(size)+' Byte(s)'
            a.append((u'Size', size))
        if obj.endswith(u':'):
            size=sysinfo.free_drivespace()[obj]
            if size>1024*1024*1024:
                size='%0.2f GB (%d bytes)' %(size/1024/1024/1024., size)
            elif size>1024*1024:
                size='%0.2f MB (%d bytes)' %(size/1024/1024., size)
            elif size>1024:
                size='%0.2f KB (%d bytes)' %(size/1024., size)
            else:
                size=str(size)+' Byte(s)'
            a.append((u'FreeSpace', size))
        mod=info[0]
        if mod&128:
            mode=u'Read and Write'
        else:
            mode=u'Read Only'
        a.append((u'Access Mode', mode))
        note="\n".join(["%s: %s" % (k, v) for k, v in a])
        if obj.endswith(':'):
            base=obj+u' Drive'
        else:
            base=os.path.basename(obj)
        return infopopup(note, base, OKREmpty)
    
    def attributes(self):
        ind=self.lb.current()
        cur=self.all[ind][0]
        if cur.endswith(':'):
            base=cur
        else:
            base=os.path.basename(cur)
        old=ui.app.title
        ui.app.title=base
        mod=os.stat(cur)[0]
        if mod&128:
            mode=u'Read and Write'
        else:
            mode=u'Read Only'
        modelist=[u'Read and Write', u'Read Only']
        data=[
            (u'Access mode', 'combo', (modelist, modelist.index(mode))),
            ]
        flag=ui.FFormEditModeOnly|ui.FFormDoubleSpaced
        def save(args):
            ui.note(u'processing')
        form=ui.Form(data, flag)
        form.save_hook=save
        form.execute()
        new_mode=modelist[form[0][2][1]]
        try:
            if new_mode==u'Read Only':
                os.chmod(cur, 0)
            else:
                os.chmod(cur, ~0)
            e32.ao_yield()
            #ui.note(u'saved', 'conf')
        except: pass
            #ui.note(u'ACCESS DENIED', 'error')
        ui.app.title=old
        return 1
    
    def findfile(self):
        ind=self.lb.current()
        obj=self.all[ind][0]
        if os.path.isfile(obj): return 1
        name=ui.query(u'enter partname of file', 'text')
        if not name: return 1
        base=os.path.basename(obj)
        path=os.path.dirname(obj)
        if obj.endswith(':'):
            path, base='None', obj
        if path.endswith('\\'):
            path=path[:-1]
        def scroll(mode='d'):
            ind=lbx.current()
            tot=len(allist)
            down=ind+5
            up=ind-5
            if mode=='d' and down<tot:
                lbx.set_list(allist, down)
            elif mode=='d' and down>=tot:
                lbx.set_list(allist, tot-1)
            elif mode=='u' and up>=0:
                lbx.set_list(allist, up)
            elif mode=='u' and up<0:
                lbx.set_list(allist, 0)
            else:
                return 1
        def lb_ret():
            index=lbx.current()
            cu=all[index][0]
            pa=os.path.dirname(cu)
            if pa.endswith('\\'):
                pa=pa[:-1]
            ba=os.path.basename(cu)
            return self.run(pa, ba)
        if os.path.isdir(obj):
            running=1
            lbx=ui.Listbox([(u'please wait...', self.wait_icon), ], lb_ret)
            ui.app.body=lbx
            ui.app.focus=None
            lbx.bind(EKeyStar, lambda: scroll('u'))
            lbx.bind(EKeyHash, scroll)
            while running:
                lbx.set_list([(u'please wait...', self.wait_icon), ])
                e32.ao_yield()
                c=[]
                found=walkfile.Walk().walk(obj+'\\')
                e32.ao_yield()
                for j in found:
                    ext=os.path.splitext(j)[1][1:].lower()
                    for i in self.dic.keys():
                        if not os.path.basename(j).lower().count(name.lower()):
                            break
                        if ext in i:
                            c.append((j, self.dic[i]))
                            break
                    else:
                        c.append((j, self.other_icon))
                    e32.ao_yield()
                running=0
            all=c
            if len(all)==0:
                all.append((obj+'\\(empty)', self.empty_icon))
            allist=[(os.path.basename(k), v) for k, v in all]
            e32.ao_yield()
            ui.app.title=u'Search Result'
            lbx.set_list(allist)
        else:
            return 1
        def back():
            return self.run(path, base)
        ui.app.menu=[(u'Goto File', lb_ret), (u'Back', back)]
        ui.app.exit_key_handler=back
    
    def rename(self):
        ind=self.lb.current()
        obj=self.all[ind][0]
        base=os.path.basename(obj)
        dir=os.path.dirname(obj)
        if dir.endswith('\\'):
            dir=dir[:-1]
        if dir.lower().startswith('z:'):
            ui.note(u'access denied'.upper(), 'error')
            return 1
        if obj.endswith(':') or not os.path.exists(obj):
            return 1
        else:
            new=ui.query(u'Enter new name:', 'text', os.path.basename(obj))
            if not new: return 1
            running=1
            while running:
                self.lb.set_list([(u'please wait...', self.wait_icon), ])
                e32.ao_yield()
                try:
                    if dir==self.pre[:-1]:
                        os.rename()
                    os.rename(obj, dir+'\\'+new)
                    return self.run(dir, new)
                except:
                    ui.note(u'can\'t rename', 'error')
                    return self.run(dir, base)
    
    def delete(self):
        ind=self.lb.current()
        obj=self.all[ind][0]
        base=os.path.basename(obj)
        dir=os.path.dirname(obj)
        if dir.endswith('\\'):
            dir=dir[:-1]
        if obj.endswith(':') or not os.path.exists(obj):
            return 1
        elif dir.lower().startswith('z:'):
            ui.note(u'access denied'.upper(), 'error')
            return 1
        else:
            if not ui.query(u'Delete?', 'query'): return 1
            running=1
            while running:
                self.lb.set_list([(u'please wait...', self.wait_icon), ])
                e32.ao_yield()
                try:
                    if dir==self.pre[:-1]:
                        os.remove()
                    if os.path.isfile(obj):
                        if not os.stat(obj)[0]&128:
                            if ui.query(u'delete Read-Only file?', 'query'):
                                os.chmod(obj, ~0)
                                os.remove(obj)
                            else: return self.run(dir, base)
                        else: os.remove(obj)
                    else:
                        try:
                            if not os.stat(obj)[0]&128:
                                if ui.query(u'delete Read-Only folder?', 'query'):
                                    os.chmod(obj, ~0)
                                    os.rmdir(obj)
                                else: return self.run(dir, base)
                            else: os.rmdir(obj)
                        except:
                            ui.query(u'Folder not empty and might contain Read-Only files, Delete?', 'query')
                            self.__deleteall(obj)
                    e32.ao_yield()
                    ui.note(u'Deleted', 'conf')
                except:
                    ui.note(u'can\'t delete', 'error')
                    return self.run(dir, base)
                running=0
            if ind==0:
                new=os.path.basename(self.all[ind][0])
            else:
                new=os.path.basename(self.all[ind-1][0])
            return self.run(dir, new)
    
    def __deleteall(self, dir):
        it=dir
        cont=1
        while cont:
            a=os.listdir(dir)
            for i in a:
                obj=dir+'\\'+i
                os.chmod(obj, ~0)
                if os.path.isfile(obj) or len(os.listdir(obj))==0:
                    try: os.remove(obj)
                    except: os.rmdir(obj)
                else:
                    self.__deleteall(obj)
                e32.ao_yield()
            if len(os.listdir(it))==0:
                os.chmod(it, ~0)
                os.rmdir(it)
                cont=0
        return 1
    
    def newdir(self):
        ind=self.lb.current()
        obj=self.all[ind][0]
        dir=os.path.dirname(obj)
        if dir.endswith('\\'):
            dir=dir[:-1]
        if dir.lower().startswith('z:'):
            ui.note(u'access denied'.upper(), 'error')
            return 1
        base=os.path.basename(obj)
        if obj.endswith(':'):
            return 1
        else:
            new=ui.query(u'Folder Name:', 'text', u'New Folder')
            if not new: return 1
            running=1
            full=dir+'\\'+new
            if os.path.exists(full):
                ui.note(u'Already Exists', 'error')
                return self.newdir()
            while running:
                self.lb.set_list([(u'please wait...', self.wait_icon), ])
                e32.ao_yield()
                try:
                    os.mkdir(full)
                    return self.run(dir, new)
                except:
                    ui.note(u'cant create folder', 'error')
                    return self.run(dir, base)
    
    def newfile(self):
        ind=self.lb.current()
        obj=self.all[ind][0]
        base=os.path.basename(obj)
        path=os.path.dirname(obj)
        if obj.endswith(':'): return 1
        if path.lower().startswith('z:'):
            ui.note(u'access denied'.upper(), 'error')
            return 1
        e32.ao_yield()
        new=ui.query(u'input filename', 'text', u'new.txt')
        if not new: return 1
        if path.endswith('\\'):
            path=path[:-1]
        name=path+'\\'+new
        if os.path.isdir(name) or new.count(':'):
            ui.note(u'cant create file', 'error')
            return self.newfile()
        elif os.path.exists(name) and not ui.query(u'file exists! overwrite?', 'query'):
            return self.newfile()
        try:
            nu=file(name, 'w')
            nu.close()
            os.remove(name)
            e32.ao_yield()
        except:
            ui.note(u'cant create file', 'error')
            return self.run(path, base)
        a=ui.Text()
        a.color=self.color
        a.font=self.font
        ui.app.body=a
        ui.app.focus=None
        ui.app.screen=self.screen
        ui.app.title=new
    
        def save(name, encode='utf-8'):
            if encode=='utf-16':
                text=a.get().encode('utf-16')
            else:
                text=a.get()
            e32.ao_yield()
            new=file(name, 'w')
            new.write(text)
            new.close()
            ui.note(u'saved', 'conf')
            exit(encode)
        def exit(content='utf-8'):
            me=a.get()
            if content=='utf-16':
                me=me.encode('utf-16')
            e32.ao_yield()
            if not os.path.exists(name) or file(name).read() != me:
                ask=ui.query(u'not saved, save now?', 'query')
                if ask: save(name, content)
                else: self.run(path, base)
            else:
                self.run(path, new)
        ui.app.exit_key_handler=exit
        ui.app.menu=[(u'save', ((u'utf-8', lambda:save(name)), (u'utf-16', lambda:save(name, 'utf-16')))), (u'back', exit)]
    
    def fileEdit(self):
        global content
        ind=self.lb.current()
        current_item=self.all[ind][0]
        path=os.path.dirname(current_item)
        obj=os.path.basename(current_item)
        if path.endswith('\\'):
            path=path[:-1]
        if os.path.isdir(current_item) or not os.path.exists(current_item):
            return 1
        e32.ao_yield()
        running=1
        while running:
            self.lb.set_list([(u'please wait...', self.wait_icon), ])
            e32.ao_yield()
            a=ui.Text()
            a.font=self.font
            a.color=self.color
            content=file(current_item).read()
            e32.ao_yield()
            try:
                a.set(unicode(content))
                a.set_pos(0)
                e32.ao_yield()
                ui.app.body=a
                ui.app.focus=None
                ui.app.screen=self.screen
                ui.app.title=obj
            except UnicodeError:
                if content.startswith('\xff\xfe'):
                    a.set(content)
                    a.set_pos(0)
                    e32.ao_yield()
                    ui.app.body=a
                    ui.app.focus=None
                    ui.app.screen=self.screen
                    ui.app.title=obj
                else:
                    ui.note(u'unable to open', 'error')
                    return self.run(path, obj)
            except:
                ui.note(u'unable to open', 'error')
                return self.run(path, obj)
            running=0
        def save():
            if path.lower().startswith('z:') or not os.stat(current_item)[0]&128:
                ui.note(u'access denied'.upper()+u'\nfile is Read-Only', 'error')
                return self.run(path, obj)
            new=file(current_item, 'w')
            me=a.get()
            e32.ao_yield()
            if content.startswith('\xff\xfe'):
                me=me.encode('utf-16')
            new.write(me)
            new.close()
            ui.note(u'saved', 'conf')
            exit()
        def exit():
            if path.lower().startswith('z:'):
                return self.run(path, obj)
            me=a.get()
            e32.ao_yield()
            if content.startswith('\xff\xfe'):
                me=me.encode('utf-16')
            we=file(current_item).read()
            e32.ao_yield()
            if not os.path.exists(current_item) or we != me:
                ask=ui.query(u'not saved, save now?', 'query')
                if ask: save()
                else:
                    self.run(path, obj)
            else:
                self.run(path, obj)
        ui.app.exit_key_handler=exit
        ui.app.menu=[(u'save', save), (u'exit', exit)]
    
    def bt_send(self):
        ind=self.lb.current()
        current_item=self.all[ind][0]
        obj=os.path.basename(current_item)
        path=os.path.dirname(current_item)
        if os.path.isdir(current_item) or not os.path.exists(current_item):
            return 1
        sock1=socket.bt_obex_discover
        sock2=socket.bt_obex_send_file
        try:
            device=sock1()
            add=device[0]
            ch=device[1].values()[0]
            ui.note(u'sending....')
            try:
                sock2(add, ch, current_item)
            except:
                ui.note(u'unable to send', 'error')
                return 1
            e32.ao_yield()
            ui.note(u'File Sent', 'conf')
        except:
            return 1
    
    def do_copy(self):
        ind=self.lb.current()
        src=self.all[ind][0]
        base=os.path.basename(src)
        if src.endswith(':') or not os.path.exists(src):
            return 1
        path=os.path.dirname(src)
        if path.endswith('\\'):
            path=path[:-1]
        ui.note(u'select destination')
        running=1
        while running:
            self.lb.set_list([(u'please wait...', self.wait_icon), ])
            #e32.ao_yield()
            dst=useFman().AskUser(path, base, type='folder')
            if dst==None:
                return self.run(path, base)
            dst=dst+'\\'+base
            if dst.lower().startswith('z:'):
                ui.note(u'ACCESS DENIED', 'error')
                return self.run(path, base)
            try:
                if os.path.isfile(src):
                    if os.path.exists(dst) and not os.stat(dst)[0]&128:
                        if ui.query(u'replace Read-Only file?', 'query'):
                            os.chmod(dst, ~0)
                            sh.copyfile(src, dst)
                        else: return self.run(path, base)
                    sh.copyfile(src, dst)
                else:
                    sh.copytree(src, dst)
                ui.note(u'successful', 'conf')
            except IOError:
                if os.path.isfile(dst):
                    os.chmod(dst, ~0)
                    os.remove(dst)
                ui.note(u'cant copy', 'error')
            except:
                if ui.query(u'Already exists! Sure to replace existing and Read-Only files?', 'query'):
                    if  self.__pwrcopy(src, dst):
                        ui.note(u'successful', 'conf')
                    else:
                        ui.note(u'cant copy', 'error')
            return self.run(path, base)
            running=0
    
    
    def do_move(self):
        ind=self.lb.current()
        src=self.all[ind][0]
        if src.lower().startswith('z:'):
            return self.do_copy()
        base=os.path.basename(src)
        if src.endswith(':') or not os.path.exists(src):
            return 1
        path=os.path.dirname(src)
        if path.endswith('\\'):
            path=path[:-1]
        ui.note(u'select destination')
        running=1
        while running:
            self.lb.set_list([(u'please wait...', self.wait_icon)])
            #e32.ao_yield()
            dst=useFman().AskUser(path, base, type='folder')
            if dst==None:
                return self.run(path, base)
            if dst.lower().startswith('z:'):
                ui.note(u'ACCESS DENIED', 'error')
                return self.run(path, base)
            try:
                sh.move(src, dst)
                ui.note(u'successful', 'conf')
            except IOError:
                fd=dst+'\\'+os.path.basename(src)
                if os.path.isfile(fd):
                    os.chmod(fd, ~0)
                    os.remove(fd)
                ui.note(u'cant move', 'error')
                return self.run(path, base)
            except:
                if ui.query(u'Already exists! Sure to replace existing and Read-Only files?', 'query'):
                    if self.__pwrmov(src, dst):
                        ui.note(u'successful', 'conf')
                    else:
                        ui.note(u'cant move', 'error')
                        return self.run(path, base)
            if ind==0:
                new=os.path.basename(self.all[ind][0])
            else:
                new=os.path.basename(self.all[ind-1][0])
            return self.run(path, new)
    
    def __pwrcopy(self, src, dst):
        try:
            try:
                if os.path.isfile(src):
                    os.chmod(dst, ~0)
                    sh.copyfile(src, dst)
                    return 1
                else:
                    sh.copytree(src, dst)
                    return 1
            except IOError:
                if os.path.isfile(dst):
                    os.chmod(dst, ~0)
                    os.remove(dst)
                return 0
            except OSError:
                a=os.listdir(src)
                if len(a)==0 and os.path.exists(dst):
                    #os.rmdir(src)
                    return 1
                else:
                    for i in a:
                        d=src+'\\'+i
                        f=dst+'\\'+i
                        if not os.path.exists(f):
                            if os.path.isfile(d):
                                sh.copyfile(d, f)
                            else:
                                sh.copytree(d, f)
                        else:
                            self.__pwrcopy(d, f)
                    return 1
            except:
                return 0
        except IOError:
            if os.path.isfile(f):
                os.chmod(f, ~0)
                os.remove(f)
            return 0
        except:
            return 0
    
    def __pwrmov(self, src, dst):
        try:
            try:
                os.chmod(src, ~0)
                sh.move(src, dst)
                return 1
            except IOError:
                fd=dst+'\\'+os.path.basename(src)
                if os.path.isfile(fd):
                    os.chmod(fd, ~0)
                    os.remove(fd)
                return 0
            except sh.Error:
                os.chmod(src, ~0)
                if os.path.isfile(src):
                    os.chmod(dst+'\\'+os.path.basename(src), ~0)
                    os.remove(dst+'\\'+os.path.basename(src))
                    sh.move(src, dst)
                    return 1
                li=os.listdir(src)
                if not li:
                    os.chmod(src, ~0)
                    os.rmdir(src)
                    return 1
                for i in li:
                    a=src+'\\'+i
                    b=dst+'\\'+os.path.basename(src)
                    os.chmod(a, ~0)
                    if not os.path.exists(b+'\\'+i):
                        sh.move(a, b)
                    else:
                        self.__pwrmov(a, b)
                try:
                    os.chmod(src, ~0)
                    os.rmdir(src)
                except: pass
                return 1
            except:
                return 0
        except IOError:
            f=b+'\\'+os.path.basename(a)
            if os.path.isfile(f):
                os.chmod(f, ~0)
                os.remove(f)
            return 0
        except:
            return 0
    
    def tasks(self, opt=0):
        import appswitch
        tup=appswitch.application_list(1)
        list='\n'.join(tup).split('\n')
        def select(mode='s'):
            index=a.current()
            cur=list[index]
            if mode=='s':
                appswitch.switch_to_fg(cur)
            elif mode=='c':
                appswitch.end_app(cur)
                if index==0:
                    return self.tasks()
                else:
                    return self.tasks(index-1)
            elif mode=='k':
                appswitch.kill_app(cur)
                if index==0:
                    return self.tasks()
                else:
                    return self.tasks(index-1)
            else:
                return 1
        def cb(foc):
            index=a.current()
            if foc: return self.tasks(index)
        def back():
            ind=self.lb.current()
            obj=self.all[ind][0]
            base=os.path.basename(obj)
            path=os.path.dirname(obj)
            if path.endswith('\\'):
                path=path[:-1]
            if obj.endswith(':'):
                path, base='None', obj
            self.run(path, base)
        a=ui.Listbox(list, select)
        a.set_list(list, opt)
        ui.app.body=a
        e32.ao_yield()
        ui.app.focus=cb
        ui.app.title=u'Taskman'
        ui.app.exit_key_handler=back
        ui.app.menu=[(u'Switch to', select), (u'Close', lambda:select('c')), (u'Kill', lambda:select('k')), (u'Back', back)]
    
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
                miso.compress_all_heaps()
                return self.run(path, base)
        except: return 1
    
    def rightArrow(self):
        ind=self.lb.current()
        current_item=self.all[ind][0]
        return self.run(path=current_item)
        
    def leftArrow(self):
        ind=self.lb.current()
        current_item=self.all[ind][0]
        return self.__previous(current_item)
        
    def scroll(self, mode='d'):
        ind=self.lb.current()
        tot=len(self.allist)
        if self.screen =='large':
            down=ind+7
            up=ind-7
        elif self.screen=='full':
            down=ind+8
            up=ind-8
        else:
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
    
    def compress(self):
        old=sysinfo.free_ram()
        miso.compress_all_heaps()
        new=sysinfo.free_ram()
        dif=(new-old)/1024
        return ui.note(str(dif)+u' kbyte(s) released')
    
    def devInfo(self):
        all=[(u'IMEI', sysinfo.imei()), (u'Total RAM', str(sysinfo.total_ram()/1024)+'KByte(s)'), (u'Free RAM', str(sysinfo.free_ram()/1024)+'KByte(s)'), (u'Battery', str(sysinfo.battery()*100/7)+u'%')]
        info='\n'.join(['%s: %s' %(k, v) for k, v in all])
        e32.ao_yield()
        return infopopup(info, u'Phone Info', OKREmpty)
    
    def netInfo(self):
        import location
        par=[u'MCC', u'MNC', u'Area ID', u'Cell ID', u'Signal Strength']
        val=list(location.gsm_location())+[sysinfo.signal_bars()*100/7]
        nfo='\n'.join(['%s: %d' %(k, v) for k, v in zip(par, val)])
        return infopopup(nfo, u'Network Info', OKREmpty)
    
    def shutdown(self, mode='r'):
        import switchoff
        if not (ui.query(u'press OK to continue', 'query')):
            return 1
        if mode=='r':
            switchoff.Restart()
        elif mode=='s':
            switchoff.Shutdown()
        else:
            return 1
    
    def settings(self):
        size=[u'normal', u'full', u'large']
        pick=[u'Yes', u'No']
        opt=[True, False]
        data=[
            (u'Screen size', 'combo', (size, size.index(self.screen))),
            (u'Set as system app', 'combo', (pick, opt.index(self.system))),
            (u'Save last path', 'combo', (pick, opt.index(self.lastpath))),
            (u'Text Size', 'combo', (self.fonts.keys(), self.fonts.keys().index(self.font_type))), 
            (u'Text Color', 'combo', (self.colors.keys(), self.colors.keys().index(self.color_type))), 
            (u'Set password', 'text', unicode(self.pw))
            ]
        flag=ui.FFormEditModeOnly|ui.FFormDoubleSpaced
        def save(args):
            ui.note(u'processing')
        form=ui.Form(data, flag)
        form.save_hook=save
        old=ui.app.title
        ui.app.title=u'Configurations'
        form.execute()
        self.screen=(form[0][2][0][form[0][2][1]]).encode('u8')
        self.system=opt[form[1][2][1]]
        self.lastpath=opt[form[2][2][1]]
        self.font_type=self.fonts.keys()[form[3][2][1]]
        self.font=self.fonts[self.font_type]
        self.color_type=self.colors.keys()[form[4][2][1]]
        self.color=self.colors[self.color_type]
        self.pw=form[5][2]
        pwd=self.pw.encode('base64').strip()
        e32.ao_yield()
        ini=file(self.pre+'ini.ini', 'w')
        ini.write(self.screen+'\n'+str(self.system)+'\n'+str(self.lastpath)+'\n'+self.font_type+'\n'+self.color_type+'\n'+pwd+'\nNone\nNone')
        e32.ao_yield()
        ini.close()
        ui.app.title=old
        ui.note(u'saved', 'conf')
        ui.app.screen=self.screen
        envy.set_app_system(self.system)
        return 1
    
    def about(self):
        abt=u'''myX-plorer v1.0\nBuild Date: 31 march, 2011\n\nThis application is created by ADIO Kingsley O. currently a 300 level student of the Department of Computer Science and Engineering, Obafemi Awolowo University. It is a system tool for the Symbian OS written in Python language.\nIts still under development, and isnt guaranteed bug-free.\nAny complaints, enquiries, modifications or likes should be kindly forwarded to:\nadiksonline@gmail.com\n+2347035536245\n\n...ADIKSonline 2011\n(c) all rights reserved.'''
        #abt=u'myX-plorer v1.0'
        infopopup(abt, u'About', OKREmpty)
        e32.ao_yield()
    
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
    
    def exit(self):
        ind=self.lb.current()
        cu=self.all[ind][0]
        if cu.endswith(':'):
            base=cu
        else:
            base=os.path.basename(cu)
        path=os.path.dirname(cu)
        if path.endswith('\\'):
            path=path[:-1]
        if cu.endswith(':'):
            path='None'
        if ui.query(u'sure to quit?', 'query'):
            ui.app.focus=None
            ini=file(self.pre+'ini.ini', 'w')
            if self.lastpath:
                ini.write(self.screen+'\n'+str(self.system)+'\n'+str(self.lastpath)+'\n'+self.font_type+'\n'+self.color_type+'\n'+self.pw.encode('base64').strip()+'\n'+path+'\n'+base)
            else:
                ini.write(self.screen+'\n'+str(self.system)+'\n'+str(self.lastpath)+'\n'+self.font_type+'\n'+self.color_type+'\n'+self.pw.encode('base64').strip()+'\nNone\nNone')
            e32.ao_yield()
            ini.close()
            sys.setdefaultencoding(default)
            miso.compress_all_heaps()
            self.lock.signal()
            ui.app.set_exit()

#if __name__=='__main__':

fman=Fman()
fman.run()
