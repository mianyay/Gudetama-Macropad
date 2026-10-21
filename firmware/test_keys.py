import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC

keyboard = KMKKeyboard()

keyboard.matrix = KeysScanner(
    pins=[
        board.D0,   # SW1
        board.D1,   # SW2
        board.D2,   # SW3
        board.D3,   # SW4
        board.D6,   # SW5
        board.D9,   # encoder press
    ],
    value_when_pressed=False,
)

keyboard.keymap = [
    [KC.A, KC.B, KC.C, KC.D, KC.E, KC.F]
]

if __name__ == '__main__':
    keyboard.go()