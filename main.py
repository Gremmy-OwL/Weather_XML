''''
Author: Gremmy OwL
Version: 0.0.6 B
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

    #Styles
    titleFont = ttk.Style()
    titleFont.configure('tFont.TLabel', font = (12))

    #Tk Variables
    cloudpil = Image.open(cloudpng)
    cloud_resize = cloudpil.resize((30, 30))
    cloudPNGtk = ImageTk.PhotoImage(cloud_resize)

    #Frames
    baseFrame = ttk.Frame(root, padding = (10, 5, 10, 5), relief = 'raised', width = 480, height = 270)

    #Grid Frames in baseFrame
    bfgFrame00 = ttk.Frame(baseFrame, width = 80, height = 30)
    bfgFrame10 = ttk.Frame(baseFrame, relief = 'sunken', width = 30, height = 30)
    bfgFrame20 = ttk.Frame(baseFrame, relief = 'sunken', width = 230, height = 30)
    bfgFrame30 = ttk.Frame(baseFrame, relief = 'sunken', width = 30, height = 30)
    bfgFrame40 = ttk.Frame(baseFrame, width = 80, height = 30)

    bfgFrame01 = ttk.Frame(baseFrame, relief = 'sunken', width = 460, height = 230)

    #Widgets
        #Labels
    cloud_label0 = ttk.Label(bfgFrame10, image = cloudPNGtk)
    cloud_label1 = ttk.Label(bfgFrame30, image = cloudPNGtk)
    bigTitle = ttk.Label(bfgFrame20, text = 'Weather XML Grabber', font = 'tFont.TLabel', width = 20, anchor = CENTER)
        #Buttons

        #Entry Fields

    #Place Frames
    baseFrame.grid(column = 0, row = 0, sticky = (N, S, W, E))

    #bfgFrames
    bfgFrame00.grid(column = 0, row = 0)
    bfgFrame10.grid(column = 1, row = 0)
    bfgFrame20.grid(column = 2, row = 0)
    bfgFrame30.grid(column = 3, row = 0)
    bfgFrame40.grid(column = 4, row = 0)

    bfgFrame01.grid(column = 0, row = 1, columnspan = 5)

    #Place Widgets
        #Place Labels
    cloud_label0.grid(column = 0, row = 0)
    cloud_label1.grid(column = 0, row = 0)
    bigTitle.grid(column = 0, row = 0, sticky = (N))
        #Place Buttons

        #Place Entry Fields

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