import sys, os, platform
import signal
import speech_recognition as sr
from pygame import mixer
import requests

r = sr.Recognizer()
m = sr.Microphone(sample_rate=16000) # snowboy requires a 16kHz sample rate

abs_path = os.path.dirname(os.path.abspath(sys.argv[0]))

def receive_command():
    print('Computer Activated')

    mixer.init(44100)
    mixer.music.load(os.path.join(abs_path, 'audio/computerbeep_42.mp3'))
    mixer.music.play()

    try:
        audio = r.listen(source, timeout=10)
        value = r.recognize_google(audio)
        # print(value)
        uri = value.replace(" ", "_")
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


#=================================== BEGIN SNOWBOY DETECTOR CONFIG AND LISTENER

# models = os.listdir('./models')
models = ['models/computer1.pmdl', 'models/computer2.pmdl']
callbacks = [lambda: receive_command()]*len(models)
if platform.linux_distribution()[0] == 'Ubuntu':
    snowboy_instance = 'snowboy_ubuntu'
elif platform.linux_distribution()[0] == 'debian':
    snowboy_instance = 'snowboy_pi'

# main loop
with m as source: r.adjust_for_ambient_noise(source)
while True:
    with m as source:
        print("Listening...")
        try:
            r.snowboy_wait_for_hot_word(snowboy_instance, models, source)
            receive_command()
        except KeyboardInterrupt:
            break
