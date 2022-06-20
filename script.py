email_do_paciente = "paos@discente.ifpe.edu.br"
from email.mime.multipart import MIMEMultipart as formatodoemail
from email.mime.text import MIMEText as textodoemail
import smtplib

conectar = smtplib.SMTP("smtp-mail.outlook.com",587) #Conecta ao servidor
conectar.starttls() #Transporte layer security
conectar.login("naoresponda_clinicdata@outlook.com", "clinicdata00_") #Realiza o login

mensagem = formatodoemail()
HTML = """
<body>
<div style="width: 520px; height:200px; background-color: #77a2ff;">
<div style="background-image: url(https://i.imgur.com/M7CHpDz.png); width: 294px; height: 85px;margin-top: 40px;margin-left: 110px;position: absolute;"></div><p style="color: white;text-align: center;font-size: 14px;padding-top: 25px;font-weight: bold;letter-spacing: 10px;">AVISO</p>

</div><div style="text-align: center;max-width: 520px;">
<h1>Olá, paciente!</h1>
<h2 style="font-size: 20px;">Você está lembrado da sua consulta no dia <div style="display: inline-block;color: #4a66a2;text-decoration: underline;">29/06/2022</div>?</h2>
<div style="border: 1px solid silver;padding: 10px;border-radius: 10px;">
<div style="border-bottom: 1px solid silver;">

<div style="text-align: left;padding: 15px;margin-left: 50px;max-width: 392px;word-break: break-word;">Endereço:<div style="display: inline;font-weight: bold;margin-left: 5px;">Rua da Aurora, s/n, Recife, Pernambuco. Próximo ao Casarão Amarelo.</div></div></div>
<div style="border-bottom: 1px solid silver;"><div style="text-align: left;padding: 15px;margin-left: 50px;max-width: 392px;word-break: break-word;"> Horário: <div style="display: inline;font-weight: bold;margin-left: 5px;">15:17</div></div>

</div>
<div style=""><div style="text-align: left;padding: 15px;margin-left: 50px;max-width: 392px;word-break: break-word;">Profissional:<div style="display: inline;font-weight: bold;margin-left: 5px;">Dr. Teste da Silva</div></div>

</div>
</div>


<div style="font-size: 15px;color: #4b69a8;margin-top: 20px;">WhatsApp: (81) 90000-0000</div><div style="font-size: 15px;color: #4b69a8;margin-top: 20px;">E-mail: naoresponda_clinicdata@outlook.com</div>

<p>Em caso de cancelamento, adiamento ou dúvidas entre em contato conosco pelos nossos canais de comunicação o mais rápido possível!</p>
<p>Nós agradecemos pela compreensão :)</p>
<p>Equipe ClinicData</p><p style="font-size: 12px;margin-top: 50px;color: silver;">EMAIL ENVIADO AUTOMATICAMENTE, POR FAVOR, NÃO RESPONDER</p></div>
</body>
"""
mensagem['Subject'] = "AVISO - ClinicData" #Assunto do e-mail
mensagem.attach(textodoemail(HTML,'html')) #Conteúdo do texto//Lê em formato HTML
texto = mensagem.as_string() #Coloca como string

conectar.sendmail("naoresponda_clinicdata@outlook.com",email_do_paciente,texto) #Envia o e-mail
conectar.close()



'''import datetime

x = datetime.datetime.today().strftime('%Y-%m-%d')
print(type(x))'''
