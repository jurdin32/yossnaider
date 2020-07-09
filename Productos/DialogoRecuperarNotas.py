# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DialogoRecuperarNotas.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem

from Clientes.views import Buscar_Nombre
from Productos.viewsVentas import Buscar_Ventas, getVenta


class Ui_DialogRecuperarVentas(QtWidgets.QDialog):
    def __init__(self, venta_id=0, parent=None):
        super(Ui_DialogRecuperarVentas, self).__init__(parent=parent)
        self.setObjectName("DialogRecuperarVentas")
        self.resize(752, 538)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../Recursos/volver.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
        self.cFecha = QtWidgets.QCalendarWidget(self)
        self.cFecha.setGeometry(QtCore.QRect(10, 10, 352, 211))
        self.cFecha.setGridVisible(True)
        self.cFecha.setObjectName("cFecha")
        self.txtNombre = QtWidgets.QLineEdit(self)
        self.txtNombre.setGeometry(QtCore.QRect(10, 230, 351, 30))
        self.txtNombre.setObjectName("txtNombre")
        self.txtCodigo = QtWidgets.QLineEdit(self)
        self.txtCodigo.setGeometry(QtCore.QRect(380, 120, 331, 30))
        self.txtCodigo.setObjectName("txtCodigo")
        self.tClientes = QtWidgets.QTableWidget(self)
        self.tClientes.setGeometry(QtCore.QRect(10, 270, 351, 241))
        self.tClientes.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.tClientes.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tClientes.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tClientes.setAlternatingRowColors(True)
        self.tClientes.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tClientes.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tClientes.setRowCount(0)
        self.tClientes.setColumnCount(2)
        self.tClientes.setColumnWidth(0,70)
        self.tClientes.setColumnWidth(1,257)
        self.tClientes.setObjectName("tClientes")
        style = "QHeaderView::section {background:#10608D;color:#FFFFFF;}"
        self.tClientes.horizontalHeader().setStyleSheet(style)
        item = QtWidgets.QTableWidgetItem()
        self.tClientes.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tClientes.setHorizontalHeaderItem(1, item)
        self.tClientes.horizontalHeader().setVisible(True)
        self.tClientes.verticalHeader().setVisible(False)
        self.groupBox = QtWidgets.QGroupBox(self)
        self.groupBox.setGeometry(QtCore.QRect(380, 10, 361, 101))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.rbPagadas = QtWidgets.QRadioButton(self.groupBox)
        self.rbPagadas.setGeometry(QtCore.QRect(20, 36, 95, 20))
        self.rbPagadas.setObjectName("rbPagadas")
        self.rbTodas = QtWidgets.QRadioButton(self.groupBox)
        self.rbTodas.setGeometry(QtCore.QRect(20, 68, 95, 20))
        self.rbTodas.setChecked(True)
        self.rbTodas.setObjectName("rbTodas")
        self.rbPorPagar = QtWidgets.QRadioButton(self.groupBox)
        self.rbPorPagar.setGeometry(QtCore.QRect(19, 5, 95, 20))
        self.rbPorPagar.setObjectName("rbPorPagar")
        self.rbFecha = QtWidgets.QCheckBox(self.groupBox)
        self.rbFecha.setGeometry(QtCore.QRect(160, 70, 121, 20))
        self.rbFecha.setObjectName("rbFecha")
        self.tVentas = QtWidgets.QTableWidget(self)
        self.tVentas.setGeometry(QtCore.QRect(380, 160, 361, 351))
        self.tVentas.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.tVentas.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tVentas.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tVentas.setAlternatingRowColors(True)
        self.tVentas.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tVentas.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tVentas.horizontalHeader().setStyleSheet(style)
        self.tVentas.setRowCount(0)
        self.tVentas.setColumnCount(4)
        self.tVentas.setObjectName("tVentas")
        item = QtWidgets.QTableWidgetItem()
        self.tVentas.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tVentas.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tVentas.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tVentas.setHorizontalHeaderItem(3, item)
        self.tVentas.horizontalHeader().setVisible(True)
        self.tVentas.horizontalHeader().setDefaultSectionSize(85)
        self.tVentas.verticalHeader().setVisible(False)
        self.cClientes = QtWidgets.QCheckBox(self)
        self.cClientes.setGeometry(QtCore.QRect(540, 50, 121, 20))
        self.cClientes.setText("")
        self.cClientes.setTristate(False)
        self.cClientes.setObjectName("cClientes")


        self.venta_id=0
        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

        self.traerClientes()
        self.traerVentas()

        self.txtNombre.textChanged.connect(self.traerClientes)
        self.txtCodigo.textChanged.connect(self.ventaUnica)
        self.rbFecha.clicked.connect(self.traerVentas)
        self.rbTodas.clicked.connect(self.traerVentas)
        self.rbPagadas.clicked.connect(self.traerVentas)
        self.rbPorPagar.clicked.connect(self.traerVentas)
        self.tClientes.clicked.connect(self.traerVentas)
        self.cClientes.clicked.connect(self.traerVentas)
        self.cFecha.clicked[QtCore.QDate].connect(self.traerVentas)
        self.tVentas.doubleClicked.connect(self.seleccionarVenta)

    def retranslateUi(self, DialogRecuperarVentas):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("DialogRecuperarVentas", "Recuperar Ventas"))
        self.txtNombre.setPlaceholderText(_translate("DialogRecuperarVentas", "Esccriba Nombre del Cliente"))
        self.txtCodigo.setPlaceholderText(_translate("DialogRecuperarVentas", "Buscar por Código de Nota de Venta"))
        item = self.tClientes.horizontalHeaderItem(0)
        item.setText(_translate("DialogRecuperarVentas", "ID"))
        item = self.tClientes.horizontalHeaderItem(1)
        item.setText(_translate("DialogRecuperarVentas", "NOMBRE"))
        self.rbPagadas.setText(_translate("DialogRecuperarVentas", "Pagadas"))
        self.rbTodas.setText(_translate("DialogRecuperarVentas", "Todas"))
        self.rbPorPagar.setText(_translate("DialogRecuperarVentas", "Por Pagar"))
        self.rbFecha.setText(_translate("DialogRecuperarVentas", "Usar la Fecha"))
        self.cClientes.setText(_translate("DialogRecuperarVentas", "Usar Cliente seleccionado"))
        item = self.tVentas.horizontalHeaderItem(0)
        item.setText(_translate("DialogRecuperarVentas", "ID"))
        item = self.tVentas.horizontalHeaderItem(1)
        item.setText(_translate("DialogRecuperarVentas", "FECHA"))
        item = self.tVentas.horizontalHeaderItem(2)
        item.setText(_translate("DialogRecuperarVentas", "VALOR"))
        item = self.tVentas.horizontalHeaderItem(3)
        item.setText(_translate("DialogRecuperarVentas", "ESTADO"))

    def seleccionarVenta(self):
        self.venta_id=int(self.tVentas.item(self.tVentas.currentRow(),0).text())
        self.close()

    def traerClientes(self):
        self.tClientes.setRowCount(0)
        self.tClientes.setHorizontalHeaderLabels(["ID", "NOMBRE"])
        for cliente in Buscar_Nombre(self.txtNombre.text()):
            rowPosition = self.tClientes.rowCount()
            self.tClientes.insertRow(rowPosition)

            id = QTableWidgetItem(str(cliente.id))
            id.setTextAlignment(QtCore.Qt.AlignCenter)
            self.tClientes.setItem(rowPosition, 0, id)
            self.tClientes.setItem(rowPosition, 1, QTableWidgetItem(str(cliente.nombres)))

    def ventaUnica(self):
        self.tVentas.setRowCount(0)
        self.tVentas.clear()
        self.tVentas.setHorizontalHeaderLabels(["ID", "FECHA", "VALOR", 'ESTADO'])
        numero=0
        try:
            numero=int(self.txtCodigo.text())
            venta = getVenta(numero)
            print(venta.fecha, venta.valor, venta.estado)
            self.tVentas.setRowCount(0)
            self.tVentas.clear()
            rowPosition = self.tVentas.rowCount()
            self.tVentas.insertRow(rowPosition)
            id = QTableWidgetItem(str(venta.id))
            id.setTextAlignment(QtCore.Qt.AlignCenter)
            self.tVentas.setItem(rowPosition, 0, id)
            self.tVentas.setItem(rowPosition, 1, QTableWidgetItem(str(venta.fecha)))
            self.tVentas.setItem(rowPosition, 2, QTableWidgetItem(str(venta.valor)))
            if venta.estado:
                self.tVentas.setItem(rowPosition, 3, QTableWidgetItem("Por Pagar"))
            else:
                self.tVentas.setItem(rowPosition, 3, QTableWidgetItem("Pagado"))
        except:
            numero=0
            self.traerVentas()

    def traerVentas(self):
        todas=False
        fecha=""
        estado=None
        id=0

        if self.cClientes.isChecked():
            try:
                id=int(self.tClientes.item(self.tClientes.currentRow(),0).text())
            except:
                id=0
        else:
            id=0

        if self.rbPorPagar.isChecked():
            estado=True
            fecha = ""
            todas = True

        if self.rbPagadas.isChecked():
            estado=False
            fecha = ""
            todas = True

        if self.rbTodas.isChecked():
            fecha = ""
            estado = None
            todas=True

        if self.rbFecha.isChecked():
            fecha = (self.cFecha.selectedDate().toString("yyyy-MM-dd"))


        self.tVentas.setRowCount(0)
        self.tVentas.clear()
        self.tVentas.setHorizontalHeaderLabels(["ID", "FECHA", "VALOR", 'ESTADO'])

        for venta in Buscar_Ventas(id=id,estado=estado,fecha=fecha,todas=todas):
            rowPosition = self.tVentas.rowCount()
            self.tVentas.insertRow(rowPosition)
            id = QTableWidgetItem(str(venta.id))
            id.setTextAlignment(QtCore.Qt.AlignCenter)
            self.tVentas.setItem(rowPosition, 0, id)
            self.tVentas.setItem(rowPosition, 1, QTableWidgetItem(str(venta.fecha)))
            self.tVentas.setItem(rowPosition, 2, QTableWidgetItem(str(venta.valor)))
            if venta.estado:
                self.tVentas.setItem(rowPosition, 3, QTableWidgetItem("Por Pagar"))
            else:
                self.tVentas.setItem(rowPosition, 3, QTableWidgetItem("Pagado"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_DialogRecuperarVentas()
    ui.show()
    sys.exit(app.exec_())

