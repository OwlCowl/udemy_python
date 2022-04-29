from pylibs.libs.mailgun import Mailgun

TO_EMAILS = ['anna@orla.com']
SUBJECT = 'Test mails'
CONTENT = 'Hello, here my first test mail'

Mailgun.send_email(TO_EMAILS, SUBJECT, CONTENT)