import sys
import numpy as np
import matplotlib.pyplot as plt
from PyQt5 import QtCore, QtWidgets, QtGui
import functools as ft
import h5py
import _data_viewer_classes as dvc

plt.style.use("bmh")

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
        self.switchWindow.emit()

    def showAboutPage(self):
        self.aboutWindow = AboutWindow()
        self.aboutWindow.widget.show()

class DataViewerWindow(QtWidgets.QMainWindow):
    
    def __init__(self):
        
        super(DataViewerWindow, self).__init__()
        
        self.fname     = ''
        self.path      = ''
    
        self.initialiseUI()

    def initialiseUI(self):
        
        self.setWindowTitle('Golem GUI')
        
        self.tree = dvc.TitledTree("File tree")
        #self.tree.tree.itemClicked.connect(self.itemClicked)
        self.tree.tree.itemExpanded.connect(self.tree.swapGroupIcon)
        self.tree.tree.itemCollapsed.connect(self.tree.swapGroupIcon)
        self.tree.tree.setMinimumWidth(250)

        self.datasetTable = dvc.TitledTable("Values")
        self.datasetTable.table.setMinimumWidth(350)

        self.attributeTable = QtWidgets.QTableWidget()
        self.attributeTable.setShowGrid(True)
        
        self.fnameLabel = QtWidgets.QLabel(self.fname)

        # Initialise buttons
        self.browseFileButton = QtWidgets.QPushButton("Browse Files")
        self.browseFileButton.clicked.connect(self.chooseFile)

        self.plotButton = QtWidgets.QPushButton("Plot")
        self.plotButton.clicked.connect(self.plot)
        self.plotButton.hide()

#        # Addtional menu options for DataViewerWindows
#        openAction   = QtWidgets.QAction("&Open", self)
#        openAction.setShortcut("Ctrl+O")
#        #openAction.triggered.connect(self.chooseFile)
#        self.fileMenu.addAction(openAction)

        # Setting layout
        grid = QtWidgets.QGridLayout()
        grid.setSpacing(10)
        
        grid.addWidget(self.browseFileButton, 1, 0, QtCore.Qt.AlignLeft)
        grid.addWidget(self.plotButton, 1, 1, QtCore.Qt.AlignLeft)
        grid.addWidget(self.fnameLabel, 2, 0)
        grid.addLayout(self.tree.layout, 3, 0)
        grid.addLayout(self.datasetTable.layout, 3, 1)
        grid.addWidget(self.attributeTable, 4, 0, 1, 2)
        
        self.setCentralWidget(QtWidgets.QWidget(self))
        self.centralWidget().setLayout(grid)
    
        self.resizeEvent = self.resize

    def resize(self, event):
        self.tree.tree.setMaximumWidth(0.7*self.width())
        self.tree.tree.setMaximumWidth(0.3*self.width())
        self.attributeTable.setMaximumHeight(0.3*self.height())
    
    def openFile(self, fname):
        self.hdf5File = h5py.File(str(fname), 'r')
    
    def chooseFile(self):
        self.fname = QtWidgets.QFileDialog.getOpenFileName(self,
                                                           'Open file','~', filter='*.hdf5 *.h5')[0]
        print(self.fname)
        self.initiateFileOpen(self.fname)
    
    def initiateFileOpen(self, fname):
        self.datasetTable.clear()
        self.attributeTable.clear()
        try:
            self.openFile(fname)
            print(type(self.hdf5File))
            self.fileItems       = self.tree.findFileItems(self.hdf5File)
            self.treeWidgetItems = self.tree.populateTree(self.fileItems, self.hdf5File)
            self.fnameLabel.setText(fname.split('/')[-1])
            self.setWindowTitle('PyHDFView - ' + fname)
        except Exception as e:
            print(e)
            self.fname = '' # if it didn't work keep the old value
            self.fnameLabel.setText('')
            self.setWindowTitle('PyHDFView')
            self.clearFileItems
            self.datasetTable.clear()
            self.attributeTable.clear()
            print("Error opening file")

    def plot(self):
            
        selectedItems = self.datasetTable.table.selectedItems()
        
        if len(selectedItems) > 0:
            minRow = selectedItems[0].row()
            maxRow = selectedItems[-1].row() + 1
            
            minCol = selectedItems[0].column()
            maxCol = selectedItems[-1].column() + 1
        
        else:
            shape = np.shape(self.values)
            if len(shape) == 1:
                max_col = 1
            else:
                max_col = shape[1]
            
            minRow = 0
            maxRow = shape[0]
            minCol = 0
        
        plt.ion()
        plt.close('all')
        
        if len(self.values) > 0: # for 2d data each plot col by col
            if len(np.shape(self.values)) > 1:
                plt.figure()
                for i in range(minRow, maxRow):
                    plt.plot(self.values[i, minCol:maxCol], '-o', label=str(i))
                
                plt.legend(loc=0)
                plt.show()
            
            else: # for 1d data we plot a row
                plt.figure()
                plt.plot(self.values[minRow:maxRow], '-o')
                plt.show()

    def clearFileItems(self):
        self.file_items = []
        self.treeWidgetItems.clear()




class Controller:

    def __init__(self):
        pass

    def showWelcomeWindow(self):
        self.welcomeWindow = WelcomeWindow()
        self.welcomeWindow.switchWindow.connect(self.showDataViewer)
        self.welcomeWindow.widget.show()
    
    def showAboutWindow(self):
        self.about = AboutWindow().widget
    
    def showDataViewer(self):
        self.dataViewer = DataViewerWindow()
        self.welcomeWindow.widget.close()
        self.dataViewer.show()

def main():
    app = QtWidgets.QApplication(sys.argv)
    controller = Controller()
    controller.showWelcomeWindow()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
