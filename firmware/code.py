#  5 keys + rotary knob + OLED + 4 RGB LEDs
#  Board: Seeed XIAO RP2040
#  Firmware: KMK (CircuitPython)
#  By: Miranda Nguyen

import board
import busio

from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.encoder import EncoderHandler
from kmk.extensions.rgb import RGB, AnimationModes
from kmk.extensions.display import Display, TextEntry
from kmk.extensions.displayssd1306 import SSD1306

keyboard = KMKKeyboard()

# PIN MAP

