# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created: Sat Dec 14 02:04:15 2013
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Main(object):
    def setupUi(self, Main):
        Main.setObjectName("Main")
        Main.resize(900, 600)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/romano-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Main.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(Main)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.refreshButton = QtGui.QPushButton(self.centralwidget)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/refresh-tickets.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.refreshButton.setIcon(icon1)
        self.refreshButton.setIconSize(QtCore.QSize(24, 24))
        self.refreshButton.setObjectName("refreshButton")
        self.horizontalLayout.addWidget(self.refreshButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.ticketsTableView = QtGui.QTableView(self.centralwidget)
        self.ticketsTableView.setAlternatingRowColors(True)
        self.ticketsTableView.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.ticketsTableView.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.ticketsTableView.setObjectName("ticketsTableView")
        self.ticketsTableView.horizontalHeader().setCascadingSectionResizes(False)
        self.ticketsTableView.horizontalHeader().setHighlightSections(False)
        self.ticketsTableView.horizontalHeader().setStretchLastSection(True)
        self.ticketsTableView.verticalHeader().setVisible(False)
        self.ticketsTableView.verticalHeader().setHighlightSections(True)
        self.verticalLayout.addWidget(self.ticketsTableView)
        Main.setCentralWidget(self.centralwidget)
        self.toolBar = QtGui.QToolBar(Main)
        self.toolBar.setMovable(False)
        self.toolBar.setIconSize(QtCore.QSize(32, 32))
        self.toolBar.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolBar.setObjectName("toolBar")
        Main.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.statusBar = QtGui.QStatusBar(Main)
        self.statusBar.setObjectName("statusBar")
        Main.setStatusBar(self.statusBar)
        self.sessionToolbar = QtGui.QToolBar(Main)
        self.sessionToolbar.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.sessionToolbar.setMovable(False)
        self.sessionToolbar.setIconSize(QtCore.QSize(24, 24))
        self.sessionToolbar.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.sessionToolbar.setObjectName("sessionToolbar")
        Main.addToolBar(QtCore.Qt.TopToolBarArea, self.sessionToolbar)
        self.actionNewReception = QtGui.QAction(Main)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/reception-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionNewReception.setIcon(icon2)
        self.actionNewReception.setIconVisibleInMenu(True)
        self.actionNewReception.setObjectName("actionNewReception")
        self.actionNewDispatch = QtGui.QAction(Main)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/dispatch-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionNewDispatch.setIcon(icon3)
        self.actionNewDispatch.setIconVisibleInMenu(True)
        self.actionNewDispatch.setObjectName("actionNewDispatch")
        self.actionLogout = QtGui.QAction(Main)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/log-out.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionLogout.setIcon(icon4)
        self.actionLogout.setObjectName("actionLogout")
        self.actionUserName = QtGui.QAction(Main)
        self.actionUserName.setEnabled(False)
        self.actionUserName.setObjectName("actionUserName")
        self.toolBar.addAction(self.actionNewReception)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionNewDispatch)
        self.sessionToolbar.addAction(self.actionLogout)
        self.sessionToolbar.addAction(self.actionUserName)

        self.retranslateUi(Main)
        QtCore.QMetaObject.connectSlotsByName(Main)

    def retranslateUi(self, Main):
        Main.setWindowTitle(QtGui.QApplication.translate("Main", "Romano", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Main", "Camiones en tránsito", None, QtGui.QApplication.UnicodeUTF8))
        self.refreshButton.setText(QtGui.QApplication.translate("Main", "Actualizar lista", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBar.setWindowTitle(QtGui.QApplication.translate("Main", "toolBar", None, QtGui.QApplication.UnicodeUTF8))
        self.sessionToolbar.setWindowTitle(QtGui.QApplication.translate("Main", "toolBar_2", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNewReception.setText(QtGui.QApplication.translate("Main", "Nueva recepción", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNewReception.setToolTip(QtGui.QApplication.translate("Main", "Crear nuevo ticket de recepción", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNewReception.setShortcut(QtGui.QApplication.translate("Main", "Ctrl+R", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNewDispatch.setText(QtGui.QApplication.translate("Main", "Nuevo despacho", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNewDispatch.setToolTip(QtGui.QApplication.translate("Main", "Crear nuevo ticket de despacho", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNewDispatch.setShortcut(QtGui.QApplication.translate("Main", "Ctrl+D", None, QtGui.QApplication.UnicodeUTF8))
        self.actionLogout.setText(QtGui.QApplication.translate("Main", "Cerrar sesión", None, QtGui.QApplication.UnicodeUTF8))
        self.actionLogout.setToolTip(QtGui.QApplication.translate("Main", "Cerrar sesión", None, QtGui.QApplication.UnicodeUTF8))
        self.actionUserName.setText(QtGui.QApplication.translate("Main", "username", None, QtGui.QApplication.UnicodeUTF8))

from . import pixmaps_rc
