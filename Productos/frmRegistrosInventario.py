# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'frmRegistrosInventario.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!
import datetime
import os

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem, QAbstractItemView, QMessageBox
from Productos.reportes import generarReporte
from Productos.views import *

class Ui_frmRegistrosInventario(QtWidgets.QMdiSubWindow):
    def __init__(self, parent=0):
        super(Ui_frmRegistrosInventario, self).__init__()
        self.setObjectName("frmRegistrosInventario")
        self.resize(799, 674)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./Recursos/impresora.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
        self.tProductos = QtWidgets.QTableWidget(self)
        self.tProductos.setGeometry(QtCore.QRect(20, 90, 761, 192))
        self.tProductos.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.tProductos.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tProductos.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tProductos.setObjectName("tProductos")
        self.tProductos.verticalHeader().setVisible(False)
        self.tProductos.setSelectionBehavior(self.tProductos.SelectRows)
        self.tProductos.setSelectionMode(QAbstractItemView.SingleSelection)

        self.tProductos.setColumnCount(5)
        self.tProductos.setRowCount(0)
        self.tProductos.setColumnWidth(0, 30)
        self.tProductos.setColumnWidth(1, 370)
        self.tProductos.setColumnWidth(4, 70)
        style = "QHeaderView::section {background:#10608D;color:#FFFFFF;}"
        self.tProductos.horizontalHeader().setStyleSheet(style)
        self.tProductos.setHorizontalHeaderLabels(["ID", "NOMBRE", "PRECIO", 'MARCA', 'STOCK'])

        self.tInventario = QtWidgets.QTableWidget(self)
        self.tInventario.setGeometry(QtCore.QRect(20, 290, 761, 271))
        self.tInventario.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.tInventario.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tInventario.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tInventario.setObjectName("tInventario")
        self.tInventario.setColumnCount(7)
        self.tInventario.setRowCount(0)
        self.tInventario.setColumnWidth(0, 30)
        self.tInventario.setColumnWidth(1, 370)
        self.tInventario.setColumnWidth(2, 30)
        self.tInventario.setColumnWidth(3, 60)
        self.tInventario.setColumnWidth(4, 70)
        self.tInventario.setColumnWidth(5, 70)
        self.tInventario.setColumnWidth(6, 70)
        self.tInventario.horizontalHeader().setStyleSheet(style)
        self.tInventario.verticalHeader().setVisible(False)
        self.tInventario.setSelectionBehavior(self.tProductos.SelectRows)
        self.tInventario.setSelectionMode(QAbstractItemView.SingleSelection)

        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(20, 50, 41, 21))
        self.label.setObjectName("label")
        self.txtBuscar = QtWidgets.QLineEdit(self)
        self.txtBuscar.setGeometry(QtCore.QRect(70, 50, 711, 30))
        self.txtBuscar.setObjectName("txtBuscar")
        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(550, 580, 53, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self)
        self.label_3.setGeometry(QtCore.QRect(550, 610, 53, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self)
        self.label_4.setGeometry(QtCore.QRect(550, 640, 53, 16))
        self.label_4.setObjectName("label_4")
        self.lbTotalIngresos = QtWidgets.QLabel(self)
        self.lbTotalIngresos.setGeometry(QtCore.QRect(620, 580, 80, 16))
        self.lbTotalIngresos.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.lbTotalIngresos.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbTotalIngresos.setObjectName("lbTotalIngresos")
        self.lbTotalEgresos = QtWidgets.QLabel(self)
        self.lbTotalEgresos.setGeometry(QtCore.QRect(620, 610, 80, 16))
        self.lbTotalEgresos.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.lbTotalEgresos.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbTotalEgresos.setObjectName("lbTotalEgresos")
        self.lbTotal = QtWidgets.QLabel(self)
        self.lbTotal.setGeometry(QtCore.QRect(620, 640, 80, 16))
        self.lbTotal.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.lbTotal.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbTotal.setObjectName("lbTotal")
        self.line = QtWidgets.QFrame(self)
        self.line.setGeometry(QtCore.QRect(620, 630, 80, 16))
        self.line.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.lbTotalEgresosCantidad = QtWidgets.QLabel(self)
        self.lbTotalEgresosCantidad.setGeometry(QtCore.QRect(720, 610, 53, 16))
        self.lbTotalEgresosCantidad.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.lbTotalEgresosCantidad.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbTotalEgresosCantidad.setObjectName("lbTotalEgresosCantidad")
        self.lbTotalIngresosCantidad = QtWidgets.QLabel(self)
        self.lbTotalIngresosCantidad.setGeometry(QtCore.QRect(720, 580, 53, 16))
        self.lbTotalIngresosCantidad.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.lbTotalIngresosCantidad.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbTotalIngresosCantidad.setObjectName("lbTotalIngresosCantidad")
        self.line_2 = QtWidgets.QFrame(self)
        self.line_2.setGeometry(QtCore.QRect(720, 630, 61, 16))
        self.line_2.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.lbTotalCantidad = QtWidgets.QLabel(self)
        self.lbTotalCantidad.setGeometry(QtCore.QRect(720, 640, 53, 16))
        self.lbTotalCantidad.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.lbTotalCantidad.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbTotalCantidad.setObjectName("lbTotalCantidad")

        self.btnReporte = QtWidgets.QPushButton(self)
        self.btnReporte.setGeometry(QtCore.QRect(20, 580, 141, 41))
        self.btnReporte.setIcon(icon)
        self.btnReporte.setObjectName("btnReporte")

        self.btnTodo = QtWidgets.QPushButton(self)
        self.btnTodo.setGeometry(QtCore.QRect(165, 580, 141, 41))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./Recursos/volver.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnTodo.setIcon(icon)
        self.btnTodo.setObjectName("btnTodo")

        self.btnGeneral = QtWidgets.QPushButton(self)
        self.btnGeneral.setGeometry(QtCore.QRect(310, 580, 141, 41))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./Recursos/impresora.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnGeneral.setIcon(icon)
        self.btnGeneral.setObjectName("btnGeneral")

        self.rutaJar = os.path.abspath(os.path.join(os.path.dirname(__file__), "../Reportes/Reporte.jar"))




        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

        self.id=0

        self.traerKardex()
        self.traerProductos()
        self.tProductos.clicked.connect(self.seleccionProducto)
        self.txtBuscar.textChanged.connect(self.buscar)
        self.btnReporte.clicked.connect(self.generarReportes)
        self.btnTodo.clicked.connect(self.volver)
        self.btnGeneral.clicked.connect(self.generarReportesGeneral)

    def retranslateUi(self, frmRegistrosInventario):
        _translate = QtCore.QCoreApplication.translate
        frmRegistrosInventario.setWindowTitle(_translate("frmRegistrosInventario", "Registros del Inventario de Productos"))
        self.label.setText(_translate("frmRegistrosInventario", "Buscar"))
        self.label_2.setText(_translate("frmRegistrosInventario", "Ingresos:"))
        self.label_3.setText(_translate("frmRegistrosInventario", "Egresos:"))
        self.label_4.setText(_translate("frmRegistrosInventario", "Total:"))
        self.lbTotalIngresos.setText(_translate("frmRegistrosInventario", "0.00"))
        self.lbTotalEgresos.setText(_translate("frmRegistrosInventario", "0.00"))
        self.lbTotal.setText(_translate("frmRegistrosInventario", "0.00"))
        self.lbTotalEgresosCantidad.setText(_translate("frmRegistrosInventario", "0"))
        self.lbTotalIngresosCantidad.setText(_translate("frmRegistrosInventario", "0"))
        self.lbTotalCantidad.setText(_translate("frmRegistrosInventario", "0"))
        self.btnReporte.setText(_translate("frmRegistrosInventario", "Generar Reporte"))
        self.btnTodo.setText(_translate("frmRegistrosInventario", "Recargar Todo"))
        self.btnGeneral.setText(_translate("frmRegistrosInventario", "Todo el kardex"))

    def volver(self):
        self.traerKardex()
        self.traerProductos()
        self.id=0

    def traerProductos(self):
        self.tProductos.clear()
        self.tProductos.setRowCount(0)
        self.tProductos.setHorizontalHeaderLabels(["ID", "NOMBRE", "PRECIO", 'MARCA', 'STOCK'])
        for producto in ListarProductos():
            rowPosition = self.tProductos.rowCount()
            self.tProductos.insertRow(rowPosition)
            id = QTableWidgetItem(str(producto.id))
            id.setTextAlignment(QtCore.Qt.AlignCenter)
            self.tProductos.setItem(rowPosition, 0, id)
            self.tProductos.setItem(rowPosition, 1,
                                    QTableWidgetItem(str(producto.nombre) + "-" + str(producto.detalle)))
            self.tProductos.setItem(rowPosition, 2, QTableWidgetItem(str(producto.precio_compra)))
            self.tProductos.setItem(rowPosition, 3, QTableWidgetItem(str(producto.marca)))
            self.tProductos.setItem(rowPosition, 4, QTableWidgetItem(str(Contador(producto.id))))

    def buscar(self):
        self.tProductos.clear()
        self.tProductos.setRowCount(0)
        self.tProductos.setHorizontalHeaderLabels(["ID", "NOMBRE", "PRECIO", 'MARCA', 'STOCK'])
        for producto in Buscar_NombreProducto(self.txtBuscar.text()):
            rowPosition = self.tProductos.rowCount()
            self.tProductos.insertRow(rowPosition)
            id = QTableWidgetItem(str(producto.id))
            id.setTextAlignment(QtCore.Qt.AlignCenter)
            self.tProductos.setItem(rowPosition, 0, id)
            self.tProductos.setItem(rowPosition, 1,
                                    QTableWidgetItem(str(producto.nombre) + "-" + str(producto.detalle)))
            self.tProductos.setItem(rowPosition, 2, QTableWidgetItem(str(producto.precio_compra)))
            self.tProductos.setItem(rowPosition, 3, QTableWidgetItem(str(producto.marca)))
            self.tProductos.setItem(rowPosition, 4, QTableWidgetItem(str(Contador(producto.id))))

    def seleccionProducto(self):
        self.id= int(self.tProductos.item(self.tProductos.currentRow(),0).text())
        self.traerKardexProducto(self.id)

    def traerKardex(self):
        self.tInventario.clear()
        self.tInventario.setRowCount(0)
        self.tInventario.setHorizontalHeaderLabels(["ID", "DETALLE", "CANT.", 'UNIT.','TOTAL','INGRESO','EGRESO'])
        ingresos=0.00
        egresos = 0.00
        ci=0
        ce=0
        for kardex in ListarKardex():
            rowPosition = self.tInventario.rowCount()
            self.tInventario.insertRow(rowPosition)
            id = QTableWidgetItem(str(kardex.producto.id))
            id.setTextAlignment(QtCore.Qt.AlignCenter)
            self.tInventario.setItem(rowPosition, 0, id)
            self.tInventario.setItem(rowPosition, 1, QTableWidgetItem(str(kardex.detalle)))
            self.tInventario.setItem(rowPosition, 2, QTableWidgetItem(str(kardex.cantidad)))
            self.tInventario.setItem(rowPosition, 3, QTableWidgetItem(str(kardex.producto.precio_compra)))
            self.tInventario.setItem(rowPosition, 4, QTableWidgetItem(str(kardex.producto.precio_compra*kardex.cantidad)))
            if kardex.tipo=="I":
                ci+=kardex.cantidad
                self.tInventario.setItem(rowPosition, 5,QTableWidgetItem(str(kardex.producto.precio_compra * kardex.cantidad)))
                ingresos+= float(kardex.producto.precio_compra) * float(kardex.cantidad)
            else:
                ce+= kardex.cantidad
                egresos+= float(kardex.producto.precio_compra) * float(kardex.cantidad)
                self.tInventario.setItem(rowPosition, 6,QTableWidgetItem(str(kardex.producto.precio_compra * kardex.cantidad)))
        totales= float(ingresos)-float(egresos)
        self.lbTotalIngresos.setText(str(round(ingresos,2)))
        self.lbTotalEgresos.setText(str(round(egresos,2)))
        self.lbTotal.setText(str(round(totales,2)))
        self.lbTotalCantidad.setText(str(ci-ce))
        self.lbTotalIngresosCantidad.setText(str(ci))
        self.lbTotalEgresosCantidad.setText(str(ce))

    def traerKardexProducto(self,id_producto):
        self.tInventario.clear()
        self.tInventario.setRowCount(0)
        self.tInventario.setHorizontalHeaderLabels(
            ["ID", "DETALLE", "CANT.", 'UNIT.', 'TOTAL', 'INGRESO', 'EGRESO'])
        ingresos = 0.00
        egresos = 0.00
        ci = 0
        ce = 0
        for kardex in ListarKardexProducto(id_producto):
            rowPosition = self.tInventario.rowCount()
            self.tInventario.insertRow(rowPosition)
            id = QTableWidgetItem(str(kardex.producto.id))
            id.setTextAlignment(QtCore.Qt.AlignCenter)
            self.tInventario.setItem(rowPosition, 0, id)
            self.tInventario.setItem(rowPosition, 1, QTableWidgetItem(str(kardex.detalle)))
            self.tInventario.setItem(rowPosition, 2, QTableWidgetItem(str(kardex.cantidad)))
            self.tInventario.setItem(rowPosition, 3, QTableWidgetItem(str(kardex.producto.precio_compra)))
            self.tInventario.setItem(rowPosition, 4,
                                     QTableWidgetItem(str(kardex.producto.precio_compra * kardex.cantidad)))
            if kardex.tipo == "I":
                ci += kardex.cantidad
                self.tInventario.setItem(rowPosition, 5,
                                         QTableWidgetItem(str(kardex.producto.precio_compra * kardex.cantidad)))
                ingresos += float(kardex.producto.precio_compra) * float(kardex.cantidad)
            else:
                ce += kardex.cantidad
                egresos += float(kardex.producto.precio_compra) * float(kardex.cantidad)
                self.tInventario.setItem(rowPosition, 6,
                                         QTableWidgetItem(str(kardex.producto.precio_compra * kardex.cantidad)))
        totales = float(ingresos) - float(egresos)
        self.lbTotalIngresos.setText(str(round(ingresos,2)))
        self.lbTotalEgresos.setText(str(round(egresos,2)))
        self.lbTotal.setText(str(round(totales,2)))
        self.lbTotalCantidad.setText(str(ci - ce))
        self.lbTotalIngresosCantidad.setText(str(ci))
        self.lbTotalEgresosCantidad.setText(str(ce))

    def generarReportesGeneral(self):
        ruta = "../Reportes/rptKardex.jasper"
        reporte = os.path.abspath(os.path.join(os.path.dirname(__file__), ruta))
        os.popen('java -jar "%s" "%s" " " "0"' % (str(self.rutaJar), str(reporte)))
        QMessageBox.information(self, "YOSSNAIDER",
                                "Espere mientras se genera el Documento, esto puede tomar tiempo.",
                                buttons=QMessageBox.Ok)

    def generarReportes(self):
        if self.id==0:
            ruta = "../Reportes/rptTotalInventario.jasper"
            reporte = os.path.abspath(os.path.join(os.path.dirname(__file__), ruta))
            os.popen('java -jar "%s" "%s" " " "0"' % (str(self.rutaJar), str(reporte)))
        else:
            ruta = "../Reportes/rptInventario.jasper"
            reporte = os.path.abspath(os.path.join(os.path.dirname(__file__), ruta))
            os.popen('java -jar "%s" "%s" "producto_id" "%s"' % (str(self.rutaJar), str(reporte),self.id))
        QMessageBox.information(self, "YOSSNAIDER",
                                "Espere mientras se genera el Documento, esto puede tomar tiempo.",
                                buttons=QMessageBox.Ok)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_frmRegistrosInventario()
    ui.show()
    sys.exit(app.exec_())
