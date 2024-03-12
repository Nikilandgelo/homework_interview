import email
import smtplib
import imaplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class Email():
    
    def __init__(self, login:str, password:str):
        self.gmail_smtp = "smtp.gmail.com"
        self.gmail_imap = "imap.gmail.com"

        self.login = login
        self.password = password
    
    def send_message(self, subject:str, recipients:list, message:str):
        msg = MIMEMultipart()
        msg['From'] = self.login
        msg['To'] = ', '.join(recipients)
        msg['Subject'] = subject
        msg.attach(MIMEText(message))

        with smtplib.SMTP(self.gmail_smtp, 587) as message_protocol:
            # identify ourselves to smtp gmail client
            message_protocol.ehlo()
            # secure our email with tls encryption
            message_protocol.starttls()
            # re-identify ourselves as an encrypted connection
            message_protocol.ehlo()
            message_protocol.login(self.login, self.password)
            message_protocol.sendmail(self.login, message_protocol, msg.as_string())
    
    def get_message(self, header = None):
        mail = imaplib.IMAP4_SSL(self.gmail_imap)
        mail.login(self.login, self.password)
        mail.list()
        mail.select("inbox")

        criterion = '(HEADER Subject "%s")' % header if header else 'ALL'
        data = mail.uid('search', None, criterion)
        assert data[0], 'There are no letters with current header'
        latest_email_uid = data[0].split()[-1]
        data = mail.uid('fetch', latest_email_uid, '(RFC822)')
        raw_email = data[0][1]
        email_message = email.message_from_string(raw_email)
        mail.logout()

if __name__ == '__main':
    instance_email = Email('login@gmail.com', 'qwerty')
    instance_email.send_message('Subject', ['vasya@email.com', 'petya@email.com'], 'Message')
    instance_email.get_message()