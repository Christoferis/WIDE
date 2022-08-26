#Terminal Emulator Tab

from subprocess import Popen, PIPE
from threading import Thread
from tab import Tab
import dearpygui.dearpygui as dpg


class terminal_tab(Tab):

    def __init__(self, window_label="Terminal", size=..., type="terminal", essential=False):
        super().__init__(window_label, size, type, essential)

        #create Terminal Link

    #design -> CMD Line and
    def gui(self):
        self.cmd_int = dpg.add_input_text(readonly=True)

        pass
        
    def on_close(self):
        return super().on_close()

    #resize Text widgets
    def on_resize(self):
        pass

