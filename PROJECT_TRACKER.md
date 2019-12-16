THINGS TO BUY
--------------------------------------

* Power switch relay breakout
* USB extension cords?
* Raspberri PI housing (maybe just 3D print this)
  * https://www.thingiverse.com/thing:559858

IDEAS
--------------------------------------

#### General

* ability to switch the sounds the computer uses for certain responses
* star trek audio sources: http://www.trekcore.com/audio/
* setup a sort of skype
  * be able to go to a website from remote location that can "call" the dorm computer
* use a config file that saves the state of the program (e.g. a YAML file or something) so that in the event of a reboot/program stop, when the program starts again, it picks up where it left off
* use 'black' python package to format custom commands

#### Device control

* Projector
* Monitor
* Accessible web UI for manual configuration/control
* Lighting determined by music/audio being played

#### Flask routes

* Flask route for "red alert"
* Flask route for "yellow alert"
* Flask route for "mood lighting"

#### UI commands

* UI command "red alert"
* UI command "yellow alert"
* UI command "mood lighting"

TO DO
---------------------------------------

#### General

* figure out how to run python scripts on Raspberri PI boot
* 404 error handling
* python error handling for unknown errors

#### Device control

* audio switcher (probably an external microcontroller?)
* silent mode light

#### Flask routes

* Flask route for "switch audio source"
  * sub-route for "andrew"
  * sub-route for "matt" or "matthew"
  * sub-route for "pi"
* Flask route for "silent mode"
* Flask route for "exit silent mode"

#### UI commands

* UI command "switch audio source"
  * UI command "andrew"
  * UI command "matt" or "matthew"
  * UI command "pi"
* UI command "silent mode"
* UI command "exit silent mode"
* UI command "cancel"


WORKING ON NOW
---------------------------------------

#### General

* find audio files for computer sounds
* parse STT output for server request

#### Device control

#### Flask routes

#### UI commands


DONE
---------------------------------------

#### General

* LED control
* figure out speech to text engine
  * speech_recognition source file located at /home/andrew/.local/lib/python3.6/site-packages
  * speech_recognition library listen function has parameter for snowboy hotword detection (not used)
* setup basic Flask RESTful server
* setup basic UI that listens for "computer" command and responds with Star Trek computer sound
* restructure to use config yaml file for information storage and transfer

#### Device control

#### Flask routes

* Flask route for "lights on"
* Flask route for "lights off"

#### UI commands

* UI command "lights on"
* UI command "lights off"


BUGS
---------------------------------------

#### General

* pygame mixer causes audio distortion sometimes on playback (research other playback libraries)
* 'fade lights' command doesn't work after 'lights off' command is given

#### Device control

#### Flask routes

#### UI commands


FIXED BUGS
---------------------------------------

#### General

* trying to run UI on raspi throws "Invalid Sample rate error"
  * solved by manually entering the sample rate into the audio.open() function in snowboydetector.py
* running UI on raspi throws `IOError: [Errno -9985] Device unavailable`
  * solution is to specify `device_index` parameter in Microphone object creation with speech_recognition
* running UI on raspi throws `IOError: [Errno -9998] Invalid number of channels`
  * caused by multiple more than one microphone object being created in a single thread by both snowboy and speech_recognition
  * multithreading/processing didn't fix issue, next attempt is to use built in snowboy implementation in speech_recognition
  * fixed by using the snowboy implementation in speech_recognition
* speech input hangs on SpeechRecognition library `listen()` function/crashes the program
  * fixed by adding timeout parameter
* hotword detection struggling to work on raspi (activates randomly with various noises but not with hotword)
  * try using better models?
  * solved by getting updated Snowboy library with needed functionality

#### Device control

* mic input volume too low (probably need better quality mic)
  * snowboy has a gain parameter I can try setting
  * solved with better quality mic

#### Flask routes

#### UI commands
