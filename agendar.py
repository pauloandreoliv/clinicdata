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
        self.label.setGeometry(QtCore.QRect(370, 110, 151, 16))
        self.label.setStyleSheet("color: white;")
        self.label.setObjectName("label")
        self.label.setText("AGENDAR UMA CONSULTA")
        
        #Título
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(100, 150, 61, 31))
        self.label_2.setStyleSheet("color: white;")
        self.label_2.setObjectName("label_2")
        self.label_2.setText("PACIENTE:")
        
        #Título
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(100, 190, 101, 31))
        self.label_3.setStyleSheet("color: white;")
        self.label_3.setObjectName("label_3")
        self.label_3.setText("RESPONSÁVEL:")       

        #Título
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(100, 230, 101, 31))
        self.label_4.setStyleSheet("color: white;")
        self.label_4.setObjectName("label_4")
        self.label_4.setText("PROFISSIONAL:")
        
        #Título
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(100, 270, 101, 31))
        self.label_5.setStyleSheet("color: white;")
        self.label_5.setObjectName("label_5")
        self.label_5.setText("E-MAIL:")        
        
        #Título
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(100, 310, 101, 31))
        self.label_6.setStyleSheet("color: white;")
        self.label_6.setObjectName("label_6")
        self.label_6.setText("CELULAR:")

        #Título
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(100, 350, 101, 31))
        self.label_7.setStyleSheet("color: white;")
        self.label_7.setObjectName("label_7")
        self.label_7.setText("LAUDO:")
        
        #Título
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(100, 430, 101, 31))
        self.label_8.setStyleSheet("color: white;")
        self.label_8.setObjectName("label_8")
        self.label_8.setText("OBSERVAÇÕES:")
        
        #Título
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(0, 0, 0, 0))
        self.label_9.setStyleSheet("color: white;")
        self.label_9.setObjectName("label_9")
        self.label_9.setText("Usuário inexistente ou nome incorreto/incompleto.")
        
        #Título
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(610, 60, 61, 31))
        self.label_10.setStyleSheet("color: white; background: transparent;")
        self.label_10.setObjectName("label_10")
        self.label_10.setText("CÓDIGO:")
        
        #Título
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(0, 0, 0, 0))
        self.label_11.setStyleSheet("color: white; background: transparent;")
        self.label_11.setObjectName("label_11")
        self.label_11.setText("Código inexistente")
        
        #Título
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(100, 390, 101, 31))
        self.label_12.setStyleSheet("color: white;")
        self.label_12.setObjectName("label_12")
        self.label_12.setText("ENDEREÇO:")
        
        #Título
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(100, 520, 101, 31))
        self.label_13.setStyleSheet("color: white;")
        self.label_13.setObjectName("label_13")
        self.label_13.setText("VALOR:")

        #Título
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(450, 520, 101, 31))
        self.label_14.setStyleSheet("color: white;")
        self.label_14.setObjectName("label_14")
        self.label_14.setText("DATA:")

        
        #Título
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(100, 570, 101, 31))
        self.label_15.setStyleSheet("color: white;")
        self.label_15.setObjectName("label_15")
        self.label_15.setText("PAGO:")
        
        #Título
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(0, 0, 0, 0))
        self.label_16.setStyleSheet("color: white;")
        self.label_16.setObjectName("label_16")
        self.label_16.setText("Consulta agendada com sucesso.")
        
        #Título
        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        self.label_17.setGeometry(QtCore.QRect(0, 0, 0, 0))
        self.label_17.setStyleSheet("color: white;")
        self.label_17.setObjectName("label_17")
        self.label_17.setText("Preencha o nome do paciente.")

        #Título
        self.label_18 = QtWidgets.QLabel(self.centralwidget)
        self.label_18.setGeometry(QtCore.QRect(450, 570, 101, 31))
        self.label_18.setStyleSheet("color: white;")
        self.label_18.setObjectName("label_18")
        self.label_18.setText("HORA:")
        
        #Linha de edição
        self.lineEdit_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_6.setGeometry(QtCore.QRect(200, 350, 581, 31))
        self.lineEdit_6.setStyleSheet("background-color: white; border-radius: 10px; color: black;")
        self.lineEdit_6.setObjectName("lineEdit_6")
        
        #Linha de edição
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(200, 230, 581, 31))
        self.lineEdit_3.setStyleSheet("background-color: white; border-radius: 10px; color: black;")
        self.lineEdit_3.setObjectName("lineEdit_3")
        
        #Linha de edição
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(200, 310, 581, 31))
        self.lineEdit_5.setStyleSheet("background-color: white; border-radius: 10px; color: black;")
        self.lineEdit_5.setObjectName("lineEdit_5")


        #Linha de edição
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(200, 190, 581, 31))
        self.lineEdit_2.setStyleSheet("background-color: white; border-radius: 10px; color: black;")
        self.lineEdit_2.setObjectName("lineEdit_2")

        #Linha de edição
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(200, 150, 581, 31))
        self.lineEdit.setStyleSheet("background-color: white; border-radius: 10px; color: black;")
        self.lineEdit.setObjectName("lineEdit")
        
        #Linha de edição
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(200, 270, 581, 31))
        self.lineEdit_4.setStyleSheet("background-color: white; border-radius: 10px; color: black;")
        self.lineEdit_4.setObjectName("lineEdit_4")

        #Caixa de texto
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(200, 430, 581, 81))
        self.textEdit.setStyleSheet("background-color: white; border-radius: 10px; color: black;")
        self.textEdit.setObjectName("textEdit")

        #Linha de edição
        self.lineEdit_7 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_7.setGeometry(QtCore.QRect(610, 90, 111, 31))
        self.lineEdit_7.setStyleSheet("background-color: white; border-radius: 10px; color: black;")
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

        #Linha de edição
        self.lineEdit_10 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_10.setGeometry(QtCore.QRect(570,570, 211, 31))
        self.lineEdit_10.setStyleSheet("background-color: white; border-radius: 10px; color: black;")
        self.lineEdit_10.setObjectName("lineEdit_10")
        
        #Selecionar data
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(self.centralwidget)
        self.dateTimeEdit.setGeometry(QtCore.QRect(570, 520, 211, 31))
        self.dateTimeEdit.setStyleSheet("background-color:white; border-radius: 10px;")
        self.dateTimeEdit.setObjectName("dateTimeEdit")

        #Função para procurar usuário pelo seu código
        def funcao_procurar_codigo():
            self.label_11.setGeometry(QtCore.QRect(0, 0, 0, 0))
            codigo_procurado = self.lineEdit_7.text()
            
            if codigo_procurado == '':
                self.label_11.setGeometry(QtCore.QRect(660, 60, 121, 31))
            else:    
                verifica_caracter = ''
                verifica_se_todos_sao_letras = 0
                numeros = []
                for numero in list(range(0,11)):
                    numeros.append(str(numero))
                    
                for num in list(range(0,11)):
                    if num < len(codigo_procurado):
                        if codigo_procurado[num] in numeros:
                            verifica_caracter += str(codigo_procurado[num])
                        else:
                            verifica_se_todos_sao_letras += 1

                if verifica_se_todos_sao_letras == len(codigo_procurado):
                    self.label_11.setGeometry(QtCore.QRect(660, 60, 121, 31))
                else:
                    manipulador.execute(f'SELECT * FROM pacientes_db WHERE codigo = "{codigo_procurado}"')
                    todos_pacientes = list(manipulador.fetchall())
                    paciente_escolhido = []
                    for paciente in todos_pacientes:
                        if codigo_procurado in paciente[2]:
                            paciente_escolhido.append(paciente)
                        else:
                            funcao_nada()
                    if len(paciente_escolhido) == 0:
                        self.label_11.setGeometry(QtCore.QRect(660, 60, 121, 31))
                    else:
                        self.lineEdit.setText(f"{paciente_escolhido[0][1]}")
                        self.lineEdit_2.setText(f"{paciente_escolhido[0][3]}")
                        self.lineEdit_3.setText(f"{paciente_escolhido[0][9]}")
                        self.lineEdit_4.setText(f"{paciente_escolhido[0][5]}")
                        self.lineEdit_5.setText(f"{paciente_escolhido[0][6]}")
                        self.lineEdit_6.setText(f"{paciente_escolhido[0][7]}")
                        self.lineEdit_8.setText(f"{paciente_escolhido[0][8]}")
                        self.textEdit.setText(f"{paciente_escolhido[0][4]}")

        #Função para limpar inputs do formulário
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
            self.lineEdit_10.setText("")
            self.textEdit.setText("")
            self.nao.setChecked(True)
            self.lineEdit.setStyleSheet("background-color: white; border-radius: 10px; color: black;")
            self.label_17.setGeometry(QtCore.QRect(0, 0, 0, 0))
            self.label_16.setGeometry(QtCore.QRect(0, 0, 0, 0))
            self.label_9.setGeometry(QtCore.QRect(0, 0, 0, 0))

        #Função para verificar se o paciente existe
        def verifica_paciente(nome_selecionado):
            return
        
        #Função de envio
        def funcao_enviar():
            paciente = str(self.lineEdit.text()).upper()
            manipulador.execute("SELECT paciente, codigo FROM pacientes_db")
            nomes_pacientes = list(manipulador.fetchall())
            conexao.commit()
            nomes_pacientes_2 = []
            selecionado = []
            for k in nomes_pacientes:
                nomes_pacientes_2.append(k[0])
                if k[0] == paciente:
                    selecionado.append(k[1])
            if len(selecionado) == 1:
                codigo = selecionado[0]
                self.label_9.setGeometry(QtCore.QRect(0, 0, 0, 0))
                responsavel = str(self.lineEdit_2.text()).upper()
                profissional = str(self.lineEdit_3.text()).upper()
                email = str(self.lineEdit_4.text()).upper()
                celular = str(self.lineEdit_5.text()).upper()
                laudo = str(self.lineEdit_6.text()).upper()
                endereco = str(self.lineEdit_8.text()).upper()
                observacoes = str(self.textEdit.toPlainText()).upper()
                valor = str(self.lineEdit_9.text()).upper()
                data = self.dateTimeEdit.date().toPyDate()
                horario = str(self.lineEdit_10.text())
                pago = ''
                if self.sim.isChecked() == True:
                    pago = 'SIM'
                if self.nao.isChecked() == True:
                    pago = 'NÃO'
                if self.lineEdit.text() == '':
                    self.label_16.setGeometry(QtCore.QRect(0, 0, 0, 0))
                    self.label_17.setGeometry(QtCore.QRect(590, 600, 181, 20))
                    self.label_9.setGeometry(QtCore.QRect(210, 130, 351, 16))
                    self.lineEdit.setStyleSheet('border-radius: 10px; color: black; background-color: rgb(255, 199, 200);')
                else:
                    self.label_17.setGeometry(QtCore.QRect(0, 0, 0, 0))
                    self.label_9.setGeometry(QtCore.QRect(0, 0, 0, 0))
                    manipulador.execute(f"INSERT INTO consultas_db (pago, paciente, codigo, responsavel, profissional_r, data, celular, valor, email, laudo, endereco, observacoes, horario) VALUES ('{pago}', '{paciente}', '{codigo}', '{responsavel}', '{profissional}', '{data}', '{celular}', '{valor}', '{email}', '{laudo}', '{endereco}', '{observacoes}', '{horario}')")
                    conexao.commit()
                    self.lineEdit.setStyleSheet("background-color: white; border-radius: 10px; color: black;")
                    self.label_16.setGeometry(QtCore.QRect(590, 600, 181, 20))
            else:
                self.label_9.setGeometry(QtCore.QRect(210, 130, 351, 16))
                self.lineEdit.setStyleSheet('border-radius: 10px; color: black; background-color: rgb(255, 199, 200);')
        
        #Botão para ativar a função de procurar pelo código
        self.procurar_codigo = QtWidgets.QPushButton(self.centralwidget)
        self.procurar_codigo.setGeometry(QtCore.QRect(730, 90, 51, 31))
        self.procurar_codigo.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.procurar_codigo.setStyleSheet("border:none; background: white; border-radius: 10px;")
        self.procurar_codigo.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("midia/lupa.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.procurar_codigo.setIcon(icon)
        self.procurar_codigo.setObjectName("procurar_codigo")
        self.procurar_codigo.clicked.connect(funcao_procurar_codigo)
        
        #Botão para chamar a função de limpeza dos inputs   
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
        
        #RadioButton - SIM
        self.sim = QtWidgets.QRadioButton(self.centralwidget)
        self.sim.setGeometry(QtCore.QRect(200, 580, 89, 20))
        self.sim.setStyleSheet("color: white;")
        self.sim.setObjectName("sim")
        self.sim.setText("SIM")
        
        #RadioButton - NÃO
        self.nao = QtWidgets.QRadioButton(self.centralwidget)
        self.nao.setGeometry(QtCore.QRect(290, 580, 89, 20))
        self.nao.setStyleSheet("color: white;")
        self.nao.setObjectName("nao")
        self.nao.setText("NÃO")
        
        ClinicData.setCentralWidget(self.centralwidget)
        QtCore.QMetaObject.connectSlotsByName(ClinicData)

#Final
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ClinicData = QtWidgets.QMainWindow()
    ui = Ui_ClinicData()
    ui.setupUi(ClinicData)
    ClinicData.show()
    sys.exit(app.exec())
    conexao.close()
