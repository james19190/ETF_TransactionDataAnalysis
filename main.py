import PySimpleGUI
from excel_to_db import input_data_to_DB
from userInput import *

#BEGIN PROGRAM
#ACCEPT LOGIN INFORMATION

login_details = getLoginDetails()

if (login_details == False):
    quit()
elif (login_details['ID'] == "admin" and login_details['Password'] == "admin"):
    choice = menuPage()
    match choice:
        case "Add Broadride Data File":
            path = getInputFile()
            input_data_to_DB(path)
        case "Print Excel Reciept":
            print("Preparing excel program")
        case "Exit Program":
            quit()

else :
    loginErrorMessage()



#SHOW USER OPTION MENU AND SAVE CHOICE

#IF UPDATE -> ASK FOR EXCEL FILE PATH AND INSERT DATA INTO POSTQRES -> BACK TO USER OPTION

#IF GENERATE REPORT, -> ASK FOR OUTPUT LOCATION AND GENERATE EXCEL REPORT -> BACK TO USER OPTION

#IF QUIT -> TERMINATE PROGRAM

