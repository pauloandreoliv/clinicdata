from config import *

#Interface
class Ui_ClinicData(object):
    def setupUi(self, ClinicData):
        
        #Define tamanho e propriedades
        ClinicData.setObjectName("ClinicData")
        ClinicData.resize(220, 494)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ClinicData.sizePolicy().hasHeightForWidth())
        ClinicData.setSizePolicy(sizePolicy)
        ClinicData.setMinimumSize(QtCore.QSize(220, 0))
        ClinicData.setMaximumSize(QtCore.QSize(220, 500))
        ClinicData.setStyleSheet("background-color:rgb(119, 162, 255);")
        self.centralwidget = QtWidgets.QWidget(ClinicData)
        self.centralwidget.setMaximumSize(QtCore.QSize(220, 500))
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")

        #Título - Boas vindas
        self.boas_vindas = QtWidgets.QLabel(self.centralwidget)
        self.boas_vindas.setGeometry(QtCore.QRect(50, 50, 101, 16))
        self.boas_vindas.setStyleSheet("color: white;")
        self.boas_vindas.setObjectName("boas_vindas")

        #Título - Usuário
        self.boas_vindas_2 = QtWidgets.QLabel(self.centralwidget)
        self.boas_vindas_2.setGeometry(QtCore.QRect(50, 70, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.boas_vindas_2.setFont(font)
        self.boas_vindas_2.setStyleSheet("color: white;")
        self.boas_vindas_2.setObjectName("boas_vindas_2")

        #Título - Menu
        self.menu_titulo = QtWidgets.QLabel(self.centralwidget)
        self.menu_titulo.setGeometry(QtCore.QRect(80, 150, 49, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.menu_titulo.setFont(font)
        self.menu_titulo.setStyleSheet("color: white;")
        self.menu_titulo.setObjectName("menu_titulo")

        #Pimeiro item do menu
        def primeiro_item():
                from agendar import Ui_ClinicData
                self.janela = QtWidgets.QMainWindow()
                self.ClinicData = Ui_ClinicData()
                self.ClinicData.setupUi(self.janela)
                self.janela.show()
                sleep(1)
                ClinicData.hide()

        #Nova consulta
        self.item_1 = QtWidgets.QPushButton(self.centralwidget)
        self.item_1.setGeometry(QtCore.QRect(40, 180, 141, 31))
        font = QtGui.QFont()
        font.setKerning(True)
        self.item_1.setFont(font)
        self.item_1.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.item_1.setMouseTracking(False)
        self.item_1.setStyleSheet("background-color: white; border-radius: 10px;")
        self.item_1.setObjectName("item_1")
        self.item_1.clicked.connect(primeiro_item)
        
        #Segundo item do menu
        def segundo_item():
                from consultas import Ui_ClinicData
                self.janela = QtWidgets.QMainWindow()
                self.ClinicData = Ui_ClinicData()
                self.ClinicData.setupUi(self.janela)
                self.janela.show()
                sleep(1)
                ClinicData.hide()
        #ClinicData     
        self.item_2 = QtWidgets.QPushButton(self.centralwidget)
        self.item_2.setGeometry(QtCore.QRect(40, 220, 141, 31))
        font = QtGui.QFont()
        font.setKerning(True)
        self.item_2.setFont(font)
        self.item_2.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.item_2.setMouseTracking(False)
        self.item_2.setStyleSheet("background-color: white; border-radius: 10px;")
        self.item_2.setObjectName("item_2")
        self.item_2.clicked.connect(segundo_item)



        #Terceiro item do menu
        def terceiro_item():
                from cadastrar import Ui_ClinicData
                self.janela = QtWidgets.QMainWindow()
                self.ClinicData = Ui_ClinicData()
                self.ClinicData.setupUi(self.janela)
                self.janela.show()
                sleep(1)
                ClinicData.hide()
        #Novo paciente
        self.item_3 = QtWidgets.QPushButton(self.centralwidget)
        self.item_3.setGeometry(QtCore.QRect(40, 260, 141, 31))
        font = QtGui.QFont()
        font.setKerning(True)
        self.item_3.setFont(font)
        self.item_3.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.item_3.setMouseTracking(False)
        self.item_3.setStyleSheet("background-color: white; border-radius: 10px;")
        self.item_3.setObjectName("item_3")
        self.item_3.clicked.connect(terceiro_item)



        #Quarto item do menu
        def quarto_item():
                from pacientes import Ui_ClinicData
                self.janela = QtWidgets.QMainWindow()
                self.ClinicData = Ui_ClinicData()
                self.ClinicData.setupUi(self.janela)
                self.janela.show()
                sleep(1)
                ClinicData.hide()
        #Pacientes     
        self.item_4 = QtWidgets.QPushButton(self.centralwidget)
        self.item_4.setGeometry(QtCore.QRect(40, 300, 141, 31))
        font = QtGui.QFont()
        font.setKerning(True)
        self.item_4.setFont(font)
        self.item_4.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.item_4.setMouseTracking(False)
        self.item_4.setStyleSheet("background-color: white; border-radius: 10px;")
        self.item_4.setObjectName("item_4")
        self.item_4.clicked.connect(quarto_item)



        
        self.item_5 = QtWidgets.QPushButton(self.centralwidget)
        self.item_5.setGeometry(QtCore.QRect(40, 340, 141, 31))
        font = QtGui.QFont()
        font.setKerning(True)
        self.item_5.setFont(font)
        self.item_5.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.item_5.setMouseTracking(False)
        self.item_5.setStyleSheet("background-color: white; border-radius: 10px;")
        self.item_5.setObjectName("item_5")

        self.item_6 = QtWidgets.QPushButton(self.centralwidget)
        self.item_6.setGeometry(QtCore.QRect(40, 380, 141, 31))
        font = QtGui.QFont()
        font.setKerning(True)
        self.item_6.setFont(font)
        self.item_6.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.item_6.setMouseTracking(False)
        self.item_6.setStyleSheet("background-color: white; border-radius: 10px;")
        self.item_6.setObjectName("item_6")
        ClinicData.setCentralWidget(self.centralwidget)

        self.retranslateUi(ClinicData)
        QtCore.QMetaObject.connectSlotsByName(ClinicData)

    def retranslateUi(self, ClinicData):
        _traduzir = QtCore.QCoreApplication.translate
        ClinicData.setWindowTitle(_traduzir("ClinicData", "ClinicData - Janela principal"))
        self.boas_vindas.setText(_traduzir("ClinicData", "Seja bem-vindo(a)"))
        self.boas_vindas_2.setText(_traduzir("ClinicData", "Usuário"))
        self.menu_titulo.setText(_traduzir("ClinicData", "MENU"))
        self.item_1.setText(_traduzir("ClinicData", "Nova consulta"))
        self.item_2.setText(_traduzir("ClinicData", "Consultas"))
        self.item_3.setText(_traduzir("ClinicData", "Novo paciente"))
        self.item_4.setText(_traduzir("ClinicData", "Pacientes"))
        self.item_5.setText(_traduzir("ClinicData", "Novo administrador"))
        self.item_6.setText(_traduzir("ClinicData", "Administradores"))


if __name__ == "__main__":
    import sys
    pgm = QtWidgets.QApplication(sys.argv)
    ClinicData = QtWidgets.QMainWindow()
    jsecundaria = Ui_ClinicData()
    jsecundaria.setupUi(ClinicData)
    ClinicData.show()
    sys.exit(pgm.exec())
