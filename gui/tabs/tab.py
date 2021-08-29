#Inheritable Class for all Tabs / Windows in wIDE

from dearpygui.dearpygui import *
from gui.tabs.tab_manager import all_tabs


class Tab:

    def __init__(self, window_label, size=[500, 500], type="tab"):
        #make new window
        self.type = type

        with window(label=window_label, height=size[0], width=size[1], on_close=self.on_close) as self.window:
            #resize handler
            add_resize_handler(self.window, callback=self.on_resize)
            self.gui()

        #add to all the widgets
        all_tabs.append(self)
        pass

    #General Stuff
    def tab_info(self):
        return get_item_info(self.window), get_item_state(self.window)


    #callbacks and refreshes
    #function to refresh anything in given Tab by command
    def refresh_tab(self):
        pass

    def on_resize(self):
        pass

    def on_close(self):
        all_tabs.remove(self)

    #write GUI Stuff here (overridable)
    def gui(self):
        pass
