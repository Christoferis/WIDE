#Functions and datasets related to control all Tabs

from gui.tabs import text_tab

#all tabs in the program
all_tabs = list()

#new Tab
def new_text_tab():
    return text_tab.Text_Tab()

def new_tab():
    return text_tab.Text_Tab()

#Refreshes All Windows
def refresh():
    for window in all_tabs:
        window.refresh_tab()
    
    print("Refreshed!")

#saves all current Tabs 


