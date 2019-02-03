from PyQt5 import QtCore, QtGui, QtWidgets
import GOLEM_GUI
import about


class WelcomeWindow(QtWidgets.QMainWindow):
    
    switchWindow = QtCore.pyqtSignal()

    def __init__(self):
        
        super(WelcomeWindow, self).__init__()
        
        QtWidgets.QWidget.__init__(self)
        self.setWindowTitle("Golem GUI")
        self.widget = QtWidgets.QWidget()

        # Add GOLEM image pixmap
        self.label  = QtWidgets.QLabel(self)
        self.pixmap = QtGui.QPixmap("images/golem.jpg")
        self.pixmap = self.pixmap.scaled(300, 333, QtCore.Qt.KeepAspectRatio)
        self.label.setPixmap(self.pixmap)

        # Add buttons
        self.startButton = QtWidgets.QPushButton("Start Wizard")
        self.startButton.clicked.connect(self.startWizard)
        self.aboutButton = QtWidgets.QPushButton("About")
        self.aboutButton.clicked.connect(self.showAboutPage)

        # Make layout
        self.hBox1 = QtWidgets.QHBoxLayout()
        self.hBox1.addStretch()
        self.hBox1.addWidget(self.label)
        self.hBox1.addStretch()
        
        self.hBox2 = QtWidgets.QHBoxLayout()
        self.hBox2.addWidget(self.aboutButton)
        self.hBox2.addWidget(self.startButton)
        self.hBox2.addStretch()
        
        self.vBox = QtWidgets.QVBoxLayout()
        self.vBox.addLayout(self.hBox1)
        self.vBox.addLayout(self.hBox2)
        
        self.widget.setLayout(self.vBox)

    def startWizard(self):
        self.dataViewer = GOLEM_GUI.DataViewerWindow()
        self.widget.close()
        self.dataViewer.show()

    def showAboutPage(self):
        self.aboutWindow = about.AboutWindow()
        self.aboutWindow.widget.show()
