#Version 1: Just responding to the button click : syntax
"""
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
"""


"""
#Version 2: Signals sending Values, Capture Values in Slots
from PySide6.QtWidgets import QApplication, QPushButton

#The Slot: responds when something happens
def button_clicked(data):
    print("Pinindot mo pa talagang inamo ka! Eto : ", data)

app = QApplication()
button = QPushButton("Wag mo pindotin.")
button.setCheckable(True) #Makes the button checkable, its unchecked by default. Clicking = toggling

#clicked is a signal of QPushButton. It's emitted when you click on the button
#You can wire a slot to the signal using the syntax below
button.clicked.connect(button_clicked)

button.show()
app.exec()
"""

#Version 3: Capture Value from a Slider - Other Example
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QSlider

#The Slot: responds when something happens 
def respond_to_slider(data):
    print("Naknampucha, Ginalaw mo yung slider! Eto value: ", data)

app = QApplication()
slider = QSlider(Qt.Vertical)
slider.setMinimum(0)
slider.setMaximum(101)
slider.setValue(69)

#You just do the connection, the QT system takes care of passing the data from the signal to the slot.

slider.valueChanged.connect(respond_to_slider)
slider.show()
app.exec()
