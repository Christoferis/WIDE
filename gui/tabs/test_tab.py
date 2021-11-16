import dearpygui.dearpygui as dpg
from gui.tabs.tab import Tab
from util.ioInterface import ioInterface as io


class test_tab(Tab):

        
    def __init__(self, window_label="untitled", size=..., type="tab", essential=False):
        super().__init__(window_label=window_label, size=size, type=type, essential=essential)

        self.io = io()


    def gui(self):

        #test ribbon + file dialog
        self.txt = dpg.add_text("hey")

        with dpg.menu_bar():
            with dpg.menu(label="test"):
                dpg.add_menu_item(label="test", callback=self.open_file)


        return super().gui()

    def open_file(self):
        filetypes = (("txt", "*.txt"), ("All Files", "*"))
        dpg.set_value(item=self.txt, value=io.open_file(filetypes=filetypes))




    pass