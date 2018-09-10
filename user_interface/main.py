from snowboy_ubuntu import snowboydecoder
import sys, os
import signal
import speech_recognition as sr
from pygame import mixer
import requests

r = sr.Recognizer()
m = sr.Microphone()

abs_path = os.path.dirname(os.path.abspath(sys.argv[0]))

def receive_command():
    print('Computer Activated')

    mixer.init(44100)
    mixer.music.load(os.path.join(abs_path, 'audio/computerbeep_42.mp3'))
    mixer.music.play()

    with m as source: r.adjust_for_ambient_noise(source)
    print("Listening...")
    with m as source: audio = r.listen(source)
    try:
        value = r.recognize_google(audio)
        print(u"Output: {}".format(value).encode('utf-8'))
    except sr.UnknownValueError:
        print("Uknown value")
    except sr.RequestError:
        print("Couldn't reach Google Speech Recognition service")


#=================================== BEGIN SNOWBOY DETECTOR CONFIG AND LISTENER

interrupted = False


def signal_handler(signal, frame):
    global interrupted
    interrupted = True


def interrupt_callback():
    global interrupted
    return interrupted

models = ['models/computer1.pmdl', 'models/computer2.pmdl']

# capture SIGINT signal, e.g., Ctrl+C
signal.signal(signal.SIGINT, signal_handler)

sensitivity = [0.45]
detector = snowboydecoder.HotwordDetector(models, sensitivity=sensitivity)
callbacks = [lambda: receive_command()]*len(models)

print('Listening... Press Ctrl+C to exit')

# main loop
# make sure you have the same numbers of callbacks and models
detector.start(detected_callback=callbacks,
               interrupt_check=interrupt_callback,
               sleep_time=0.03)

detector.terminate()
