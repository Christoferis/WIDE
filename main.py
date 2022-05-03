#Wide is developed by Christoferis using the DearPyGUI Framework courtesy of Jonathan Hoffstadt
#main execution file 
#TODO: Rewrite to tkinter style gui (without context managers)

#imports
from gui.tabs import tab_manager as tm
from gui.tabs.text_tab import Text_Tab
from dearpygui.dearpygui import *
import sys
from time import time

from gui.tabs.test_tab import test_tab

#options
refresh_time = 2


def main():
    #create new Viewport and all Viewport oriented stuff First of all
    main_vp = create_viewport(title="wIDE")
    setup_dearpygui(viewport=main_vp)
    show_viewport(main_vp)

    mb = add_viewport_menu_bar()
    filemen = add_menu(parent=mb, label="File")
    add_menu_item(callback=lambda: Text_Tab(), parent=filemen, label="New Tab")

    #Prequisits
    # test_tab()
    Text_Tab()

    #start Threads for Accessories

    #Render loop
    while is_dearpygui_running() and len(tm.all_tabs) >= 1:
        render_dearpygui_frame()
        #handle refresh
        tm.refresh()


    cleanup_dearpygui()
    sys.exit()


#Adds tab to the Window


if __name__ == "__main__":
    main()
