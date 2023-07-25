import PySimpleGUI as sg

from pathlib import Path
from gui_layouts import *

def getLoginDetails():
    window = sg.Window('Login Information', loginLayout)
    event, values = window.read()
    if (event == "Cancel"):
            return False
    window.close()
    return values

def loginErrorMessage():
    sg.popup("Wrong Credentials")

def menuPage():
    window = sg.Window('Options Menu', menuLayout)
    event, values = window.read()
    window.close()
    return event
    
def getInputFile():
    window = sg.Window("Update Database", updateLayout)
    event, values = window.read()
    window.close()
    return (values['Browse'])

def connectToDB():
    pass
    # needs to be adjusted for non-local server

