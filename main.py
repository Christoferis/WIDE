#Wide is developed by Christoferis using the DearPyGUI Framework courtesy of Jonathan Hoffstadt
#main execution file 

#imports
from threading import Thread #for linting and AutoFill later
from tab import Tab
from dearpygui.dearpygui import *


def main():

    Tab().open_file("poop.txt")
    Tab()
    Tab()
    
    #start 
    start_dearpygui()


main()
