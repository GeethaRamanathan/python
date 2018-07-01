import smtplib
    
content = "example email stuff here"
mail = smtplib.SMTP('smtp.gmail.com:587')
mail.starttls()
mail.login('yourmail','yourpwd')
mail.sendmail('sender mail','receiver mail',content)
print("Successfully sent")
mail.close()
