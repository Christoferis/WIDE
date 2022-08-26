#Functions and datasets related to control all Tabs

import dearpygui.dearpygui as dpg
from time import time

#all tabs in the program
all_tabs = []
start = time()
refresh_time = 2


#Refreshes All Windows every like 2 secs or so -> current one always
def refresh():
    global start
    end = time()

    #only active tabs
    for window in all_tabs:

        if dpg.is_item_focused(window.window):
            window.refresh_tab()
        elif end - start >= refresh_time:
            window.refresh_tab()
            print("General Refresh")
            continue

    if end - start >= refresh_time:
        start = end
    #saves all current Tabs 


