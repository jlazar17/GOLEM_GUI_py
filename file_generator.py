# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_files/file_generator.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class FileGeneratorWindow(QtWidgets.QMainWindow):
    
    def __init__(self, pathList):
        super(FileGeneratorWindow,self).__init__()
        self.setupUi(pathList)
    
    def setupUi(self, pathList):
        self.setObjectName("MainWindow")
        self.resize(628, 308)
        self.setMinimumSize(QtCore.QSize(628, 308))
        self.centralWidget = QtWidgets.QWidget()
        self.centralWidget.setObjectName("centralWidget")
        self.labelTitle = QtWidgets.QLabel(self.centralWidget)
        self.labelTitle.setGeometry(QtCore.QRect(-10, -30, 59, 19))
        self.labelTitle.setObjectName("labelTitle")
        self.layoutWidget = QtWidgets.QWidget(self.centralWidget)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 610, 228))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_5.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_5.setSpacing(6)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.tableView = QtWidgets.QTableView(self.layoutWidget)
        self.tableView.setObjectName("tableView")
        self.gridLayout.addWidget(self.tableView, 0, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.horizontalLayout_5.addLayout(self.verticalLayout)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.labelAnalysisName = QtWidgets.QLabel(self.layoutWidget)
        self.labelAnalysisName.setObjectName("labelAnalysisName")
        self.horizontalLayout_2.addWidget(self.labelAnalysisName)
        self.lineEditAnalysisName = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEditAnalysisName.setClearButtonEnabled(False)
        self.lineEditAnalysisName.setObjectName("lineEditAnalysisName")
        self.horizontalLayout_2.addWidget(self.lineEditAnalysisName)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.checkBoxPython = QtWidgets.QCheckBox(self.layoutWidget)
        self.checkBoxPython.setChecked(True)
        self.checkBoxPython.setObjectName("checkBoxPython")
        self.verticalLayout_2.addWidget(self.checkBoxPython)
        self.checkBoxCpp = QtWidgets.QCheckBox(self.layoutWidget)
        self.checkBoxCpp.setChecked(True)
        self.checkBoxCpp.setObjectName("checkBoxCpp")
        self.verticalLayout_2.addWidget(self.checkBoxCpp)
        self.horizontalLayout_3.addLayout(self.verticalLayout_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setSpacing(6)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.pushButton = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_4.addWidget(self.pushButton)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5.addLayout(self.verticalLayout_3)
        self.setCentralWidget(self.centralWidget)
        #        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        #        self.menuBar.setGeometry(QtCore.QRect(0, 0, 628, 22))
        #        self.menuBar.setObjectName("menuBar")
        #        self.setMenuBar(self.menuBar)
        #        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        #        self.mainToolBar.setObjectName("mainToolBar")
        #        self.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        #        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        #        self.statusBar.setObjectName("statusBar")
        #        self.setStatusBar(self.statusBar)
        
        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)
        
        # Below this point, things have been added in by hand
        
        self.variableLineEditList = []
        self.standardItemModel    = QtGui.QStandardItemModel()
        self.populateTable(pathList)
        self.centralWidget.setLayout(self.horizontalLayout_5)
    
    
    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.labelTitle.setText(_translate("MainWindow", "TextLabel"))
        self.label.setText(_translate("MainWindow", "TextLabel"))
        self.labelAnalysisName.setText(_translate("MainWindow", "Analysis Name"))
        self.lineEditAnalysisName.setText(_translate("MainWindow", "MyAnalysis"))
        self.checkBoxPython.setText(_translate("MainWindow", "Generate Python"))
        self.checkBoxCpp.setText(_translate("MainWindow", "Generate Cpp"))
        self.pushButton.setText(_translate("MainWindow", "Finish"))
    
    def makeModel(self, pathList):
        headers = ["Dataset Path", "Variable Name"]
        self.standardItemModel.setHorizontalHeaderLabels(headers)
        for path in pathList:
            self.variableLineEditList.append(QtWidgets.QLineEdit(path.split("/")[-1]))
            self.standardItemModel.appendRow([QtGui.QStandardItem(i) for i in
                                              [path,"Error"]])
    
    def populateTable(self, pathList):
        self.makeModel(pathList)
        self.tableView.setModel(self.standardItemModel)
        for i in range(len(pathList)):
            _ = self.variableLineEditList[i]
            self.tableView.setIndexWidget(self.standardItemModel.index(i,1),_)
        self.tableView.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
#    ui.setupUi(MainWindow)
    ui.setupUi(MainWindow, ["longer/path/to/dset1","path/to/dset2"])
    MainWindow.show()
    sys.exit(app.exec_())

