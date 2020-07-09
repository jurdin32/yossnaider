# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'frmCuentasCobrar.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!
import os
import threading
from threading import Lock

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *

from Clientes.views import getCliente, ListarTarjetas, RegistrarPago
from Cobradores.views import ListarCobrador
from Productos.frmBuscador import Ui_Dialog
from Productos.viewsVentas import *


class Ui_frmCuentasCobrar(QtWidgets.QMdiSubWindow):
    def __init__(self, parent=None):
        super(Ui_frmCuentasCobrar, self).__init__()
        self.setObjectName("frmCuentasCobrar")
        self.resize(902, 580)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./Recursos/caluladora.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
        self.groupBox = QtWidgets.QGroupBox(self)
        self.groupBox.setGeometry(QtCore.QRect(20, 40, 581, 181))
        self.groupBox.setObjectName("groupBox")
        self.txtCedula = QtWidgets.QLineEdit(self.groupBox)
        self.txtCedula.setGeometry(QtCore.QRect(10, 20, 191, 30))
        self.txtCedula.setReadOnly(True)
        self.txtCedula.setObjectName("txtCedula")
        self.txtNombres = QtWidgets.QLineEdit(self.groupBox)
        self.txtNombres.setGeometry(QtCore.QRect(10, 60, 561, 30))
        self.txtNombres.setReadOnly(True)
        self.txtNombres.setObjectName("txtNombres")
        self.txtDireccion = QtWidgets.QLineEdit(self.groupBox)
        self.txtDireccion.setGeometry(QtCore.QRect(10, 100, 561, 30))
        self.txtDireccion.setReadOnly(True)
        self.txtDireccion.setObjectName("txtDireccion")
        self.txtCiudad = QtWidgets.QLineEdit(self.groupBox)
        self.txtCiudad.setGeometry(QtCore.QRect(10, 140, 191, 30))
        self.txtCiudad.setReadOnly(True)
        self.txtCiudad.setObjectName("txtCiudad")
        self.txtZona = QtWidgets.QLineEdit(self.groupBox)
        self.txtZona.setGeometry(QtCore.QRect(230, 140, 171, 30))
        self.txtZona.setReadOnly(True)
        self.txtZona.setObjectName("txtZona")
        self.txtTelefono = QtWidgets.QLineEdit(self.groupBox)
        self.txtTelefono.setGeometry(QtCore.QRect(420, 140, 151, 30))
        self.txtTelefono.setReadOnly(True)
        self.txtTelefono.setObjectName("txtTelefono")
        self.btnBuscar = QtWidgets.QPushButton(self.groupBox)
        self.btnBuscar.setGeometry(QtCore.QRect(210, 20, 41, 30))
        self.btnBuscar.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("./Recursos/buscar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnBuscar.setIcon(icon1)
        self.btnBuscar.setObjectName("btnBuscar")
        self.groupBox_2 = QtWidgets.QGroupBox(self)
        self.groupBox_2.setGeometry(QtCore.QRect(20, 230, 281, 331))
        self.groupBox_2.setObjectName("groupBox_2")
        self.tCuentas = QtWidgets.QTableWidget(self.groupBox_2)
        self.tCuentas.setGeometry(QtCore.QRect(10, 20, 261, 301))
        self.tCuentas.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.tCuentas.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tCuentas.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tCuentas.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tCuentas.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tCuentas.setObjectName("tCuentas")
        self.tCuentas.setColumnCount(3)
        self.tCuentas.setRowCount(0)
        self.tCuentas.setColumnWidth(0,30)
        self.tCuentas.setColumnWidth(1, 90)
        self.tCuentas.setColumnWidth(2, 90)
        self.tCuentas.setHorizontalHeaderLabels(["ID", "FECHA", "VALOR"])


        self.tCuentas.verticalHeader().setVisible(True)
        self.groupBox_3 = QtWidgets.QGroupBox(self)
        self.groupBox_3.setGeometry(QtCore.QRect(320, 230, 281, 331))
        self.groupBox_3.setObjectName("groupBox_3")
        self.tDetalles = QtWidgets.QTableWidget(self.groupBox_3)
        self.tDetalles.setGeometry(QtCore.QRect(10, 20, 261, 301))
        self.tDetalles.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.tDetalles.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tDetalles.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tDetalles.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tDetalles.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tDetalles.setObjectName("tDetalles")
        self.tDetalles.setColumnCount(3)
        self.tDetalles.setRowCount(0)
        self.tDetalles.setHorizontalHeaderLabels(["COD.","FECHA", "ABONO"])
        self.tDetalles.verticalHeader().setVisible(False)
        self.tDetalles.setColumnWidth(0,20)
        self.tDetalles.setColumnWidth(1,100)
        self.tDetalles.setColumnWidth(2,100)
        self.groupBox_4 = QtWidgets.QGroupBox(self)
        self.groupBox_4.setGeometry(QtCore.QRect(610, 40, 281, 521))
        self.groupBox_4.setObjectName("groupBox_4")
        self.label = QtWidgets.QLabel(self.groupBox_4)
        self.label.setGeometry(QtCore.QRect(20, 30, 53, 31))
        self.label.setObjectName("label")
        self.deFecha = QtWidgets.QDateEdit(self.groupBox_4)
        self.deFecha.setGeometry(QtCore.QRect(90, 30, 181, 30))
        self.deFecha.setObjectName("deFecha")

        self.label_2 = QtWidgets.QLabel(self.groupBox_4)
        self.label_2.setGeometry(QtCore.QRect(20, 150, 71, 31))
        self.label_2.setObjectName("label_2")

        self.dsPorCobrar = QtWidgets.QDoubleSpinBox(self.groupBox_4)
        self.dsPorCobrar.setGeometry(QtCore.QRect(90, 150, 181, 30))
        self.dsPorCobrar.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.dsPorCobrar.setReadOnly(True)
        self.dsPorCobrar.setMaximum(999999999.99)
        self.dsPorCobrar.setObjectName("dsPorCobrar")

        self.label_3 = QtWidgets.QLabel(self.groupBox_4)
        self.label_3.setGeometry(QtCore.QRect(20, 70, 53, 31))
        self.label_3.setObjectName("label_3")

        self.txtNota = QtWidgets.QLineEdit(self.groupBox_4)
        self.txtNota.setGeometry(QtCore.QRect(90, 70, 181, 30))
        self.txtNota.setObjectName("txtNota")
        self.txtNota.setAlignment(QtCore.Qt.AlignCenter)

        self.txtRecibo = QtWidgets.QLineEdit(self.groupBox_4)
        self.txtRecibo.setGeometry(QtCore.QRect(90, 110, 181, 30))
        self.txtRecibo.setObjectName("txtRecibo")
        self.txtRecibo.setAlignment(QtCore.Qt.AlignCenter)

        self.dsAbono = QtWidgets.QDoubleSpinBox(self.groupBox_4)
        self.dsAbono.setGeometry(QtCore.QRect(90, 190, 181, 30))
        self.dsAbono.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.dsAbono.setReadOnly(False)
        self.dsAbono.setMaximum(999999999.99)
        self.dsAbono.setObjectName("dsAbono")
        self.dsSaldo = QtWidgets.QDoubleSpinBox(self.groupBox_4)
        self.dsSaldo.setGeometry(QtCore.QRect(90, 230, 181, 30))
        self.dsSaldo.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.dsSaldo.setReadOnly(True)
        self.dsSaldo.setMaximum(999999999.99)
        self.dsSaldo.setObjectName("dsSaldo")
        self.label_4 = QtWidgets.QLabel(self.groupBox_4)
        self.label_4.setGeometry(QtCore.QRect(20, 190, 71, 31))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.groupBox_4)
        self.label_5.setGeometry(QtCore.QRect(20, 230, 71, 31))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.groupBox_4)
        self.label_6.setGeometry(QtCore.QRect(20, 280, 71, 31))
        self.label_6.setObjectName("label_6")

        self.label_10 = QtWidgets.QLabel(self.groupBox_4)
        self.label_10.setGeometry(QtCore.QRect(20, 110, 71, 31))
        self.label_10.setObjectName("label_10")

        self.cbCobrador = QtWidgets.QComboBox(self.groupBox_4)
        self.cbCobrador.setGeometry(QtCore.QRect(90, 280, 181, 30))
        self.cbCobrador.setObjectName("cbCobrador")
        self.btnProcesar = QtWidgets.QPushButton(self.groupBox_4)
        self.btnProcesar.setGeometry(QtCore.QRect(90, 330, 180, 35))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("./Recursos/pagos.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnProcesar.setIcon(icon2)
        self.btnProcesar.setObjectName("btnProcesar")
        self.btnReporte = QtWidgets.QPushButton(self.groupBox_4)
        self.btnReporte.setGeometry(QtCore.QRect(90, 380, 180, 35))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("./Recursos/impresora.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnReporte.setIcon(icon3)
        self.btnReporte.setObjectName("btnReporte")
        self.btnEstadoCuenta = QtWidgets.QPushButton(self.groupBox_4)
        self.btnEstadoCuenta.setGeometry(QtCore.QRect(90, 430, 180, 35))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("./Recursos/estadoCuenta.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnEstadoCuenta.setIcon(icon4)
        self.btnEstadoCuenta.setObjectName("btnEstadoCuenta")
        style = "QHeaderView::section {background:#10608D;color:#FFFFFF;}"
        self.tCuentas.horizontalHeader().setStyleSheet(style)
        self.tDetalles.horizontalHeader().setStyleSheet(style)
        self.rutaJar= os.path.abspath(os.path.join(os.path.dirname(__file__), "../Reportes/Reporte.jar"))
        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)


        self.cliente_id=0
        self.traerCobradores()
        self.valorPagar=0
        self.nota=0

        self.btnBuscar.clicked.connect(self.cargarCliente)
        self.tCuentas.clicked.connect(self.cargarTarjetas)
        self.tDetalles.clicked.connect(self.verDetallesPago)
        self.btnProcesar.clicked.connect(self.registrarPago)
        self.dsAbono.valueChanged.connect(self.Calcularsaldo)
        self.btnEstadoCuenta.clicked.connect(self.reporteEstadoCuenta)
        self.btnReporte.clicked.connect(self.reporteVentas)

    def reporteEstadoCuenta(self):
        try:
            if int(self.txtNota.text())>0:
                ruta= "../Reportes/rptEstadoCuenta.jasper"
                reporte = os.path.abspath(os.path.join(os.path.dirname(__file__), ruta))
                os.popen('java -jar "%s" "%s" "%s" "%s"' % (str(self.rutaJar), str(reporte), "venta_id", str(self.txtNota.text())))
                QMessageBox.information(self, "YOSSNAIDER",
                                        "Espere mientras se genera el Documento, esto puede tomar tiempo.",
                                        buttons=QMessageBox.Ok)
            else:
                QMessageBox.critical(self, "Error",
                                        "Seleccione Primero un Registro en el panel de Cuentas.",
                                        buttons=QMessageBox.Ok)
        except:
            QMessageBox.critical(self, "Error",
                                    "Seleccione Primero un Registro en el panel de Cuentas.",
                                    buttons=QMessageBox.Ok)

    def reporteVentas(self):
        if self.cliente_id>0:
            ruta="../Reportes/rptCuentasCliente.jasper"
            reporte = os.path.abspath(os.path.join(os.path.dirname(__file__), ruta))
            os.popen('java -jar "%s" "%s" "%s" "%s"' % (str(self.rutaJar), str(reporte),"cliente_id",str(self.cliente_id)))
            QMessageBox.information(self, "YOSSNAIDER",
                                    "Espere mientras se genera el Documento, esto puede tomar tiempo.",
                                    buttons=QMessageBox.Ok)
        else:
            QMessageBox.warning(self, "Error","Primero Seleccione un cliente..!",buttons=QMessageBox.Ok)

    def Calcularsaldo(self):
        porcobrar=self.dsPorCobrar.value()
        abono=self.dsAbono.value()
        saldo=float(porcobrar)-float(abono)
        self.dsSaldo.setValue(saldo)

    def sumarAbonos(self):
        suma = 0
        for i in range(self.tDetalles.rowCount()):
            suma+= float(self.tDetalles.item(i,2).text())
        saldo= round(self.valorPagar - suma,2)
        print(saldo)
        self.dsPorCobrar.setValue(saldo)


    def registrarPago(self):
        try:
            if self.dsAbono.value()>self.dsPorCobrar.value():
                QMessageBox.critical(self, "Información", " El Abono excede el saldo..!",
                                        buttons=QMessageBox.Ok)
            elif self.dsSaldo.value()==0 and self.dsAbono.value()>0 and len(self.txtRecibo.text())>0:
                CambiarEstado(int(self.txtNota.text()))
                self.cargarVentas()
                RegistrarPago(int(self.txtNota.text()), self.deFecha.date().toString("yyyy-MM-dd"),
                                       float(self.dsAbono.value()), self.cbCobrador.currentData(),self.txtRecibo.text())
                QMessageBox.information(self,"YOSSNAIDER","El Pago se ha registrado correctamente..!",buttons=QMessageBox.Ok)
            elif self.dsAbono.value()>0 and self.dsPorCobrar.value()>0 and len(self.txtRecibo.text())>0:
                RegistrarPago(int(self.txtNota.text()),self.deFecha.date().toString("yyyy-MM-dd"),float(self.dsAbono.value()),self.cbCobrador.currentData(),self.txtRecibo.text())
                QMessageBox.information(self,"YOSSNAIDER", "El Pago se ha registrado correctamente..!",buttons=QMessageBox.Ok)
            elif len(self.txtRecibo.text())==0:
                QMessageBox.critical(self, "No se puede Registrar", "El Campo No. de Recibo es Obligatorio..!", buttons=QMessageBox.Ok)
            else:
                QMessageBox.information(self,"YOSSNAIDER", "No hay nada que pagar..!",buttons=QMessageBox.Ok)
            self.cargarTarjetas()
            self.dsAbono.setValue(0)
        except Exception as error:
            print(error)


    def verDetallesPago(self):
        print("Aqui el detalle del pago")

    def traerCobradores(self):
        for cobrador in ListarCobrador():
            self.cbCobrador.addItem(cobrador.nombre,cobrador.id)

    def cargarTarjetas(self):
        self.nota = int(self.tCuentas.item(self.tCuentas.currentRow(),0).text())
        self.valorPagar = float(self.tCuentas.item(self.tCuentas.currentRow(),2).text())
        print(float(self.tCuentas.item(self.tCuentas.currentRow(),2).text()))
        self.txtRecibo.setText("")
        self.txtNota.setText(str.zfill(str(self.nota), 12))
        lista = ListarTarjetas(self.nota)
        self.tDetalles.setRowCount(0)
        self.tDetalles.clear()
        self.tDetalles.setHorizontalHeaderLabels(["COD","FECHA", "ABONO"])
        for tarjeta in lista:
            rowPosition = self.tDetalles.rowCount()
            self.tDetalles.insertRow(rowPosition)
            codigo = QTableWidgetItem(str(tarjeta.id))
            codigo.setTextAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
            self.tDetalles.setItem(rowPosition, 0, codigo)

            fecha = QTableWidgetItem(str(tarjeta.fecha))
            fecha.setTextAlignment(QtCore.Qt.AlignCenter|QtCore.Qt.AlignVCenter)
            self.tDetalles.setItem(rowPosition, 1, fecha)

            valor = QTableWidgetItem(str(round(tarjeta.abono,2)))
            valor.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
            self.tDetalles.setItem(rowPosition, 2, valor)
        self.sumarAbonos()
        self.Calcularsaldo()


    def cargarCliente(self):
        frm = Ui_Dialog(self)
        frm.exec_()
        if frm.cliente_id > 0:
            self.tCuentas.clear()
            self.tCuentas.setRowCount(0)
            self.tDetalles.clear()
            self.tDetalles.setRowCount(0)
            self.tDetalles.setHorizontalHeaderLabels(["COD.","FECHA", "ABONO"])

            cliente=getCliente(frm.cliente_id)
            self.cliente_id=frm.cliente_id
            self.txtNombres.setText(cliente.nombres)
            self.txtCedula.setText(cliente.cedula)
            self.txtCiudad.setText(cliente.ciudad.nombre)
            self.cbCobrador.setCurrentText(cliente.cobrador.nombre)
            if cliente.zona=="C":
                self.txtZona.setText("Centro")
            elif cliente.zona=="N":
                self.txtZona.setText("Norte")
            if cliente.zona=="S":
                self.txtZona.setText("Sur")
            self.txtTelefono.setText(cliente.telefono)
            self.txtDireccion.setText(cliente.direccion)
            self.cargarVentas()


    def cargarVentas(self):
        self.valorPagar =0
        self.tCuentas.setRowCount(0)
        self.tCuentas.clear()
        self.tCuentas.setHorizontalHeaderLabels(["ID", "FECHA", "VALOR"])
        for venta in ListarVentasCliente(self.cliente_id):
            if venta.estado:
                color = QtGui.QColor(158, 24, 3)
                fore=QtGui.QColor(255, 255, 255)
            else:
                color = QtGui.QColor(13, 143, 10)
                fore = QtGui.QColor(255, 255, 255)
            rowPosition = self.tCuentas.rowCount()
            self.tCuentas.insertRow(rowPosition)
            id = QTableWidgetItem(str(venta.id))
            id.setTextAlignment(QtCore.Qt.AlignCenter|QtCore.Qt.AlignVCenter)
            id.setBackground(color)
            id.setForeground(fore)
            self.tCuentas.setItem(rowPosition, 0, id)

            fecha=QTableWidgetItem(str(venta.fecha))
            fecha.setTextAlignment(QtCore.Qt.AlignCenter|QtCore.Qt.AlignVCenter)
            fecha.setBackground(color)
            fecha.setForeground(fore)
            self.tCuentas.setItem(rowPosition, 1, fecha)

            valor = QTableWidgetItem(str(venta.valor))
            valor.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
            valor.setBackground(color)
            valor.setForeground(fore)
            self.tCuentas.setItem(rowPosition, 2, valor)

    def retranslateUi(self, frmCuentasCobrar):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("frmCuentasCobrar", "Registro de Cuentas por Cobrar"))
        self.groupBox.setTitle(_translate("frmCuentasCobrar", "Cliente"))
        self.groupBox_2.setTitle(_translate("frmCuentasCobrar", "Cuentas"))
        self.groupBox_3.setTitle(_translate("frmCuentasCobrar", "Detalles"))
        self.groupBox_4.setTitle(_translate("frmCuentasCobrar", "Registro de pagos"))
        self.label.setText(_translate("frmCuentasCobrar", "Fecha"))
        self.label_2.setText(_translate("frmCuentasCobrar", "Por Cobrar"))
        self.dsPorCobrar.setPrefix(_translate("frmCuentasCobrar", "$ "))
        self.label_3.setText(_translate("frmCuentasCobrar", "Nota No."))
        self.dsAbono.setPrefix(_translate("frmCuentasCobrar", "$ "))
        self.dsSaldo.setPrefix(_translate("frmCuentasCobrar", "$ "))
        self.label_4.setText(_translate("frmCuentasCobrar", "Abono"))
        self.label_5.setText(_translate("frmCuentasCobrar", "Saldo"))
        self.label_6.setText(_translate("frmCuentasCobrar", "Cobrador"))
        self.label_10.setText(_translate("frmCuentasCobrar", "No. Recibo"))
        self.btnProcesar.setText(_translate("frmCuentasCobrar", "Procesar Pago"))
        self.btnReporte.setText(_translate("frmCuentasCobrar", "Reporte"))
        self.btnEstadoCuenta.setText(_translate("frmCuentasCobrar", "Estado de Cuenta"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_frmCuentasCobrar()
    ui.show()
    sys.exit(app.exec_())

