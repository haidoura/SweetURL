'''
Created on Dec 12, 2010

@author: H.Haidoura
'''
import pygtk
pygtk.require("2.0")

import gtk, glib
try:
    import appindicator
except ImportError:
    appindicator = None

class TrayIcon():
    '''
    classdocs
    '''
    icon_status = None
    
    def __init__(self):
        '''
        Constructor
        '''
        try:
            if appindicator:
                self.icon_status = indicatorHandler
            else:
                self.icon_status =  statusHandler
                
        except KeyboardInterrupt:
        # Ignore user interruption
            pass

        
     
                
#application indicator
#TODO implement all settings for appindicator 
class indicatorHandler():
    '''
    application indicator is available in ubuntu 10.10
    '''   
    def __init__(self):
        #create application indicator
        indicator = appindicator.Indicator('sweetURL',
                       'sweetURL-status-on',
                       appindicator.CATEGORY_APPLICATION_STATUS)
        indicator.set_status(appindicator.STATUS_ACTIVE)
        
#gtk status icon
#TODO handle the gtk icon if appindicator library does not exist
class statusHandler():
    '''
    gtk status icon
    '''
    def __init__(self):
        # Create status icon
            status_icon = gtk.StatusIcon()
            status_icon.set_from_icon_name('sweetURL-status-on')
            status_icon.set_tooltip('sweetURL')
            
            

if __name__ == '__main__':
    TrayIcon()