from PyQt5.QtWidgets import QMessageBox


def showDialog(tipo=QMessageBox.Information,titulo=None,mensaje=None) :
    try:
        msgBox = QMessageBox()
        msgBox.setIcon (tipo)
        msgBox.setText (mensaje)
        msgBox.setWindowTitle (titulo)
        return msgBox.exec()
    except Exception as error:
        print(error)
        msgBox = QMessageBox()
        msgBox.show()