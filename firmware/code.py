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
#  SW1   copy
#  SW2   paste
#  SW3   undo
#  SW4   redo
#  SDA   OLED data
#  SCL   OLED clock
#  SW5   play / pause
#  ENC_A encoder turn
#  DENC_B encoder turn
#  ENC_SW encoder press - mute

# BUTTONS
keyboard.matrix = KeysScanner(
    pins = [
        board.D0,   # SW1
        board.D1,   # SW2
        board.D2,   # SW3
        board.D3,   # SW4
        board.D6,   # SW5
        board.D9,   # encoder press
    ],
    value_when_pressed=False,
)

# KEY MAP
keyboard.keymap = [
    [
        KC.LCTL(KC.C),   # SW1 - copy
        KC.LCTL(KC.V),   # SW2 - paste
        KC.LCTL(KC.Z),   # SW3 - undo
        KC.LCTL(KC.Y),   # SW4 - redo
        KC.MPLY,         # SW5 - play / pause
        KC.MUTE,         # knob press - mute
    ]
]

# KNOB
encoder_handler = EncoderHandler()
keyboard.modules.append(encoder_handler)

# pin A, pin B, button
encoder_handler.pins = ((board.D7, board.D8, None),)

# anticlockwise, clockwise
encoder_handler.map = (((KC.VOLD, KC.VOLU),),)

# RBG LEDs
rgb = RGB(
    pixel_pin=board.D10,
    num_pixels=4,
    val_limit=100,       # a brightness cap to protect USB power
    val_default=60,
    animation_mode=AnimationModes.RAINBOW,
    animation_speed=2,
)
keyboard.extensions.append(rgb)

# OLED
i2c = busio.I2C(board.SCL, board.SDA)

driver = SSD1306(i2c=i2c, device_address=0x3C)

display = Display(
    display=driver,
    width=128,
    height=32,
    entries=[
        TextEntry(text='Gudetama Macropad :D', x=0, y=0),
        TextEntry(text='by Miranda', x=0, y=14),
    ],
)
keyboard.extensions.append(display)

# START
if __name__ == '__main__':
    keyboard.go()