import sys, os, platform
import signal
import speech_recognition as sr
from pygame import mixer
import requests

if platform.linux_distribution()[0] == 'Ubuntu':
    from snowboy_ubuntu_py3 import snowboydecoder
elif platform.linux_distribution()[0] == 'debian':
    from snowboy_pi_py3 import snowboydecoder

abs_path = os.path.dirname(os.path.abspath(sys.argv[0]))

def receive_command(fname):
    r = sr.Recognizer()

    with sr.AudioFile(fname) as source:
        audio = r.record(source)

    try:
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

    os.remove(fname)


#=================================== BEGIN SNOWBOY DETECTOR CONFIG AND LISTENER

interrupted = False
model = 'models/computer.umdl'

def detectedCallback():
    print('Computer Activated')

    mixer.init(44100)
    mixer.music.load(os.path.join(abs_path, 'audio/computerbeep_42.mp3'))
    mixer.music.play()

def signal_handler(signal, frame):
    global interrupted
    interrupted = True


def interrupt_callback():
    global interrupted
    return interrupted

detector = snowboydecoder.HotwordDetector(model, sensitivity=0.6)
print('Listening... Press Ctrl+C to exit')

# main loop
detector.start(detected_callback=detectedCallback,
               audio_recorder_callback=receive_command,
               interrupt_check=interrupt_callback,
               sleep_time=0.01)

detector.terminate()