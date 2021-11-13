#has most dearpygui / tkinter file dialogs and stuff
import dearpygui.dearpygui as dpg
import tkinter.filedialog as fd
import tkinter as tk


class ioInterface:

    def __init__(self, window):
        self.window = window
        self.file = None
        self.edited = False

        pass

    def open_file(self, filetypes):
        # this sure is gonna bite me later (open stream)
        win = tk.Tk()
        win.withdraw()
        self.file = fd.askopenfile(defaultextension=filetypes[0], filetypes=filetypes)
        win.destroy()

        return self.file.read()

        

    def open_directory(self):
        return

    def save_file(self):
        pass

    def io_refresh(self):
        pass



