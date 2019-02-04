# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'data_viewer_warning.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_data_viewer_warning(QtWidgets.QMainWindow):
    
    def __init__(self):
        super(Ui_data_viewer_warning,self).__init__()
        self.setupUi()
    
    def setupUi(self):
        self.setObjectName("data_viewer_warning")
        self.resize(380, 174)
        self.centralWidget = QtWidgets.QWidget()
        self.centralWidget.setObjectName("centralWidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralWidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 0, 371, 111))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout_2.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_2.setSpacing(6)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton.setAutoDefault(True)
        self.pushButton.setDefault(True)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.pushButtonClicked)
        self.horizontalLayout.addWidget(self.pushButton)
        self.gridLayout_2.addLayout(self.horizontalLayout, 1, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setMaximumSize(QtCore.QSize(51, 51))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("images/alert-triangle.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 0, 1, 1, 1)
        self.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar()
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 380, 22))
        self.menuBar.setObjectName("menuBar")
        self.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar()
        self.mainToolBar.setObjectName("mainToolBar")
        self.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar()
        self.statusBar.setObjectName("statusBar")
        self.setStatusBar(self.statusBar)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)
    
        self.centralWidget.setLayout(self.gridLayout_2)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("data_viewer_warning", "data_viewer_warning"))
        self.pushButton.setText(_translate("data_viewer_warning", "Okay"))
        self.label_2.setText(_translate("data_viewer_warning", "At least one dataset must be selected to proceed"))

    def pushButtonClicked(self):
        self.close()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_data_viewer_warning()
    ui.show()
    sys.exit(app.exec_())

