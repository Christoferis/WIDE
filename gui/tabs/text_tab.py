#class for handling all text tabs

import dearpygui.dearpygui as dpg
from gui.tabs import tab
from util.ioInterface import ioInterface
from random import random


class Text_Tab(tab.Tab):

    def __init__(self, text=""):
        super().__init__(window_label="untitled", type="text")

        self.file = ioInterface()

    def gui(self):
        self.line_nums = dpg.add_input_text(multiline=True, no_spaces=True, readonly=True, width=50, height=500, label="")
        dpg.add_same_line(spacing=5)
        self.txt_widget = dpg.add_input_text(multiline=True, tab_input=True, width=500, height=500, label="", on_enter=True, callback=self.on_enter)

        #context menu 
        with dpg.menu_bar():
            with dpg.menu(label="File"):
                dpg.add_menu_item(label="hey", callback=lambda: dpg.set_value(self.line_nums, str(random())))
                dpg.add_menu_item(label="Open File", callback=self.open_file)

    #Save current open File
    def save_file(self):
        #open file 
        if self.savepath != None:
            open(self.savepath, mode="w").write(dpg.get_value(self.txt_widget))

    #Open a file 
    def open_file(self):
        #save before open
        self.save_file()

        self.tab_input(self.file.open_file())
        dpg.set_item_label(self.window, self.file.get_directory())
        self.refresh_tab()
        pass

    def save_file(self):
        self.file.save_file(dpg.get_value(self.txt_widget))

    #refresh current tabs Linting, Syntax Highlighting and Line Count 
    def refresh_tab(self):
        super().refresh_tab()

        #this might cause a loop

        # self.update_line_nums()
        self.on_enter()
        # self.io_refresh()s
        pass

    #input txt directly into window
    def tab_input(self, input):
        dpg.set_value(self.txt_widget, value=input)
        pass

    #callbacks
    #resize widget according to window
    def on_resize(self):
        dpg.set_item_height(self.txt_widget, dpg.get_item_height(self.window))
        dpg.set_item_height(self.line_nums, dpg.get_item_height(self.window))
        dpg.set_item_width(self.txt_widget, dpg.get_item_width(self.window))
        pass

    #todo: synchronize those text tabs
    def on_enter(self):
        buffer = dpg.get_value(self.txt_widget)
        linenums = "1 \n"

        for i in range(buffer.count("\n")):
            linenums += str(i + 2) + "\n"
        

        dpg.set_value(self.line_nums, linenums)
    

def new_text_tab(self):
    return Text_Tab()