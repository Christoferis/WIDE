#has most dearpygui / tkinter file dialogs and stuff
import os
from tkinter.constants import NO
import dearpygui.dearpygui as dpg
import tkinter.filedialog as fd
import tkinter as tk


#file managing io 

class ioInterface:

    def __init__(self):
        self.file = None
        self.edited = False
        pass

    #open single file returns contents
    def open_file(self):

        # this sure is gonna bite me later (open stream)
        win = tk.Tk()
        win.withdraw()
        self.file = open(fd.askopenfilename(defaultextension="*", filetypes=("All Files", "*")), mode="+")
        win.destroy()

        return self.file.read()

        
    def save_file(self, content, saveas):

        if self.file is None or saveas:
            self.open_file()

        self.file.write(content)

        self.edited = False

        pass

    def get_directory(self):
        return

    #closes and reopens all streams
    def io_refresh(self):
        path = os.path.abspath(self.file.name)
        self.file.close()
        self.file = open(path, mode="+")
        pass



