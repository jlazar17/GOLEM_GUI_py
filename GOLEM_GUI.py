import sys
import numpy as np
import matplotlib.pyplot as plt
from PyQt5 import QtCore, QtWidgets, QtGui
import functools as ft
import h5py
import _data_viewer_classes as dvc
import file_generator
import about
import welcome
import data_viewer_warning as dv_warning
import auxiliary_functions as aux


plt.style.use("bmh")

class DataViewerWindow(QtWidgets.QMainWindow):
    
    switchWindow = QtCore.pyqtSignal()
    
    def __init__(self):
        
        super(DataViewerWindow, self).__init__()
        
        self.fname            = ''
        self.path             = ''
        self.currentDataset   = ''
        self.selectedPathList = []
        self.treeWidgetItems  = []
    
        self.initialiseUI()

    def initialiseUI(self):
        
        self.setWindowTitle('Golem GUI')
        
        self.tree = dvc.TitledTree("File tree")
        self.tree.tree.itemClicked.connect(self.itemClicked)
        self.tree.tree.itemExpanded.connect(self.tree.swapGroupIcon)
        self.tree.tree.itemCollapsed.connect(self.tree.swapGroupIcon)
        self.tree.tree.setMinimumWidth(250)

        self.datasetTable = dvc.TitledTable("Values")
        self.datasetTable.table.setMinimumWidth(350)
        self.datasetTable.previewButton.clicked.connect(self.displayDataset)

        self.attributeTable = QtWidgets.QTableWidget()
        self.attributeTable.setShowGrid(True)
        
        self.fnameLabel = QtWidgets.QLabel(self.fname)

        # Initialise buttons
        self.browseFileButton = QtWidgets.QPushButton("Browse Files")
        self.browseFileButton.clicked.connect(self.chooseFile)

        self.plotButton = QtWidgets.QPushButton("Plot")
        self.plotButton.clicked.connect(self.plot)
        self.plotButton.setDisabled(True)

        self.nextButton = QtWidgets.QPushButton("Next")
        self.nextButton.clicked.connect(self.nextButtonClicked)


#        self.fileMenu.addAction(openAction)

        # Setting layout
        grid = QtWidgets.QGridLayout()
        grid.setSpacing(10)
        
        grid.addWidget(self.browseFileButton, 1, 0, QtCore.Qt.AlignLeft)
        grid.addWidget(self.plotButton, 1, 1, QtCore.Qt.AlignLeft)
        grid.addWidget(self.fnameLabel, 2, 0)
        grid.addLayout(self.tree.layout, 3, 0)
        grid.addLayout(self.datasetTable.vBox, 3, 1)
        grid.addWidget(self.attributeTable, 4, 0, 1, 2)
        grid.addWidget(self.nextButton, 4,3)
        
        self.setCentralWidget(QtWidgets.QWidget(self))
        self.centralWidget().setLayout(grid)
    
        self.resizeEvent = self.resize

    def resize(self, event):
        self.tree.tree.setMaximumWidth(0.7*self.width())
        self.tree.tree.setMaximumWidth(0.3*self.width())
        self.attributeTable.setMaximumHeight(0.3*self.height())
    
    def openFile(self, fname):
        self.h5File = h5py.File(str(fname), 'r')
    
    def chooseFile(self):
        self.fname = QtWidgets.QFileDialog.getOpenFileName(self,
                                                           'Open file','~', filter='*.hdf5 *.h5')[0]
        return self.initiateFileOpen(self.fname)
    
    def initiateFileOpen(self, fname):
        self.tree.clear()
        self.datasetTable.clear()
        self.attributeTable.clear()
        self.datasetTable.numPreviewRowsLE.setDisabled(True)
        self.datasetTable.previewButton.setDisabled(True)
        try:
            self.openFile(fname)
            self.fileItems       = self.tree.findFileItems(self.h5File)
            self.treeWidgetItems = self.tree.populateTree(self.fileItems, self.h5File)
            
            self.fnameLabel.setText(fname.split('/')[-1])
            self.setWindowTitle('PyHDFView - ' + fname)
            self.datasetTable.previewButton.setDisabled(False)
            self.datasetTable.numPreviewRowsLE.setDisabled(False)
        except Exception as e:
            print(e)
            self.fname = '' # if it didn't work keep the old value
            self.fnameLabel.setText('')
            self.setWindowTitle('PyHDFView')
            self.clearFileItems
            self.datasetTable.clear()
            self.attributeTable.clear()
            self.datasetTable.previewButton.setDisabled(True)
            self.datasetTable.numPreviewRowsLE.setDisabled(True)
            print("Error opening file")

        return self.h5File

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
                maxCol = 1
            else:
                maxCol = shape[1]
            
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
        self.fileItems = []
        self.treeWidgetItems.clear()

    def enablePreviewWidgets(self):
        selectedRow = self.tree.tree.currentItem()
        path        = self.tree.fullItemPath(selectedRow)
        if (not (path) == self.currentDataset) and aux.isDataSet(self.h5File,path):
            self.datasetTable.previewButton.setDisabled(False)
            self.datasetTable.numPreviewRowsLE.setDisabled(False)
        else:
            self.datasetTable.previewButton.setDisabled(True)
            self.datasetTable.numPreviewRowsLE.setDisabled(True)

    def displayDataset(self):
        
        selectedRow = self.tree.tree.currentItem()
        path        = self.tree.fullItemPath(selectedRow)
            
        self.currentDataset = path
        keys = []
        while not path in self.h5File:
            _ = path.split("/")
            path = ("/").join(_[:-1])
            keys.append(_[-1])
        keys = keys[::-1]
        self.values = self.h5File[path][()]
        for key in keys:
            self.values = self.values[key]

        
        if len(self.values) > 0: # If the dataset is not empty
            self.plotButton.setDisabled(False)
            self.datasetTable.clear()
            
            if len(self.values) <= 1000:
                numrows = len(self.values)
            else:
                numrows = int(self.datasetTable.numPreviewRowsLE.text())
            numcols = self.datasetTable.numCols(self.values)
            self.datasetTable.table.setRowCount(numrows)
            self.datasetTable.table.setColumnCount(numcols)
            
            for i in range(numrows):
                if numcols > 1:
                    for j in range(numcols):
                        self.datasetTable.setItem(i, j, str(self.values[i,j]))
                else:
                    self.datasetTable.setItem(i, 0, str(self.values[i]))
#
    def isQTreeWidgetItem(self,item):
        if isinstance(item, QtWidgets.QTreeWidgetItem):
            return True
        else:
            return False
    
    def itemClicked(self):
        if isinstance(self.tree.tree.currentItem(),QtWidgets.QTreeWidgetItem):
            self.enablePreviewWidgets()

    def plotGraph(self):
        
        selected_items = self.dataset_table.table.selectedItems()
        
        if len(selectedItems) > 0:
            minRow = selectedItems[0].row()
            maxRow = selectedItems[-1].row() + 1
            
            minCol = selectedItems[0].column()
            maxCol = selectedItems[-1].column() + 1
        
        else:
            shape = np.shape(self.values)
            if len(shape) == 1:
                maxCol = 1
            else:
                maxCol = shape[1]
            
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

    def setSelectedPathList(self):
        for item in self.treeWidgetItems:
            isDSet = aux.isDataSet(self.h5File, self.tree.fullItemPath(item))
            if (item.checkState(0) == QtCore.Qt.Checked) and (isDSet) :
                self.selectedPathList.append(self.tree.fullItemPath(item))
            else:
                pass

    def getH5File(self):
        return self.h5File

    def getSelectedPathList(self):
        return self.selectedPathList

    def nextButtonClicked(self):
        self.setSelectedPathList()
        if len(self.selectedPathList)>0:
            self.close()
            self.FileGeneratorWindow =\
            file_generator.FileGeneratorWindow(self.selectedPathList,
                    self.fname)
            self.FileGeneratorWindow.show()
        else:
            self.dvWarningWindow = dv_warning.Ui_data_viewer_warning()
            self.dvWarningWindow.show()


            

def main():
    app = QtWidgets.QApplication(sys.argv)
    welcomeWindow = welcome.WelcomeWindow()
    welcomeWindow.widget.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
