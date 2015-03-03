# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qt/advanceddialog.ui'
#
# Created: Mon Jan 12 10:13:06 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_AdvancedDialog(object):
    def setupUi(self, AdvancedDialog):
        AdvancedDialog.setObjectName("AdvancedDialog")
        AdvancedDialog.resize(525, 450)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/mapclient/images/icon-app.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        AdvancedDialog.setWindowIcon(icon)
        self.verticalLayout = QtGui.QVBoxLayout(AdvancedDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtGui.QTabWidget(AdvancedDialog)
        self.tabWidget.setTabPosition(QtGui.QTabWidget.North)
        self.tabWidget.setTabShape(QtGui.QTabWidget.Rounded)
        self.tabWidget.setIconSize(QtCore.QSize(16, 16))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtGui.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.tab)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtGui.QLabel(self.tab)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        spacerItem = QtGui.QSpacerItem(218, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.analyseButton = QtGui.QPushButton(self.tab)
        self.analyseButton.setMinimumSize(QtCore.QSize(100, 0))
        self.analyseButton.setObjectName("analyseButton")
        self.horizontalLayout.addWidget(self.analyseButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.listWidget = QtGui.QListWidget(self.tab)
        self.listWidget.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout_2.addWidget(self.listWidget)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.updateLabel = QtGui.QLabel(self.tab)
        self.updateLabel.setText("")
        self.updateLabel.setObjectName("updateLabel")
        self.horizontalLayout_2.addWidget(self.updateLabel)
        spacerItem1 = QtGui.QSpacerItem(118, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.updateButton = QtGui.QPushButton(self.tab)
        self.updateButton.setObjectName("updateButton")
        self.horizontalLayout_2.addWidget(self.updateButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.tabWidget.addTab(self.tab, "")
        self.verticalLayout.addWidget(self.tabWidget)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.buttonBox = QtGui.QDialogButtonBox(AdvancedDialog)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.horizontalLayout_3.addWidget(self.buttonBox)
        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.retranslateUi(AdvancedDialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), AdvancedDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), AdvancedDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(AdvancedDialog)

    def retranslateUi(self, AdvancedDialog):
        AdvancedDialog.setWindowTitle(QtGui.QApplication.translate("AdvancedDialog", "Advanced", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("AdvancedDialog", "Plugins:", None, QtGui.QApplication.UnicodeUTF8))
        self.analyseButton.setText(QtGui.QApplication.translate("AdvancedDialog", "Analyse Plugins", None, QtGui.QApplication.UnicodeUTF8))
        self.updateButton.setText(QtGui.QApplication.translate("AdvancedDialog", "Update", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QtGui.QApplication.translate("AdvancedDialog", "Updates", None, QtGui.QApplication.UnicodeUTF8))

from . import resources_rc
