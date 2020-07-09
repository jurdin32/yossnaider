# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'frmNotasVenta.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!
import datetime
import os

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QTableWidgetItem, QAbstractItemView, QMessageBox, QSystemTrayIcon

from Clientes.views import getCliente
from Productos.DialogoRecuperarNotas import Ui_DialogRecuperarVentas
from Productos.frmBuscador import Ui_Dialog
from Productos.views import ListarProductos, Contador, Buscar_NombreProducto, getProducto, CrearRegstroKardex, \
    EliminarRegistroKardex
from Productos.viewsVentas import getCountVentas, Crear, CrearDetalles, getVenta, VerDetalles, Actualizar, \
    EliminarDetalle


class Ui_frmVentas(QtWidgets.QMdiSubWindow):
    def __init__(self, parent=None):
        super(Ui_frmVentas, self).__init__()
        self.setObjectName("frmVentas")
        self.resize(923, 660)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./Recursos/ventas.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
        self.setStyleSheet("background: rgb(255, 255, 255);")
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(20, 40, 471, 131))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("./Recursos/logo.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(590, 40, 31, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self)
        self.label_3.setGeometry(QtCore.QRect(590, 75, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.deFecha = QtWidgets.QDateEdit(self)
        self.deFecha.setGeometry(QtCore.QRect(660, 65, 251, 30))
        self.deFecha.setAlignment(QtCore.Qt.AlignCenter)
        self.deFecha.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
        self.deFecha.setCurrentSection(QtWidgets.QDateTimeEdit.MonthSection)
        self.deFecha.setObjectName("deFecha")
        self.lbNumero = QtWidgets.QLabel(self)
        self.rutaJar = os.path.abspath(os.path.join(os.path.dirname(__file__), "../Reportes/Reporte.jar"))
        self.lbNumero.setGeometry(QtCore.QRect(660, 40, 251, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.lbNumero.setFont(font)
        self.lbNumero.setStyleSheet("color: rgb(122, 8, 0);")
        self.lbNumero.setAlignment(QtCore.Qt.AlignCenter)
        self.lbNumero.setObjectName("lbNumero")
        self.groupBox = QtWidgets.QGroupBox(self)
        self.groupBox.setGeometry(QtCore.QRect(660, 99, 251, 61))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.lbTotal = QtWidgets.QLabel(self.groupBox)
        self.lbTotal.setGeometry(QtCore.QRect(10, 10, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.lbTotal.setFont(font)
        self.lbTotal.setStyleSheet("color: rgb(122, 8, 0);")
        self.lbTotal.setAlignment(QtCore.Qt.AlignCenter)
        self.lbTotal.setObjectName("lbTotal")
        self.label_4 = QtWidgets.QLabel(self)
        self.label_4.setGeometry(QtCore.QRect(590, 130, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.groupBox_2 = QtWidgets.QGroupBox(self)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 170, 900, 60))
        self.groupBox_2.setObjectName("groupBox_2")
        self.btnBuscar = QtWidgets.QPushButton(self.groupBox_2)
        self.btnBuscar.setGeometry(QtCore.QRect(850, 22, 41, 25))
        self.btnBuscar.setStyleSheet("background-color: rgb(232, 232, 232);")
        self.btnBuscar.setText("")

        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("./Recursos/buscar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnBuscar.setIcon(icon1)
        self.btnBuscar.setObjectName("btnBuscar")
        self.txtNombreCliente = QtWidgets.QLineEdit(self.groupBox_2)
        self.txtNombreCliente.setGeometry(QtCore.QRect(10, 22, 371, 25))
        self.txtNombreCliente.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(7)
        self.txtNombreCliente.setFont(font)
        self.txtNombreCliente.setObjectName("txtNombreCliente")
        self.txtCedula = QtWidgets.QLineEdit(self.groupBox_2)
        self.txtCedula.setGeometry(QtCore.QRect(390, 22, 140, 25))
        self.txtCedula.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(7)
        self.txtCedula.setFont(font)
        self.txtCedula.setObjectName("txtCedula")
        self.txtCiudad = QtWidgets.QLineEdit(self.groupBox_2)
        self.txtCiudad.setGeometry(QtCore.QRect(540, 22, 140, 25))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.txtCiudad.setFont(font)
        self.txtCiudad.setObjectName("txtCiudad")
        self.txtCiudad.setEnabled(False)
        self.txtZona = QtWidgets.QLineEdit(self.groupBox_2)
        self.txtZona.setGeometry(QtCore.QRect(690, 22, 151, 25))
        self.txtZona.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(7)
        self.txtZona.setFont(font)
        self.txtZona.setObjectName("txtZona")
        self.groupBox_3 = QtWidgets.QGroupBox(self)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 240, 900, 60))
        self.groupBox_3.setObjectName("groupBox_3")
        self.txtBuscar = QtWidgets.QLineEdit(self.groupBox_3)
        self.txtBuscar.setGeometry(QtCore.QRect(10, 20, 401, 28))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.txtBuscar.setFont(font)
        self.txtBuscar.setObjectName("txtBuscar")
        self.sbPrecio = QtWidgets.QDoubleSpinBox(self.groupBox_3)
        self.sbPrecio.setGeometry(QtCore.QRect(430, 20, 100, 28))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.sbPrecio.setFont(font)
        self.sbPrecio.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.sbPrecio.setSuffix("")
        self.sbPrecio.setMaximum(99999.99)
        self.sbPrecio.setProperty("value", 0.0)
        self.sbPrecio.setObjectName("sbPrecio")
        self.sbPrecio.setEnabled(False)
        self.sbCantidad = QtWidgets.QSpinBox(self.groupBox_3)
        self.sbCantidad.setGeometry(QtCore.QRect(760, 20, 81, 28))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.sbCantidad.setFont(font)
        self.sbCantidad.setMaximum(999999999)
        self.sbCantidad.setProperty("value", 1)
        self.sbCantidad.setObjectName("sbCantidad")
        self.sbPorcentaje = QtWidgets.QDoubleSpinBox(self.groupBox_3)
        self.sbPorcentaje.setGeometry(QtCore.QRect(540, 20, 100, 28))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.sbPorcentaje.setFont(font)
        self.sbPorcentaje.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.sbPorcentaje.setPrefix("")
        self.sbPorcentaje.setMaximum(99999.99)
        self.sbPorcentaje.setProperty("value", 0.0)
        self.sbPorcentaje.setObjectName("sbPorcentaje")
        self.btnAgregar = QtWidgets.QPushButton(self.groupBox_3)
        self.btnAgregar.setGeometry(QtCore.QRect(850, 20, 41, 28))
        self.btnAgregar.setStyleSheet("background-color: rgb(232, 232, 232);")
        self.btnAgregar.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("./Recursos/agregar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnAgregar.setIcon(icon2)
        self.btnAgregar.setObjectName("btnAgregar")
        self.sbTotal = QtWidgets.QDoubleSpinBox(self.groupBox_3)
        self.sbTotal.setEnabled(True)
        self.sbTotal.setGeometry(QtCore.QRect(650, 20, 100, 28))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.sbTotal.setFont(font)
        self.sbTotal.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.sbTotal.setSuffix("")
        self.sbTotal.setMaximum(99999.99)
        self.sbTotal.setProperty("value", 0.0)
        self.sbTotal.setObjectName("sbTotal")
        self.tabVenta = QtWidgets.QTabWidget(self)
        self.tabVenta.setGeometry(QtCore.QRect(10, 310, 901, 291))
        self.tabVenta.setObjectName("tabVenta")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tVenta = QtWidgets.QTableWidget(self.tab)
        self.tVenta.setGeometry(QtCore.QRect(10, 10, 880, 250))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.tVenta.setFont(font)
        self.tVenta.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.tVenta.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tVenta.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tVenta.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tVenta.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tVenta.setObjectName("tVenta")
        self.tVenta.verticalHeader().setVisible(False)
        self.tabVenta.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tProductos = QtWidgets.QTableWidget(self.tab_2)
        self.tProductos.setGeometry(QtCore.QRect(10, 10, 880, 250))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.tProductos.setFont(font)
        self.tProductos.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.tProductos.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tProductos.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tProductos.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tProductos.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tProductos.setObjectName("tProductos")
        self.tProductos.verticalHeader().setVisible(False)
        self.tabVenta.addTab(self.tab_2, "")
        self.btnRegistrar = QtWidgets.QPushButton(self)
        self.btnRegistrar.setGeometry(QtCore.QRect(680, 605, 111, 40))
        self.btnRegistrar.setStyleSheet("background-color: rgb(232, 232, 232);")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("./Recursos/guardar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnRegistrar.setIcon(icon3)
        self.btnRegistrar.setObjectName("btnRegistrar")
        self.btnImprimir = QtWidgets.QPushButton(self)
        self.btnImprimir.setGeometry(QtCore.QRect(560, 605, 111, 40))
        self.btnImprimir.setStyleSheet("background-color: rgb(232, 232, 232);")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("./Recursos/impresora.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnImprimir.setIcon(icon4)
        self.btnImprimir.setObjectName("btnImprimir")
        self.btnRecuperar = QtWidgets.QPushButton(self)
        self.btnRecuperar.setGeometry(QtCore.QRect(440, 605, 111, 40))
        self.btnRecuperar.setStyleSheet("background-color: rgb(232, 232, 232);")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("./Recursos/recuperar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnRecuperar.setIcon(icon5)
        self.btnRecuperar.setObjectName("btnRecuperar")
        self.btnNuevo = QtWidgets.QPushButton(self)
        self.btnNuevo.setGeometry(QtCore.QRect(320, 605, 111, 40))
        self.btnNuevo.setStyleSheet("background-color: rgb(232, 232, 232);")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("./Recursos/nuevo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnNuevo.setIcon(icon6)
        self.btnNuevo.setObjectName("btnNuevo")

        self.btnCancelar = QtWidgets.QPushButton(self)
        self.btnCancelar.setGeometry(QtCore.QRect(800, 605, 111, 40))
        self.btnCancelar.setStyleSheet("background-color: rgb(232, 232, 232);")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("./Recursos/cancelar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnCancelar.setIcon(icon6)
        self.btnCancelar.setObjectName("btnNuevo")

        self.retranslateUi(self)
        self.tabVenta.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(self)


        self.tVenta.setColumnCount(6)
        self.tVenta.setRowCount(0)
        self.tVenta.setColumnWidth(0, 50)
        self.tVenta.setColumnWidth(1, 400)
        self.tVenta.setColumnWidth(3, 60)
        self.tVenta.setColumnWidth(4, 95)
        style = "QHeaderView::section {background:#10608D;color:#FFFFFF;}"
        self.tVenta.horizontalHeader().setStyleSheet(style)
        self.tVenta.setHorizontalHeaderLabels(["ID", "NOMBRE", "PRECIO",'%', 'CANT', 'TOTAL'])
        self.tProductos.setColumnCount(5)
        self.tProductos.setRowCount(0)
        self.tProductos.setColumnWidth(0, 50)
        self.tProductos.setColumnWidth(1, 500)
        self.tProductos.setColumnWidth(2, 100)
        self.tProductos.setColumnWidth(3, 100)
        self.tProductos.setColumnWidth(4, 100)
        self.tProductos.horizontalHeader().setStyleSheet(style)
        self.tProductos.setHorizontalHeaderLabels(["ID", "NOMBRE", "PRECIO", 'MARCA', 'STOCK'])
        self.sbPorcentaje.setEnabled(True)
        self.sbPrecio.setEnabled(True)

        self.retranslateUi(self)
        self.tabVenta.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(self)

        self.id=0
        self.id_venta=0

        self.producto=None
        self.row=-1
        self.rowPosition=-1
        self.cliente_id=0
        self.estado=0

        self.cancelar()


        self.traerProductos()
        self.btnBuscar.clicked.connect(self.buscarCliente)
        self.lbNumero.setText(str.zfill(str(getCountVentas()+1),12))
        self.deFecha.setDate(datetime.datetime.now().date())

        QtWidgets.QShortcut(QtCore.Qt.Key_Delete, self.tVenta, activated=self.eliminarFila)
        self.txtBuscar.textChanged.connect(self.traerProductos)
        self.tProductos.doubleClicked.connect(self.seleccionar)
        self.btnAgregar.clicked.connect(self.agregar)
        self.sbTotal.valueChanged.connect(self.cambiarPrecio)
        # self.sbPorcentaje.connect(self.cambiarPrecio)
        self.tVenta.doubleClicked.connect(self.seleccionarTVentas)

        self.btnRegistrar.clicked.connect(self.registrar)
        self.btnRecuperar.clicked.connect(self.recuperar)
        self.btnNuevo.clicked.connect(self.nuevo)
        self.btnImprimir.clicked.connect(self.imprimir)
        self.btnCancelar.clicked.connect(self.cancelar)

        self.precioT=0
        self.porcentaje=0
        self.porc=0



    def retranslateUi(self, frmVentas):
        _translate = QtCore.QCoreApplication.translate
        frmVentas.setWindowTitle(_translate("frmVentas", "Notas de Venta"))
        self.label_2.setText(_translate("frmVentas", "No."))
        self.label_3.setText(_translate("frmVentas", "Fecha:"))
        self.lbNumero.setText(_translate("frmVentas", "000000000000000-00001"))
        self.lbTotal.setText(_translate("frmVentas", "00,00"))
        self.label_4.setText(_translate("frmVentas", "Valor:"))
        self.groupBox_2.setTitle(_translate("frmVentas", "Información del Cliente"))
        self.groupBox_3.setTitle(_translate("frmVentas", "Detalle de la Venta"))
        self.txtBuscar.setPlaceholderText(_translate("frmVentas", "Escriba el nombre del Producto"))
        self.sbPrecio.setPrefix(_translate("frmVentas", "$ "))
        self.sbPorcentaje.setSuffix(_translate("frmVentas", " %"))
        self.tabVenta.setTabText(self.tabVenta.indexOf(self.tab), _translate("frmVentas", "Venta"))
        self.tabVenta.setTabText(self.tabVenta.indexOf(self.tab_2), _translate("frmVentas", "Productos"))
        self.btnRegistrar.setText(_translate("frmVentas", "Registrar"))
        self.btnImprimir.setText(_translate("frmVentas", "Imprimir"))
        self.btnRecuperar.setText(_translate("frmVentas", "Recuperar"))
        self.btnNuevo.setText(_translate("frmVentas", "Nuevo"))
        self.btnCancelar.setText(_translate("frmVentas", "Cancelar"))

    def recuperar(self):
        try:
            frm=Ui_DialogRecuperarVentas(self)
            frm.exec_()
            if frm.venta_id>0:
                self.recuperarVenta(frm.venta_id)
                self.btnRecuperar.setEnabled(False)
                self.btnRegistrar.setEnabled(True)
                self.btnImprimir.setEnabled(True)
                self.btnNuevo.setEnabled(True)
                self.sbCantidad.setEnabled(True)
                self.sbTotal.setEnabled(True)
                self.sbPorcentaje.setEnabled(True)
                self.btnAgregar.setEnabled(True)
                self.btnBuscar.setEnabled(True)
                self.estado=1
                self.id_venta=frm.venta_id
        except Exception as error:
            print(error)
            self.estado=0
            self.id_venta=0

    def recuperarVenta(self,id):
        venta=getVenta(id)
        self.tabVenta.setEnabled(True)
        self.lbNumero.setText(str.zfill(str(venta.id),12))
        self.cliente_id =venta.cliente.id
        self.txtNombreCliente.setText(venta.cliente.nombres)
        self.txtCedula.setText(venta.cliente.cedula)
        self.txtCiudad.setText(venta.cliente.ciudad.nombre)
        if venta.cliente.zona == "S":
            self.txtZona.setText("Sur")
        elif venta.cliente.zona == "N":
            self.txtZona.setText("Norte")
        elif venta.cliente.zona == "C":
            self.txtZona.setText("Centro")
        self.deFecha.setDate(venta.fecha)
        self.tabVenta.setCurrentIndex(0)
        self.tVenta.clear()
        self.tVenta.setRowCount(0)
        self.tVenta.setHorizontalHeaderLabels(["ID", "NOMBRE", "PRECIO", '%', 'CANT', 'TOTAL'])
        for det in VerDetalles(venta):
            rowPosition = self.tVenta.rowCount()
            self.tVenta.insertRow(rowPosition)
            id = QTableWidgetItem(str(det.producto.id))
            id.setTextAlignment(QtCore.Qt.AlignCenter)
            id.setBackground(QtGui.QColor(162, 191, 249))
            self.tVenta.setItem(rowPosition, 0, id)
            self.tVenta.setItem(rowPosition, 1,
                                QTableWidgetItem(str(det.producto.nombre + "-" + det.producto.detalle)))
            self.tVenta.setItem(rowPosition, 2, QTableWidgetItem(str(det.valor)))


            porcentaje = QTableWidgetItem(str(det.ganancia))
            porcentaje.setTextAlignment(QtCore.Qt.AlignCenter)
            porcentaje.setBackground(QtGui.QColor(223, 233, 9))
            self.tVenta.setItem(rowPosition, 3, porcentaje)

            cant = QTableWidgetItem(str(det.cantidad))
            cant.setTextAlignment(QtCore.Qt.AlignCenter)
            self.tVenta.setItem(rowPosition, 4, cant)

            ttotal = QTableWidgetItem(str(det.total))
            ttotal.setTextAlignment(QtCore.Qt.AlignRight)
            ttotal.setBackground(QtGui.QColor(246, 200, 200))
            self.tVenta.setItem(rowPosition, 5, ttotal)
        self.totales()


    def seleccionar(self):
        self.id = int(self.tProductos.item(self.tProductos.currentRow(),0).text())
        self.producto= getProducto(self.id)
        self.txtBuscar.setText(self.producto.nombre+"-"+ self.producto.detalle)
        self.sbPrecio.setValue(self.producto.precio_compra)
        self.sbTotal.setValue(self.producto.precio_compra)
        self.tabVenta.setCurrentIndex(0)
        self.sbCantidad.setMaximum(Contador(self.id))
        self.cambiarPrecio()

    def seleccionarTVentas(self):
        self.id = int(self.tVenta.item(self.tVenta.currentRow(), 0).text())
        self.row =self.tVenta.currentRow()
        self.producto = getProducto(self.id)
        self.txtBuscar.setText(self.producto.nombre + "-" + self.producto.detalle)
        self.sbPrecio.setValue(self.producto.precio_compra)
        try:
            porc=float(self.tVenta.item(self.tVenta.currentRow(),3).text())/100
            self.sbTotal.setValue((porc*float(self.producto.precio_compra))+float(self.producto.precio_compra))
            self.sbPorcentaje.setValue(porc)
        except Exception as error:
            print(error)
        self.sbCantidad.setValue(int(self.tVenta.item(self.tVenta.currentRow(),4).text()))
        self.tabVenta.setCurrentIndex(0)
        self.sbCantidad.setMaximum(Contador(self.id))
        self.cambiarPrecio()

    def agregar(self):
        rowPosition=-1
        try:
            if self.row>=0:
                rowPosition=self.row
                self.row=-1
            else:
                rowPosition = self.tVenta.rowCount()
                self.tVenta.insertRow(rowPosition)
            if self.id>0 and self.sbCantidad.value()>0:
                id = QTableWidgetItem(str(self.id))
                id.setTextAlignment(QtCore.Qt.AlignCenter)
                id.setBackground(QtGui.QColor(162, 191, 249))
                self.tVenta.setItem(rowPosition, 0, id)
                self.tVenta.setItem(rowPosition, 1, QTableWidgetItem(str(self.producto.nombre+"-"+self.producto.detalle)))
                self.tVenta.setItem(rowPosition, 2, QTableWidgetItem(str(self.sbPrecio.value())))

                porcentaje = QTableWidgetItem(str(self.sbPorcentaje.value()))
                porcentaje.setTextAlignment(QtCore.Qt.AlignCenter)
                porcentaje.setBackground(QtGui.QColor(223, 233, 9))
                self.tVenta.setItem(rowPosition, 3, porcentaje)

                cant = QTableWidgetItem(str(self.sbCantidad.value()))
                cant.setTextAlignment(QtCore.Qt.AlignCenter)
                self.tVenta.setItem(rowPosition, 4, cant)

                ttotal = QTableWidgetItem(str(self.sbTotal.value()*self.sbCantidad.value()))
                ttotal.setTextAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignVCenter)
                ttotal.setBackground(QtGui.QColor(246, 200, 200))
                self.tVenta.setItem(rowPosition, 5, ttotal)
                self.txtBuscar.setText("")
                self.sbPrecio.setValue(0)
                self.sbPorcentaje.setValue(0)
                self.sbCantidad.setValue(1)
                self.sbTotal.setValue(0)
                self.totales()
                self.tabVenta.setCurrentIndex(0)
                self.id=0
            else:
                self.tVenta.removeRow(rowPosition)
                QMessageBox.information(self, "Mensaje del Sistema",
                                        "Primero Seleccione un Artículo",QMessageBox.Ok, )
        except Exception as error:
            print(error)


    def cambiarPrecio(self):
        self.precio = float(self.producto.precio_compra)
        self.porcentaje = float(self.sbPorcentaje.value())
        self.precioT = float(self.sbTotal.value())

        try:
            self.porc =((self.precioT *100) / self.precio)-100
            self.sbPorcentaje.setValue(self.porc)
            print(self.porc)
        except Exception as error:
            print(error)


    def totales(self):
        suma=0
        for row in range(self.tVenta.rowCount()):
            suma+=float(self.tVenta.item(row,5).text())
            print(suma)
        self.lbTotal.setText(str(suma))

    def eliminarFila(self):
        self.tVenta.removeRow(self.tVenta.currentRow())
        self.totales()

    def eliminarTodasLasFilasProductos(self):
        try:
            for i in range(self.tVenta.rowCount()):
                self.tVenta.removeRow(i)
        except Exception as error:
            print(error)


    def traerProductos(self):
        self.tProductos.setRowCount(0)
        self.tProductos.clear()
        self.tProductos.setHorizontalHeaderLabels(["ID", "NOMBRE", "PRECIO", 'MARCA', 'STOCK'])
        self.tabVenta.setCurrentIndex(1)
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

    def buscarCliente(self):
        frm=Ui_Dialog(self)
        frm.exec_()
        if frm.cliente_id>0:
            cliente=getCliente(frm.cliente_id)
            self.cliente_id=frm.cliente_id
            self.txtNombreCliente.setText(cliente.nombres)
            self.txtCedula.setText(cliente.cedula)
            self.txtCiudad.setText(cliente.ciudad.nombre)
            if cliente.zona=="S":
                self.txtZona.setText("Sur")
            elif cliente.zona == "N":
                self.txtZona.setText("Norte")
            elif cliente.zona == "C":
                self.txtZona.setText("Centro")
        else:
            self.txtNombreCliente.setText("")
            self.txtCedula.setText("")
            self.txtCiudad.setText("")
            self.txtZona.setText("")

    def nuevo(self):
        self.estado=0
        self.btnRecuperar.setEnabled(False)
        self.btnRegistrar.setEnabled(True)
        self.btnImprimir.setEnabled(False)
        self.btnNuevo.setEnabled(False)
        self.btnBuscar.setEnabled(True)
        self.btnAgregar.setEnabled(True)
        self.sbPrecio.setEnabled(False)
        self.txtZona.setText("")
        self.sbTotal.setEnabled(True)
        self.txtCiudad.setText("")
        self.txtCedula.setText("")
        self.txtNombreCliente.setText("")
        self.txtBuscar.setText("")
        self.sbCantidad.setValue(1)
        self.sbPorcentaje.setValue(0)
        self.sbPrecio.setValue(0)
        self.sbPorcentaje.setEnabled(True)
        self.lbNumero.setText(str.zfill(str(getCountVentas()),12))
        self.id = 0
        self.producto = None
        self.row = -1
        self.rowPosition = -1
        self.cliente_id = 0
        self.tVenta.clear()
        self.tVenta.setHorizontalHeaderLabels(["ID", "NOMBRE", "PRECIO", '%', 'CANT', 'TOTAL'])
        self.tabVenta.setEnabled(True)
        self.sbCantidad.setEnabled(True)
        self.traerProductos()
        self.eliminarTodasLasFilasProductos()

    def cancelar(self):
        self.nuevo()
        self.sbTotal.setEnabled(False)
        self.btnRecuperar.setEnabled(True)
        self.btnRegistrar.setEnabled(False)
        self.btnImprimir.setEnabled(False)
        self.btnNuevo.setEnabled(True)
        self.tabVenta.setEnabled(False)
        self.btnBuscar.setEnabled(False)
        self.btnAgregar.setEnabled(False)
        self.sbPorcentaje.setEnabled(False)
        self.sbCantidad.setValue(0)
        self.sbCantidad.setEnabled(False)

    def imprimir(self):
        id=int(self.lbNumero.text())
        ruta = "../Reportes/rptNota.jasper"
        reporte = os.path.abspath(os.path.join(os.path.dirname(__file__), ruta))
        os.popen('java -jar "%s" "%s" "%s" "%s"' % (str(self.rutaJar), str(reporte), "nota_venta_id", id))
        QMessageBox.information(self, "YOSSNAIDER",
                                "Espere mientras se genera el Documento, esto puede tomar tiempo.",
                                buttons=QMessageBox.Ok)

    def registrar(self):
        try:
            if self.cliente_id>0 and self.tVenta.rowCount()>0:
                if self.estado==0:
                    result=Crear(self.cliente_id,self.deFecha.date().toString("yyyy-MM-dd"),float(self.lbTotal.text()))
                    self.lbNumero.setText(str.zfill(str(result), 12))
                    for i in range(self.tVenta.rowCount()):
                        CrearDetalles(result,self.deFecha.date().toString("yyyy-MM-dd"),int(self.tVenta.item(i,0).text()),int(self.tVenta.item(i,4).text()),float(self.tVenta.item(i,2).text()),float(self.tVenta.item(i,3).text()),float(self.tVenta.item(i,5).text()))
                        porcentaje = (
                                    float(self.tVenta.item(i, 2).text()) * (float(self.tVenta.item(i, 3).text()) / 100))
                        precioventa = float(self.tVenta.item(i, 2).text())
                        CrearRegstroKardex(int(self.tVenta.item(i,0).text()),"Registro de Nota de venta No.%s del Sr/a. %s "%(self.lbNumero.text(),self.txtNombreCliente.text()),"E",self.deFecha.date().toString("yyyy-MM-dd"),int(self.tVenta.item(i,4).text()),float(self.tVenta.item(i,2).text()),precioventa,0,float(self.tVenta.item(i,5).text()),result)

                    QMessageBox.information(self,"YOSSNAIDER", "La Nota de Venta registrado correctamente..!",buttons=QMessageBox.Ok)
                else:
                    result=Actualizar(self.id_venta,self.cliente_id,self.deFecha.date().toString("yyyy-MM-dd"),float(self.lbTotal.text()))
                    EliminarDetalle(result)
                    EliminarRegistroKardex(result)

                    self.lbNumero.setText(str.zfill(str(result), 12))
                    for i in range(self.tVenta.rowCount()):
                        CrearDetalles(result, self.deFecha.date().toString("yyyy-MM-dd"),int(self.tVenta.item(i, 0).text()), int(self.tVenta.item(i, 4).text()),float(self.tVenta.item(i, 2).text()), float(self.tVenta.item(i, 3).text()),float(self.tVenta.item(i, 5).text()))
                        porcentaje= (float(self.tVenta.item(i, 2).text()) * (float(self.tVenta.item(i, 3).text())/100))
                        precioventa= float(self.tVenta.item(i, 2).text())
                        print("valor ",self.tVenta.item(i, 2).text(),"Porcentaje",porcentaje,"venta",precioventa)
                        CrearRegstroKardex(int(self.tVenta.item(i, 0).text()),"Se Registro una modificación a la  Nota de venta No.%s del Sr/a. %s " % (self.lbNumero.text(), self.txtNombreCliente.text()), "E",self.deFecha.date().toString("yyyy-MM-dd"),int(self.tVenta.item(i, 4).text()), float(self.tVenta.item(i, 2).text()),precioventa, 0, float(self.tVenta.item(i, 5).text()),result)
                    QMessageBox.information(self,"YOSSNAIDER", "La Nota de Venta se ha acttualizado correctamente..!",buttons=QMessageBox.Ok)
                self.btnRecuperar.setEnabled(False)
                self.btnRegistrar.setEnabled(False)
                self.btnImprimir.setEnabled(True)
                self.btnNuevo.setEnabled(True)
            else:
                QMessageBox.critical(self,"YOSSNAIDER", "Es posible que no se pueda crear debido a que no hay datos del cliente o no se seleccionaron artículos..!",buttons=QMessageBox.Ok)
        except Exception as error:
            print(error)
        self.traerProductos()
        self.tabVenta.setCurrentIndex(0)
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_frmVentas()
    ui.show()
    sys.exit(app.exec_())
