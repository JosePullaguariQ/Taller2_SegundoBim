# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TallerUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(611, 318)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 30, 55, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 60, 55, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(40, 100, 55, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(40, 130, 131, 31))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(40, 180, 101, 21))
        self.label_5.setObjectName("label_5")
        self.txtNombre = QtWidgets.QTextEdit(self.centralwidget)
        self.txtNombre.setGeometry(QtCore.QRect(120, 20, 111, 31))
        self.txtNombre.setObjectName("txtNombre")
        self.txtApellido = QtWidgets.QTextEdit(self.centralwidget)
        self.txtApellido.setGeometry(QtCore.QRect(120, 60, 111, 31))
        self.txtApellido.setObjectName("txtApellido")
        self.txtCorreo = QtWidgets.QTextEdit(self.centralwidget)
        self.txtCorreo.setGeometry(QtCore.QRect(120, 100, 111, 31))
        self.txtCorreo.setObjectName("txtCorreo")
        self.txtCelular = QtWidgets.QTextEdit(self.centralwidget)
        self.txtCelular.setGeometry(QtCore.QRect(200, 140, 111, 31))
        self.txtCelular.setObjectName("txtCelular")
        self.txtCedula = QtWidgets.QTextEdit(self.centralwidget)
        self.txtCedula.setGeometry(QtCore.QRect(200, 180, 111, 31))
        self.txtCedula.setObjectName("txtCedula")
        self.btn_Validar = QtWidgets.QPushButton(self.centralwidget)
        self.btn_Validar.setGeometry(QtCore.QRect(40, 240, 93, 28))
        self.btn_Validar.setObjectName("btn_Validar")
        self.btn_Limpiar = QtWidgets.QPushButton(self.centralwidget)
        self.btn_Limpiar.setGeometry(QtCore.QRect(170, 240, 93, 28))
        self.btn_Limpiar.setObjectName("btn_Limpiar")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(370, 40, 61, 21))
        self.label_6.setObjectName("label_6")
        self.lbl_SitioPersona = QtWidgets.QLabel(self.centralwidget)
        self.lbl_SitioPersona.setGeometry(QtCore.QRect(370, 80, 161, 21))
        self.lbl_SitioPersona.setObjectName("lbl_SitioPersona")
        self.lbl_Correo = QtWidgets.QLabel(self.centralwidget)
        self.lbl_Correo.setGeometry(QtCore.QRect(370, 130, 161, 31))
        self.lbl_Correo.setText("")
        self.lbl_Correo.setObjectName("lbl_Correo")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.btn_Limpiar.clicked.connect(self.txtNombre.clear) # type: ignore
        self.btn_Limpiar.clicked.connect(self.txtApellido.clear) # type: ignore
        self.btn_Limpiar.clicked.connect(self.txtCorreo.clear) # type: ignore
        self.btn_Limpiar.clicked.connect(self.txtCelular.clear) # type: ignore
        self.btn_Limpiar.clicked.connect(self.txtCedula.clear) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Validaci├│n de informaci├│n"))
        self.label.setText(_translate("MainWindow", "Nombre:"))
        self.label_2.setText(_translate("MainWindow", "Apellido:"))
        self.label_3.setText(_translate("MainWindow", "Correo:"))
        self.label_4.setText(_translate("MainWindow", "N├║mero de tel├®fono celular:"))
        self.label_5.setText(_translate("MainWindow", "N├║mero de c├®dula:"))
        self.btn_Validar.setText(_translate("MainWindow", "Validar"))
        self.btn_Limpiar.setText(_translate("MainWindow", "Limpiar"))
        self.label_6.setText(_translate("MainWindow", "Resultados:"))
        self.lbl_SitioPersona.setText(_translate("MainWindow", " "))
