import dearpygui.dearpygui as dpg
from gui.tabs.tab import Tab
from util.ioInterface import ioInterface


class test_tab(Tab, ioInterface):

    def __init__(self, window_label="test", size=[100, 100], type="tab", essential=False):
        super().__init__(window_label, size=size, type=type, essential=essential)

    def gui(self):

        #test ribbon + file dialog
        self.txt = dpg.add_text("hey")

        with dpg.menu_bar():
            with dpg.menu(label="test"):
                dpg.add_menu_item(label="test", callback=self.open_file)


        return super().gui()

    def open_file(self):
        filetypes = (("txt", "*.txt"), ("All Files", "*"))
        dpg.set_value(item=self.txt, value=super().open_file(filetypes=filetypes).read())

        return super().open_file(filetypes)

    pass