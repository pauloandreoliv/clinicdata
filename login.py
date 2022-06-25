from config import *

#Interface
class Ui_ClinicData(object):
    def setupUi(self, ClinicData):
        
        #Define tamanho e propriedades
        ClinicData.setObjectName("ClinicData")
        ClinicData.resize(640, 500)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ClinicData.sizePolicy().hasHeightForWidth())
        ClinicData.setSizePolicy(sizePolicy)
        ClinicData.setMaximumSize(QtCore.QSize(640, 500))
        ClinicData.setStyleSheet("background-color:rgb(119, 162, 255);")
        self.centralwidget = QtWidgets.QWidget(ClinicData)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMinimumSize(QtCore.QSize(640, 437))
        self.centralwidget.setMaximumSize(QtCore.QSize(640, 437))
        self.centralwidget.setObjectName("centralwidget")
        
        #Input do usuário
        self.caixa_usuario = QtWidgets.QLineEdit(self.centralwidget)
        self.caixa_usuario.setGeometry(QtCore.QRect(230, 210, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        self.caixa_usuario.setFont(font)
        self.caixa_usuario.setStyleSheet("background: white; border: none; color: rgb(80, 106, 138); border-radius: 2px; padding: 5px;")
        self.caixa_usuario.setText("")
        self.caixa_usuario.setEchoMode(QtWidgets.QLineEdit.EchoMode.Normal)
        self.caixa_usuario.setObjectName("caixa_usuario")
        
        #Input da senha
        self.caixa_senha = QtWidgets.QLineEdit(self.centralwidget)
        self.caixa_senha.setGeometry(QtCore.QRect(230, 300, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        self.caixa_senha.setFont(font)
        self.caixa_senha.setStyleSheet("background: white; border: none; color: rgb(80, 106, 138); border-radius: 2px; padding: 5px;")
        self.caixa_senha.setText("")
        self.caixa_senha.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.caixa_senha.setObjectName("caixa_senha")

        #Titulo 1
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 0, 0))
        self.label.setStyleSheet("")
        self.label.setObjectName("label")
        
        #Define a função de login
        def funcao_true(user,password):
            #Seleciona no banco de dados
            manipulador.execute('SELECT usuario, senha FROM administradores ORDER BY id')
            lista = list(manipulador.fetchall())

            cont = 0
            nomes = []
            while cont < len(lista):
                cont_ = 0
                while cont_ < len(lista[cont]) - 1:
                    nomes.append(lista[cont][cont_])
                    cont_+=1
                cont+=1
                
            cont2 = 0
            senhas = []
            while cont2 < len(lista):
                cont2_ = 0
                while cont2_ < len(lista[cont2]) -1 :
                    senhas.append(lista[cont2][1])
                    cont2_+=1
                cont2+=1

            nome__ = False
            senha__ = False
            entrou = True
            if user in nomes:
                mostre = nomes.index(user)
                nome__ = True
                
            if password in senhas:
                mostrar = senhas.index(password)
                senha__ = True
            if (nome__ != True or senha__ != True) or mostrar != mostre:
                entrou = False
                self.label.setGeometry(QtCore.QRect(240, 140, 151, 16))
                
            if (nome__ == True and senha__ == True) and mostrar == mostre:
                #Esconde o erro de login, caso esteja visível
                self.label.setGeometry(QtCore.QRect(0, 0, 0, 0))
                from principal import Ui_Menu
                from time import sleep
                #Chama a janela do menu, código do final do arquivo principal.py
                self.ClinicData = QtWidgets.QMainWindow()
                self.clinicdata = Ui_Menu()
                self.clinicdata.setupUi(self.ClinicData)
                self.ClinicData.show()
                sleep(1)
                ClinicData.hide()
                
        #Função que chama a função de logar, ou seja, a funcao_true    
        def funcao_login():
            #Define os parâmetros para a função funcao_true
            user = self.caixa_usuario.text()
            password = self.caixa_senha.text()
            funcao_true(user,password)
            
        #Botão de login
        self.enviar = QtWidgets.QPushButton(self.centralwidget)
        self.enviar.setGeometry(QtCore.QRect(280, 380, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        self.enviar.setFont(font)
        self.enviar.setStyleSheet("border:none; background: white; border-radius: 10px; color:rgb(80, 109, 171);")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("midia/entrar.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.enviar.setIcon(icon)
        self.enviar.setIconSize(QtCore.QSize(16, 16))
        self.enviar.setObjectName("enviar")
        self.enviar.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.enviar.clicked.connect(funcao_login)

        #Logo
        self.logo_login = QtWidgets.QLabel(self.centralwidget)
        self.logo_login.setGeometry(QtCore.QRect(170, 50, 311, 91))
        self.logo_login.setText("")
        self.logo_login.setPixmap(QtGui.QPixmap("midia/logo_.png"))
        self.logo_login.setObjectName("logo_login")

        #Texto "Usuário"
        self.texto_usuario = QtWidgets.QLabel(self.centralwidget)
        self.texto_usuario.setGeometry(QtCore.QRect(230, 179, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.texto_usuario.setFont(font)
        self.texto_usuario.setStyleSheet("color:white;")
        self.texto_usuario.setObjectName("texto_usuario")

        #Texto "Senha"
        self.texto_senha = QtWidgets.QLabel(self.centralwidget)
        self.texto_senha.setGeometry(QtCore.QRect(230, 270, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.texto_senha.setFont(font)
        self.texto_senha.setStyleSheet("color:white;")
        self.texto_senha.setObjectName("texto_senha")
        
        ClinicData.setCentralWidget(self.centralwidget)
        self.retranslateUi(ClinicData)
        QtCore.QMetaObject.connectSlotsByName(ClinicData)

    #Insere os textos das labels e o título da janela
    def retranslateUi(self, ClinicData):
        _translate = QtCore.QCoreApplication.translate
        ClinicData.setWindowTitle(_translate("ClinicData", "ClinicData - Login"))
        self.texto_usuario.setText(_translate("ClinicData", "USUÁRIO:"))
        self.texto_senha.setText(_translate("ClinicData", "SENHA:"))
        self.label.setText(_translate("ClinicData", "Usuário ou senha incorretos."))
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ClinicData = QtWidgets.QMainWindow()
    ui = Ui_ClinicData()
    ui.setupUi(ClinicData)
    ClinicData.show()
    sys.exit(app.exec())
    conexão.close()
