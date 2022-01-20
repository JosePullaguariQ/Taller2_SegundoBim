import sys
import re
import numpy as np

from PyQt5.QtWidgets import QMainWindow, QApplication 
from gui.Ui_validacion import *

class DialogoSaludoAplicacion(QMainWindow):
    def __init__(self):
        super().__init__()

        self.dialogo = Ui_MainWindow()
        self.dialogo.setupUi(self)

        self.dialogo.btn_calcular.clicked.connect(self.calcularDescuento)


    def validarInformacion(self):
        nombre = self.dialogo.txtNombre.text()
        apellido = self.dialogo.txtApellido.text()
        correo = self.dialogo.txtCorreo.text()
        celular = self.dialogo.txtCelular.text()
        cedula = self.dialogo.txtCedula.text()
        self.validarProvincia(cedula)

    def validarProvincia(self, codigo):
        var = re.compile(r'{\d}*2')
        mo = var.search(codigo)
        listProvincias = np.array([['01', 'Azuay'], ['02', 'Bolivar'],['03', 'Cañar'],['04', 'Carchi'],['05', 'Cotopaxi'],
                                    ['06', 'Chimborazo'], ['07', 'El Oro'],['08', 'Esmeraldas'],['09', 'Guayas'],
                                    ['10', 'Imbabura'],['11', 'Loja'],['12', 'Los Rios'],['13', 'Manabi'],['14', 'Morono Santiago'],
                                    ['15', 'Napo'],['16', 'Pastaza'],['17', 'Pichincha'],['18', 'Tungurahua'],['19', 'Zamora Chinchipe'],['20', 'Galápagos'],
                                    ['21', 'Sucumbios'],['22', 'Orellana'],['23', 'Santo Domingo de los Tsáchilas'],['24', 'Santa Elena']])
        var2 = listProvincias[mo]

        return var2[1]
         
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialogo = DialogoSaludoAplicacion()
    dialogo.show()
    sys.exit(app.exec_())