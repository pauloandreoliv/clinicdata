from config import *

#Interface
class Ui_ClinicData(object):
    def setupUi(self, ClinicData):

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
        ClinicData.setWindowTitle("Cadastrar paciente")
        self.centralwidget = QtWidgets.QWidget(ClinicData)
        self.centralwidget.setObjectName("centralwidget")

        #Logo
        self.logo = QtWidgets.QLabel(self.centralwidget)
        self.logo.setGeometry(QtCore.QRect(320, 50, 221, 51))
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap("midia/logo_menu.png"))
        self.logo.setObjectName("logo")

        #Título "CADASTRO DE PACIENTE"
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(370, 110, 151, 16))
        self.label.setStyleSheet("color: white;")
        self.label.setObjectName("label")
        self.label.setText("CADASTRO DE PACIENTE")

        #Título "PACIENTE:"
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(100, 150, 61, 31))
        self.label_2.setStyleSheet("color: white;")
        self.label_2.setObjectName("label_2")
        self.label_2.setText("*PACIENTE:")
        
        #Título "RESPONSÁVEL:"
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(100, 190, 101, 31))
        self.label_3.setStyleSheet("color: white;")
        self.label_3.setObjectName("label_3")
        self.label_3.setText("RESPONSÁVEL:")

        #Título "PROFISSIONAL:"
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(100, 230, 101, 31))
        self.label_4.setStyleSheet("color: white;")
        self.label_4.setObjectName("label_4")
        self.label_4.setText("PROFISSIONAL:")

        #Título "E-MAIL:"
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(100, 270, 101, 31))
        self.label_5.setStyleSheet("color: white;")
        self.label_5.setObjectName("label_5")
        self.label_5.setText("*E-MAIL:")

        #Título "CELULAR:"
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(100, 310, 101, 31))
        self.label_6.setStyleSheet("color: white;")
        self.label_6.setObjectName("label_6")
        self.label_6.setText("*CELULAR:")

        #Título "LAUDO:"
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(100, 350, 101, 31))
        self.label_7.setStyleSheet("color: white;")
        self.label_7.setObjectName("label_7")
        self.label_7.setText("LAUDO:")

        #Título "OBSERVAÇÕES:"
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(100, 430, 101, 31))
        self.label_8.setStyleSheet("color: white;")
        self.label_8.setObjectName("label_8")
        self.label_8.setText("OBSERVAÇÕES:")

        #Título "CÓDIGO GERADO:"
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(610, 60, 101, 31))
        self.label_10.setStyleSheet("color: white; background: transparent;")
        self.label_10.setObjectName("label_10")
        self.label_10.setText("CÓDIGO GERADO:")

        #Título "ENDEREÇO:"
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(100, 390, 101, 31))
        self.label_12.setStyleSheet("color: white;")
        self.label_12.setObjectName("label_12")
        self.label_12.setText("ENDEREÇO:")

        #Título "CPF:"
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(100, 520, 101, 31))
        self.label_13.setStyleSheet("color: white;")
        self.label_13.setObjectName("label_13")
        self.label_13.setText("CPF:")

        #Título "NASCIMENTO:"
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(450, 520, 101, 31))
        self.label_14.setStyleSheet("color: white;")
        self.label_14.setObjectName("label_14")
        self.label_14.setText("NASCIMENTO:")

        #Título "FREQUÊNCIA:"
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(100, 570, 101, 31))
        self.label_15.setStyleSheet("color: white;")
        self.label_15.setObjectName("label_15")
        self.label_15.setText("FREQUÊNCIA:")

        #Título "Paciente cadastrado com sucesso"
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(0, 0, 0, 0))
        self.label_16.setStyleSheet("color: white;")
        self.label_16.setObjectName("label_16")
        self.label_16.setText("Paciente cadastrado com sucesso")
        
        #Título "Preencha os campos obrigatórios"
        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        self.label_17.setGeometry(QtCore.QRect(0, 0, 0, 0))
        self.label_17.setStyleSheet("color: white;")
        self.label_17.setObjectName("label_17")
        self.label_17.setText("Preencha os campos obrigatórios")

        #Linha de edição
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(200, 150, 581, 31))
        self.lineEdit.setStyleSheet("background-color: white; border-radius: 10px; color: black;")
        self.lineEdit.setObjectName("lineEdit")

        #Linha de edição        
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(200, 190, 581, 31))
        self.lineEdit_2.setStyleSheet("background-color: white; border-radius: 10px; color: black;")
        self.lineEdit_2.setObjectName("lineEdit_2")

        #Linha de edição
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(200, 230, 581, 31))
        self.lineEdit_3.setStyleSheet("background-color: white; border-radius: 10px; color: black;")
        self.lineEdit_3.setObjectName("lineEdit_3")

        #Linha de edição
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(200, 270, 581, 31))
        self.lineEdit_4.setStyleSheet("background-color: white; border-radius: 10px; color: black;")
        self.lineEdit_4.setObjectName("lineEdit_4")

        #Linha de edição
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(200, 310, 581, 31))
        self.lineEdit_5.setStyleSheet("background-color: white; border-radius: 10px; color: black;")
        self.lineEdit_5.setObjectName("lineEdit_5")

        #Linha de edição
        self.lineEdit_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_6.setGeometry(QtCore.QRect(200, 350, 581, 31))
        self.lineEdit_6.setStyleSheet("background-color: white; border-radius: 10px; color: black;")
        self.lineEdit_6.setObjectName("lineEdit_6")

        #Linha de edição
        self.lineEdit_7 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_7.setGeometry(QtCore.QRect(610, 90, 171, 31))
        self.lineEdit_7.setStyleSheet("background-color: white; border-radius: 10px; color: black;")
        self.lineEdit_7.setEnabled(False)
        self.lineEdit_7.setObjectName("lineEdit_7")

        #Linha de edição
        self.lineEdit_8 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_8.setGeometry(QtCore.QRect(200, 390, 581, 31))
        self.lineEdit_8.setStyleSheet("background-color: white; border-radius: 10px; color: black;")
        self.lineEdit_8.setObjectName("lineEdit_8")

        #Linha de edição
        self.lineEdit_9 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_9.setGeometry(QtCore.QRect(200, 520, 211, 31))
        self.lineEdit_9.setStyleSheet("background-color: white; border-radius: 10px; color: black;")
        self.lineEdit_9.setText("")
        self.lineEdit_9.setObjectName("lineEdit_9")

        #Edição de data
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(self.centralwidget)
        self.dateTimeEdit.setGeometry(QtCore.QRect(570, 520, 211, 31))
        self.dateTimeEdit.setStyleSheet("background-color:white; border-radius: 10px;")
        self.dateTimeEdit.setObjectName("dateTimeEdit")

        #Edição de texto
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(200, 430, 581, 81))
        self.textEdit.setStyleSheet("background-color: white; border-radius: 10px; color: black;")
        self.textEdit.setObjectName("textEdit")

        #Opções de frequência
        #Semanal
        self.sem = QtWidgets.QRadioButton(self.centralwidget)
        self.sem.setGeometry(QtCore.QRect(200, 580, 89, 20))
        self.sem.setStyleSheet("color: white;")
        self.sem.setObjectName("sem")
        self.sem.setText("SEMANAL")
        #Mensal
        self.men = QtWidgets.QRadioButton(self.centralwidget)
        self.men.setGeometry(QtCore.QRect(290, 580, 89, 20))
        self.men.setStyleSheet("color: white;")
        self.men.setObjectName("men")
        self.men.setText("MENSAL")
        #Outra
        self.outra = QtWidgets.QRadioButton(self.centralwidget)
        self.outra.setGeometry(QtCore.QRect(380, 580, 89, 20))
        self.outra.setStyleSheet("color: white;")
        self.outra.setObjectName("outra")
        self.outra.setText("OUTRA")

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
        
        #Função para limpar o formulário
        def funcao_limpar():
            self.lineEdit.setText("")
            self.lineEdit_2.setText("")
            self.lineEdit_3.setText("")
            self.lineEdit_4.setText("")
            self.lineEdit_5.setText("")
            self.lineEdit_6.setText("")
            self.lineEdit_7.setText("")
            self.lineEdit_8.setText("")
            self.lineEdit_9.setText("")
            self.textEdit.setText("")
            self.outra.setChecked(True)
            self.lineEdit.setStyleSheet("background-color: white; border-radius: 10px; color: black;")
            self.label_17.setGeometry(QtCore.QRect(0, 0, 0, 0))
            self.label_16.setGeometry(QtCore.QRect(0, 0, 0, 0))

        #Botão para ativar a função limpar
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

        #Função para gerar código de novo usuário
        def funcao_codigo():
            manipulador.execute('SELECT codigo FROM pacientes_db')
            todos_codigos = list(manipulador.fetchall())
            codigos_sem_tupla = []
            for codigo in todos_codigos:
                codigos_sem_tupla.append(codigo[0])
            import random
            caracteres = list(range(0,10))
            codigo_final = ''
            while len(codigo_final) < 5:
                caracter = random.choice(caracteres)
                codigo_final += str(caracter)
            if codigo_final in codigos_sem_tupla:
                funcao_codigo()
            else:
                self.lineEdit_7.setText(f"{codigo_final}")

        #Função para cadastrar o novo usuário
        def funcao_enviar():
            paciente = str(self.lineEdit.text()).upper()
            responsavel = str(self.lineEdit_2.text()).upper()
            profissional = str(self.lineEdit_3.text()).upper()
            email = str(self.lineEdit_4.text()).upper()
            celular = str(self.lineEdit_5.text()).upper()
            laudo = str(self.lineEdit_6.text()).upper()
            endereco = str(self.lineEdit_8.text()).upper()
            observacoes = str(self.textEdit.toPlainText()).upper()
            cpf = str(self.lineEdit_9.text()).upper()
            nascimento = self.dateTimeEdit.date().toPyDate()
            frequencia = ''
            if self.sem.isChecked() == True:
                frequencia = 'SEM'
            if self.men.isChecked() == True:
                frequencia = 'MEN'
            if self.outra.isChecked() == True:
                frequencia = 'OUTRA'
            
            if self.lineEdit.text() == '':
                self.label_16.setGeometry(QtCore.QRect(0, 0, 0, 0))
                self.label_17.setGeometry(QtCore.QRect(588, 586, 181, 20))
                self.lineEdit.setStyleSheet('border-radius: 10px; color: black; background-color: rgb(255, 199, 200);')
            if self.lineEdit_4.text() == '':
                self.label_16.setGeometry(QtCore.QRect(0, 0, 0, 0))
                self.label_17.setGeometry(QtCore.QRect(588, 586, 181, 20))
                self.lineEdit_4.setStyleSheet('border-radius: 10px; color: black; background-color: rgb(255, 199, 200);')
            if self.lineEdit_5.text() == '':
                self.label_16.setGeometry(QtCore.QRect(0, 0, 0, 0))
                self.label_17.setGeometry(QtCore.QRect(588, 586, 181, 20))
                self.lineEdit_5.setStyleSheet('border-radius: 10px; color: black; background-color: rgb(255, 199, 200);')
            else:
                funcao_codigo()
                codigo = self.lineEdit_7.text()
                self.label_17.setGeometry(QtCore.QRect(0, 0, 0, 0))
                manipulador.execute(f"INSERT INTO pacientes_db (paciente, codigo, responsavel, profissional, nascimento, celular, email, laudo, endereco, observacoes, cpf, nascimento, frequencia) VALUES ('{paciente}', '{codigo}', '{responsavel}', '{profissional}', '{nascimento}', '{celular}', '{email}', '{laudo}', '{endereco}', '{observacoes}', '{cpf}', '{nascimento}', '{frequencia}')")
                conexao.commit()
                self.lineEdit.setStyleSheet("background-color: white; border-radius: 10px; color: black;")
                self.lineEdit_4.setStyleSheet("background-color: white; border-radius: 10px; color: black;")
                self.lineEdit_5.setStyleSheet("background-color: white; border-radius: 10px; color: black;")
                self.label_16.setGeometry(QtCore.QRect(590, 586, 181, 20))
        
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
