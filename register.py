import sys
import json
import os
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox



#1. Class defination
#class ChildClass(ParentClass): PascalCase
class AccountingApp(QWidget):
    #1.Properties = Varaible = Store
    setting={}
    #2. Class constructor
    def __init__(self): # self=cio
        super().__init__() # I can call the parent construtor this way
        print("Hello from constructor")
        # Lets try to read the json file
        try:
            with open('accounting.json', 'r') as file:
                self.settings = json.load(file)
        except FileNotFoundError:
            self.settings = {}
        print(self.settings)    
        print(type(self.settings))
        self.buildUI()
        pass
    
    #3.Method=Function
    
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

