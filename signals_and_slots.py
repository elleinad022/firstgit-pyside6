#Version 1: Just responding to the button click : syntax
from PySide6.QtWidgets import QApplication, QPushButton

#The slot: responds when something happens
def button_clicked():
    print("Pinindot mo nga naman talaga!")

app = QApplication()
button = QPushButton("Sige! Pindutin mo!")

#clicked is a signal of QPushButton. It's emitted when you click on the button
#You can wire a slot to the signal using the syntax below:
button.clicked.connect(button_clicked)

button.show()
app.exec()
