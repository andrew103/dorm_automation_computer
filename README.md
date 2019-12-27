**Note: The SnowBoy hotword detection library requires that specific binaries be used for certain operating systems and languages. Prebuilt binaries can be found on the [SnowBoy documentation page](http://docs.kitt.ai/snowboy/). Instructions for building a custom binary can be found on the [Snowboy GitHub repository README](https://github.com/Kitt-AI/snowboy)**

Sources
-----------------

https://dordnung.de/raspberrypi-ledstrip/

https://www.raspberrypi.org/documentation/usage/gpio/README.md

http://docs.kitt.ai/snowboy/

https://www.raspberrypi.org/forums/viewtopic.php?t=136974

https://www.raspberrypi.org/forums/viewtopic.php?f=37&t=97702

Required installations outside of pip
-------------------------------------

* `sudo apt install python3-pyaudio libatlas-base-dev sox flac`
* `sudo apt install libasound-dev portaudio19-dev libportaudio2 libportaudiocpp0`
* Follow instructions at https://stackoverflow.com/questions/20023131/cannot-install-pyaudio-gcc-error if error encountered during pip install


Required pip packages
------------------------
* SpeechRecognition
* flask
* requests
* pygame
* gTTS
