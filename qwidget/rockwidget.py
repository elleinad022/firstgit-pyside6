from PySide6.QtWidgets import QWidget, QPushButton, QHBoxLayout

class RockWidget (QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("RockWidget")
        button1 = QPushButton("Button1")

        button_layout = QHBoxLayout()
        button_layout.addWidget(button1)

        self.setLayout(button_layout)