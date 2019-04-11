import sys, os, platform
import signal
from _thread import start_new_thread

import user_interface.main as ui
if platform.linux_distribution()[0] == 'Ubuntu':
    from user_interface.snowboy_ubuntu_py3 import snowboydecoder
elif platform.linux_distribution()[0] == 'debian':
    from user_interface.snowboy_pi_py3 import snowboydecoder

# =============== Backend server startup

def start_server():
    if platform.linux_distribution()[0] == 'Ubuntu':
        from server_backend.main import app
    elif platform.linux_distribution()[0] == 'debian':
        from server_backend_pi.main import app

    app.secret_key = "dorm_comp_password"
    app.debug = False # app.debug must be set to False to start the Flask server on a separate thread
    app.run(port=8000)

start_new_thread(start_server, ())

# =============== Snowboy startup

interrupted = False
model = 'user_interface/models/computer.umdl'

def signal_handler(signal, frame):
    global interrupted
    interrupted = True


def interrupt_callback():
    global interrupted
    return interrupted

detector = snowboydecoder.HotwordDetector(model, sensitivity=0.6)
print('Listening... Press Ctrl+C to exit')

# main loop
detector.start(detected_callback=ui.detectedCallback,
               audio_recorder_callback=ui.receive_command,
               interrupt_check=interrupt_callback,
               sleep_time=0.01)

detector.terminate()
