# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'frmCliente.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMessageBox, QTableWidgetItem, QAbstractItemView, QSystemTrayIcon

from Ciudades.views import Listar
from Clientes.views import Crear, ListarClientes, getCliente, Actualizar, Buscar_Nombre, Eliminar, CambiarEstado
from Cobradores.views import  ListarCobrador


class Ui_frmClientes(QtWidgets.QMdiSubWindow):
    def __init__(self, parent=None):
        super(Ui_frmClientes, self).__init__()
        self.setObjectName("frmRegistroClientes")
        self.resize(724, 486)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./Recursos/personas.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
        self.tabClientes = QtWidgets.QTabWidget(self)
        self.tabClientes.setGeometry(QtCore.QRect(20, 50, 681, 421))
        self.tabClientes.setObjectName("tabClientes")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.label_9 = QtWidgets.QLabel(self.tab)
        self.label_9.setGeometry(QtCore.QRect(40, 310, 53, 30))
        self.label_9.setObjectName("label_9")
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(40, 110, 91, 30))
        self.label_3.setObjectName("label_3")
        self.label_8 = QtWidgets.QLabel(self.tab)
        self.label_8.setGeometry(QtCore.QRect(40, 270, 53, 30))
        self.label_8.setObjectName("label_8")
        self.label_6 = QtWidgets.QLabel(self.tab)
        self.label_6.setGeometry(QtCore.QRect(40, 190, 91, 30))
        self.label_6.setObjectName("label_6")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(37, 38, 84, 30))
        self.label.setObjectName("label")
        self.label_4 = QtWidgets.QLabel(self.tab)
        self.label_4.setGeometry(QtCore.QRect(40, 230, 53, 30))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.tab)
        self.label_5.setGeometry(QtCore.QRect(40, 150, 81, 30))
        self.label_5.setObjectName("label_5")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(37, 72, 91, 30))
        self.label_2.setObjectName("label_2")
        self.txtInterno = QtWidgets.QLineEdit(self.tab)
        self.txtInterno.setEnabled(False)
        self.txtInterno.setGeometry(QtCore.QRect(130, 38, 162, 30))
        self.txtInterno.setObjectName("txtInterno")
        self.txtCedula = QtWidgets.QLineEdit(self.tab)
        self.txtCedula.setEnabled(False)
        self.txtCedula.setGeometry(QtCore.QRect(130, 72, 162, 30))
        self.txtCedula.setMaxLength(11)
        self.txtCedula.setCursorPosition(1)
        self.txtCedula.setObjectName("txtCedula")
        self.txtNombre = QtWidgets.QLineEdit(self.tab)
        self.txtNombre.setEnabled(False)
        self.txtNombre.setGeometry(QtCore.QRect(130, 108, 531, 30))
        self.txtNombre.setObjectName("txtNombre")
        self.txtdireccion = QtWidgets.QLineEdit(self.tab)
        self.txtdireccion.setEnabled(False)
        self.txtdireccion.setGeometry(QtCore.QRect(130, 150, 531, 30))
        self.txtdireccion.setObjectName("txtdireccion")
        self.txtTelefono = QtWidgets.QLineEdit(self.tab)
        self.txtTelefono.setEnabled(False)
        self.txtTelefono.setGeometry(QtCore.QRect(130, 190, 162, 30))
        self.txtTelefono.setText("")
        self.txtTelefono.setMaxLength(10)
        self.txtTelefono.setObjectName("txtTelefono")

        self.cbCiudad = QtWidgets.QComboBox(self.tab)
        self.cbCiudad.setEnabled(True)
        self.cbCiudad.setGeometry(QtCore.QRect(130, 230, 160, 30))
        self.cbCiudad.setObjectName("cbCiudad")

        self.cbZona = QtWidgets.QComboBox(self.tab)
        self.cbZona.setEnabled(True)
        self.cbZona.setGeometry(QtCore.QRect(130, 270, 160, 30))
        self.cbZona.setObjectName("cbZona")
        self.cbZona.addItem("Norte","N")
        self.cbZona.addItem("Centro","C")
        self.cbZona.addItem("Sur","S")

        self.cbCobrador = QtWidgets.QComboBox(self.tab)
        self.cbCobrador.setEnabled(True)
        self.cbCobrador.setGeometry(QtCore.QRect(130, 310, 160, 30))
        self.cbCobrador.setObjectName("cbCobrador")

        self.layoutWidget = QtWidgets.QWidget(self.tab)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 350, 651, 31))
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

        self.tabClientes.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.txtBuscar = QtWidgets.QLineEdit(self.tab_2)
        self.txtBuscar.setEnabled(True)
        self.txtBuscar.setGeometry(QtCore.QRect(83, 10, 581, 30))
        self.txtBuscar.setObjectName("txtBuscar")
        self.txtBuscar.setPlaceholderText("Ingrese nombre del Cliente")
        self.label_7 = QtWidgets.QLabel(self.tab_2)
        self.label_7.setGeometry(QtCore.QRect(10, 10, 61, 30))
        self.label_7.setObjectName("label_7")
        self.tClientes = QtWidgets.QTableWidget(self.tab_2)
        self.tClientes.setGeometry(QtCore.QRect(10, 50, 654, 331))
        self.tClientes.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.tClientes.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tClientes.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tClientes.setSelectionBehavior(self.tClientes.SelectRows)
        self.tClientes.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tClientes.setObjectName("tClientes")
        self.tClientes.setColumnCount(6)
        self.tClientes.setColumnWidth(0, 30)
        self.tClientes.setColumnWidth(1, 100)
        self.tClientes.setColumnWidth(2, 100)
        self.tClientes.setColumnWidth(3, 200)
        self.tClientes.setColumnWidth(4, 150)
        self.tClientes.setColumnWidth(5, 120)
        self.tClientes.verticalHeader().setVisible(False)

        self.tabClientes.addTab(self.tab_2, "")
        self.retranslateUi(self)
        self.tabClientes.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(self)
        self.cancelar()

        self.ciudad=0
        self.cobrador=0
        self.zona=""
        self.estado=0
        self.id=0

        self.TraerCiudades()
        self.TraerCobradores()
        self.traerClientes()

        self.tClientes.doubleClicked.connect(self.seleccionar)
        self.cbCiudad.currentIndexChanged.connect(self.seleccionarCiudad)
        self.cbCobrador.currentIndexChanged.connect(self.seleccionarCobrador)
        self.cbZona.currentTextChanged.connect(self.seleccionarZona)
        self.txtBuscar.textChanged.connect(self.buscarClientes)
        self.btnNuevo.clicked.connect(self.nuevo)
        self.btnGuardar.clicked.connect(self.guardar)
        self.btnModificar.clicked.connect(self.modificar)
        self.btnEliminar.clicked.connect(self.eliminar)
        self.btnCancelar.clicked.connect(self.cancelar)

    def habilitar(self,valor):
        self.txtCedula.setEnabled(valor)
        self.txtNombre.setEnabled(valor)
        self.txtTelefono.setEnabled(valor)
        self.txtdireccion.setEnabled(valor)
        self.txtInterno.setEnabled(valor)
        self.cbCobrador.setEnabled(valor)
        self.cbCiudad.setEnabled(valor)
        self.cbZona.setEnabled(valor)

    def limpiar(self):
        self.txtCedula.setText("")
        self.txtNombre.setText("")
        self.txtTelefono.setText("")
        self.txtdireccion.setText("")
        self.txtInterno.setText("")


    def nuevo(self):
        self.estado=0
        self.id=0
        self.limpiar()
        self.habilitar(True)
        self.btnNuevo.setEnabled(False)
        self.btnGuardar.setEnabled(True)
        self.btnCancelar.setEnabled(True)
        self.btnEliminar.setEnabled(False)
        self.btnModificar.setEnabled(False)

    def modificar(self):
        self.estado=1
        self.habilitar(True)
        self.btnNuevo.setEnabled(True)
        self.btnGuardar.setEnabled(True)
        self.btnCancelar.setEnabled(True)
        self.btnEliminar.setEnabled(True)
        self.btnModificar.setEnabled(False)

    def guardar(self):
        self.habilitar(False)
        if self.estado==0:
            self.btnNuevo.setEnabled(True)
            self.btnGuardar.setEnabled(False)
            self.btnCancelar.setEnabled(True)
            self.btnEliminar.setEnabled(False)
            self.btnModificar.setEnabled(True)
            self.registro=0
            try:
                self.id=Crear(cedula=self.txtCedula.text().replace("-",""),nombre=self.txtNombre.text(),
                      telefono=self.txtTelefono.text(),direccion=self.txtdireccion.text(),
                      ciudad=self.seleccionarCiudad(),zona=self.seleccionarZona(),
                      cobrador=self.seleccionarCobrador(),interno=self.txtInterno.text())
                QMessageBox.information(self,"YOSSNAIDER", "La Registro ha sido creado..!",buttons=QMessageBox.Ok)
            except:
                QMessageBox.information(self,"YOSSNAIDER", "Posiblemente el registro ya este creado, no es posible crearlo dos veces..!",buttons=QMessageBox.Ok)

        elif self.estado==1 and self.id>0:
            print("Actualizar registro: ",self.id)
            self.id=Actualizar(id=self.id,cedula=self.txtCedula.text().replace("-",""),nombres=self.txtNombre.text(),
                      telefono=self.txtTelefono.text(),direccion=self.txtdireccion.text(),
                      ciudad=self.seleccionarCiudad(),zona=self.seleccionarZona(),
                      cobrador=self.seleccionarCobrador(),interno=self.txtInterno.text())

            self.btnNuevo.setEnabled(True)
            self.btnGuardar.setEnabled(False)
            self.btnCancelar.setEnabled(True)
            self.btnEliminar.setEnabled(False)
            self.btnModificar.setEnabled(True)
            QMessageBox.information(self,"YOSSNAIDER", "La Registro ha sido actualizado..!",buttons=QMessageBox.Ok)
        self.traerClientes()

    def eliminar(self):
        self.estado=1
        self.habilitar(False)
        if self.id>0:
            buttonReply = QMessageBox.question(self, 'Mensaje', "Seguro que desea eliminar este registro?",QMessageBox.Yes | QMessageBox.No)
            if buttonReply == QMessageBox.Yes:
                if (self.id) > 0:
                    CambiarEstado(id=self.id)
                    QMessageBox.information(self,"YOSSNAIDER", "La Registro ha sido desactivado..!",buttons=QMessageBox.Ok)
                    self.id = 0
                else:
                    QMessageBox.information(self,"YOSSNAIDER", "Primero seleccione un registro..!",buttons=QMessageBox.Ok)
            elif buttonReply == QMessageBox.No:
                pass
            self.traerClientes()
            self.limpiar()

    def cancelar(self):
        self.estado=0
        self.id=0
        self.limpiar()
        self.habilitar(False)
        self.btnNuevo.setEnabled(True)
        self.btnGuardar.setEnabled(False)
        self.btnCancelar.setEnabled(True)
        self.btnEliminar.setEnabled(False)
        self.btnModificar.setEnabled(False)

    def seleccionarCiudad(self):
        self.ciudad=int(self.cbCiudad.currentData())
        print(self.ciudad)
        return self.ciudad

    def seleccionarCobrador(self):
        self.cobrador=int(self.cbCobrador.currentData())
        print(self.cobrador)
        return self.cobrador

    def seleccionarZona(self):
        self.zona=(self.cbZona.currentData())
        print(self.zona)
        return self.zona

    def TraerCobradores(self):
        for cobrador in ListarCobrador():
            self.cbCobrador.addItem(cobrador.nombre,cobrador.id)

    def TraerCiudades(self):
        for ciudad in Listar():
            self.cbCiudad.addItem(ciudad.nombre,ciudad.id)

    def traerClientes(self):
        style = "QHeaderView::section {background:#10608D;color:#FFFFFF;}"
        self.tClientes.horizontalHeader().setStyleSheet(style)
        self.tClientes.setRowCount(0)
        self.tClientes.setHorizontalHeaderLabels(["ID","INTERNO","CEDULA","NOMBRE","CIUDAD","TELEFONO"])
        for cliente in ListarClientes():
            rowPosition = self.tClientes.rowCount()
            self.tClientes.insertRow(rowPosition)

            id = QTableWidgetItem(str(cliente.id))
            id.setTextAlignment(QtCore.Qt.AlignCenter)
            self.tClientes.setItem(rowPosition, 0, id)

            interno = QTableWidgetItem(str(cliente.interno))
            interno.setTextAlignment(QtCore.Qt.AlignCenter)
            self.tClientes.setItem(rowPosition, 1, interno)

            cedula = QTableWidgetItem(str(cliente.cedula))
            cedula.setTextAlignment(QtCore.Qt.AlignCenter)
            self.tClientes.setItem(rowPosition, 2, cedula)

            self.tClientes.setItem(rowPosition, 3, QTableWidgetItem(str(cliente.nombres)))
            self.tClientes.setItem(rowPosition, 4, QTableWidgetItem(str(cliente.ciudad.nombre)))
            self.tClientes.setItem(rowPosition, 5, QTableWidgetItem(str(cliente.telefono)))

    def buscarClientes(self):
        style = "QHeaderView::section {background:#10608D;color:#FFFFFF;}"
        self.tClientes.horizontalHeader().setStyleSheet(style)
        self.tClientes.setRowCount(0)
        self.tClientes.setHorizontalHeaderLabels(["ID","INTERNO","CEDULA","NOMBRE","CIUDAD","TELEFONO"])
        for cliente in Buscar_Nombre(self.txtBuscar.text()):
            rowPosition = self.tClientes.rowCount()
            self.tClientes.insertRow(rowPosition)

            id = QTableWidgetItem(str(cliente.id))
            id.setTextAlignment(QtCore.Qt.AlignCenter)
            self.tClientes.setItem(rowPosition, 0, id)

            interno = QTableWidgetItem(str(cliente.interno))
            interno.setTextAlignment(QtCore.Qt.AlignCenter)
            self.tClientes.setItem(rowPosition, 1, interno)

            cedula = QTableWidgetItem(str(cliente.cedula))
            cedula.setTextAlignment(QtCore.Qt.AlignCenter)
            self.tClientes.setItem(rowPosition, 2, cedula)

            self.tClientes.setItem(rowPosition, 3, QTableWidgetItem(str(cliente.nombres)))
            self.tClientes.setItem(rowPosition, 4, QTableWidgetItem(str(cliente.ciudad.nombre)))
            self.tClientes.setItem(rowPosition, 5, QTableWidgetItem(str(cliente.telefono)))

    def seleccionar(self):
        self.id = int(self.tClientes.item(self.tClientes.currentRow(),0).text())
        cliente=getCliente(self.id)
        self.habilitar(False)
        print(cliente.id)
        self.limpiar()
        self.txtInterno.setText(cliente.interno)
        self.txtCedula.setText(cliente.cedula)
        self.txtdireccion.setText(cliente.direccion)
        self.txtTelefono.setText(cliente.telefono)
        self.txtNombre.setText(cliente.nombres)
        self.cbCiudad.setCurrentText(cliente.ciudad.nombre)
        zona=""
        if cliente.zona=="C":
            zona="Centro"
        elif cliente.zona=="S":
            zona="Sur"
        else:
            zona="Norte"
        self.cbZona.setCurrentText(zona)
        self.cbCobrador.setCurrentText(cliente.cobrador.nombre)
        self.tabClientes.setCurrentIndex(0)
        self.btnNuevo.setEnabled(True)
        self.btnGuardar.setEnabled(False)
        self.btnCancelar.setEnabled(True)
        self.btnEliminar.setEnabled(True)
        self.btnModificar.setEnabled(True)


    def retranslateUi(self, frmRegistroClientes):
        _translate = QtCore.QCoreApplication.translate
        frmRegistroClientes.setWindowTitle(_translate("frmRegistroClientes", "Registro de Clientes"))
        self.label_9.setText(_translate("frmRegistroClientes", "Cobrador"))
        self.label_3.setText(_translate("frmRegistroClientes", "Nombres"))
        self.label_8.setText(_translate("frmRegistroClientes", "Zona"))
        self.label_6.setText(_translate("frmRegistroClientes", "Teléfono"))
        self.label.setText(_translate("frmRegistroClientes", "Código Interno"))
        self.label_4.setText(_translate("frmRegistroClientes", "Ciudad"))
        self.label_5.setText(_translate("frmRegistroClientes", "Dirección"))
        self.label_2.setText(_translate("frmRegistroClientes", "Cédula"))
        self.txtCedula.setInputMask(_translate("frmRegistroClientes", "999999999-9"))
        self.txtCedula.setText(_translate("frmRegistroClientes", "-"))
        self.txtTelefono.setInputMask(_translate("frmRegistroClientes", "9999999999"))
        self.btnNuevo.setText(_translate("frmRegistroClientes", "Nuevo"))
        self.btnGuardar.setText(_translate("frmRegistroClientes", "Guardar"))
        self.btnModificar.setText(_translate("frmRegistroClientes", "Modificar"))
        self.btnEliminar.setText(_translate("frmRegistroClientes", "Eliminar"))
        self.btnCancelar.setText(_translate("frmRegistroClientes", "Cancelar"))
        self.tabClientes.setTabText(self.tabClientes.indexOf(self.tab), _translate("frmRegistroClientes", "Página de Registro"))
        self.label_7.setText(_translate("frmRegistroClientes", "Buscador"))
        self.tabClientes.setTabText(self.tabClientes.indexOf(self.tab_2), _translate("frmRegistroClientes", "Listado"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_frmClientes()
    ui.show()
    sys.exit(app.exec_())
