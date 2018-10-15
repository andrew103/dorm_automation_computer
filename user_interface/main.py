from snowboy_ubuntu import snowboydecoder # needs to be changed based on used platform
import sys, os
import signal
import speech_recognition as sr
from pygame import mixer
import requests

r = sr.Recognizer()
m = sr.Microphone()

abs_path = os.path.dirname(os.path.abspath(sys.argv[0]))

def receive_command(audio_in):
    # print('Computer Activated')

    # mixer.init(44100)
    # mixer.music.load(os.path.join(abs_path, 'audio/computerbeep_42.mp3'))
    # mixer.music.play()

    try:
        value = r.recognize_google(audio_in)
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

    # print('Computer Activated')
    #
    # mixer.init(44100)
    # mixer.music.load(os.path.join(abs_path, 'audio/computerbeep_42.mp3'))
    # mixer.music.play()
    #
    # with m as source: r.adjust_for_ambient_noise(source)
    # print("Listening...")
    # with m as source: audio = r.listen(source)
    # try:
    #     value = r.recognize_google(audio)
    #     uri = value.replace(" ", "_")
    #     response = requests.get('http://127.0.0.1:8000/{}'.format(uri))
    #
    #     if response.status_code != 200:
    #         print("Command does not exist")
    #     else:
    #         print(response.text)
    #
    # except sr.UnknownValueError:
    #     print("Uknown value")
    # except sr.RequestError:
    #     print("Couldn't reach Google Speech Recognition service")
    # except requests.exceptions.ConnectionError:
    #     print("Backend server could not be reached")


#=================================== BEGIN SNOWBOY DETECTOR CONFIG AND LISTENER

# models = os.listdir('./models')
models = ['models/computer1.pmdl', 'models/computer2.pmdl']
callbacks = [lambda: receive_command()]*len(models)

# main loop
# make sure you have the same numbers of callbacks and models
# THIS IS A TEMPORARY SOLUTION THAT WILL BE REDONE WITH MULTITHREADING
while True:
    with m as source:
        r.adjust_for_ambient_noise(source)
        print("Listening...")
        audio = r.listen(source, snowboy_configuration=('snowboy_ubuntu', models))
        receive_command(audio)
