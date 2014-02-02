try:
    import me
except:
    import sys, e32, traceback
    import appuifw as ui
    ui.app.title=u'Fatal Error'
    ui.app.body=a=ui.Text()
    a.style=ui.STYLE_BOLD|ui.STYLE_ITALIC|ui.HIGHLIGHT_SHADOW
    a.set(u'the exception encountered is: ')
    a.add(unicode(''.join(traceback.format_exception(*sys.exc_info()))))
    ui.note(u'reinstall d application', 'error')
    e32.ao_sleep(2)
    e32.Ao_lock().signal()
    ui.app.set_exit()
    
e32.Ao_lock().wait()