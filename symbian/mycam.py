import os, e32, sys, camera
import appuifw as ui
from graphics import Images

apps=(u'Imaging', u'Videos')
ui.app.set_tabs(apps, choose)

class Imaging:
    def __init__(self):
        self.image_mode=camera.image_modes()
        self.image_size=camera.image_sizes()
        self.flash_mode=camera.flash_modes()
        self.exp_mode=camera.exposure_modes()
        self.wbalance=camera.white_balance_modes()
        
    def

class Videos:
    def __init__(self):
        
        
        
        
def choose(self, ind):
    if ind==0:
        return Imaging()
    else:
        return Videos()