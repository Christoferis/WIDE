#class for handling all text tabs

import dearpygui.dearpygui as dpg


class Tab:

    def __init__(self, **kwargs) -> None:
        #open a window
        with dpg.window(label="test") as self.win:
            txt_widget = dpg.add_input_text()

        #kwargs for savepath, input text and so on
        #input
        try:
            self.input = kwargs["savepath"]
        except KeyError:
            self.input = None

        pass


    def save_file(self):
        #open file 
        if self.savepath != None:
            open(self.savepath, mode="w").write()

    def open_file(self, path):
        #spawn dialog

        path = self.savepath
        pass

    def tab_input(self, input):
        pass