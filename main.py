''''
Author: Gremmy OwL
Version: 0.1.2 B
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
import requests, os, threading

#Variables
save_path = 'weather.xml'
cloudpng = os.path.normpath('Assets\\Images\\cloud.png')
cloudico = os.path.normpath('Assets\\Images\\cloud.ico')

#Functions

#GUI Function
def getDir():
    global save_dir
    save_dir = os.path.normpath(filedialog.askdirectory(title = 'Select a Location') + '\\weather.xml')

    return save_dir

def getXML(site):
    global response
    response = requests.get(site)

    return response

def display():

    #Display specific Functions
    def siteCommand():
        global site
        site = xmlSiteField.get()

        return site
    
    def saveCommand():
        global save_dir
        save_dir = getDir()
        xmlDestField.delete(0, 'end')
        xmlDestField.insert(0, save_dir)

        return 0
    
    def witeXML():
        global save_dir
        global site

        site = siteCommand()
        save_dir = xmlDestField.get()
        response = getXML(site)

        if response.status_code == 200:
            with open(save_dir, 'w') as f:
                f.write(response.text)
            return 0
        else:
            return response.status_code
        
        return 0

    #Tkinter window
    root = Tk()
    root.iconbitmap(cloudico)   #Set icon as cloud icon
    root.title('Weather XML Grabber')   #Set window title
    root.geometry('512x286')
    root.resizable(False, False)    

    #Styles
    titleFont = ttk.Style()
    titleFont.configure('tFont.TLabel', font = ('Arial', 20, 'bold'))

    bigButton = ttk.Style()
    bigButton.configure('bButton.TButton', font = (10))

    StartButton = ttk.Style()
    StartButton.configure('St.TButton', foreground = 'green', font = (36))

    StopButton = ttk.Style()
    StopButton.configure('Sp.TButton', foreground = 'red', font = (36))

    #Tk Variables
    cloudpil = Image.open(cloudpng)
    cloud_resize = cloudpil.resize((30, 30))
    cloudPNGtk = ImageTk.PhotoImage(cloud_resize)

    mUpdate = BooleanVar(value = True)
    updateInt = StringVar(value = '30')

    #Frames
    baseFrame = ttk.Frame(root, padding = (10, 5, 10, 5), relief = 'raised', width = 480, height = 270)

    #Grid Frames in baseFrame
    baseFrame = ttk.Frame(root, padding = (10, 5, 10, 5))

    frame0 = ttk.Frame(baseFrame, padding = (10, 5, 10, 5), width = 492, height = 246)
    frame0a = ttk.Frame(frame0, width = 40, height = 55)
    frame0b = ttk.Frame(frame0, width = 41, height = 55)
    frame0c = ttk.Frame(frame0, width = 145, height = 55)
    frame0d = ttk.Frame(frame0, width = 145, height = 55)
    frame0e = ttk.Frame(frame0, width = 80, height = 55)

    frame1 = ttk.Frame(baseFrame, padding = (10, 5, 10, 5), width = 492, height = 200)
    frame1a = ttk.Frame(frame1, relief = 'sunken', width = 142, height = 20)
    frame1b = ttk.Frame(frame1, relief = 'sunken', width = 50, height = 20)
    frame1c = ttk.Frame(frame1, relief = 'sunken', width = 50, height = 20)
    frame1d = ttk.Frame(frame1, width = 132, height = 20)
    frame1e = ttk.Frame(frame1, relief = 'sunken', width = 23, height = 20)
    frame1f = ttk.Frame(frame1, relief = 'sunken', width = 85, height = 20)

    frame2 = ttk.Frame(baseFrame, padding = (10, 5, 10, 5), width = 492, height = 200)
    frame2a = ttk.Frame(frame2, relief = 'sunken', width = 90, height = 20)
    frame2b = ttk.Frame(frame2, relief = 'sunken', width = 382, height = 20)
    frame2c = ttk.Frame(frame2, relief = 'sunken', width = 90, height = 20)
    frame2d = ttk.Frame(frame2, relief = 'sunken', width = 382, height = 20)
    frame2e = ttk.Frame(frame2, relief = 'sunken', width = 30, height = 20)

    frame3 = ttk.Frame(baseFrame, padding = (10, 5, 10, 5), width = 492, height = 200)
    frame3a = ttk.Frame(frame3, relief = 'sunken', width = 472, height = 190)

    #Widgets
        #Labels
    cloud_label0 = ttk.Label(frame0, image = cloudPNGtk)
    cloud_label1 = ttk.Label(frame0, image = cloudPNGtk)
    bigTitle = ttk.Label(frame0, text = 'Weather XML Grabber', font = ('Arial', 20, 'bold'))
    xmlSiteLabel = ttk.Label(frame2a, text = 'XML Site:')
    destLabel = ttk.Label(frame2c, text = 'Destination File:')
    aUpLabel = ttk.Label(frame1a, text = 'Check for update every: ')
    seconds = ttk.Label(frame1c, text = ' seconds')
    mUpLabel = ttk.Label(frame1f, text = 'Manual Update')

        #Buttons
    startB = ttk.Button(frame0, text = '\nStart\n', width = 18, style = 'St.TButton')
    stopB = ttk.Button(frame0, text = '\nStop\n', width = 18, style = 'Sp.TButton')
    saveB = ttk.Button(frame2e, text = 'Save As')
    updateB = ttk.Button(frame3a, text = '\nUpdate\n', width = 77)
    manualCheck = ttk.Checkbutton(frame1e, variable = mUpdate, onvalue = True, offvalue = False)

        #Entry Fields
    xmlSiteField = ttk.Entry(frame2b, width = 48)
    xmlDestField = ttk.Entry(frame2d, width = 48)
    updateSpin = ttk.Spinbox(frame1b, from_ = 5, to = 1800, width = 4, textvariable = updateInt)

    #Place Frames
    baseFrame.grid(column = 0, row = 0, sticky = (N, S, W, E))

    #bfgFrames
    frame0.grid(column = 0, row = 0, sticky = (N, E, W))
    frame0a.grid(column = 0, row = 1, sticky = (W))
    frame0b.grid(column = 1, row = 1, sticky = (W))
    frame0c.grid(column = 2, row = 1, sticky = (W))
    frame0d.grid(column = 3, row = 1, sticky = (W))
    frame0e.grid(column = 4, row = 1, sticky = (W))

    frame1.grid(column = 0, row = 2, sticky = (N))
    frame1a.grid(column = 0, row = 0, sticky = (N, W))
    frame1b.grid(column = 1, row = 0, sticky = (N, W))
    frame1c.grid(column = 2, row = 0, sticky = (N, W))
    frame1d.grid(column = 3, row = 0, sticky = (N, W))
    frame1e.grid(column = 4, row = 0, sticky = (N, W))
    frame1f.grid(column = 5, row = 0, sticky = (N, W))

    frame2.grid(column = 0, row = 3, sticky = (N, S, E, W))
    frame2a.grid(column = 0, row = 0, sticky = (N, W))
    frame2b.grid(column = 1, row = 0, sticky = (N, W))
    frame2c.grid(column = 0, row = 1, sticky = (N, W))
    frame2d.grid(column = 1, row = 1, sticky = (N, W))
    frame2e.grid(column = 2, row = 1, sticky = (N, E))

    frame3.grid(column = 0, row = 4, sticky = (N, S, E, W))
    frame3a.grid(column = 0, row = 0, sticky = (N))

    #Place Widgets
        #Place Labels
    cloud_label0.grid(column = 1, row = 0, sticky = (E))
    cloud_label1.grid(column = 4, row = 0, sticky = (W))
    bigTitle.grid(column = 2, row = 0, sticky = (W), columnspan = 2)
    xmlSiteLabel.grid(column = 0, row = 0, sticky = (N, W))
    destLabel.grid(column = 0, row = 0, sticky = (N, W))
    aUpLabel.grid(column = 0, row = 0, sticky = (N, W))
    seconds.grid(column = 0, row = 0, sticky = (N, W))
    mUpLabel.grid(column = 0, row = 0, sticky = (N, E))
        #Place Buttons
    startB.grid(column = 1, row = 1, sticky = (N, E), columnspan = 2)
    stopB.grid(column = 3, row = 1, sticky = (N, W), columnspan = 2)
    saveB.grid(column = 0, row = 0, sticky = (N, E))
    updateB.grid(column = 0, row = 0)
    manualCheck.grid(column = 0, row = 0, sticky = (N, E))

        #Place Entry Fields
    xmlSiteField.grid(column = 0, row = 0, sticky = (W))
    xmlDestField.grid(column = 0, row = 0, sticky = (W))
    updateSpin.grid(column = 0, row = 0, sticky = (N, W))

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