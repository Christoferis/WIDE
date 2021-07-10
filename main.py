#Wide is developed by Christoferis using the DearPyGUI Framework courtesy of Jonathan Hoffstadt
#main execution file 

#imports
from threading import Thread #for linting and AutoFill later
from tab import Tab
from dearpygui.dearpygui import start_dearpygui

def main():
    Tab()
    
    #start 
    start_dearpygui()

main()
