#
#

def sectime(seconds):
    '''Converts seconds timecount to "HH:MM:SS" format.

Note: seconds must be either integer or floating point number'''
    min=seconds//60
    sec=seconds%60
    if min>59:
        hr=min//60
        min=min%60
    else:
        hr=0
    return u'%02d:%02d:%02d' %(hr, min, sec)

#
#