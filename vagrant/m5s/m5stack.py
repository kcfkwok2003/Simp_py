#
# This file is part of MicroPython M5Stack package
# Copyright (c) 2017-2018 Mika Tuupola
#
# Licensed under the MIT license:
#   http://www.opensource.org/licenses/mit-license.php
#
# Project home:
#   https://github.com/tuupola/micropython-m5stack
#

"""
M5Stack specific constants and classes.
"""

import display # pylint: disable=import-error
from input import DigitalInput # pylint: disable=import-error
from machine import Pin # pylint: disable=import-error
from micropython import const # pylint: disable=import-error

BUTTON_A_PIN = const(39)
BUTTON_B_PIN = const(38)
BUTTON_C_PIN = const(37)
SPEAKER_PIN = const(25)

TFT_LED_PIN = const(32)
TFT_DC_PIN = const(27)
TFT_CS_PIN = const(14)
TFT_MOSI_PIN = const(23)
TFT_CLK_PIN = const(18)
TFT_RST_PIN = const(33)
TFT_MISO_PIN = const(19)

class ButtonA(DigitalInput):
    def __init__(self, callback=None, trigger=Pin.IRQ_FALLING):
        pin = Pin(BUTTON_A_PIN, Pin.IN)
        DigitalInput.__init__(self, pin, callback=callback, trigger=trigger)

class ButtonB(object):
    def __init__(self, callback=None, trigger=Pin.IRQ_FALLING):
        pin = Pin(BUTTON_B_PIN, Pin.IN)
        DigitalInput.__init__(self, pin, callback=callback, trigger=trigger)

class ButtonC(object):
    def __init__(self, callback=None, trigger=Pin.IRQ_FALLING):
        pin = Pin(BUTTON_C_PIN, Pin.IN)
        DigitalInput.__init__(self, pin, callback=callback, trigger=trigger)

class Display(object):

    def __init__(self):
        self.tft = self.create()

    def __getattr__(self, name):
        return getattr(self.tft, name)

    def create(self):
        tft = display.TFT()
        tft.init(
            tft.ILI9341,
            spihost=tft.HSPI,
            width=240,
            height=320,
            mosi=TFT_MOSI_PIN,
            miso=TFT_MISO_PIN,
            clk=TFT_CLK_PIN,
            cs=TFT_CS_PIN,
            dc=TFT_DC_PIN,
            rst_pin=TFT_RST_PIN,
            backl_pin=TFT_LED_PIN,
            backl_on=1,
            speed=2600000,
            invrot=3,
            bgr=True
        )

        #tft.orient(tft.PORTRAIT_FLIP)
        tft.orient(tft.LANDSCAPE)
        tft.font(tft.FONT_Ubuntu, fixedwidth=True)


        return tft

    def on(self):
        power = Pin(TFT_LED_PIN, Pin.OUT)
        power.value(1)

    def off(self):
        power = Pin(TFT_LED_PIN, Pin.OUT)
        power.value(0)
