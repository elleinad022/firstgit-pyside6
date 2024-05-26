from PySide6.QtCore import QSize
from PySide6.QtGui import QAction, QIcon
from PySide6.QtWidgets import QMainWindow, QToolBar, QPushButton, QStatusBar

class MainWindow(QMainWindow):
    def __init__(self, app):
        super().__init__()
        self.app = app #declare an app member
        self.setWindowTitle("Unang MainWindow")

        #MENUBAR AND MENUS
        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu("File")
        quit_action = file_menu.addAction("Quit")
        quit_action.triggered.connect(self.quit_app)

        edit_menu = menu_bar.addMenu("Edit")
        edit_menu.addAction("Copy")
        edit_menu.addAction("Paste")
        edit_menu.addAction("Cut")
        edit_menu.addAction("Undo")
        edit_menu.addAction("Redo")

        #More menus for trying
        menu_bar.addMenu("Window")
        menu_bar.addMenu("Setting")
        menu_bar.addMenu("Help")

        #WORKING WITH TOOLBARS
        toolbar = QToolBar("Una kong Toolbar")
        toolbar.setIconSize(QSize(16,16))
        self.addToolBar(toolbar)

        #Adding the quit action to the toolbar
        toolbar.addAction(quit_action)

        toolbar.addSeparator()

        action1 = QAction("Some Action", self)
        action1.setStatusTip("Status message for some action")
        action1.triggered.connect(self.toolbar_button_click)
        toolbar.addAction(action1)

        toolbar.addSeparator()

        action2 = QAction(QIcon("qmainwindow/ubel.png"), "Another Action", self)
        action2.setStatusTip("Status message for another action")
        action2.triggered.connect(self.toolbar_button_click)
        #action2.setCheckable(True)
        toolbar.addAction(action2)

        toolbar.addSeparator()
        toolbar.addWidget(QPushButton("Click Here"))

        #WORKING WITH STATUS BARS
        self.setStatusBar(QStatusBar(self))

        button1 = QPushButton("Button sa Gitna")
        button1.clicked.connect(self.button1_clicked)
        self.setCentralWidget(button1)


        
    def button1_clicked(self):
        print("Pinindot mo yung button sa gitna!")
    
    def quit_app(self):
        self.app.quit()
    
    def toolbar_button_click(self):
        self.statusBar().showMessage("Eto mensahe mula sa app", 3000)
        print("action triggered")