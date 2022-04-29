import request

class Mailgun:
    MAILGUN_API_URL = 'your_url'
    MAILGUN_API_KEY = 'your_email'

    FROM_NAME = 'Jana'
    FROM_EMAIL = 'yanaafonaseva@gmail.com'

    @classmethod
    def send_email(cls, to_emails, subject, content):
        request.post(
            cls.MAILGUN_API_URL,
            auth=('api', cls.MAILGUN_API_KEY),
            data={
                'from': f'{cls.FROM_NAME} <{cls.FROM_EMAIL}',
                'to': to_emails,
                'subject': subject,
                'text': content
            }
        )