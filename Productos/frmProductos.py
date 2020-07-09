# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'frmProductos.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!
import datetime

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem, QAbstractItemView, QMessageBox

from Productos.models import Kardex
from Productos.views import ListarProductos, getProducto, Crear, Actualizar, CrearRegstroKardex, Contador, \
    CambiarEstado, Buscar_NombreProducto


class Ui_frmProductos(QtWidgets.QMdiSubWindow):
    def __init__(self, parent=0):
        super(Ui_frmProductos, self).__init__()
        self.setObjectName("frmProductos")
        self.resize(778, 528)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./Recursos/productos.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
        self.tabProductos = QtWidgets.QTabWidget(self)
        self.tabProductos.setGeometry(QtCore.QRect(20, 40, 741, 471))
        self.tabProductos.setObjectName("tabProductos")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.sbExistencia = QtWidgets.QSpinBox(self.tab)
        self.sbExistencia.setGeometry(QtCore.QRect(130, 320, 201, 30))
        self.sbExistencia.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.sbExistencia.setReadOnly(True)
        self.sbExistencia.setObjectName("sbExistencia")
        self.sbExistencia.setMaximum(100000)
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(20, 60, 53, 81))
        self.label_2.setObjectName("label_2")
        self.label_6 = QtWidgets.QLabel(self.tab)
        self.label_6.setGeometry(QtCore.QRect(20, 330, 61, 16))
        self.label_6.setObjectName("label_6")

        self.sbValorUnitario = QtWidgets.QDoubleSpinBox(self.tab)
        self.sbValorUnitario.setGeometry(QtCore.QRect(130, 160, 201, 30))
        self.sbValorUnitario.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.sbValorUnitario.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.sbValorUnitario.setButtonSymbols(QtWidgets.QAbstractSpinBox.PlusMinus)
        self.sbValorUnitario.setDecimals(2)
        self.sbValorUnitario.setMaximum(999999.99)
        self.sbValorUnitario.setSuffix(" $")

        self.sbValorUnitario.setObjectName("sbValorUnitario")

        self.txtMarca = QtWidgets.QLineEdit(self.tab)
        self.txtMarca.setGeometry(QtCore.QRect(130, 200, 201, 30))
        self.txtMarca.setObjectName("txtMarca")
        self.txtSerie = QtWidgets.QLineEdit(self.tab)
        self.txtSerie.setGeometry(QtCore.QRect(130, 240, 201, 30))
        self.txtSerie.setObjectName("txtSerie")
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(20, 205, 101, 21))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.tab)
        self.label_4.setGeometry(QtCore.QRect(20, 165, 81, 21))
        self.label_4.setObjectName("label_4")
        self.txtDetalles = QtWidgets.QTextEdit(self.tab)
        self.txtDetalles.setGeometry(QtCore.QRect(130, 60, 591, 87))
        self.txtDetalles.setObjectName("txtDetalles")
        self.label_7 = QtWidgets.QLabel(self.tab)
        self.label_7.setGeometry(QtCore.QRect(20, 290, 53, 16))
        self.label_7.setObjectName("label_7")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(20, 20, 53, 21))
        self.label.setObjectName("label")
        self.label_5 = QtWidgets.QLabel(self.tab)
        self.label_5.setGeometry(QtCore.QRect(20, 245, 101, 21))
        self.label_5.setObjectName("label_5")
        self.sbStock = QtWidgets.QSpinBox(self.tab)
        self.sbStock.setGeometry(QtCore.QRect(130, 280, 201, 30))
        self.sbStock.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.sbStock.setObjectName("sbStock")
        self.sbStock.setMinimum(-100000)
        self.sbStock.setMaximum(100000)
        self.txtNombre = QtWidgets.QLineEdit(self.tab)
        self.txtNombre.setGeometry(QtCore.QRect(130, 20, 591, 30))
        self.txtNombre.setObjectName("txtNombre")
        self.layoutWidget = QtWidgets.QWidget(self.tab)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 380, 711, 51))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.btnNuevo = QtWidgets.QPushButton(self.layoutWidget)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("./Recursos/nuevo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnNuevo.setIcon(icon1)
        self.btnNuevo.setObjectName("btnNuevo")
        self.gridLayout.addWidget(self.btnNuevo, 0, 0, 1, 1)
        self.btnGuardar = QtWidgets.QPushButton(self.layoutWidget)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("./Recursos/guardar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnGuardar.setIcon(icon2)
        self.btnGuardar.setObjectName("btnGuardar")
        self.gridLayout.addWidget(self.btnGuardar, 0, 1, 1, 1)
        self.btnModificar = QtWidgets.QPushButton(self.layoutWidget)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("./Recursos/editar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnModificar.setIcon(icon3)
        self.btnModificar.setObjectName("btnModificar")
        self.gridLayout.addWidget(self.btnModificar, 0, 2, 1, 1)
        self.btnEliminar = QtWidgets.QPushButton(self.layoutWidget)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("./Recursos/eliminar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnEliminar.setIcon(icon4)
        self.btnEliminar.setObjectName("btnEliminar")
        self.gridLayout.addWidget(self.btnEliminar, 0, 3, 1, 1)
        self.btnCancelar = QtWidgets.QPushButton(self.layoutWidget)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("./Recursos/cancelar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnCancelar.setIcon(icon5)
        self.btnCancelar.setObjectName("btnCancelar")
        self.gridLayout.addWidget(self.btnCancelar, 0, 4, 1, 1)
        self.tabProductos.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.label_8 = QtWidgets.QLabel(self.tab_2)
        self.label_8.setGeometry(QtCore.QRect(17, 10, 61, 31))
        self.label_8.setObjectName("label_8")
        self.txtBuscador = QtWidgets.QLineEdit(self.tab_2)
        self.txtBuscador.setGeometry(QtCore.QRect(87, 10, 631, 30))
        self.txtBuscador.setObjectName("txtBuscador")
        self.tProductos = QtWidgets.QTableWidget(self.tab_2)
        self.tProductos.setGeometry(QtCore.QRect(17, 50, 701, 361))
        self.tProductos.setObjectName("tProductos")
        self.tProductos.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.tProductos.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tProductos.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tProductos.setSelectionBehavior(self.tProductos.SelectRows)
        self.tProductos.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tProductos.verticalHeader().setVisible(False)
        self.tProductos.setColumnCount(5)
        self.tProductos.setRowCount(0)
        self.tProductos.setColumnWidth(0, 30)
        self.tProductos.setColumnWidth(1, 310)
        self.tProductos.setColumnWidth(4, 70)
        style = "QHeaderView::section {background:#10608D;color:#FFFFFF;}"
        self.tProductos.horizontalHeader().setStyleSheet(style)

        self.tProductos.setHorizontalHeaderLabels(["ID", "NOMBRE", "PRECIO", 'MARCA','STOCK'])
        self.tabProductos.addTab(self.tab_2, "")

        self.retranslateUi(self)
        self.tabProductos.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(self)

        self.id=0
        self.estado=0

        self.traerProductos()
        self.cancelar()

        self.btnNuevo.clicked.connect(self.nuevo)
        self.btnGuardar.clicked.connect(self.guardar)
        self.tProductos.doubleClicked.connect(self.seleccionar)
        self.btnModificar.clicked.connect(self.modificar)
        self.btnCancelar.clicked.connect(self.cancelar)
        self.btnEliminar.clicked.connect(self.eliminar)
        self.sbStock.valueChanged.connect(self.stock)
        self.txtBuscador.textChanged.connect(self.traerProductos)

    def retranslateUi(self, frmProductos):
        _translate = QtCore.QCoreApplication.translate
        frmProductos.setWindowTitle(_translate("frmProductos", "Registro de Productos"))
        self.label_2.setText(_translate("frmProductos", "Detalle"))
        self.label_6.setText(_translate("frmProductos", "Existencia"))
        self.label_3.setText(_translate("frmProductos", "Marca"))
        self.label_4.setText(_translate("frmProductos", "Valor Unitario"))
        self.label_7.setText(_translate("frmProductos", "Stock"))
        self.label.setText(_translate("frmProductos", "Nombre"))
        self.label_5.setText(_translate("frmProductos", "Serie"))
        self.btnNuevo.setText(_translate("frmProductos", "Nuevo"))
        self.btnGuardar.setText(_translate("frmProductos", "Guardar"))
        self.btnModificar.setText(_translate("frmProductos", "Modificar"))
        self.btnEliminar.setText(_translate("frmProductos", "Eliminar"))
        self.btnCancelar.setText(_translate("frmProductos", "Cancelar"))
        self.tabProductos.setTabText(self.tabProductos.indexOf(self.tab), _translate("frmProductos", "Registro de Productos"))
        self.label_8.setText(_translate("frmProductos", "Buscador"))
        self.txtBuscador.setPlaceholderText(_translate("frmProductos", "Escriba nombre del Producto"))
        self.tabProductos.setTabText(self.tabProductos.indexOf(self.tab_2), _translate("frmProductos", "Listado"))

    def stock(self):
        cantidad = Contador(self.id)
        nuevo = self.sbStock.value()
        total=cantidad+nuevo
        if total>0:
            self.sbExistencia.setValue(total)
        else:
            self.sbExistencia.setValue(cantidad)
            self.sbStock.setValue(0)

    def traerProductos(self):
        self.tProductos.clear()
        self.tProductos.setRowCount(0)
        self.tProductos.setHorizontalHeaderLabels(["ID", "NOMBRE", "PRECIO", 'MARCA','STOCK'])
        for producto in Buscar_NombreProducto(self.txtBuscador.text()):
            rowPosition = self.tProductos.rowCount()
            self.tProductos.insertRow(rowPosition)
            id = QTableWidgetItem(str(producto.id))
            id.setTextAlignment(QtCore.Qt.AlignCenter)
            self.tProductos.setItem(rowPosition, 0, id)
            self.tProductos.setItem(rowPosition, 1, QTableWidgetItem(str(producto.nombre)+"-"+str(producto.detalle)))
            self.tProductos.setItem(rowPosition, 2, QTableWidgetItem(str(producto.precio_compra)))
            self.tProductos.setItem(rowPosition, 3, QTableWidgetItem(str(producto.marca)))
            self.tProductos.setItem(rowPosition,4,QTableWidgetItem(str(Contador(producto.id))))

    def habilitar(self,valor):
        self.txtSerie.setEnabled(valor)
        self.txtMarca.setEnabled(valor)
        self.txtDetalles.setEnabled(valor)
        self.txtNombre.setEnabled(valor)
        self.sbValorUnitario.setEnabled(valor)
        self.sbExistencia.setEnabled(False)
        self.sbStock.setEnabled(valor)

    def limpiar(self):
        self.txtSerie.setText("SN")
        self.txtMarca.setText("SN")
        self.txtDetalles.setText("SN")
        self.txtNombre.setText("SN")
        self.sbValorUnitario.setValue(0)
        self.sbExistencia.setValue(0)
        self.sbStock.setValue(0)


    def nuevo(self):
        self.estado=0
        self.cancelar()
        self.limpiar()
        self.habilitar(True)
        self.btnNuevo.setEnabled(False)
        self.btnGuardar.setEnabled(True)
        self.btnCancelar.setEnabled(True)
        self.btnEliminar.setEnabled(False)
        self.btnModificar.setEnabled(False)

    def guardar(self):
        if self.estado==0 and len(self.txtNombre.text())>0:
            result=Crear(nombre=self.txtNombre.text(),detalle=self.txtDetalles.toPlainText(),
                          precio_compra=self.sbValorUnitario.value(),marca=self.txtMarca.text(),
                          serie=self.txtSerie.text())
            self.id=result
            QMessageBox.information(self, "Información", "Registro se ha creado exitosamente..!",
                                    buttons=QMessageBox.Ok)
            self.btnNuevo.setEnabled(True)
            self.btnGuardar.setEnabled(False)
            self.btnCancelar.setEnabled(True)
            self.btnEliminar.setEnabled(False)
            self.btnModificar.setEnabled(True)
            self.habilitar(False)
        elif self.estado==1 and len(self.txtNombre.text())>0:
            result = Actualizar(id=self.id,nombre=self.txtNombre.text(), detalle=self.txtDetalles.toPlainText(),
                           precio_compra=self.sbValorUnitario.value(), marca=self.txtMarca.text(),
                           serie=self.txtSerie.text())
            self.id = result
            QMessageBox.information(self, "Información", "Registro se ha modificado exitosamente..!",
                                    buttons=QMessageBox.Ok)
            self.btnNuevo.setEnabled(True)
            self.btnGuardar.setEnabled(False)
            self.btnCancelar.setEnabled(True)
            self.btnEliminar.setEnabled(False)
            self.btnModificar.setEnabled(True)
            self.habilitar(False)
        else:
            QMessageBox.information(self, "Información", "Debe al menos registrar el nombre..!",
                                    buttons=QMessageBox.Ok)
        det=""
        if len(self.txtNombre.text())>0:
            stock=0
            if self.sbStock.value()>0:
                det="I"
                stock=self.sbStock.value()
            else:
                det="E"
                stock=self.sbStock.value()*-1
            try:
                CrearRegstroKardex(self.id,
                                   "Para registrar Movimiento de inventario desde el formulario creación de Productos..",
                                   det, datetime.datetime.now(),
                                   stock, self.sbValorUnitario.value(), 0,
                                   stock * self.sbValorUnitario.value(), 0,1)
            except Exception as error:
                print(error)
        self.traerProductos()
        self.sbExistencia.setValue(Contador(self.id))

    def modificar(self):
        if self.id > 0:
            self.habilitar(True)
            self.estado = 1
            self.btnNuevo.setEnabled(True)
            self.btnGuardar.setEnabled(True)
            self.btnCancelar.setEnabled(True)
            self.btnEliminar.setEnabled(True)
            self.btnModificar.setEnabled(False)

    def seleccionar(self):
        self.limpiar()
        self.id = int(self.tProductos.item(self.tProductos.currentRow(),0).text())
        producto= getProducto(self.id)
        self.txtNombre.setText(producto.nombre)
        self.txtDetalles.setText(producto.detalle)
        self.txtMarca.setText(producto.marca)
        self.txtSerie.setText(producto.serie)
        self.sbValorUnitario.setValue(producto.precio_compra)
        self.tabProductos.setCurrentIndex(0)
        self.habilitar(False)
        self.sbExistencia.setValue(Contador(self.id))
        self.btnNuevo.setEnabled(True)
        self.btnGuardar.setEnabled(False)
        self.btnCancelar.setEnabled(True)
        self.btnEliminar.setEnabled(True)
        self.btnModificar.setEnabled(True)

    def eliminar(self):
        buttonReply = QMessageBox.question(self, 'Mensaje', "Seguro que desea eliminar este registro?",
                                           QMessageBox.Yes | QMessageBox.No)
        if buttonReply == QMessageBox.Yes:
            if (self.id) > 0:
                CambiarEstado(self.id)
                QMessageBox.information(self, "Información", "El registro se ha desactivado..!", buttons=QMessageBox.Ok)
                self.id = 0
            else:
                QMessageBox.information(self, "Información", "Primero seleccione el registro..!",
                                        buttons=QMessageBox.Ok)
        elif buttonReply == QMessageBox.No:
            pass
        self.traerProductos()
        self.cancelar()


    def cancelar(self):
        self.habilitar(False)
        self.limpiar()
        self.estado=0
        self.id=0
        self.btnNuevo.setEnabled(True)
        self.btnGuardar.setEnabled(False)
        self.btnCancelar.setEnabled(True)
        self.btnEliminar.setEnabled(False)
        self.btnModificar.setEnabled(False)



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_frmProductos()
    ui.show()
    sys.exit(app.exec_())

