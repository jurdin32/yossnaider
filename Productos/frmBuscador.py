# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'frmBuscador.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem, QAbstractItemView

from Clientes.views import Buscar_Nombre


class Ui_Dialog(QtWidgets.QDialog):
    def __init__(self,cliente_id=0, parent=None):
        super(Ui_Dialog, self).__init__(parent=parent)
        self.setObjectName("Dialog")
        self.resize(675, 500)
        self.txtNombreCliente = QtWidgets.QLineEdit(self)
        self.txtNombreCliente.setGeometry(QtCore.QRect(20, 40, 641, 30))
        self.txtNombreCliente.setObjectName("txtNombreCliente")
        self.tabla = QtWidgets.QTableWidget(self)
        self.tabla.setGeometry(QtCore.QRect(20, 80, 641, 371))
        self.tabla.setColumnCount(6)
        self.tabla.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.tabla.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tabla.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tabla.setSelectionBehavior(self.tabla.SelectRows)
        self.tabla.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tabla.verticalHeader().setVisible(False)
        self.tabla.setColumnWidth(0, 30)
        self.tabla.setColumnWidth(1, 100)
        self.tabla.setColumnWidth(2, 100)
        self.tabla.setColumnWidth(3, 200)
        self.tabla.setColumnWidth(4, 150)
        self.tabla.setColumnWidth(5, 120)
        self.tabla.setObjectName("tabla")
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(20, 460, 641, 16))
        self.label.setObjectName("label")

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

        self.cliente_id=0
        self.traerClientes()
        self.txtNombreCliente.textChanged.connect(self.traerClientes)
        self.tabla.doubleClicked.connect(self.seleccionar)

    def traerClientes(self):
        style = "QHeaderView::section {background:#10608D;color:#FFFFFF;}"
        self.tabla.horizontalHeader().setStyleSheet(style)
        self.tabla.setRowCount(0)
        self.tabla.setHorizontalHeaderLabels(["ID","INTERNO","CEDULA","NOMBRE","CIUDAD","TELEFONO"])
        for cliente in Buscar_Nombre(self.txtNombreCliente.text()):
            rowPosition = self.tabla.rowCount()
            self.tabla.insertRow(rowPosition)

            id = QTableWidgetItem(str(cliente.id))
            id.setTextAlignment(QtCore.Qt.AlignCenter)
            self.tabla.setItem(rowPosition, 0, id)

            interno = QTableWidgetItem(str(cliente.interno))
            interno.setTextAlignment(QtCore.Qt.AlignCenter)
            self.tabla.setItem(rowPosition, 1, interno)

            cedula = QTableWidgetItem(str(cliente.cedula))
            cedula.setTextAlignment(QtCore.Qt.AlignCenter)
            self.tabla.setItem(rowPosition, 2, cedula)

            self.tabla.setItem(rowPosition, 3, QTableWidgetItem(str(cliente.nombres)))
            self.tabla.setItem(rowPosition, 4, QTableWidgetItem(str(cliente.ciudad.nombre)))
            self.tabla.setItem(rowPosition, 5, QTableWidgetItem(str(cliente.telefono)))

    def seleccionar(self):
        self.cliente_id = int(self.tabla.item(self.tabla.currentRow(),0).text())
        self.close()


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Doble Clic Para Seleccionar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_Dialog()
    ui.show()
    sys.exit(app.exec_())
