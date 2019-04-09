**WARNING: For the SnowBoy hotword detection library, it will only work if the correct binary is used. The default on this repository is the binary for Ubuntu. Binaries for other operating systems can be found on the [SnowBoy documentation page](http://docs.kitt.ai/snowboy/). The name of the binary file that differs for each operating system is `_snowboydetect.so`**

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

* `sudo apt install python-pyaudio`
* `sudo apt install libatlas-base-dev`
* `sudo apt install sox`
* `sudo apt install flac`
* `sudo apt install libasound-dev`
* Follow instructions at https://stackoverflow.com/questions/20023131/cannot-install-pyaudio-gcc-error


Required pip packages
------------------------
* SpeechRecognition
* flask
* requests
* pygame
* gTTS
