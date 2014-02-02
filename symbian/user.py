import e32, os
import appuifw2 as ui
from graphics import *
from camera import _main_pane_size as pixels

app_lock=e32.Ao_lock()
folder=os.path.dirname(ui.app.full_name())+'\\packages\\'

ui.app.title=u'myGPCalc'
ui.app.screen='normal'
img=Image.open(folder+'me.jpg')
e32.ao_yield()
img=img.resize(pixels())
e32.ao_yield()
ui.note(u'my GPA Calculator\namplified...')

def handle_redraw(rect):
    canvas.blit(img)
    
canvas=ui.Canvas(event_callback=None, redraw_callback=handle_redraw)

ui.app.body=canvas

def static(tnu=0, tcp=0):
    noc=ui.query(u'total no of courses taken:', 'number')
    if not noc:
        ui.note(u'no course taken')
        return 0
    iter=0
    tcp=float(tcp)
    while iter<noc:
        while True:
            unit=ui.query(u'enter course unit:', 'number')
            if unit==0:
                ui.note(u'a value is required')
            elif not unit:
                if ui.query(u'Stop Calc', 'query', None, u'Yes', u'No'):
                    return 0
            else:
                break
        tnu+=unit
        while True:
            score=ui.query(u'enter score or grade:', 'text')
            if not score:
                if ui.query(u'Stop Calc', 'query', None, u'Yes', u'No'):
                    return 0
            elif score in (['%d'%x for x in range(70, 101)]+['A', 'a']):
                tcp+=5*unit
                break
            elif score in (['%d'%x for x in range(60, 70)]+['B', 'b']):
                tcp+=4*unit
                break
            elif score in (['%d'%x for x in range(50, 60)]+['C', 'c']):
                tcp+=3*unit
                break
            elif score in (['%d'%x for x in range(46, 50)]+['D', 'd']):
                tcp+=2*unit
                break
            elif score in (['%d'%x for x in range(40, 46)]+['E', 'e']):
                tcp+=unit
                break
            elif score in (['%d'%x for x in range(40)]+['F', 'f']):
                break
            else:
                ui.note(u'invalid score', 'error')
        
        iter+=1
    gpa=tcp/tnu
    if not ui.query(u'ur GPA is: %.3f'%gpa, 'query', None, u'ok', u'comments'):
        __comments(gpa)
    return [tnu, tcp]

def dynamic(tnu=0, tcp=0):
    ui.note(u'lets get started')
    #tnu=0
    tcp=float(tcp)
    while True:
        while True:
            unit=ui.query(u'enter course unit:', 'number')
            if unit==0:
                ui.note(u'a value is required')
            elif not unit:
                if ui.query(u'Stop Calc', 'query', None, u'Yes', u'No'):
                    return 0
            else:
                break
        tnu+=unit
        while True:
            score=ui.query(u'enter score or grade:', 'text')
            if not score:
                if ui.query(u'Stop Calc', 'query', None, u'Yes', u'No'):
                    return 0
            elif score in (['%d'%x for x in range(70, 101)]+['A', 'a']):
                tcp+=5*unit
                break
            elif score in (['%d'%x for x in range(60, 70)]+['B', 'b']):
                tcp+=4*unit
                break
            elif score in (['%d'%x for x in range(50, 60)]+['C', 'c']):
                tcp+=3*unit
                break
            elif score in (['%d'%x for x in range(46, 50)]+['D', 'd']):
                tcp+=2*unit
                break
            elif score in (['%d'%x for x in range(40, 46)]+['E', 'e']):
                tcp+=unit
                break
            elif score in (['%d'%x for x in range(40)]+['F', 'f']):
                break
            else:
                ui.note(u'invalid score', 'error')
        gpa=tcp/tnu
        if not ui.query(u'ur GPA is: %.3f'%gpa, 'query', None, u'continue', u'stop'):
            break
    __comments(gpa)
    return [tnu, tcp]

def __comments(GPA):
    if 5.0>=GPA>=4.5:
        ui.note(u'FIRST CLASS\nwhao! keep it up', 'info')
    elif 4.5>GPA>=3.5:
        ui.note(u'SECOND class\nUPPER division\nur best is yet to come')
    elif 3.5>GPA>=2.5:
        ui.note(u'SECOND class\nLOWER division\nu can do beta')
    elif 2.5>GPA>=1.5:
        ui.note(u'THIRD class\nput in more effort')
    elif 1.5>GPA>=1.0:
        ui.note(u'This is just a PASS result')
    elif 1.0>GPA>=0.0:
        ui.note(u'You are Advised to WITHDRAW')
    else:
        ui.note(u'Unrecognized Gradepoint')
    return 1

class User(object):
    def __init__(self):
        try:
            a=open(folder+'ini.db').read()
        except:
            f=open(folder+'ini.db', 'w')
            f.write('{}')
            f.close()
            a='{}'
        self.db=eval(a)

    def login(self):
        user=ui.query(u'enter username:', 'text')
        if not user:
            return 1
        else:
            user=user.lower()
            if user not in self.db.keys():
                ui.note(u'username does not exist', 'error')
                return 0
        passw=ui.query(u'enter password:', 'code')
        if not passw:
            return 0
        else:
            if passw!=self.db[user]:
                ui.note(u'incorrect password', 'error')
                return 0
            else:
                self.passw=passw
                ui.note(u'Welcome')
                return self.user_data(user)
    
    def new_user(self):
        while True:
            user=ui.query(u'enter username:', 'text')
            if not user:
                return 0
            user=user.lower()
            if os.path.exists(folder+'%s.gpd'%user):
                ui.note(u'username already exists', 'error')
            else:
                break
        while True:
            passw=ui.multi_query(u'enter password', u'retype password')
            if not passw:
                return 0
            if passw[0]!=passw[1]:
                ui.note(u'password mismatch', 'error')
            else:
                break
        new=open(folder+'%s.gpd'%user, 'w')
        data=('0', '0')
        for i in data:
            new.write(i+'\n')
        new.close()
        self.db[user]=passw[0]
        db=open(folder+'ini.db', 'w')
        db.write(str(self.db))
        db.close()
        ui.note(u'Success', 'conf')
        return 1
    
    def clear_data(self, user):
        if ui.query(u'sure to clear all records', 'query', None, u'Yes', u'No'):
            new=open(folder+'%s.gpd'%user, 'w')
            data=('0', '0')
            for i in data:
                new.write(i+'\n')
            new.close()
            self.update(user)
            ui.note(u'cleared', 'conf')
            return 1
    
    def update(self, user):
        self.user=user
        try:
            data=open(folder+'%s.gpd'%user).readlines()
        except IOError:
            del self.db[user]
            a=open(folder+'ini.db', 'w')
            a.write(str(self.db))
            a.close()
            return 0
        self.tcp=unicode(data[0])
        self.tnu=unicode(data[1])
        return 1
    
    def all_users(self):
        if not self.db:
            ui.note(u'no user yet')
            return 0
        a=ui.View()
        a.title=u'All Users'
        lb=ui.Listbox(self.db.keys())
        a.body=lb
        ui.app.view=a
        a.exit_key_text=u'Close'
        a.menu_key_text=''
        a.exit_key_handler=a.close
    
    def ch_pass(self, user):
        new=ui.multi_query(u'enter current password:', u'enter new password:')
        if not new:
            return 0
        else:
            if new[0]!=self.passw:
                ui.note(u'wrong password', 'error')
                return 0
            else:
                self.db[user]=new[1]
                a=open(folder+'ini.db', 'w')
                a.write(str(self.db))
                a.close()
                ui.note(u'success', 'conf')
                return 1
    
    def cgpa(self):
        tnu=int(self.tnu)
        tcp=float(self.tcp)
        if tnu==0:
            return u'0.000'
        else:
            return u'%0.3f'%(tcp/tnu)
    
    def user_data(self, user):
        def logout():
            ui.note(u'Goodbye')
            a.close()
        def del_user():
            try:
                if ui.query(u'Confirm Account Delete', 'query', None, u'Confirm', u'Cancel'):
                    os.chmod(folder+'%s.gpd'%user, ~0)
                    os.remove(folder+'%s.gpd'%user)
                    f=open(folder+'ini.db', 'w')
                    del self.db[user]
                    f.write(str(self.db))
                    f.close()
                    ui.note(u'deleted', 'conf')
                    a.close()
                return 1
            except:
                ui.note(u'Error\nTry Again', 'error')
                return 1
        if not self.update(user):
            ui.note(u'user data not found\naccount deleted', 'error')
            return 0
        a=ui.View()
        a.title=user
        self.choice=[u'Current CGPA Details', u'Update Profile', u'Instant GPCalc']
        self.lb=ui.Listbox(self.choice, self.lbox)
        a.body=self.lb
        a.exit_key_text=u'Logout'
        a.exit_key_handler=logout
        a.menu=[
            (u'CGPA', lambda: ui.note(self.cgpa())),
            (u'Clear Data', lambda: self.clear_data(self.user)),
            (u'Change Password', lambda: self.ch_pass(self.user)),
            (u'Logout', logout),
            (u'Delete Account', del_user)]
        ui.app.view=a
    
    def lbox(self):
        ind=self.lb.current()
        if ind==2:
            a=ui.selection_list([u'Static', u'Dynamic'])
            if a==0:
                static()
            elif a==1:
                dynamic()
        elif ind==0:
            tnu=self.tnu
            tcp=self.tcp
            cgpa=self.cgpa()
            ui.query(u'TCP :> '+tcp.strip()+'\nTNU :> '+tnu+'\n\nCGPA :> '+cgpa, 'query', None, u'OK', u'Back')
        else:
            new=static(int(self.tnu), float(self.tcp))
            if not new:
                return 0
            if type(new)!=list:
                ui.note(u'an error occurred', 'error')
                return 0
            a=open(folder+'%s.gpd'%self.user, 'w')
            a.write(str(new[1])+'\n')
            a.write(str(new[0]))
            a.close()
        self.update(self.user)
        

def exit_key_handler():
    if ui.query(u'sure to exit', 'query', None, u'Yes', u'No'):
        e32.ao_sleep(0.2)
        app_lock.signal()
        #ui.app.set_exit()
    
def la():
    ui.note(u'ADIO Kingsley O\n(c) June 2011\n\nadiksonline@gmail.com')
    
def ma():
    ui.note(u'VERSION: 1.4')
            
user=User()
ui.app.menu=[(u'Users', ((u'Login', user.login), (u'New User', user.new_user), (u'All Users', user.all_users))), (u'Static Calculator', static), (u'Dynamic Calculator', dynamic), (u'Author', la), (u'Version', ma), (u'Exit', exit_key_handler)]

ui.app.exit_key_handler=exit_key_handler
app_lock.wait()