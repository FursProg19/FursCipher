import smtplib
from email.mime.text import MIMEText

class EmailSender ():
    def __init__ (self, config_file_name, debug_enabled):
        self.login = None
        self.password = None
        self.server = None
        self.port = None
        self.server_name = None
        self.parse_config_file (config_file_name)
        self.connect (debug_enabled)
        self.login_to_mail ()

    def parse_config_file (self, file_name):
        with open(file_name) as config:
            self.server_name, self.port, self.login, self.password = config.readline().strip().split(' ')
            self.port = int(self.port)

            
    def connect (self, debug_enabled):
        self.server = smtplib.SMTP(self.server_name, self.port)
        self.server.set_debuglevel(debug_enabled)
        self.server.ehlo()
        self.server.starttls()
        self.server.ehlo()
   
    def login_to_mail (self):
        self.server.login(self.login, self.password)
    
    def send_mail (self, message_text, subject, sender_name, reciever_name, reciever_email):
        message = MIMEText(message_text)
        message ['Subject'] = subject
        message ['From'] = sender_name
        message ['To'] = reciever_name
        self.server.sendmail(self.login, reciever_email, message.as_string())
    
    def destroy (self):
        self.server.quit()
