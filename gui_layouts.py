import PySimpleGUI as sg

loginLayout = [
    [sg.Text('Please enter your username and password')],
    [sg.Text('Username', size =(15, 1)), sg.InputText(key = 'ID')],
    [sg.Text('Password', size=(15, 1)), sg.InputText('', key='Password', password_char='*')],
    [sg.Submit(), sg.Cancel()]
]

menuLayout = [
        [sg.Button("Add Broadride Data File")],
        [sg.Button("Print Excel Reciept")],
        [sg.Button("Exit Program")]
]

updateLayout = [
    [sg.Text('Choose the Broadridge Data file to upload into the database'), sg.FileBrowse()], #update so only excel files are created
    [sg.Submit(), sg.Cancel()]
]
