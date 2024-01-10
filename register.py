import sys
import json
import os
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox

print("Current Working Directory:", os.getcwd())
# Get the absolute path to the script's directory
script_directory = os.path.dirname(os.path.abspath(__file__))

# Construct the absolute path to the "accounting.json" file
json_file_path = os.path.join(script_directory, 'accounting.json')
if os.path.exists(json_file_path):
    with open(json_file_path, 'r') as file:
        settings = json.load(file)
        print(settings)

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle('Admin Registration')
window.showMaximized()
window.show()
sys.exit(app.exec())
