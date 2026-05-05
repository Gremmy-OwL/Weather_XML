''''
Author: Gremmy OwL
Version: 0.0.3 B
Description: Pull XML files
'''
#Imports
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import font as tkfont
from PIL import Image
from PIL import ImageTk
from time import sleep
import requests, os

#Variables
save_path = 'weather.xml'
cloudpng = os.path.normpath('Assets\Images\cloud.png')
cloudico = os.path.normpath('Assets\Images\cloud.ico')

#Functions

#GUI Function
def display():

    #Tkinter window
    root = Tk()
    root.iconbitmap(cloudico)   #Set icon as cloud icon
    root.title('Weather XML Grabber')   #Set window title
    root.geometry('480x270')
    root.resizable(False, False)    

    #Main loop for display
    root.mainloop()
    return 0
#Main function
def main():

    #Calls display to run GUI
    display()

    return 0

#Calls
main()