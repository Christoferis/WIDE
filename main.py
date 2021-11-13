#Wide is developed by Christoferis using the DearPyGUI Framework courtesy of Jonathan Hoffstadt
#main execution file 
#TODO: Rewrite to tkinter style gui (without context managers)

#imports
from gui.tabs import text_tab, tab_manager as tm
from dearpygui.dearpygui import *
import sys

from gui.tabs.test_tab import test_tab


def main():
    #create new Viewport First of all
    
    main_vp = create_viewport(title="wIDE")
    setup_dearpygui(viewport=main_vp)
    show_viewport(main_vp)


    #Prequisits
    text_tab.Text_Tab()
    test_tab()
    

    #start Threads for Accesorries

    #Render loop
    while is_dearpygui_running() and len(tm.all_tabs) >= 1:
        render_dearpygui_frame()

    cleanup_dearpygui()
    sys.exit()


#Adds tab to the Window



if __name__ == "__main__":
    main()
