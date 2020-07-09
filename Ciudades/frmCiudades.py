# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'frmCiudades.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!
import sys
from PyQt5 import QtCore, QtGui, QtWidgets, Qt
from PyQt5.QtGui import QWindow, QIcon
from PyQt5.QtWidgets import QTableWidgetItem, QAbstractItemView, QMessageBox, QLineEdit, QSystemTrayIcon

from Ciudades.views import Listar, Crear, Actualizar, CambiarEstado, Buscar_Nombre


class Ui_frmCiudades(QtWidgets.QMdiSubWindow):
    def __init__(self, parent=None):
        super(Ui_frmCiudades, self).__init__()
        self.setObjectName("frmCiudades")
        self.resize(403, 590)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./Recursos/mundo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
        self.btnRegistrar = QtWidgets.QPushButton(self)
        self.btnRegistrar.setGeometry(QtCore.QRect(310, 80, 71, 33))
        self.btnRegistrar.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("./Recursos/guardar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnRegistrar.setIcon(icon1)
        self.btnRegistrar.setObjectName("btnRegistrar")
        self.txtNombre = QtWidgets.QLineEdit(self)
        self.txtNombre.setGeometry(QtCore.QRect(20, 80, 281, 33))
        self.txtNombre.setObjectName("txtNombre")
        self.tCiudades = QtWidgets.QTableWidget(self)
        self.tCiudades.setGeometry(QtCore.QRect(20, 120, 361, 411))
        self.tCiudades.setColumnCount(2)
        style = "QHeaderView::section {background:#10608D;color:#FFFFFF;}"
        self.tCiudades.horizontalHeader().setStyleSheet(style)
        self.tCiudades.setSelectionBehavior(self.tCiudades.SelectRows)
        self.tCiudades.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tCiudades.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tCiudades.setObjectName("tCiudades")
        self.tCiudades.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tCiudades.setColumnWidth(1,240)
        self.tCiudades.verticalHeader().setVisible(False)
        self.tCiudades.setHorizontalHeaderLabels(["ID", "NOMBRE"])
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(30, 40, 351, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(20, 530, 361, 16))
        self.label_2.setObjectName("label_2")


        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)
        self.TraerCiudades()

        self.tCiudades.doubleClicked.connect(self.modificar)
        self.btnRegistrar.clicked.connect(self.crearCiudades)
        self.id=0
        self.nombre=""

        QtWidgets.QShortcut(QtCore.Qt.Key_Delete, self.tCiudades, activated=self.eliminarFila)

    def keyReleaseEvent(self, event):
        self.tCiudades.clear()
        self.tCiudades.setRowCount(0)
        self.tCiudades.setHorizontalHeaderLabels(["ID", "NOMBRE"])
        for ciudad in Buscar_Nombre(self.txtNombre.text()):
            rowPosition = self.tCiudades.rowCount()
            self.tCiudades.insertRow(rowPosition)
            id = QTableWidgetItem(str(ciudad.id))
            id.setTextAlignment(QtCore.Qt.AlignCenter)
            self.tCiudades.setItem(rowPosition, 0, id)
            self.tCiudades.setItem(rowPosition, 1, QTableWidgetItem(str(ciudad.nombre)))


    def buscar(self):
        print(self.txtNombre.text())
    def TraerCiudades(self):
        self.tCiudades.clear()
        self.tCiudades.setRowCount(0)
        self.tCiudades.setHorizontalHeaderLabels(["ID", "NOMBRE"])
        for ciudad in Listar():
            rowPosition = self.tCiudades.rowCount()
            self.tCiudades.insertRow(rowPosition)
            id=QTableWidgetItem(str(ciudad.id))
            id.setTextAlignment(QtCore.Qt.AlignCenter)
            self.tCiudades.setItem(rowPosition,0,id)
            self.tCiudades.setItem(rowPosition, 1, QTableWidgetItem(str(ciudad.nombre)))

    def crearCiudades(self):
        if self.id >0:
            if len(self.txtNombre.text()) > 0:
                valor = Actualizar(self.id,self.txtNombre.text())
                if valor>0:
                    QMessageBox.information(self,"YOSSNAIDER","Registro Modificado..!",buttons=QMessageBox.Ok)
                    self.id=0
        else:
            if len(self.txtNombre.text())>0:
                valor = Crear(self.txtNombre.text())
                if valor>0:
                    QMessageBox.information(self,"YOSSNAIDER", "La Ciudad ha sido creada..!",buttons=QMessageBox.Ok)
            else:
                QMessageBox.critical(self,"YOSSNAIDER", "El Cuadro de Entrada esta Vacío..!",buttons=QMessageBox.Ok)
        self.TraerCiudades()
        self.txtNombre.setText("")

    def modificar(self):
        print("entra a modificar")
        buttonReply = QMessageBox.question(self, 'Mensaje', "Preparado para modificar",
                                           QMessageBox.Yes | QMessageBox.No)
        print(int(buttonReply))
        if buttonReply == QMessageBox.Yes:
            seleccion = self.tCiudades.currentRow()
            self.id = int(self.tCiudades.item(seleccion, 0).text())
            self.nombre = self.tCiudades.item(seleccion, 1).text()
            self.txtNombre.setText(self.nombre)
        if buttonReply == QMessageBox.No:
            self.txtNombre.setText("")
            self.id=0

    def eliminarFila(self):
        rowPosition = self.tCiudades.currentRow()
        buttonReply = QMessageBox.question(self, 'Mensaje', "Seguro que desea desactivar este registro..!",
                                           QMessageBox.Yes | QMessageBox.No)
        if buttonReply == QMessageBox.Yes:
            CambiarEstado(int(self.tCiudades.item(rowPosition,0).text()))
            self.TraerCiudades()
            QMessageBox.information(self, "Información", "El Registro se ha eliminado, es posible recuperarlo desde la Base de datos", QMessageBox.Ok)
        else:
            pass

    def retranslateUi(self, frmCiudades):
        _translate = QtCore.QCoreApplication.translate
        frmCiudades.setWindowTitle(_translate("frmCiudades", "Ciudades"))
        self.txtNombre.setPlaceholderText(_translate("frmCiudades", "Nombre de la Ciudad"))
        self.label.setText(_translate("frmCiudades", "REGISTRO DE CIUDADES"))
        self.label_2.setText(_translate("frmCiudades", "Doble clic para editar un registro"))