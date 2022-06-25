from config import *

#Interface
class Ui_ClinicData(object):
    def setupUi(self, ClinicData):

        #Função nada - Evita erros
        def funcao_nada():
            return
        
        #Define tamanho e propriedades
        ClinicData.setObjectName("ClinicData")
        ClinicData.resize(891, 678)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ClinicData.sizePolicy().hasHeightForWidth())
        ClinicData.setSizePolicy(sizePolicy)
        ClinicData.setMinimumSize(QtCore.QSize(891, 0))
        ClinicData.setMaximumSize(QtCore.QSize(891, 678))
        ClinicData.setStyleSheet("background-color:rgb(119, 162, 255);")
        ClinicData.setWindowTitle("Nova consulta")
        self.centralwidget = QtWidgets.QWidget(ClinicData)
        self.centralwidget.setObjectName("centralwidget")

        #Logo
        self.logo = QtWidgets.QLabel(self.centralwidget)
        self.logo.setGeometry(QtCore.QRect(320, 50, 221, 51))
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap("midia/logo_menu.png"))
        self.logo.setObjectName("logo")

        #Título
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(368, 110, 161, 16))
        self.label.setStyleSheet("color: white;")
        self.label.setObjectName("label")
        self.label.setText("INSERIR UM ADMINISTRADOR")
        
        #Título
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(100, 290, 61, 31))
        self.label_2.setStyleSheet("color: white;")
        self.label_2.setObjectName("label_2")
        self.label_2.setText("NOME:")
        
        #Título
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(100, 330, 101, 31))
        self.label_3.setStyleSheet("color: white;")
        self.label_3.setObjectName("label_3")
        self.label_3.setText("USUÁRIO:")       

        #Título
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(100, 370, 101, 31))
        self.label_4.setStyleSheet("color: white;")
        self.label_4.setObjectName("label_4")
        self.label_4.setText("SENHA:")    
        
        #Título
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(0, 0, 0, 0))
        self.label_16.setStyleSheet("color: white;")
        self.label_16.setObjectName("label_16")
        self.label_16.setText("Cadastrado com sucesso.")
        
        #Título
        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        self.label_17.setGeometry(QtCore.QRect(0, 0, 0, 0))
        self.label_17.setStyleSheet("color: white;")
        self.label_17.setObjectName("label_17")
        self.label_17.setText("Preencha os campos.")

        #Título
        self.label_18 = QtWidgets.QLabel(self.centralwidget)
        self.label_18.setGeometry(QtCore.QRect(0, 0, 0, 0))
        self.label_18.setStyleSheet("color: white;")
        self.label_18.setObjectName("label_18")
        self.label_18.setText("Erro no envio.")

        #Título
        self.label_19 = QtWidgets.QLabel(self.centralwidget)
        self.label_19.setGeometry(QtCore.QRect(0, 0, 0, 0))
        self.label_19.setStyleSheet("color: white;")
        self.label_19.setObjectName("label_19")
        self.label_19.setText("Usuário já existente.")
        
        #Linha de edição
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(200, 330, 581, 31))
        self.lineEdit_2.setStyleSheet("background-color: white; border-radius: 10px; color: black;")
        self.lineEdit_2.setObjectName("lineEdit_2")

        #Linha de edição
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(200, 290, 581, 31))
        self.lineEdit.setStyleSheet("background-color: white; border-radius: 10px; color: black;")
        self.lineEdit.setObjectName("lineEdit")

        #Linha de edição
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(200, 370, 581, 31))
        self.lineEdit_3.setStyleSheet("background-color: white; border-radius: 10px; color: black;")
        self.lineEdit_3.setObjectName("lineEdit_3")

        #Função para abrir o menu
        def funcao_abrir_menu():
            from principal import Ui_Menu
            self.clinicdata = QtWidgets.QMainWindow()
            self.ClinicData = Ui_Menu()
            self.ClinicData.setupUi(self.clinicdata)
            sleep(1)
            self.clinicdata.show()
        
        #Botão para ativar a função de abrir o menu
        self.abrir_menu = QtWidgets.QPushButton(self.centralwidget)
        self.abrir_menu.setGeometry(QtCore.QRect(100, 90, 51, 31))
        self.abrir_menu.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.abrir_menu.setStyleSheet("border:none; background: white; border-radius: 10px; color:rgb(119, 162, 255);")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("midia/menu.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.abrir_menu.setIcon(icon1)
        self.abrir_menu.setIconSize(QtCore.QSize(30, 30))
        self.abrir_menu.setObjectName("abrir_menu")
        self.abrir_menu.clicked.connect(funcao_abrir_menu)

        #Função para limpar inputs do formulário
        def funcao_limpar():
            self.lineEdit.setText("")
            self.lineEdit_2.setText("")
            self.lineEdit_3.setText("")
            self.lineEdit.setStyleSheet("background-color: white; border-radius: 10px; color: black;")
            self.lineEdit_2.setStyleSheet("background-color: white; border-radius: 10px; color: black;")
            self.lineEdit_3.setStyleSheet("background-color: white; border-radius: 10px; color: black;")
            self.label_17.setGeometry(QtCore.QRect(0, 0, 0, 0))
            self.label_16.setGeometry(QtCore.QRect(0, 0, 0, 0))
            self.label_19.setGeometry(QtCore.QRect(0, 0, 0, 0))
            self.label_18.setGeometry(QtCore.QRect(0, 0, 0, 0))

        #Função de envio
        def funcao_enviar():
            try:
                manipulador.execute(f"SELECT usuario FROM administradores")
                lista = list(manipulador.fetchall())
                lista_usuarios = []
                for k in lista:
                    for n in k:
                        lista_usuarios.append(n)
                usuario_ = str(self.lineEdit.text()).lower()
                if usuario_ in lista_usuarios:
                    self.label_16.setGeometry(QtCore.QRect(0, 0, 0, 0))
                    self.label_17.setGeometry(QtCore.QRect(0, 0, 0, 0))
                    self.label_18.setGeometry(QtCore.QRect(0, 0, 0, 0))
                    self.label_19.setGeometry(QtCore.QRect(620, 600, 181, 20))
                    self.lineEdit_2.setStyleSheet('border-radius: 10px; color: black; background-color: rgb(255, 199, 200);')
                else:
                    if self.lineEdit.text() == '':
                        self.label_16.setGeometry(QtCore.QRect(0, 0, 0, 0))
                        self.label_19.setGeometry(QtCore.QRect(0, 0, 0, 0))
                        self.label_17.setGeometry(QtCore.QRect(615, 600, 181, 20))
                        self.lineEdit.setStyleSheet('border-radius: 10px; color: black; background-color: rgb(255, 199, 200);')
                        self.lineEdit_2.setStyleSheet('border-radius: 10px; color: black; background-color: white;')
                    elif self.lineEdit_2.text() == '':
                        self.label_19.setGeometry(QtCore.QRect(0, 0, 0, 0))
                        self.label_16.setGeometry(QtCore.QRect(0, 0, 0, 0))
                        self.label_17.setGeometry(QtCore.QRect(615, 600, 181, 20))
                        self.lineEdit_2.setStyleSheet('border-radius: 10px; color: black; background-color: rgb(255, 199, 200);')
                    elif self.lineEdit_3.text() == '':
                        self.label_19.setGeometry(QtCore.QRect(0, 0, 0, 0))
                        self.label_16.setGeometry(QtCore.QRect(0, 0, 0, 0))
                        self.label_17.setGeometry(QtCore.QRect(615, 600, 181, 20))
                        self.lineEdit_3.setStyleSheet('border-radius: 10px; color: black; background-color: rgb(255, 199, 200);')
                    else:
                        nome = str(self.lineEdit.text()).upper()
                        usuario = str(self.lineEdit_2.text()).lower()
                        senha = str(self.lineEdit_3.text())
                        self.label_17.setGeometry(QtCore.QRect(0, 0, 0, 0))
                        manipulador.execute(f"INSERT INTO administradores (nome, usuario, senha) VALUES ('{nome}', '{usuario}', '{senha}')")
                        conexao.commit()
                        self.lineEdit.setStyleSheet("background-color: white; border-radius: 10px; color: black;")
                        self.lineEdit_2.setStyleSheet("background-color: white; border-radius: 10px; color: black;")
                        self.lineEdit_3.setStyleSheet("background-color: white; border-radius: 10px; color: black;")
                        self.label_19.setGeometry(QtCore.QRect(0, 0, 0, 0))
                        self.label_16.setGeometry(QtCore.QRect(610, 600, 181, 20))
            except:
                self.lineEdit.setStyleSheet('border-radius: 10px; color: black; background-color: rgb(255, 199, 200);')
                self.label_19.setGeometry(QtCore.QRect(0, 0, 0, 0))
                self.label_18.setGeometry(QtCore.QRect(615, 600, 181, 20))
        
        #Botão para ativar a função de limpeza dos inputs   
        self.limpar = QtWidgets.QPushButton(self.centralwidget)
        self.limpar.setGeometry(QtCore.QRect(200, 620, 211, 41))
        self.limpar.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.limpar.setStyleSheet("border:none; background: white; border-radius: 10px;")
        self.limpar.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("midia/borracha.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.limpar.setIcon(icon1)
        self.limpar.setIconSize(QtCore.QSize(20, 20))
        self.limpar.setObjectName("limpar")
        self.limpar.clicked.connect(funcao_limpar)
        
        #Botão para ativar a função de envio   
        self.enviar = QtWidgets.QPushButton(self.centralwidget)
        self.enviar.setGeometry(QtCore.QRect(570, 620, 211, 41))
        self.enviar.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.enviar.setStyleSheet("border:none; background: white; border-radius: 10px;")
        self.enviar.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("midia/enviar.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.enviar.setIcon(icon2)
        self.enviar.setIconSize(QtCore.QSize(20, 20))
        self.enviar.setObjectName("enviar")
        self.enviar.clicked.connect(funcao_enviar)
        
        ClinicData.setCentralWidget(self.centralwidget)
        QtCore.QMetaObject.connectSlotsByName(ClinicData)

#Final - Padrão PyQt
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ClinicData = QtWidgets.QMainWindow()
    ui = Ui_ClinicData()
    ui.setupUi(ClinicData)
    ClinicData.show()
    sys.exit(app.exec())
    conexao.close()
