''''
Author: Gremmy OwL
Version: 0.0.2 B
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