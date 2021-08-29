#class for handling all text tabs

import dearpygui.dearpygui as dpg
from gui.tabs import tab_manager as gd, tab


class Text_Tab(tab.Tab):

    def __init__(self, text=""):
        super().__init__(window_label="untitled", type="text")
        self.tab_input(text)

    def gui(self):
        self.line_nums = dpg.add_input_text(multiline=True, no_spaces=True, readonly=True, width=100, height=500, label="")
        dpg.add_same_line(spacing=5)
        self.txt_widget = dpg.add_input_text(multiline=True, tab_input=True, width=500, height=500, label="", on_enter=True, callback=self.on_enter)
        return super().gui()

    #Save current open File
    def save_file(self):
        #open file 
        if self.savepath != None:
            open(self.savepath, mode="w").write(dpg.get_value(self.txt_widget))

    #Open a file 
    def open_file(self, path):
        self.savepath = path
        val = open(path, mode="r").read()
        dpg.set_value(self.txt_widget, val)
        dpg.set_item_label(self.win, path)
        self.update_tab()
        pass

    #refresh current tabs Linting, Syntax Highlighting and Line Count 
    def refresh_tab(self):
        self.update_line_nums()
        self.on_enter()
        self.on_resize()
        pass

    #input txt directly into window
    def tab_input(self, input):
        dpg.set_value(self.txt_widget, value=input)
        pass

    #callbacks
    #resize widget according to window
    def on_resize(self):
        dpg.set_item_height(self.txt_widget, dpg.get_item_height(self.win))
        dpg.set_item_height(self.line_nums, dpg.get_item_height(self.win))
        dpg.set_item_width(self.txt_widget, dpg.get_item_width(self.win))
        pass


    def on_enter(self):
        buffer = dpg.get_value(self.txt_widget)
        linenums = "0"

        for i in range(buffer.count("\n")):
            linenums += str(i) + "\n"
        
        dpg.set_value(self.line_nums, linenums)
    