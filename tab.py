#class for handling all text tabs

import dearpygui.dearpygui as dpg


class Tab:

    def __init__(self, **kwargs) -> None:
        #open a window
        with dpg.window(label="test", width=500, height=500) as self.win:

            #create resizing callback
            self.txt_widget = dpg.add_input_text(multiline=True, tab_input=True, width=500, height=500)
            dpg.add_resize_handler(self.win, callback=self.resize)

        #kwargs for savepath, input text and so on
        #input
        try:
            self.savepath = kwargs["savepath"]
        except KeyError:
            self.savepath = None
        pass



    def save_file(self):
        #open file 
        if self.savepath != None:
            open(self.savepath, mode="w").write(dpg.get_value(self.txt_widget))

    def open_file(self, path):
        self.savepath = path
        val = open(path, mode="r").read()
        dpg.set_value(self.txt_widget, val)
        pass

    #input txt directly into window
    def tab_input(self, input):
        dpg.set_value(self.txt_widget, value=input)
        pass

    #resize widget according to window
    def resize(self, sender):
        dpg.set_item_height(self.txt_widget, dpg.get_item_height(self.win))
        dpg.set_item_width(self.txt_widget, dpg.get_item_width(self.win))
        pass