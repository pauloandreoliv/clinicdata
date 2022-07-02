from os import sep, path, mkdir
            if str(sep + " ") == str('\ '):
                try:
                    pasta = path.join(path.expanduser("~\Documents"))
                    pasta_existe = path.exists(pasta)
                    if pasta_existe == True:
                        pasta_clinicdata = path.join(path.expanduser("~\Documents\\Planilhas - ClinicData"))
                        pasta_clinicdata_existe = path.exists(pasta_clinicdata)
                        if pasta_clinicdata_existe == False:
                            mkdir(pasta_clinicdata)
                        from openpyxl import Workbook
                        if int(self.tableWidget.rowCount())!=0 and int(self.tableWidget.columnCount())!=0:
                            planilha = Workbook()
                            planilha.create_sheet(index = 0, title = "Dados")
                            folha = planilha.active
                            folha.append(['PAGO','PACIENTE','CÓDIGO','RESPONSÁVEL','PROFISSIONAL','HORÁRIO','DATA','CELULAR','VALOR','E-MAIL','LAUDO','ENDEREÇO','OBSERVAÇÕES','ID'])
                            cont = 0
                            while cont < int(self.tableWidget.rowCount()):
                                    cont2 = 0
                                    linha = []
                                    while cont2 < int(self.tableWidget.columnCount()):
                                        linha.append(self.tableWidget.item(cont, cont2).text())
                                        #Linha, coluna, Item
                                        cont2 += 1
                                    folha.append(linha)
                                    cont += 1
                            planilha.save("consultas.xlsx")
                        else:
                            self.label_7.setGeometry(QtCore.QRect(0, 0, 0, 0))
                            self.label_8.setGeometry(QtCore.QRect(500, 200, 350, 31))
                except:
                    self.label_7.setGeometry(QtCore.QRect(0, 0, 0, 0))
                    self.label_8.setGeometry(QtCore.QRect(500, 200, 350, 31))
            else:
                self.label_8.setGeometry(QtCore.QRect(0, 0, 0, 0))
                self.label_7.setGeometry(QtCore.QRect(500, 200, 350, 31))
