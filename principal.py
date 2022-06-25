from config import *

#Interface
class Ui_Menu(object):
    def setupUi(self, Menu):
        
        #Define tamanho e propriedades
        Menu.setObjectName("Menu")
        Menu.resize(220, 494)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Menu.sizePolicy().hasHeightForWidth())
        Menu.setSizePolicy(sizePolicy)
        Menu.setMinimumSize(QtCore.QSize(220, 0))
        Menu.setMaximumSize(QtCore.QSize(220, 500))
        Menu.setStyleSheet("background-color:rgb(119, 162, 255);")
        Menu.setWindowTitle("Menu - Janela principal")
        self.centralwidget = QtWidgets.QWidget(Menu)
        self.centralwidget.setMaximumSize(QtCore.QSize(220, 500))
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")

        #Título - Boas vindas
        self.boas_vindas = QtWidgets.QLabel(self.centralwidget)
        self.boas_vindas.setGeometry(QtCore.QRect(50, 50, 101, 16))
        self.boas_vindas.setStyleSheet("color: white;")
        self.boas_vindas.setObjectName("boas_vindas")
        self.boas_vindas.setText("Seja bem-vindo(a)")

        #Título - Administrador
        self.boas_vindas_2 = QtWidgets.QLabel(self.centralwidget)
        self.boas_vindas_2.setGeometry(QtCore.QRect(35, 70, 150, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.boas_vindas_2.setFont(font)
        self.boas_vindas_2.setStyleSheet("color: white;")
        self.boas_vindas_2.setObjectName("boas_vindas_2")
        self.boas_vindas_2.setText("Administrador")

        #Título - Menu
        self.menu_titulo = QtWidgets.QLabel(self.centralwidget)
        self.menu_titulo.setGeometry(QtCore.QRect(80, 150, 49, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.menu_titulo.setFont(font)
        self.menu_titulo.setStyleSheet("color: white;")
        self.menu_titulo.setObjectName("menu_titulo")
        self.menu_titulo.setText("MENU")

        #Pimeiro item do menu
        def primeiro_item():
                from agendar import Ui_ClinicData
                self.clinicdata = QtWidgets.QMainWindow()
                self.ClinicData = Ui_ClinicData()
                self.ClinicData.setupUi(self.clinicdata)
                self.clinicdata.show()
                sleep(1)
                Menu.hide()
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
        self.item_1.setText("Nova consulta")
        self.item_1.clicked.connect(primeiro_item)

        
        #Segundo item do menu
        def segundo_item():
                from consultas import Ui_ClinicData
                self.clinicdata = QtWidgets.QMainWindow()
                self.ClinicData = Ui_ClinicData()
                self.ClinicData.setupUi(self.clinicdata)
                self.clinicdata.show()
                sleep(1)
                Menu.hide()
        #Consultas     
        self.item_2 = QtWidgets.QPushButton(self.centralwidget)
        self.item_2.setGeometry(QtCore.QRect(40, 220, 141, 31))
        font = QtGui.QFont()
        font.setKerning(True)
        self.item_2.setFont(font)
        self.item_2.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.item_2.setMouseTracking(False)
        self.item_2.setStyleSheet("background-color: white; border-radius: 10px;")
        self.item_2.setObjectName("item_2")
        self.item_2.setText("Consultas")
        self.item_2.clicked.connect(segundo_item)


        #Terceiro item do menu
        def terceiro_item():
                from cadastrar import Ui_ClinicData
                self.clinicdata = QtWidgets.QMainWindow()
                self.ClinicData = Ui_ClinicData()
                self.ClinicData.setupUi(self.clinicdata)
                self.clinicdata.show()
                sleep(1)
                Menu.hide()
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
        self.item_3.setText("Novo paciente")
        self.item_3.clicked.connect(terceiro_item)



        #Quarto item do menu
        def quarto_item():
                from pacientes import Ui_ClinicData
                self.clinicdata = QtWidgets.QMainWindow()
                self.ClinicData = Ui_ClinicData()
                self.ClinicData.setupUi(self.clinicdata)
                self.clinicdata.show()
                sleep(1)
                Menu.hide()
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
        self.item_4.setText("Pacientes")
        self.item_4.clicked.connect(quarto_item)


        #Novo administrador
        self.item_5 = QtWidgets.QPushButton(self.centralwidget)
        self.item_5.setGeometry(QtCore.QRect(40, 340, 141, 31))
        font = QtGui.QFont()
        font.setKerning(True)
        self.item_5.setFont(font)
        self.item_5.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.item_5.setMouseTracking(False)
        self.item_5.setStyleSheet("background-color: white; border-radius: 10px;")
        self.item_5.setObjectName("item_5")
        self.item_5.setText("Novo administrador")

        #Administradores
        self.item_6 = QtWidgets.QPushButton(self.centralwidget)
        self.item_6.setGeometry(QtCore.QRect(40, 380, 141, 31))
        font = QtGui.QFont()
        font.setKerning(True)
        self.item_6.setFont(font)
        self.item_6.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.item_6.setMouseTracking(False)
        self.item_6.setStyleSheet("background-color: white; border-radius: 10px;")
        self.item_6.setObjectName("item_6")
        self.item_6.setText("Administradores")
        
        Menu.setCentralWidget(self.centralwidget)
        QtCore.QMetaObject.connectSlotsByName(Menu)

#Final - Padrão PyQt
if __name__ == "__main__":
    import sys
    pgm = QtWidgets.QApplication(sys.argv)
    Menu = QtWidgets.QMainWindow()
    jsecundaria = Ui_Menu()
    jsecundaria.setupUi(Menu)
    Menu.show()
    sys.exit(pgm.exec())
