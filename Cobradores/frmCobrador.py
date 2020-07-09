# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cobrador.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QTableWidgetItem, QAbstractItemView, QMessageBox, QSystemTrayIcon

from Cobradores.views import ListarCobrador, Crear, Actualizar, Eliminar
from Productos.views import Contador


class Ui_frmCobrador(QtWidgets.QMdiSubWindow):
    def __init__(self,parent=0):
        super(Ui_frmCobrador, self).__init__()
        self.setObjectName("frmCobrador")
        self.resize(635, 470)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./Recursos/clientes.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
        self.tCobradores = QtWidgets.QTableWidget(self)
        self.tCobradores.setGeometry(QtCore.QRect(20, 220, 591, 231))
        self.tCobradores.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.tCobradores.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tCobradores.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tCobradores.setSelectionBehavior(self.tCobradores.SelectRows)
        self.tCobradores.setSelectionMode(QAbstractItemView.SingleSelection)

        self.tCobradores.setObjectName("tCobradores")
        self.tCobradores.setColumnCount(4)
        self.tCobradores.setColumnWidth(0, 50)
        self.tCobradores.setColumnWidth(2, 269)
        style = "QHeaderView::section {background:#10608D;color:#FFFFFF;}"
        self.tCobradores.horizontalHeader().setStyleSheet(style)
        self.tCobradores.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tCobradores.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tCobradores.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setBackground(QtGui.QColor(44, 88, 132))
        self.tCobradores.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tCobradores.setHorizontalHeaderItem(3, item)
        self.tCobradores.verticalHeader().setVisible(False)
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(20, 40, 111, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(20, 80, 111, 31))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self)
        self.label_3.setGeometry(QtCore.QRect(20, 120, 111, 31))
        self.label_3.setObjectName("label_3")
        self.txtCedula = QtWidgets.QLineEdit(self)
        self.txtCedula.setGeometry(QtCore.QRect(130, 40, 201, 30))
        self.txtCedula.setObjectName("txtCedula")
        self.txtCedula.setMaxLength(10)
        self.txtNombre = QtWidgets.QLineEdit(self)
        self.txtNombre.setGeometry(QtCore.QRect(130, 80, 471, 30))
        self.txtNombre.setObjectName("txtNombre")
        self.txtTelefono = QtWidgets.QLineEdit(self)
        self.txtTelefono.setGeometry(QtCore.QRect(130, 120, 201, 30))
        self.txtTelefono.setMaxLength(10)
        self.txtTelefono.setObjectName("txtTelefono")
        self.widget = QtWidgets.QWidget(self)
        self.widget.setGeometry(QtCore.QRect(20, 170, 591, 31))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.btnNuevo = QtWidgets.QPushButton(self.widget)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("./Recursos/nuevo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnNuevo.setIcon(icon1)
        self.btnNuevo.setObjectName("btnNuevo")
        self.gridLayout.addWidget(self.btnNuevo, 0, 0, 1, 1)
        self.btnGuardar = QtWidgets.QPushButton(self.widget)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("./Recursos/guardar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnGuardar.setIcon(icon2)
        self.btnGuardar.setObjectName("btnGuardar")
        self.gridLayout.addWidget(self.btnGuardar, 0, 1, 1, 1)
        self.btnModificar = QtWidgets.QPushButton(self.widget)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("./Recursos/editar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnModificar.setIcon(icon3)
        self.btnModificar.setObjectName("btnModificar")
        self.gridLayout.addWidget(self.btnModificar, 0, 2, 1, 1)
        self.btnEliminar = QtWidgets.QPushButton(self.widget)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("./Recursos/eliminar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnEliminar.setIcon(icon4)
        self.btnEliminar.setObjectName("btnEliminar")
        self.gridLayout.addWidget(self.btnEliminar, 0, 3, 1, 1)
        self.btnCancelar = QtWidgets.QPushButton(self.widget)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("./Recursos/cancelar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnCancelar.setIcon(icon5)
        self.btnCancelar.setObjectName("btnCancelar")
        self.gridLayout.addWidget(self.btnCancelar, 0, 4, 1, 1)

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

        self.habilitar(False)
        self.TraerTodo()
        self.estado=0
        self.id=0

        self.btnNuevo.setEnabled(True)
        self.btnGuardar.setEnabled(False)
        self.btnCancelar.setEnabled(True)
        self.btnEliminar.setEnabled(False)
        self.btnModificar.setEnabled(False)

        self.btnNuevo.clicked.connect(self.nuevo)
        self.btnGuardar.clicked.connect(self.registrar)
        self.tCobradores.doubleClicked.connect(self.seleccionar)
        self.btnModificar.clicked.connect(self.modificar)
        self.btnCancelar.clicked.connect(self.cancelar)
        self.btnEliminar.clicked.connect(self.eliminar)

    def retranslateUi(self, frmCobrador):
        _translate = QtCore.QCoreApplication.translate
        frmCobrador.setWindowTitle(_translate("frmCobrador", "Registro de Cobradores"))
        item = self.tCobradores.horizontalHeaderItem(0)
        item.setText(_translate("frmCobrador", "ID"))
        item = self.tCobradores.horizontalHeaderItem(1)
        item.setText(_translate("frmCobrador", "CÉDULA"))
        item = self.tCobradores.horizontalHeaderItem(2)
        item.setText(_translate("frmCobrador", "NOMBRE Y APELLIDO"))
        item = self.tCobradores.horizontalHeaderItem(3)
        item.setText(_translate("frmCobrador", "TELEFONO"))
        self.label.setText(_translate("frmCobrador", "Cédula"))
        self.label_2.setText(_translate("frmCobrador", "Nombre Completo"))
        self.label_3.setText(_translate("frmCobrador", "Teléfono"))
        self.btnNuevo.setText(_translate("frmCobrador", "Nuevo"))
        self.btnGuardar.setText(_translate("frmCobrador", "Guardar"))
        self.btnModificar.setText(_translate("frmCobrador", "Modificar"))
        self.btnEliminar.setText(_translate("frmCobrador", "Eliminar"))
        self.btnCancelar.setText(_translate("frmCobrador", "Cancelar"))
        self.txtCedula.setPlaceholderText(_translate("frmCobrador", "Ingrese solo numeros"))
        self.txtNombre.setPlaceholderText(_translate("frmCobrador", "Ingrese solo texto"))
        self.txtTelefono.setPlaceholderText(_translate("frmCobrador", "Ingrese solo numeros"))

    def TraerTodo(self):
        self.tCobradores.clear()
        self.tCobradores.setRowCount(0)
        self.tCobradores.setHorizontalHeaderLabels(["ID", "CÉDULA","NOMBRES Y APELLIDOS",'TELÉFONO'])
        for cobrador in ListarCobrador():
            rowPosition = self.tCobradores.rowCount()
            self.tCobradores.insertRow(rowPosition)
            id = QTableWidgetItem(str(cobrador.id))
            id.setTextAlignment(QtCore.Qt.AlignCenter)
            self.tCobradores.setItem(rowPosition, 0, id)
            self.tCobradores.setItem(rowPosition, 1, QTableWidgetItem(str(cobrador.cedula)))
            self.tCobradores.setItem(rowPosition, 2, QTableWidgetItem(str(cobrador.nombre)))
            self.tCobradores.setItem(rowPosition, 3, QTableWidgetItem(str(cobrador.telefono)))

    def habilitar(self,estado):
        self.txtTelefono.setEnabled(estado)
        self.txtNombre.setEnabled(estado)
        self.txtCedula.setEnabled(estado)

    def limpiar(self):
        self.txtTelefono.setText("")
        self.txtNombre.setText("")
        self.txtCedula.setText("")

    def cancelar(self):
        self.limpiar()
        self.habilitar(False)
        self.id=0
        self.btnNuevo.setEnabled(True)
        self.btnGuardar.setEnabled(False)
        self.btnCancelar.setEnabled(True)
        self.btnEliminar.setEnabled(False)
        self.btnModificar.setEnabled(False)

    def nuevo(self):
        self.habilitar(True)
        self.estado=0
        self.id=0
        self.limpiar()
        self.txtCedula.setFocus()
        self.btnNuevo.setEnabled(False)
        self.btnGuardar.setEnabled(True)
        self.btnCancelar.setEnabled(True)
        self.btnEliminar.setEnabled(False)
        self.btnModificar.setEnabled(False)


    def modificar(self):
        if self.id>0:
            self.habilitar(True)
            self.estado=1
            self.btnNuevo.setEnabled(True)
            self.btnGuardar.setEnabled(True)
            self.btnCancelar.setEnabled(True)
            self.btnEliminar.setEnabled(True)
            self.btnModificar.setEnabled(False)

    def seleccionar(self):
        self.id = int(self.tCobradores.item(self.tCobradores.currentRow(),0).text())
        self.txtCedula.setText(self.tCobradores.item(self.tCobradores.currentRow(), 1).text())
        self.txtNombre.setText(self.tCobradores.item(self.tCobradores.currentRow(),2).text())
        self.txtTelefono.setText(self.tCobradores.item(self.tCobradores.currentRow(), 3).text())
        print(self.id)
        self.btnNuevo.setEnabled(True)
        self.btnGuardar.setEnabled(False)
        self.btnCancelar.setEnabled(True)
        self.btnEliminar.setEnabled(True)
        self.btnModificar.setEnabled(True)


    def registrar(self):
        if self.estado==0 and len(self.txtCedula.text())==10  and len(self.txtNombre.text())>0 and len(self.txtTelefono.text())>=7:
            result=Crear(cedula=self.txtCedula.text(),nombre=self.txtNombre.text(),telefono=self.txtTelefono.text())
            self.habilitar(False)
            self.btnNuevo.setEnabled(True)
            self.btnGuardar.setEnabled(False)
            self.btnCancelar.setEnabled(True)
            self.btnEliminar.setEnabled(False)
            self.btnModificar.setEnabled(True)
            self.id=result
            QMessageBox.information(self,"YOSSNAIDER", "El registro se ha sido creado..!",buttons=QMessageBox.Ok)
        elif self.estado==1 and self.id>0 and len(self.txtCedula.text())==10  and len(self.txtNombre.text())>0 and len(self.txtTelefono.text())==10:
            result=Actualizar(id=self.id,cedula=self.txtCedula.text(),nombre=self.txtNombre.text(),telefono=self.txtTelefono.text())
            self.habilitar(False)
            self.btnNuevo.setEnabled(True)
            self.btnGuardar.setEnabled(False)
            self.btnCancelar.setEnabled(True)
            self.btnEliminar.setEnabled(False)
            self.btnModificar.setEnabled(True)
            self.id=result
            QMessageBox.information(self,"YOSSNAIDER", "El registro se ha sido actualizado..!",buttons=QMessageBox.Ok)
        else:
            QMessageBox.critical(self,"YOSSNAIDER", "Compruebe Nombre, Cédula o Telefono, estos deben contener 10 y 7 carateres numéricos respectivamente..!",buttons=QMessageBox.Ok)
        self.TraerTodo()

    def eliminar(self):
        buttonReply = QMessageBox.question(self, 'Mensaje', "Seguro que desea eliminar este registro?",
                                           QMessageBox.Yes | QMessageBox.No)
        if buttonReply == QMessageBox.Yes:
            if(self.id)>0:
                Eliminar(id=self.id)
                QMessageBox.information(self,"YOSSNAIDER", "El registro se ha sido desactivado..!",buttons=QMessageBox.Ok)
                self.id=0
            else:
                QMessageBox.critical(self,"YOSSNAIDER", "Primero seleccione un registro..!",buttons=QMessageBox.Ok)
        elif buttonReply == QMessageBox.No:
            pass
        self.TraerTodo()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_frmCobrador()
    ui.show()
    sys.exit(app.exec_())
