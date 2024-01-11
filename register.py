import sys
import json
import os
import winreg
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox



#1. Class defination
#class ChildClass(ParentClass): PascalCase
class AccountingApp(QWidget):
    #1.Properties = Varaible = Store
    settings={}
    #2. Class constructor
    def __init__(self): # self=cio
        super().__init__() # I can call the parent construtor this way
        print("Hello from constructor")
        #2. function calling
        self.readJsonFile()
        self.checkIfAdminIsCreated()
        self.buildUI()
        pass
    
    #3.Method=Function
    def readJsonFile(self):
         # Lets try to read the json file
        try:
            with open('accounting.json', 'r') as file:
                self.settings = json.load(file)
        except FileNotFoundError:
            self.settings = {}
        print(self.settings)    
        print(type(self.settings)) #cio
        pass 
    # Define
    def checkIfAdminIsCreated(self):
        print('Hello from checkIfAdminIsCreated')
        
        registry_key_path = r"SOFTWARE\accountingsoftware"
        value_name = "isAdminCreated"
         # Open the registry key for reading
        try:
            # Open the registry key for reading
            key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, registry_key_path)
            
            # Read the value of the specified entry
            value, _ = winreg.QueryValueEx(key, value_name)
            #print(type(value.lower()))
            if value.lower() == "true":
                # Show the Login Form
                print("Show the Login Form")
                pass
            elif value.lower() == "false":
                # Show the Registeration Form
                print("Show the Registeration Form")
                pass
            else:
                # Create a entry with the registry key
                # isAdminCreated= false
                print("Create a entry isAdminCreated= false")
                
            # Close the registry key
        except FileNotFoundError:
            key = winreg.CreateKey(winreg.HKEY_LOCAL_MACHINE, registry_key_path)
            winreg.SetValueEx(key, value_name, 0, winreg.REG_SZ, "false")
        
        winreg.CloseKey(key)
        pass
    
    def buildUI(self):
        #self=window
        self.setStyleSheet("background-color: #A4BFD8;") #aa
        self.setWindowTitle(self.settings["windowTitle"])
        self.showMaximized()
        self.show()
        pass
    pass
#2. Create class Object
app = QApplication([])
ceo = AccountingApp()
ceo.showMaximized()
sys.exit(app.exec())

