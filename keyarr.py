# USB Usage ID values for the keycodes that TinyPilot can emit to the target
# computer through the USB keyboard interface.
#
# Source: HID Usage Tables for USB, v1.21, section "10 - Keyboard/Keypad Page"
# https://usb.org/sites/default/files/hut1_21.pdf

MODIFIER_LEFT_CTRL = 1 << 0
MODIFIER_LEFT_SHIFT = 1 << 1
MODIFIER_LEFT_ALT = 1 << 2
MODIFIER_LEFT_META = 1 << 3
MODIFIER_RIGHT_CTRL = 1 << 4
MODIFIER_RIGHT_SHIFT = 1 << 5
MODIFIER_RIGHT_ALT = 1 << 6
MODIFIER_RIGHT_META = 1 << 7

reference = dict()

reference = {
'a':0,
'b':0,
'c':0,
'd':0,
'e':0,
'f':0,
'g':0,
'h':0,
'i':0,
'j':0,
'k':0,
'l':0,
'm':0,
'n':0,
'o':0,
'p':0,
'q':0,
'r':0,
's':0,
't':0,
'u':0,
'v':0,
'w':0,
'x':0,
'y':0,
'z':0,
'1':0,
'2':0,
'3':0,
'4':0,
'5':0,
'6':0,
'7':0,
'8':0,
'9':0,
'0':0,
'enter':0,
'esc':0,
'backspace':0,
'tab':0,
'space':0,
'-':0,
'=':0,
'[':0,
']':0,
'\\':0,
#KEYCODE_HASH = 0x32
';':0,
'\'':0,
'`':0,
#KEYCODE_ACCENT_GRAVE = 0x35
',':0,
'.':0,
'/':0,
'caps lock':0,
'f1':0,
'f2':0,
'f3':0,
'f4':0,
'f5':0,
'f6':0,
'f7':0,
'f8':0,
'f9':0,
'f10':0,
'f11':0,
'f12':0,
#'print screen':0,
'scroll lock':0,
'pause':0,
'insert':0,
'home':0,
'page up':0,
'delete':0,
'end':0,
'page down':0,
'right':0,
'left':0,
'down':0,
'up':0,
#'clear':0,
'num lock':0,
'/':0,
#'*':0,
#'-':0,
#'+':0,
'enter':0,
#KEYCODE_NUMPAD_1 = 0x59
#KEYCODE_NUMPAD_2 = 0x5a
#KEYCODE_NUMPAD_3 = 0x5b
#KEYCODE_NUMPAD_4 = 0x5c
#KEYCODE_NUMPAD_5 = 0x5d
#KEYCODE_NUMPAD_6 = 0x5e
#KEYCODE_NUMPAD_7 = 0x5f
#KEYCODE_NUMPAD_8 = 0x60
#KEYCODE_NUMPAD_9 = 0x61
#KEYCODE_NUMPAD_0 = 0x62
#KEYCODE_NUMPAD_DOT = 0x63
#KEYCODE_102ND = 0x64  # Right of left Shift on non-US keyboards
#KEYCODE_CONTEXT_MENU = 0x65
#KEYCODE_F13 = 0x68
#KEYCODE_F14 = 0x69
#KEYCODE_F15 = 0x6a
#KEYCODE_F16 = 0x6b
#KEYCODE_F17 = 0x6c
#KEYCODE_F18 = 0x6d
#KEYCODE_F19 = 0x6e
#KEYCODE_F20 = 0x6f
#KEYCODE_F21 = 0x70
#KEYCODE_F22 = 0x71
#KEYCODE_F23 = 0x72
#KEYCODE_EXECUTE = 0x74
#KEYCODE_HELP = 0x75
#KEYCODE_SELECT = 0x77
#KEYCODE_HANGEUL = 0x90
#KEYCODE_HANJA = 0x91
'ctrl':0,
'shift':0,
'alt':0,
'command':0
#KEYCODE_RIGHT_CTRL = 0xe4
#KEYCODE_RIGHT_SHIFT = 0xe5
#KEYCODE_RIGHT_ALT = 0xe6
#KEYCODE_RIGHT_META = 0xe7
#KEYCODE_MEDIA_PLAY_PAUSE = 0xe8
#KEYCODE_REFRESH = 0xfa
}

def setKey(key, val):
	reference[key] = val
def getKey(key):
	return reference[key]
