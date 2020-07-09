# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'yossnaider.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

from Ciudades.frmCiudades import Ui_frmCiudades
from Clientes.frmCliente import Ui_frmClientes
from Clientes.frmCuentasCobrar import Ui_frmCuentasCobrar
from Cobradores.frmCobrador import Ui_frmCobrador
from Productos.frmNotasVenta import Ui_frmVentas
from Productos.frmProductos import Ui_frmProductos
from Productos.frmRegistrosInventario import Ui_frmRegistrosInventario


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 800)
        self.mdi = QtWidgets.QMdiArea()
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Recursos/clientes.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.mdi)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        self.menuConfiguraci_n = QtWidgets.QMenu(self.menubar)
        self.menuConfiguraci_n.setObjectName("menuConfiguraci_n")
        self.menuClientes = QtWidgets.QMenu(self.menubar)
        self.menuClientes.setObjectName("menuClientes")
        self.menuProductos = QtWidgets.QMenu(self.menubar)
        self.menuProductos.setObjectName("menuProductos")
        self.menuNotas_de_Venta = QtWidgets.QMenu(self.menubar)
        self.menuNotas_de_Venta.setObjectName("menuNotas_de_Venta")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionCiudades = QtWidgets.QAction(MainWindow)
        self.actionCiudades.setObjectName("actionCiudades")
        self.actionCobradores = QtWidgets.QAction(MainWindow)
        self.actionCobradores.setObjectName("actionCobradores")
        self.actionRegistro_de_Clientes = QtWidgets.QAction(MainWindow)
        self.actionRegistro_de_Clientes.setObjectName("actionRegistro_de_Clientes")
        self.actionCuentas_por_Cobbrar = QtWidgets.QAction(MainWindow)
        self.actionCuentas_por_Cobbrar.setObjectName("actionCuentas_por_Cobbrar")
        self.actionRegistro_de_Productos = QtWidgets.QAction(MainWindow)
        self.actionRegistro_de_Productos.setObjectName("actionRegistro_de_Productos")
        self.actionInventario = QtWidgets.QAction(MainWindow)
        self.actionInventario.setObjectName("actionInventario")
        self.actionRegistro = QtWidgets.QAction(MainWindow)
        self.actionRegistro.setObjectName("actionRegistro")
        self.actionReporte = QtWidgets.QAction(MainWindow)
        self.actionReporte.setObjectName("actionReporte")
        self.menuConfiguraci_n.addAction(self.actionCiudades)
        self.menuConfiguraci_n.addSeparator()
        self.menuConfiguraci_n.addAction(self.actionCobradores)
        self.menuClientes.addAction(self.actionRegistro_de_Clientes)
        self.menuClientes.addAction(self.actionCuentas_por_Cobbrar)
        self.menuProductos.addAction(self.actionRegistro_de_Productos)
        self.menuProductos.addAction(self.actionInventario)
        self.menuNotas_de_Venta.addAction(self.actionRegistro)
        self.menuNotas_de_Venta.addAction(self.actionReporte)
        self.menubar.addAction(self.menuConfiguraci_n.menuAction())
        self.menubar.addAction(self.menuClientes.menuAction())
        self.menubar.addAction(self.menuProductos.menuAction())
        self.menubar.addAction(self.menuNotas_de_Venta.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.actionCiudades.triggered.connect(self.cargarCiudades)
        self.actionCobradores.triggered.connect(self.cargarCobradores)
        self.actionRegistro_de_Clientes.triggered.connect(self.cargarClientes)
        self.actionRegistro_de_Productos.triggered.connect(self.cargarProductos)
        self.actionInventario.triggered.connect(self.cargarInventario)
        self.actionRegistro.triggered.connect(self.cargarVentas)
        self.actionCuentas_por_Cobbrar.triggered.connect(self.cargarCuentasCobrar)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "YOSSNAIDER"))
        self.menuConfiguraci_n.setTitle(_translate("MainWindow", "Configuración"))
        self.menuClientes.setTitle(_translate("MainWindow", "Clientes"))
        self.menuProductos.setTitle(_translate("MainWindow", "Productos"))
        self.menuNotas_de_Venta.setTitle(_translate("MainWindow", "Notas de Venta"))
        self.actionCiudades.setText(_translate("MainWindow", "Ciudades"))
        self.actionCobradores.setText(_translate("MainWindow", "Cobradores"))
        self.actionRegistro_de_Clientes.setText(_translate("MainWindow", "Registro de Clientes"))
        self.actionCuentas_por_Cobbrar.setText(_translate("MainWindow", "Cuentas por Cobrar"))
        self.actionRegistro_de_Productos.setText(_translate("MainWindow", "Registro de Productos"))
        self.actionInventario.setText(_translate("MainWindow", "Inventario"))
        self.actionRegistro.setText(_translate("MainWindow", "Registro"))
        self.actionReporte.setText(_translate("MainWindow", "Reportes"))

    def cargarCiudades(self):
        print("Cargar frm Ciudades")
        frm = Ui_frmCiudades()
        self.mdi.addSubWindow(frm)
        frm.show()

    def cargarCobradores(self):
        print("Cargar frm Cobradores")
        frm = Ui_frmCobrador()
        self.mdi.addSubWindow(frm)
        frm.show()

    def cargarClientes(self):
        print("Cargar frm Ciudades")
        frm = Ui_frmClientes()
        self.mdi.addSubWindow(frm)
        frm.show()

    def cargarProductos(self):
        print("Cargar frm Ciudades")
        frm = Ui_frmProductos()
        self.mdi.addSubWindow(frm)
        frm.show()

    def cargarVentas(self):
        print("Cargar frm Ventas")
        frm = Ui_frmVentas()
        self.mdi.addSubWindow(frm)
        frm.show()

    def cargarInventario(self):
        frm = Ui_frmRegistrosInventario()
        self.mdi.addSubWindow(frm)
        frm.show()

    def cargarCuentasCobrar(self):
        frm = Ui_frmCuentasCobrar()
        self.mdi.addSubWindow(frm)
        frm.show()
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
