from PyQt5 import QtCore, QtGui, QtWidgets

class AboutWindow(QtWidgets.QMainWindow):

    def __init__(self):
        
        self.widget = QtWidgets.QWidget()
        
        self.label1 = QtWidgets.QLabel("Golem version 1.0.0")
        self.label2 = QtWidgets.QLabel("Created by the HESE Team")
        self.label3 = QtWidgets.QLabel("Dated: January 31, 2019")
        
        self.boldFont = QtGui.QFont()
        self.boldFont.setBold(True)
        self.label1.setFont(self.boldFont)

        self.button = QtWidgets.QPushButton("OK")
        self.button.clicked.connect(self.widget.close)

        # Specifying layout
        self.hBox = QtWidgets.QHBoxLayout()
        self.hBox.addStretch()
        self.hBox.addWidget(self.button)

        self.vBox = QtWidgets.QVBoxLayout()
        self.vBox.addWidget(self.label1)
        self.vBox.addWidget(self.label2)
        self.vBox.addWidget(self.label3)
        self.vBox.addLayout(self.hBox)

        self.widget.setLayout(self.vBox)
