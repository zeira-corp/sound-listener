#!/usr/bin/env python
# sudo python listen.py
import json
import time
import math
import thread
import sys
sys.path.insert(0, '../noob')
from noob import *

class SoundListener:

    def initialize(self):
        # A0 on the GrovePI shield
        self.soundSensor = SoundSensor().initialize({
            'name': "Listener",
            'analogPort': 0
        })
        # D7 on the GrovePI shield
        self.ultrasonicRanger = UltrasonicRanger().initialize({
          'name': "Ranger",
          'digitalPort': 7
        })
        return self

    def listening(self):
        while True:
            try:
                sound = self.soundSensor.soundValue()
                distance = self.ultrasonicRanger.distance()

                print("distance:" + str(distance) + " cm")
                print("sound:" + str(sound) + " db(?)")

                time.sleep(1)

            except (IOError,TypeError) as e:
                print e

# main

soundListener = SoundListener().initialize()

try:
  thread.start_new_thread( soundListener.listening, () )

except Exception as e:
   print e

while 1:
  pass
