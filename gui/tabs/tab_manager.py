#Functions and datasets related to control all Tabs


#all tabs in the program
all_tabs = list()


#Refreshes All Windows
def refresh():
    for window in all_tabs:
        window.refresh_tab()
    
    print("Refreshed!")

#saves all current Tabs 


