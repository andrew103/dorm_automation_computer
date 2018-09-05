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

* setup basic Flask RESTful server
* setup basic UI that listens for "computer" command and responds with Star Trek computer sound
* figure out how to run python scripts on Raspberri PI boot
* 404 error handling
* python error handling for unknown errors
* find audio files for computer sounds

#### Device control

* audio switcher (probably an external microcontroller?)
* silent mode light

#### Flask routes

* Flask route for "lights on"
* Flask route for "lights off"
* Flask route for "switch audio source"
  * sub-route for "andrew"
  * sub-route for "matt" or "matthew"
  * sub-route for "pi"
* Flask route for "silent mode"
* Flask route for "exit silent mode"

#### UI commands

* UI command "lights on"
* UI command "lights off"
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

* figure out speech to text engine
  * speech_recognition source file located at /home/andrew/.local/lib/python3.6/site-packages
  * speech_recognition library listen function has parameter for snowboy hotword detection
  * snowboy hotword model located in downloads

#### Device control

#### Flask routes

#### UI commands


DONE
---------------------------------------

#### General

* LED control

#### Device control

#### Flask routes

#### UI commands


BUGS
---------------------------------------

#### General

* speech input hangs on SpeechRecognition library `listen()` function/crashes the program
* pygame mixer causes audio distortion sometimes on playback (research other playback libraries)

#### Device control

#### Flask routes

#### UI commands
