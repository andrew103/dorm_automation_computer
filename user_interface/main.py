import sys, os, platform
import speech_recognition as sr
from pygame import mixer
import requests
import time
import yaml

if platform.linux_distribution()[0] == 'debian':
    import pigpio
    pi = pigpio.pi()

config = yaml.load(open('config.yaml'), Loader=yaml.Loader)
LED_PIN = config['data']['constants']['LED_PIN']
abs_path = os.path.dirname(os.path.abspath(sys.argv[0]))

def receive_command(fname):
    r = sr.Recognizer()

    with sr.AudioFile(fname) as source:
        audio = r.record(source)

    try:
        value = r.recognize_google(audio)
        # print(value)
        value = value.replace(" ", "_")
        uri = ""

        for command in config['data']['default_commands']:
            if command in value:
                uri = command
                break

        response = requests.get('http://127.0.0.1:8000/{}'.format(uri))

        if response.status_code != 200:
            print("Command does not exist")
        else:
            print(response.text)

    except sr.UnknownValueError:
        print("Uknown value")
    except sr.RequestError:
        print("Couldn't reach Google Speech Recognition service")
    except requests.exceptions.ConnectionError:
        print("Backend server could not be reached")
    except:
        print("Recognizer timed out")

    os.remove(fname)
    if platform.linux_distribution()[0] == 'debian':
         pi.set_PWM_dutycycle(LED_PIN, 0)

def detectedCallback():
    print('Computer Activated')

    if platform.linux_distribution()[0] == 'debian':
        pi.set_PWM_dutycycle(LED_PIN, 255)

    updateConfig()
    if not config['data']['variables']['silent_mode']:
        mixer.init(44100)
        mixer.music.load(os.path.join(abs_path, 'user_interface/audio/computerbeep_42.mp3'))
        mixer.music.play()

def updateConfig():
    global config
    config = yaml.load(open('config.yaml'), Loader=yaml.Loader)
