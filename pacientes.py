from config import *

#Interface
class Ui_ClinicData(object):
    def setupUi(self, ClinicData):
        
        #Define o tamanho
        ClinicData.setObjectName("ClinicData")
        ClinicData.setWindowTitle("Visualizar pacientes")
        ClinicData.resize(891, 678)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ClinicData.sizePolicy().hasHeightForWidth())
        ClinicData.setSizePolicy(sizePolicy)
        ClinicData.setMinimumSize(QtCore.QSize(891, 0))
        ClinicData.setMaximumSize(QtCore.QSize(891, 678))
        ClinicData.setStyleSheet("background-color:rgb(119, 162, 255);")
        self.centralwidget = QtWidgets.QWidget(ClinicData)
        self.centralwidget.setObjectName("centralwidget")

        #Logo
        self.logo = QtWidgets.QLabel(self.centralwidget)
        self.logo.setGeometry(QtCore.QRect(320, 50, 221, 51))
        self.logo.setPixmap(QtGui.QPixmap("midia/logo_menu.png"))
        self.logo.setObjectName("logo")

        #Título
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(370, 110, 151, 16))
        self.label.setStyleSheet("color: white;")
        self.label.setObjectName("label")
        
        #Título "Deletado com sucesso"
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        self.label_3.setFont(font)
        self.label_3.setGeometry(QtCore.QRect(0, 0, 0, 0))
        self.label_3.setStyleSheet("color: white;")
        self.label_3.setObjectName("label_3")

        #Título "Editado com sucesso"
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        self.label_4.setFont(font)
        self.label_4.setGeometry(QtCore.QRect(0, 0, 0, 0))
        self.label_4.setStyleSheet("color: white;")
        self.label_4.setObjectName("label_4")

        #Título "Você está configurando"
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        self.label_5.setFont(font)
        self.label_5.setGeometry(QtCore.QRect(80, 200, 691, 31))
        self.label_5.setStyleSheet("color: white;")
        self.label_5.setObjectName("label_5")

        #Título "INSIRA O NOME COMPLETO OU O CÓDIGO DO PACIENTE"
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        self.label_6.setFont(font)
        self.label_6.setGeometry(QtCore.QRect(80, 135, 350, 31))
        self.label_6.setStyleSheet("color: white; background: transparent;")
        self.label_6.setObjectName("label_6")
        self.label_6.setText("INSIRA O NOME COMPLETO OU O CÓDIGO DO PACIENTE:")

        #Título "ERRO AO BAIXAR A PLANILHA"
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_8.setFont(font)
        self.label_8.setGeometry(QtCore.QRect(0, 0, 0, 0))
        self.label_8.setStyleSheet("color: white; background: rgb(119, 162, 255);")
        self.label_8.setObjectName("label_8")
        self.label_8.setText("ERRO AO BAIXAR A PLANILHA")

        #Título "PLANILHA BAIXADA COM SUCESSO"
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_9.setFont(font)
        self.label_9.setGeometry(QtCore.QRect(0, 0, 0, 0))
        self.label_9.setStyleSheet("color: white; background: rgb(119, 162, 255);")
        self.label_9.setObjectName("label_9")
        self.label_9.setText("PLANILHA BAIXADA COM SUCESSO")        

        #Caixa de pesquisa
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(80, 160, 681, 31))
        self.lineEdit.setStyleSheet("background-color: white; border: none; border-radius: 2px;")
        self.lineEdit.setObjectName("lineEdit")
        
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
        self.abrir_menu.setGeometry(QtCore.QRect(80, 90, 51, 31))
        self.abrir_menu.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.abrir_menu.setStyleSheet("border:none; background: white; border-radius: 10px; color:rgb(119, 162, 255);")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("midia/menu.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.abrir_menu.setIcon(icon1)
        self.abrir_menu.setIconSize(QtCore.QSize(30, 30))
        self.abrir_menu.setObjectName("abrir_menu")
        self.abrir_menu.clicked.connect(funcao_abrir_menu)
        
        #Área de rolagem
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(80, 240, 741, 391))
        self.scrollArea.setStyleSheet("background-color: white; border: none;")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 741, 391))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")

        #Tabela
        self.tableWidget = QtWidgets.QTableWidget(self.scrollAreaWidgetContents)
        self.tableWidget.setGeometry(QtCore.QRect(0, 0, 741, 391))
        self.tableWidget.setObjectName("tableWidget")


        #Função que mostra a tabela com os dados vindos da base de dados
        def funcao_tabela():
            manipulador.execute('SELECT * FROM pacientes_db ORDER BY id')
            lista_ = list(manipulador.fetchall())
            self.tableWidget.insertRow
            self.tableWidget.setColumnCount(13)
            linhas = len(lista_)
            self.tableWidget.setRowCount(linhas)
            cont = 0
            while cont < linhas:
                cont2 = 0
                while cont2 < 13:
                    self.tableWidget.setItem(cont, cont2, QtWidgets.QTableWidgetItem(str(lista_[cont][cont2])))
                    #Linha, coluna, Item
                    cont2 += 1
                cont += 1
                
        funcao_tabela()


        #Função nada
        def funcao_nada():
            return

        #Função que pega o nome do paciente e coloca na variável nome
        def funcao_pega_nome():
            linha_ = self.tableWidget.currentItem().row()
            nome = str(self.tableWidget.item(linha_,1).text())
            self.label_8.setGeometry(QtCore.QRect(0, 0, 0, 0))
            self.label_9.setGeometry(QtCore.QRect(0, 0, 0, 0))
            self.label_5.setText(f"Você está configurando {nome}")
        
        #Botão que chama a função  
        self.tableWidget.itemClicked.connect(lambda: funcao_pega_nome())
        
        #Define as colunas da tabela
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(12, item)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        #Função pesquisar - Seleciona o dado da base de dados que possui o valor (nome completo ou código) pesquisado
        def funcao_pesquisar():
            self.label_5.setText("")
            pesquisar = self.lineEdit.text().upper().strip()
            self.tableWidget.setRowCount(0)
            manipulador.execute('SELECT * FROM pacientes_db')
            pacientes = list(manipulador.fetchall())
            selecionados = []

            if pesquisar != '':
                numeros = []
                for numero in list(range(0,11)):
                    numeros.append(str(numero))
                    
                string_codigo = ''
                for num in pesquisar:
                    if num in numeros:
                        string_codigo += str(num)
                        
                if string_codigo != '':
                    for qual_o_nome in pacientes:
                        if pesquisar not in list(qual_o_nome):
                            funcao_nada()
                        if pesquisar in list(qual_o_nome):
                            selecionados.append(qual_o_nome[2])
                    outros = []
                    for quem_e in selecionados:
                        for qual_o_nome in pacientes:
                            if quem_e in qual_o_nome:
                                indice_ = pacientes.index(qual_o_nome)
                                outros.append(pacientes[indice_])
                    self.tableWidget.setRowCount(len(selecionados))
                    cont = 0
                    while cont < len(outros):
                        cont2 = 0
                        while cont2 < 13:
                            self.tableWidget.setItem(cont, cont2, QtWidgets.QTableWidgetItem(str(outros[cont][cont2])))
                            #Linha, coluna, Item
                            cont2 += 1
                        cont += 1
                        
                if string_codigo == '':
                    for qual_o_nome in pacientes:
                        if pesquisar not in list(qual_o_nome):
                            funcao_nada()
                        if pesquisar in list(qual_o_nome):
                            selecionados.append(qual_o_nome[1])
                    outros = []
                    for quem_e in selecionados:
                        for qual_o_nome in pacientes:
                            if quem_e in qual_o_nome:
                                indice_ = pacientes.index(qual_o_nome)
                                outros.append(pacientes[indice_])
                    self.tableWidget.setRowCount(len(selecionados))
                    cont = 0
                    while cont < len(outros):
                        cont2 = 0
                        while cont2 < 13:
                            self.tableWidget.setItem(cont, cont2, QtWidgets.QTableWidgetItem(str(outros[cont][cont2])))
                            #Linha, coluna, Item
                            cont2 += 1
                        cont += 1
            else:
                funcao_tabela()

        
        #Botão de pesquisa
        self.pesquisar = QtWidgets.QPushButton(self.centralwidget)
        self.pesquisar.setGeometry(QtCore.QRect(770, 160, 51, 31))
        self.pesquisar.setStyleSheet("border:none; background: white; border-radius: 10px;")
        self.pesquisar.setText("")
        self.pesquisar.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("midia/lupa.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pesquisar.setIcon(icon)
        self.pesquisar.setIconSize(QtCore.QSize(25, 25))
        self.pesquisar.setObjectName("pesquisar")
        self.pesquisar.clicked.connect(funcao_pesquisar)

        #Função editar para editar item específico
        def funcao_editar():
            self.label_5.setText("")
            if int(self.tableWidget.rowCount())!=0 and int(self.tableWidget.columnCount())!=0:
                linha_tb = self.tableWidget.currentItem()
                if linha_tb != None:
                    linha_tb = self.tableWidget.currentItem().row()
                    linha_tb = int(linha_tb)
                    freq_ = self.tableWidget.item(linha_tb,0).text().upper()
                    paciente_ = self.tableWidget.item(linha_tb,1).text().upper()
                    codigo_ = self.tableWidget.item(linha_tb,2).text()
                    responsavel_ = self.tableWidget.item(linha_tb,3).text().upper()
                    observacoes_ = self.tableWidget.item(linha_tb,4).text().upper()
                    email_ = self.tableWidget.item(linha_tb,5).text()
                    celular_ = self.tableWidget.item(linha_tb,6).text()
                    laudo_ = self.tableWidget.item(linha_tb,7).text()
                    endereco_ = self.tableWidget.item(linha_tb,8).text()
                    profissional_ = self.tableWidget.item(linha_tb,9).text()
                    cpf_ = str(self.tableWidget.item(linha_tb,10).text())
                    nascimento_ = self.tableWidget.item(linha_tb,11).text()
                    id_ = int(self.tableWidget.item(linha_tb,12).text())
                    manipulador.execute(f"UPDATE pacientes_db SET paciente = '{paciente_}', responsavel = '{responsavel_}', profissional = '{profissional_}', celular = '{celular_}', email = '{email_}', laudo = '{laudo_}', endereco = '{endereco_}', observacoes = '{observacoes_}', cpf = '{cpf_}', nascimento = '{nascimento_}', frequencia = '{freq_}' WHERE id = {id_}")
                    conexao.commit()
                    self.label_3.setGeometry(QtCore.QRect(0, 0, 0, 0))
                    self.label_4.setGeometry(QtCore.QRect(210, 640, 121, 31))
            else:
                funcao_nada()


        #Botão para ativar a função editar
        self.enviar_2 = QtWidgets.QPushButton(self.centralwidget)
        self.enviar_2.setGeometry(QtCore.QRect(80, 640, 51, 31))
        self.enviar_2.setStyleSheet("border:none; background: white; border-radius: 10px;")
        self.enviar_2.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("midia/editar.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.enviar_2.setIcon(icon2)
        self.enviar_2.setIconSize(QtCore.QSize(25, 25))
        self.enviar_2.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.enviar_2.setObjectName("enviar_2")
        self.enviar_2.clicked.connect(funcao_editar)


        #Função para baixar planilha
        def baixar_planilha():
                try:
                        from openpyxl import Workbook
                        if int(self.tableWidget.rowCount())!=0 and int(self.tableWidget.columnCount())!=0:
                            planilha = Workbook()
                            planilha.create_sheet(index = 0, title = "Pacientes")
                            folha = planilha["Pacientes"]
                            folha.append(['FREQUÊNCIA','PACIENTE','CÓDIGO','RESPONSÁVEL','OBSERVAÇÕES','E-MAIL','CELULAR','LAUDO','ENDEREÇO','PROFISSIONAL','CPF','NASCIMENTO','ID'])

                            cont = 0
                            while cont < int(self.tableWidget.rowCount()):
                                    cont2 = 0
                                    linha = []
                                    while cont2 < int(self.tableWidget.columnCount()):
                                        linha.append(self.tableWidget.item(cont, cont2).text())
                                        #Linha, coluna, Item
                                        cont2 += 1
                                    folha.append(linha)#Adiciona a linha na tabela
                                    cont += 1

                            from os import path, mkdir, listdir
                            import platform
                            if str(platform.system()) == str("Windows"): #Para salvar caso seja Windows
                                pasta = path.join(path.expanduser("~\Documents"))
                                pasta_existe = path.exists(pasta)
                                if pasta_existe == True:
                                    pasta_clinicdata = path.join(path.expanduser("~\Documents\\Planilhas - ClinicData"))
                                    pasta_clinicdata_existe = path.exists(pasta_clinicdata)#Verifica se a pasta existe
                                if pasta_clinicdata_existe == False:
                                    mkdir(pasta_clinicdata)#Caso a pasta não exista, cria a pasta
                                    
                                if listdir(pasta_clinicdata) == [] or "pacientes.xlsx" not in listdir(pasta_clinicdata):
                                    nome = "pacientes.xlsx"
                                else:
                                    numero = 1
                                    for k in range(0,len(listdir(pasta_clinicdata))):
                                        nome = str("pacientes" + "(" + str(numero) + ")" + ".xlsx")
                                        if nome in listdir(pasta_clinicdata):
                                            numero +=1
                                planilha.save(pasta_clinicdata + "\\" + nome)#Salva a planilha na pasta
                                self.label_9.setGeometry(QtCore.QRect(500, 200, 350, 31))
                            else: #Para salvar nos outros sistemas
                                planilha.save("pacientes.xlsx")#Salva a planilha na pasta
                                self.label_9.setGeometry(QtCore.QRect(500, 200, 350, 31))
                        else:
                            self.label_9.setGeometry(QtCore.QRect(0, 0, 0, 0))
                            self.label_8.setGeometry(QtCore.QRect(500, 200, 350, 31))
                except:
                    self.label_9.setGeometry(QtCore.QRect(0, 0, 0, 0))
                    self.label_8.setGeometry(QtCore.QRect(500, 200, 350, 31))


        #Botão para baixar planilha
        self.pesquisar_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pesquisar_2.setGeometry(QtCore.QRect(770, 200, 51, 31))
        self.pesquisar_2.setStyleSheet("border:none;")
        self.pesquisar_2.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("midia/download.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pesquisar_2.setIcon(icon3)
        self.pesquisar_2.setIconSize(QtCore.QSize(25, 25))
        self.pesquisar_2.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.pesquisar_2.setObjectName("pesquisar_2")
        self.pesquisar_2.clicked.connect(lambda: baixar_planilha())


        #Função de exclusão de um item específico
        def funcao_excluir():
            self.label_5.setText("")
            if int(self.tableWidget.rowCount())!=0 and int(self.tableWidget.columnCount())!=0:
                linha_tb = self.tableWidget.currentItem()
                if linha_tb != None:
                    linha_tb = self.tableWidget.currentItem().row()
                    linha_tb = int(linha_tb)
                    id_ = int(self.tableWidget.item(linha_tb,12).text())
                    import sqlite3
                    from sqlite3 import Error
                    from config import conexao, manipulador
                    manipulador.execute(f"DELETE FROM pacientes_db WHERE id = {id_}")
                    conexao.commit()
                    self.label_4.setGeometry(QtCore.QRect(0, 0, 0, 0))
                    self.label_3.setGeometry(QtCore.QRect(210, 640, 121, 31))
            else:
                funcao_nada()

            
        #Botão para ativar a função de exclusão do item
        self.enviar_3 = QtWidgets.QPushButton(self.centralwidget)
        self.enviar_3.setGeometry(QtCore.QRect(150, 640, 51, 31))
        self.enviar_3.setStyleSheet("border:none; background: white; border-radius: 10px;")
        self.enviar_3.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("midia/lixeira.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.enviar_3.setIcon(icon3)
        self.enviar_3.setIconSize(QtCore.QSize(25, 25))
        self.enviar_3.clicked.connect(funcao_excluir)
        self.enviar_3.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.enviar_3.setObjectName("enviar_3")
        
        #Finalizando conteúdos do objeto
        ClinicData.setCentralWidget(self.centralwidget)
        self.retranslateUi(ClinicData)
        QtCore.QMetaObject.connectSlotsByName(ClinicData)

    #Insere os textos nas labels, nomes das colunas da tabela e título da janela
    def retranslateUi(self, ClinicData):
        _translate = QtCore.QCoreApplication.translate
        self.label.setText(_translate("ClinicData", "VER PACIENTES EXISTENTES"))
        self.label_3.setText(_translate("ClinicData", "Deletado com sucesso!"))
        self.label_4.setText(_translate("ClinicData", "Editado com sucesso!"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("ClinicData", "FREQUÊNCIA")) 
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("ClinicData", "PACIENTE"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("ClinicData", "CÓDIGO"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("ClinicData", "RESPONSÁVEL"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("ClinicData", "OBSERVAÇÕES"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("ClinicData", "E-MAIL"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("ClinicData", "CELULAR"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("ClinicData", "LAUDO"))
        item = self.tableWidget.horizontalHeaderItem(8)
        item.setText(_translate("ClinicData", "ENDEREÇO"))
        item = self.tableWidget.horizontalHeaderItem(9)
        item.setText(_translate("ClinicData", "PROFISSIONAL"))
        item = self.tableWidget.horizontalHeaderItem(10)
        item.setText(_translate("ClinicData", "CPF"))
        item = self.tableWidget.horizontalHeaderItem(11)
        item.setText(_translate("ClinicData", "NASCIMENTO"))
        item = self.tableWidget.horizontalHeaderItem(12)
        item.setText(_translate("ClinicData", "ID"))

#Final
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ClinicData = QtWidgets.QMainWindow()
    ui = Ui_ClinicData()
    ui.setupUi(ClinicData)
    ClinicData.show() #Mostra a janela
    sys.exit(app.exec())
    conexao.close() #Encerra a conexão do SQLite
