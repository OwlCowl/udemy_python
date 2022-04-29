import smtplib
from email.message import EmailMessage

email = EmailMessage()
email['Subject'] = 'Test Email'
email['Frrom'] = 'youe@mail.com'
email['To'] = 'someone@else.com'

content = """ Content of my mail """
email.set_content(content)


smtp_connector = smtplib.SMTP(host='smtp.gmail.com', port = 587)
smtp_connector.starttls()

smtp_connector.login('fake@gmail.com', 'password')
smtp_connector.send_message(email)

smtp_connector.close()
