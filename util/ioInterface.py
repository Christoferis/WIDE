#has most dearpygui / tkinter file dialogs and stuff
import os
import dearpygui.dearpygui as dpg
import tkinter.filedialog as fd
import tkinter as tk


#file managing io 

class ioInterface:

    def __init__(self):
        self.file = None
        pass

    #statics for one time use -> returns whole file obj / list if multiple
    @staticmethod
    def static_open_files(path):
        win = tk.Tk()
        win.withdraw()
        file = open(fd.askopenfiles(defaultextension="*", filetypes=("All Files", "*")), mode="+")
        win.destroy()

        return file
        
    @staticmethod
    def static_save(path, content):
        with open(path, mode="w") as f:
            f.write(content)


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

        pass

    def get_directory(self):
        return

    #closes and reopens all streams
    def io_refresh(self):
        path = os.path.abspath(self.file.name)
        self.file.close()
        self.file = open(path, mode="+")
        pass



