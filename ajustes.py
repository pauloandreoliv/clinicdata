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
        ClinicData.setWindowTitle("Ajustes")
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
        self.label.setGeometry(QtCore.QRect(380, 110, 161, 16))
        self.label.setStyleSheet("color: white;")
        self.label.setObjectName("label")
        self.label.setText("AJUSTAR INFORMAÇÕES")
        
        #Título
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(100, 200, 61, 31))
        self.label_2.setStyleSheet("color: white;")
        self.label_2.setObjectName("label_2")
        self.label_2.setText("NOME:")
        
        #Título
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(100, 240, 101, 31))
        self.label_3.setStyleSheet("color: white;")
        self.label_3.setObjectName("label_3")
        self.label_3.setText("ENDEREÇO:")       

        #Título
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(100, 280, 101, 31))
        self.label_4.setStyleSheet("color: white;")
        self.label_4.setObjectName("label_4")
        self.label_4.setText("DDD:")

        #Título
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(100, 320, 101, 31))
        self.label_5.setStyleSheet("color: white;")
        self.label_5.setObjectName("label_5")
        self.label_5.setText("WHATSAPP:")

        #Título
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(100, 360, 105, 31))
        self.label_6.setStyleSheet("color: white;")
        self.label_6.setObjectName("label_6")
        self.label_6.setText("E-MAIL (CONTATO):")

        #Título
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(100, 400, 101, 31))
        self.label_7.setStyleSheet("color: white;")
        self.label_7.setObjectName("label_7")
        self.label_7.setText("E-MAIL (ENVIOS):")

        #Título
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(100, 440, 101, 31))
        self.label_8.setStyleSheet("color: white;")
        self.label_8.setObjectName("label_8")
        self.label_8.setText("SENHA (ENVIOS):") 
        
        #Título
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(0, 0, 0, 0))
        self.label_16.setStyleSheet("color: white;")
        self.label_16.setObjectName("label_16")
        self.label_16.setText("Editado com sucesso.")
        
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

        #Linha de edição
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(200, 200, 581, 31))
        self.lineEdit.setStyleSheet("background-color: white; border-radius: 10px; color: black;")
        self.lineEdit.setObjectName("lineEdit")

        #Linha de edição
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(200, 240, 581, 31))
        self.lineEdit_2.setStyleSheet("background-color: white; border-radius: 10px; color: black;")
        self.lineEdit_2.setObjectName("lineEdit_2")
        
        #Linha de edição
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(200, 280, 581, 31))
        self.lineEdit_3.setStyleSheet("background-color: white; border-radius: 10px; color: black;")
        self.lineEdit_3.setObjectName("lineEdit_3")

        #Linha de edição
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(200, 320, 581, 31))
        self.lineEdit_4.setStyleSheet("background-color: white; border-radius: 10px; color: black;")
        self.lineEdit_4.setObjectName("lineEdit_4")

        #Linha de edição
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(210, 360, 571, 31))
        self.lineEdit_5.setStyleSheet("background-color: white; border-radius: 10px; color: black;")
        self.lineEdit_5.setObjectName("lineEdit_5")

        #Linha de edição
        self.lineEdit_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_6.setGeometry(QtCore.QRect(200, 400, 581, 31))
        self.lineEdit_6.setStyleSheet("background-color: white; border-radius: 10px; color: black;")
        self.lineEdit_6.setObjectName("lineEdit_6")

        #Linha de edição
        self.lineEdit_7 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_7.setGeometry(QtCore.QRect(200, 440, 581, 31))
        self.lineEdit_7.setStyleSheet("background-color: white; border-radius: 10px; color: black;")
        self.lineEdit_7.setObjectName("lineEdit_7")

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

        #Função para inserir dados atuais nos inputs
        def funcao_inserir_dados():
            manipulador.execute("SELECT * FROM clinica_db")
            lista = list(manipulador.fetchone())
            dados = []
            for k in lista:
                dados.append(k)
            self.lineEdit.setText(f"{dados[0]}")
            self.lineEdit_2.setText(f"{dados[1]}")
            self.lineEdit_3.setText(f"{dados[2]}")
            self.lineEdit_4.setText(f"{dados[3]}")
            self.lineEdit_5.setText(f"{dados[4]}")
            self.lineEdit_6.setText(f"{dados[5]}")
            self.lineEdit_7.setText(f"{dados[6]}")
        funcao_inserir_dados()
            
        #Função para limpar inputs do formulário
        def funcao_limpar():
            self.lineEdit.setText("")
            self.lineEdit_2.setText("")
            self.lineEdit_3.setText("")
            self.lineEdit_4.setText("")
            self.lineEdit_5.setText("")
            self.lineEdit_6.setText("")
            self.lineEdit_7.setText("")
            self.lineEdit.setStyleSheet("background-color: white; border-radius: 10px; color: black;")
            self.lineEdit_2.setStyleSheet("background-color: white; border-radius: 10px; color: black;")
            self.lineEdit_3.setStyleSheet("background-color: white; border-radius: 10px; color: black;")
            self.lineEdit_4.setStyleSheet("background-color: white; border-radius: 10px; color: black;")
            self.lineEdit_5.setStyleSheet("background-color: white; border-radius: 10px; color: black;")
            self.lineEdit_6.setStyleSheet("background-color: white; border-radius: 10px; color: black;")
            self.lineEdit_7.setStyleSheet("background-color: white; border-radius: 10px; color: black;")
            self.label_17.setGeometry(QtCore.QRect(0, 0, 0, 0))
            self.label_16.setGeometry(QtCore.QRect(0, 0, 0, 0))
            self.label_18.setGeometry(QtCore.QRect(0, 0, 0, 0))

        #Função de envio
        def funcao_enviar():
            try:
                if self.lineEdit.text() == '':
                    self.label_16.setGeometry(QtCore.QRect(0, 0, 0, 0))
                    self.label_17.setGeometry(QtCore.QRect(615, 600, 181, 20))
                    self.lineEdit.setStyleSheet('border-radius: 10px; color: black; background-color: rgb(255, 199, 200);')
                    self.lineEdit_2.setStyleSheet('border-radius: 10px; color: black; background-color: white;')
                elif self.lineEdit_2.text() == '':
                    self.label_16.setGeometry(QtCore.QRect(0, 0, 0, 0))
                    self.label_17.setGeometry(QtCore.QRect(615, 600, 181, 20))
                    self.lineEdit_2.setStyleSheet('border-radius: 10px; color: black; background-color: rgb(255, 199, 200);')
                elif self.lineEdit_3.text() == '':
                    self.label_16.setGeometry(QtCore.QRect(0, 0, 0, 0))
                    self.label_17.setGeometry(QtCore.QRect(615, 600, 181, 20))
                    self.lineEdit_3.setStyleSheet('border-radius: 10px; color: black; background-color: rgb(255, 199, 200);')
                elif self.lineEdit_4.text() == '':
                    self.label_16.setGeometry(QtCore.QRect(0, 0, 0, 0))
                    self.label_17.setGeometry(QtCore.QRect(615, 600, 181, 20))
                    self.lineEdit_4.setStyleSheet('border-radius: 10px; color: black; background-color: rgb(255, 199, 200);')
                elif self.lineEdit_5.text() == '':
                    self.label_16.setGeometry(QtCore.QRect(0, 0, 0, 0))
                    self.label_17.setGeometry(QtCore.QRect(615, 600, 181, 20))
                    self.lineEdit_5.setStyleSheet('border-radius: 10px; color: black; background-color: rgb(255, 199, 200);')
                elif self.lineEdit_6.text() == '':
                    self.label_16.setGeometry(QtCore.QRect(0, 0, 0, 0))
                    self.label_17.setGeometry(QtCore.QRect(615, 600, 181, 20))
                    self.lineEdit_6.setStyleSheet('border-radius: 10px; color: black; background-color: rgb(255, 199, 200);')
                elif self.lineEdit_7.text() == '':
                    self.label_16.setGeometry(QtCore.QRect(0, 0, 0, 0))
                    self.label_17.setGeometry(QtCore.QRect(615, 600, 181, 20))
                    self.lineEdit_7.setStyleSheet('border-radius: 10px; color: black; background-color: rgb(255, 199, 200);')
                else:
                    nome = str(self.lineEdit.text())
                    endereco = str(self.lineEdit_2.text())
                    ddd = str(self.lineEdit_3.text())
                    whatsapp = str(self.lineEdit_4.text())
                    contato = str(self.lineEdit_5.text())
                    email = str(self.lineEdit_6.text())
                    senha = str(self.lineEdit_7.text())
                    self.label_17.setGeometry(QtCore.QRect(0, 0, 0, 0))
                    self.label_18.setGeometry(QtCore.QRect(0, 0, 0, 0))
                    manipulador.execute("DELETE FROM clinica_db")
                    conexao.commit()
                    manipulador.execute(f"INSERT INTO clinica_db (nome, endereco, ddd, whatsapp, contato, email, senha) VALUES ('{nome}', '{endereco}', '{ddd}', '{whatsapp}', '{contato}', '{email}', '{senha}')")
                    conexao.commit()
                    self.lineEdit.setStyleSheet("background-color: white; border-radius: 10px; color: black;")
                    self.lineEdit_2.setStyleSheet("background-color: white; border-radius: 10px; color: black;")
                    self.lineEdit_3.setStyleSheet("background-color: white; border-radius: 10px; color: black;")
                    self.label_16.setGeometry(QtCore.QRect(610, 600, 181, 20))
            except:
                self.label_17.setGeometry(QtCore.QRect(0, 0, 0, 0))
                self.label_16.setGeometry(QtCore.QRect(0, 0, 0, 0))
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
