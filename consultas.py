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
        self.centralwidget = QtWidgets.QWidget(ClinicData)
        self.centralwidget.setObjectName("centralwidget")

        #Logo
        self.logo = QtWidgets.QLabel(self.centralwidget)
        self.logo.setGeometry(QtCore.QRect(320, 50, 221, 51))
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap("midia/logo_menu.png"))
        self.logo.setObjectName("logo")

        #Título "VER CONSULTAS EXISTENTES"
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(370, 110, 151, 16))
        self.label.setStyleSheet("color: white;")
        self.label.setObjectName("label")
        self.label.setText("VER CONSULTAS EXISTENTES")

        #Título "Insira o código do paciente:"
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(340, 640, 161, 31))
        self.label_2.setStyleSheet("color: white;")
        self.label_2.setObjectName("label_2")
        self.label_2.setText("Insira o código do paciente:")

        #Título "Deletado com sucesso!"
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_3.setFont(font)
        self.label_3.setGeometry(QtCore.QRect(0, 0, 0, 0))
        self.label_3.setStyleSheet("color: white;")
        self.label_3.setObjectName("label_3")
        self.label_3.setText("Deletado com sucesso!")

        #Título "Editado com sucesso!"
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_4.setFont(font)
        self.label_4.setGeometry(QtCore.QRect(0, 0, 0, 0))
        self.label_4.setStyleSheet("color: white;")
        self.label_4.setObjectName("label_4")
        self.label_4.setText("Editado com sucesso!")

        #Título "Você está editando"
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
        self.label_6.setFont(font)
        self.label_6.setGeometry(QtCore.QRect(80, 135, 350, 31))
        self.label_6.setStyleSheet("color: white; background: transparent;")
        self.label_6.setObjectName("label_6")
        self.label_6.setText("INSIRA O NOME COMPLETO OU O CÓDIGO DO PACIENTE:")

        #Linha de edição - Barra de pesquisa
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(80, 160, 681, 31))
        self.lineEdit.setStyleSheet("background-color: white; border: none; border-radius: 2px;")
        self.lineEdit.setObjectName("lineEdit")

        #Linha de edição - Caixa para colocar o código do paciente
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(510, 640, 251, 31))
        self.lineEdit_2.setStyleSheet("background-color: white; border: none; border-radius: 2px;")
        self.lineEdit_2.setObjectName("lineEdit_2")
        
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

        #Função nada
        def funcao_nada():
            return

        #Função que mostra a tabela
        def funcao_tabela():
            manipulador.execute('SELECT * FROM consultas_db ORDER BY id')
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

        #Títulos das colunas
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

        #Função que pega o nome do paciente e coloca na variável nome
        def funcao_pega_nome():
            linha_ = self.tableWidget.currentItem().row()
            nome = str(self.tableWidget.item(linha_,1).text())
            self.label_5.setText(f"Você está configurando {nome}")
        
        #Botão que chama a função pega_nome
        self.tableWidget.itemClicked.connect(lambda: funcao_pega_nome())

        #Função de pesquisa
        def funcao_pesquisar():
            pesquisar = self.lineEdit.text().upper().strip()
            self.tableWidget.setRowCount(0)
            manipulador.execute('SELECT * FROM consultas_db')
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
                    pago_ = self.tableWidget.item(linha_tb,0).text().upper()
                    paciente_ = self.tableWidget.item(linha_tb,1).text().upper()
                    codigo_ = self.tableWidget.item(linha_tb,2).text()
                    responsavel_ = self.tableWidget.item(linha_tb,3).text().upper()
                    profissional_ = self.tableWidget.item(linha_tb,4).text().upper()
                    data_ = self.tableWidget.item(linha_tb,5).text()
                    celular_ = self.tableWidget.item(linha_tb,6).text()
                    valor_ = self.tableWidget.item(linha_tb,7).text()
                    email_ = self.tableWidget.item(linha_tb,8).text()
                    laudo_ = self.tableWidget.item(linha_tb,9).text()
                    endereco_ = str(self.tableWidget.item(linha_tb,10).text())
                    observacoes_ = self.tableWidget.item(linha_tb,11).text()
                    id_ = int(self.tableWidget.item(linha_tb,12).text())
                    import sqlite3
                    from sqlite3 import Error
                    from config import conexao, manipulador
                    manipulador.execute(f"UPDATE consultas_db SET pago = '{pago_}', paciente = '{paciente_}', codigo = '{codigo_}', responsavel = '{responsavel_}', profissional_r = '{profissional_}', data = '{data_}', celular = '{celular_}', valor = '{valor_}', email = '{email_}', laudo = '{laudo_}', endereco = '{endereco_}', observacoes = '{observacoes_}' WHERE id = {id_}")
                    conexao.commit()
                    self.label_3.setGeometry(QtCore.QRect(0, 0, 0, 0))
                    self.label_4.setGeometry(QtCore.QRect(210, 640, 121, 31))
            else:
                funcao_nada()
        
        #Botão para ativar a função de edição
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
                    manipulador.execute(f"DELETE FROM consultas_db WHERE id = {id_}")
                    conexao.commit()
                    self.label_4.setGeometry(QtCore.QRect(0, 0, 0, 0))
                    self.label_3.setGeometry(QtCore.QRect(210, 640, 121, 31))
            else:
                funcao_nada()
            

        #Botão para ativar a função de exclusão
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

        #Botão para enviar e-mail
        self.enviar = QtWidgets.QPushButton(self.centralwidget)
        self.enviar.setGeometry(QtCore.QRect(770, 640, 51, 31))
        self.enviar.setStyleSheet("border:none; background: white; border-radius: 10px;")
        self.enviar.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("midia/email.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.enviar.setIcon(icon1)
        self.enviar.setIconSize(QtCore.QSize(25, 25))
        self.enviar.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.enviar.setObjectName("enviar")
        
        #Botão para baixar planilha
        self.pesquisar_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pesquisar_2.setGeometry(QtCore.QRect(770, 200, 51, 31))
        self.pesquisar_2.setStyleSheet("border:none;")
        self.pesquisar_2.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("midia/download.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pesquisar_2.setIcon(icon3)
        self.pesquisar_2.setIconSize(QtCore.QSize(25, 25))
        self.pesquisar_2.setObjectName("pesquisar_2")
        
        ClinicData.setCentralWidget(self.centralwidget)
        self.retranslateUi(ClinicData)
        QtCore.QMetaObject.connectSlotsByName(ClinicData)

    #Função padrão - Insere títulos das colunas
    def retranslateUi(self, ClinicData):
        _translate = QtCore.QCoreApplication.translate
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("ClinicData", "PAGO"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("ClinicData", "PACIENTE"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("ClinicData", "CÓDIGO"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("ClinicData", "RESPONSÁVEL"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("ClinicData", "PROFISSIONAL"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("ClinicData", "DATA"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("ClinicData", "CELULAR"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("ClinicData", "VALOR"))
        item = self.tableWidget.horizontalHeaderItem(8)
        item.setText(_translate("ClinicData", "E-MAIL"))
        item = self.tableWidget.horizontalHeaderItem(9)
        item.setText(_translate("ClinicData", "LAUDO"))
        item = self.tableWidget.horizontalHeaderItem(10)
        item.setText(_translate("ClinicData", "ENDEREÇO:"))
        item = self.tableWidget.horizontalHeaderItem(11)
        item.setText(_translate("ClinicData", "OBSERVAÇÕES:"))
        item = self.tableWidget.horizontalHeaderItem(12)
        item.setText(_translate("ClinicData", "ID:"))

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
