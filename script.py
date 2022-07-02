from os import *
if str(sep + " ") == str('\ '):
    pasta = path.join(path.expanduser("~\Documents"))
    pasta_existe = path.exists(pasta)
    if pasta_existe == True:
        pasta_clinicdata = path.join(path.expanduser("~\Documents\\Planilhas - ClinicData"))
        pasta_clinicdata_existe = path.exists(pasta_clinicdata)
        if pasta_clinicdata_existe == False:
            mkdir(pasta_clinicdata)
        
else:
    print('Apenas Windows')
