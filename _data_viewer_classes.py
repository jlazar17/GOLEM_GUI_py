import numpy as np
import h5py
from PyQt5 import QtCore, QtGui, QtWidgets
import auxiliary_functions as aux

class plotOptionWindow(QtWidgets.QWidget):
    def __init__(self, parxent=None):
        super(plotOptionWindow, self).__init__(parent)
        self.setWindowTitle('Plot Options')


class TitledTree():
    def __init__(self, title):
        self.tree = QtWidgets.QTreeWidget()
        self.title = QtWidgets.QLabel(title)
        #self.list.setHeaderLabel(str(title))
        self.tree.header().close()

        self.layout = QtWidgets.QVBoxLayout()
        self.layout.addWidget(self.title)
        self.layout.addWidget(self.tree)

        self.rowList        = []
        self.expandableList = []
        self.hasAttrsList   = []
        self.fileItems      = []
        self.isNpArray      = []

        self.iconClosedGroup = QtGui.QIcon('images/closed_group.svg')
        self.iconOpenGroup = QtGui.QIcon('images/open_group.svg')
        self.iconClosedGroupWithAttrs = QtGui.QIcon('images/closed_group_with_attrs.svg')
        self.iconOpenGroupWithAttrs = QtGui.QIcon('images/open_group_with_attrs.svg')

        self.iconDataset = QtGui.QIcon('images/dataset.svg')
        self.iconDatasetWithAttrs = QtGui.QIcon('images/dataset_with_attrs.svg')


    def clear(self):
        self.rowList        = []
        self.expandableList = []
        self.hasAttrsList   = []
        self.fileItems      = []
        self.isNpArray      = []
        self.tree.clear()

    def swapGroupIcon(self):
        for i in range(len(self.treeWidgetItems)):
            if self.treeWidgetItems[i].isExpanded():
                if self.hasAttrsList[i]:
                    self.treeWidgetItems[i].setIcon(0, self.iconOpenGroupWithAttrs)
                else:
                    self.treeWidgetItems[i].setIcon(0, self.iconOpenGroup)
        
            elif self.expandableList[i] == True:
                if self.hasAttrsList[i]:
                    self.treeWidgetItems[i].setIcon(0, self.iconClosedGroupWithAttrs)
                else:
                    self.treeWidgetItems[i].setIcon(0, self.iconClosedGroup)

    def setIcon(self, treeWidgetItem, hdf5Object):
        
        hasAttrs      = len(list(hdf5Object.attrs.keys())) > 0
        isExpandable  = isinstance(hdf5Object, h5py.Group) or aux.isRecarrayLike(hdf5Object)
        
        self.hasAttrsList.append(hasAttrs)
        self.expandableList.append(isExpandable)
        
        if isExpandable:
            if hasAttrs:
                treeWidgetItem.setIcon(0, self.iconClosedGroupWithAttrs)
            else:
                treeWidgetItem.setIcon(0, self.iconClosedGroup)
        else:
            if hasAttrs:
                treeWidgetItem.setIcon(0, self.iconDatasetWithAttrs)
            else:
                treeWidgetItem.setIcon(0, self.iconDataset)

    def findFileItems(self, hdfObject):
        # Sorry for this one
        if aux.hasKeys(hdfObject):
            for key in hdfObject.keys():
                self.fileItems.append(hdfObject[key].name)
                if isinstance(hdfObject[key], h5py.Group):
                    a = self.findFileItems(hdfObject[key])
                    self.isNpArray.append(False)
                elif aux.isRecarrayLike(hdfObject[key].value):
                    for n in list(hdfObject[key].dtype.names):
                        self.isNpArray.append(True)
                        self.fileItems.append((n,hdfObject[key].name))
        return self.fileItems

    def populateTree(self, fileItems, hdf5File):
        # Also I apologize for this one
        self.treeWidgetItems  = np.array([])
        self.names            = np.array([])
        
        for i in range(len(self.fileItems)):
            if isinstance(self.fileItems[i],str):
                a          = self.fileItems[i].split("/")
                parentName = a[-2]
                childName  = a[-1]
                if aux.is__I3Index__(parentName,childName):
                    pass
                else:
                    if parentName == "":
                        parent = self.tree
                        self.addQTreeWidgetItem(parent, parentName, childName,hdf5File)
                    else:
                        parent = self.treeWidgetItems[np.where(self.names==parentName)][0]
                        self.addQTreeWidgetItem(parent, parentName, childName,hdf5File)
            else:
                parentName = self.fileItems[i][1].split("/")[-1]
                childName  = self.fileItems[i][0]
                if aux.is__I3Index__(self.fileItems[i][1],childName):
                    pass
                else:
                    parent     = self.treeWidgetItems[np.where(self.names==parentName)][-1]
                    self.addQTreeWidgetItem(parent, parentName, childName,hdf5File)
        return self.treeWidgetItems

    def fullItemPath(self, selectedRow):
        path = selectedRow.text(0)
        parentRow = selectedRow.parent()
    
        while not parentRow == None:
            path = parentRow.text(0) + '/' + path
            parentRow = parentRow.parent()
        return path


    def addQTreeWidgetItem(self, parent,parentName,childName,hdf5File):
        child  = QtWidgets.QTreeWidgetItem(parent)
        self.treeWidgetItems = np.append(self.treeWidgetItems, child)
        self.names           = np.append(self.names, childName)
        self.setIcon(child,hdf5File)
        child.setText(0,childName)
        np.append(self.treeWidgetItems,child)
        child.setFlags(child.flags() | QtCore.Qt.ItemIsTristate |
                       QtCore.Qt.ItemIsUserCheckable)
        child.setCheckState(0, QtCore.Qt.Unchecked)


class TitledTable():
    def __init__(self, title):
        self.title = QtWidgets.QLabel(title)
        self.table = QtWidgets.QTableWidget()
        self.table.setShowGrid(True)
        
        self.previewButton = QtWidgets.QPushButton("Preview Data")
        self.numPreviewRowsLE = QtWidgets.QLineEdit("1000")
        
        self.previewButton.setDisabled(True)
        self.numPreviewRowsLE.setDisabled(True)
        self.previewButton.setDisabled(True)
        self.numPreviewRowsLE.setDisabled(True)

        self.hBox = QtWidgets.QHBoxLayout()
        self.hBox.addWidget(self.title)
        self.hBox.addStretch()
        self.hBox.addWidget(self.numPreviewRowsLE)
        self.hBox.addWidget(self.previewButton)
        
        self.vBox = QtWidgets.QVBoxLayout()
        self.vBox.addLayout(self.hBox)
        self.vBox.addWidget(self.table)
    
        self.layout = self.vBox


    def clear(self):
        self.table.setRowCount(0)
        self.table.setColumnCount(0)
        self.table.clear()


    def setItem(self, row, col, item):
        if isinstance(item, str):
            self.table.setItem(row, col, QtWidgets.QTableWidgetItem(item))
        else:
            print("Type Error: Item must be a str")

    def numCols(self, values):
        valueShape = np.shape(values)
        numcols = 1

        if len(valueShape) > 1:
            numcols = valueShape[1]

        return numcols
