#class for handling all text tabs

import dearpygui.dearpygui as dpg


class Tab:

    def __init__(self, **kwargs) -> None:
        #open a window
        with dpg.window(label="test", width=500, height=500) as self.win:
            
            #create resizing callback
            self.txt_widget = dpg.add_input_text(multiline=True, tab_input=True)
            dpg.add_resize_handler(self.win, callback=self.resize)

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

    #input txt directly into window
    def tab_input(self, input):
        dpg.set_value()
        pass

    #resize widget according to window
    def resize(self, sender):
        dpg.set_item_height(self.txt_widget, dpg.get_item_height(self.win))
        dpg.set_item_width(self.txt_widget, dpg.get_item_width(self.win))
        pass