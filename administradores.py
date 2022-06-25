from config import *

#Interface
class Ui_ClinicData(object):
    def setupUi(self, ClinicData):
        
        #Define o tamanho
        ClinicData.setObjectName("ClinicData")
        ClinicData.setWindowTitle("Visualizar administradores")
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
        self.label.setGeometry(QtCore.QRect(350, 110, 201, 16))
        self.label.setStyleSheet("color: white;")
        self.label.setObjectName("label")
        self.label.setText("VER ADMINISTRADORES EXISTENTES")
        
        #Título "Deletado com sucesso"
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        self.label_3.setFont(font)
        self.label_3.setGeometry(QtCore.QRect(0, 0, 0, 0))
        self.label_3.setStyleSheet("color: white;")
        self.label_3.setText("Deletado com sucesso!")
        self.label_3.setObjectName("label_3")

        #Título "Editado com sucesso"
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        self.label_4.setFont(font)
        self.label_4.setGeometry(QtCore.QRect(0, 0, 0, 0))
        self.label_4.setStyleSheet("color: white;")
        self.label_4.setText("Editado com sucesso!")
        self.label_4.setObjectName("label_4")

        #Título "Você está configurando"
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        self.label_5.setFont(font)
        self.label_5.setGeometry(QtCore.QRect(80, 180, 691, 31))
        self.label_5.setStyleSheet("color: white;")
        self.label_5.setObjectName("label_5")

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
        self.scrollArea.setGeometry(QtCore.QRect(80, 220, 741, 371))
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
            manipulador.execute('SELECT * FROM administradores')
            lista_ = list(manipulador.fetchall())
            self.tableWidget.insertRow
            self.tableWidget.setColumnCount(4)
            linhas = len(lista_)
            self.tableWidget.setRowCount(linhas)
            cont = 0
            while cont < linhas:
                cont2 = 0
                while cont2 < 4:
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
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        #Função editar para editar item específico
        def funcao_editar():
            self.label_5.setText("")
            if int(self.tableWidget.rowCount())!=0 and int(self.tableWidget.columnCount())!=0:
                linha_tb = self.tableWidget.currentItem()
                if linha_tb != None:
                    linha_tb = self.tableWidget.currentItem().row()
                    linha_tb = int(linha_tb)
                    nome = self.tableWidget.item(linha_tb,1).text().upper()
                    usuario = self.tableWidget.item(linha_tb,2).text().lower()
                    senha = str(self.tableWidget.item(linha_tb,3).text())
                    id_ = int(self.tableWidget.item(linha_tb,0).text())
                    manipulador.execute(f"UPDATE administradores SET nome = '{nome}', usuario = '{usuario}', senha = '{senha}' WHERE id = {id_}")
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

        #Função de exclusão de um item específico
        def funcao_excluir():
            self.label_5.setText("")
            if int(self.tableWidget.rowCount())!=0 and int(self.tableWidget.columnCount())!=0:
                linha_tb = self.tableWidget.currentItem()
                if linha_tb != None:
                    linha_tb = self.tableWidget.currentItem().row()
                    linha_tb = int(linha_tb)
                    id_ = int(self.tableWidget.item(linha_tb,0).text())
                    import sqlite3
                    from sqlite3 import Error
                    from config import conexao, manipulador
                    manipulador.execute(f"DELETE FROM administradores WHERE id = {id_}")
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
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("ClinicData", "ID"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("ClinicData", "NOME"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("ClinicData", "USUÁRIO"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("ClinicData", "SENHA"))


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
