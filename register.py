import sys
import json
import os
import winreg
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox
from cryptography.fernet import Fernet


#1. Class defination
#class ChildClass(ParentClass): PascalCase
class AccountingApp(QWidget):
    #1.Properties = Varaible = Store
    settings={}
    encryption_key = b'OKLABSisTheBestChannel'
    cipher = Fernet(encryption_key)
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
    def encrypt_value(self, value):
        encrypted_value = self.cipher.encrypt(value.encode())
        return encrypted_value

    def decrypt_value(self, encrypted_value):
        decrypted_value = self.cipher.decrypt(encrypted_value).decode()
        return decrypted_value
    
    def checkIfAdminIsCreated(self):
        print('Hello from checkIfAdminIsCreated')
        
        registry_key_path = r"SOFTWARE\as"
        value_name = "dt"
        default_json = '{"isAdminCreated":false,"isLicenseActivated":false}'
        # Open the registry key for reading
        # Initialize key outside the try block
        key = None
        try:
            # Open the registry key for reading
            key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, registry_key_path)
            
            # Read the encrypted value of the specified entry
            encrypted_value, _ = winreg.QueryValueEx(key, value_name)

            if encrypted_value:
                # Decrypt the value if it exists
                decrypted_value = self.decrypt_value(encrypted_value)
                print(f"Existing decrypted value: {decrypted_value}")
            else:
                # Encrypt and create an entry with the registry key and set the default JSON string
                encrypted_default_json = self.encrypt_value(default_json)
                print("Create an entry dt with default JSON value")
                winreg.SetValueEx(key, value_name, 0, winreg.REG_SZ, encrypted_default_json)
                
            # Close the registry key
        except FileNotFoundError:
            print("KeyNotFoundError")
            
            #ceo = ceo2.ClassName(ca1,ca2)
            key = winreg.CreateKey(winreg.HKEY_LOCAL_MACHINE, registry_key_path)
            winreg.SetValueEx(key, value_name, 0, winreg.REG_SZ, default_json)
        
        finally:
            # Close the registry key if it's open
            if key:
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

