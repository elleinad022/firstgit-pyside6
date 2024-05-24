#Version 1: Everything in Global Scope
"""
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton

import sys 

app = QApplication(sys.argv)

window = QMainWindow()
window.setWindowTitle("Main Window App")

button = QPushButton()
button.setText("Press me")

window.setCentralWidget(button)
window.show()

app.exec()
"""


#Version 2: Setting up a separate class
"""
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton

class ButtonHolder(QMainWindow):
    def __init__ (self):
        super().__init__()
        self.setWindowTitle("Button Holder App")
        button = QPushButton("Press Me")

        #Set up the button as a central widget
        self.setCentralWidget(button)

app = QApplication(sys.argv)
window = ButtonHolder()
window.show()
app.exec()
"""

import sys
from PySide6.QtWidgets import QApplication
from button_holder import ButtonHolder

app = QApplication(sys.argv)

window = ButtonHolder()
window.show()
app.exec()
