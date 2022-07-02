from os import *
if str(sep + "") == str('\ '):
    pasta = path.join(path.expanduser("~\Documents"))
    print(pasta)
    pasta_existe = path.exists(pasta)
    print(pasta_existe)
    pasta_clinicdata = pasta = path.join(path.expanduser("~\Documents\Planilhas - ClinicData"))
    if pasta_existe == True:
        try:
            pass
        except:
            pass
else:
    print('Apenas Windows')
