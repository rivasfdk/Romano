# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add_transaction.ui'
#
# Created: Mon Aug  6 14:46:29 2012
#      by: pyside-uic 0.2.13 running on PySide 1.1.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_AddTransaction(object):
    def setupUi(self, AddTransaction):
        AddTransaction.setObjectName("AddTransaction")
        AddTransaction.resize(584, 540)
        self.verticalLayout = QtGui.QVBoxLayout(AddTransaction)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtGui.QGroupBox(AddTransaction)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.ingredientButton = QtGui.QRadioButton(self.groupBox)
        self.ingredientButton.setChecked(True)
        self.ingredientButton.setObjectName("ingredientButton")
        self.horizontalLayout_2.addWidget(self.ingredientButton)
        self.productButton = QtGui.QRadioButton(self.groupBox)
        self.productButton.setObjectName("productButton")
        self.horizontalLayout_2.addWidget(self.productButton)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.verticalLayout.addWidget(self.groupBox)
        self.warehousesTableView = QtGui.QTableView(AddTransaction)
        self.warehousesTableView.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.warehousesTableView.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.warehousesTableView.setObjectName("warehousesTableView")
        self.warehousesTableView.horizontalHeader().setCascadingSectionResizes(False)
        self.warehousesTableView.horizontalHeader().setHighlightSections(False)
        self.warehousesTableView.horizontalHeader().setStretchLastSection(False)
        self.warehousesTableView.verticalHeader().setVisible(False)
        self.verticalLayout.addWidget(self.warehousesTableView)
        self.groupBox_2 = QtGui.QGroupBox(AddTransaction)
        self.groupBox_2.setTitle("")
        self.groupBox_2.setFlat(False)
        self.groupBox_2.setCheckable(False)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.sackButton = QtGui.QRadioButton(self.groupBox_2)
        self.sackButton.setChecked(True)
        self.sackButton.setObjectName("sackButton")
        self.horizontalLayout_3.addWidget(self.sackButton)
        self.grainButton = QtGui.QRadioButton(self.groupBox_2)
        self.grainButton.setObjectName("grainButton")
        self.horizontalLayout_3.addWidget(self.grainButton)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.verticalLayout.addWidget(self.groupBox_2)
        self.sackWidget = QtGui.QWidget(AddTransaction)
        self.sackWidget.setObjectName("sackWidget")
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.sackWidget)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem4)
        self.label = QtGui.QLabel(self.sackWidget)
        self.label.setObjectName("label")
        self.horizontalLayout_4.addWidget(self.label)
        self.sackSpinBox = QtGui.QSpinBox(self.sackWidget)
        self.sackSpinBox.setMinimumSize(QtCore.QSize(80, 0))
        self.sackSpinBox.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.sackSpinBox.setMaximum(999999)
        self.sackSpinBox.setObjectName("sackSpinBox")
        self.horizontalLayout_4.addWidget(self.sackSpinBox)
        self.label_3 = QtGui.QLabel(self.sackWidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        self.kgSackSpinBox = QtGui.QSpinBox(self.sackWidget)
        self.kgSackSpinBox.setMinimumSize(QtCore.QSize(80, 0))
        self.kgSackSpinBox.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.kgSackSpinBox.setMaximum(999999)
        self.kgSackSpinBox.setProperty("value", 60)
        self.kgSackSpinBox.setObjectName("kgSackSpinBox")
        self.horizontalLayout_4.addWidget(self.kgSackSpinBox)
        self.label_4 = QtGui.QLabel(self.sackWidget)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.totalSackSpinBox = QtGui.QSpinBox(self.sackWidget)
        self.totalSackSpinBox.setEnabled(False)
        self.totalSackSpinBox.setMinimumSize(QtCore.QSize(150, 0))
        self.totalSackSpinBox.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.totalSackSpinBox.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        self.totalSackSpinBox.setMaximum(999999)
        self.totalSackSpinBox.setObjectName("totalSackSpinBox")
        self.horizontalLayout_4.addWidget(self.totalSackSpinBox)
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem5)
        self.verticalLayout.addWidget(self.sackWidget)
        self.grainWidget = QtGui.QWidget(AddTransaction)
        self.grainWidget.setObjectName("grainWidget")
        self.horizontalLayout_5 = QtGui.QHBoxLayout(self.grainWidget)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem6 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem6)
        self.label_2 = QtGui.QLabel(self.grainWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_5.addWidget(self.label_2)
        self.totalGrainSpinBox = QtGui.QSpinBox(self.grainWidget)
        self.totalGrainSpinBox.setMinimumSize(QtCore.QSize(150, 0))
        self.totalGrainSpinBox.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.totalGrainSpinBox.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        self.totalGrainSpinBox.setMaximum(999999)
        self.totalGrainSpinBox.setObjectName("totalGrainSpinBox")
        self.horizontalLayout_5.addWidget(self.totalGrainSpinBox)
        spacerItem7 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem7)
        self.verticalLayout.addWidget(self.grainWidget)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem8 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem8)
        self.cancelButton = QtGui.QPushButton(AddTransaction)
        self.cancelButton.setObjectName("cancelButton")
        self.horizontalLayout.addWidget(self.cancelButton)
        self.addTransactionButton = QtGui.QPushButton(AddTransaction)
        self.addTransactionButton.setObjectName("addTransactionButton")
        self.horizontalLayout.addWidget(self.addTransactionButton)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(AddTransaction)
        QtCore.QMetaObject.connectSlotsByName(AddTransaction)

    def retranslateUi(self, AddTransaction):
        AddTransaction.setWindowTitle(QtGui.QApplication.translate("AddTransaction", "Añadir transacción", None, QtGui.QApplication.UnicodeUTF8))
        self.ingredientButton.setText(QtGui.QApplication.translate("AddTransaction", "Ingredientes", None, QtGui.QApplication.UnicodeUTF8))
        self.productButton.setText(QtGui.QApplication.translate("AddTransaction", "Producto terminado", None, QtGui.QApplication.UnicodeUTF8))
        self.sackButton.setText(QtGui.QApplication.translate("AddTransaction", "Sacos", None, QtGui.QApplication.UnicodeUTF8))
        self.grainButton.setText(QtGui.QApplication.translate("AddTransaction", "Granel", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("AddTransaction", "Sacos", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("AddTransaction", "Kg/Saco", None, QtGui.QApplication.UnicodeUTF8))
        self.kgSackSpinBox.setSuffix(QtGui.QApplication.translate("AddTransaction", " Kg", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("AddTransaction", "Total", None, QtGui.QApplication.UnicodeUTF8))
        self.totalSackSpinBox.setSuffix(QtGui.QApplication.translate("AddTransaction", " Kg", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("AddTransaction", "Total granel", None, QtGui.QApplication.UnicodeUTF8))
        self.totalGrainSpinBox.setSuffix(QtGui.QApplication.translate("AddTransaction", " Kg", None, QtGui.QApplication.UnicodeUTF8))
        self.cancelButton.setText(QtGui.QApplication.translate("AddTransaction", "Cancelar", None, QtGui.QApplication.UnicodeUTF8))
        self.addTransactionButton.setText(QtGui.QApplication.translate("AddTransaction", "Agregar", None, QtGui.QApplication.UnicodeUTF8))

