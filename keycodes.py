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
'a':'04',
'b':'05',
'c':'06',
'd':'07',
'e':'08',
'f':'09',
'g':'0a',
'h':'0b',
'i':'0c',
'j':'0d',
'k':'0e',
'l':'0f',
'm':'10',
'n':'11',
'o':'12',
'p':'13',
'q':'14',
'r':'15',
's':'16',
't':'17',
'u':'18',
'v':'19',
'w':'1a',
'x':'1b',
'y':'1c',
'z':'1d',
'1':'1e',
'2':'1f',
'3':'20',
'4':'21',
'5':'22',
'6':'23',
'7':'24',
'8':'25',
'9':'26',
'0':'27',
'enter':'28',
'esc':'29',
'backspace':'2a',
'tab':'2b',
'space':'2c',
'-':'2d',
'=':'2e',
'[':'2f',
']':'30',
'\\':'31',
#KEYCODE_HASH = 0x32
';':'33',
'\'':'34',
'`':'35',
#KEYCODE_ACCENT_GRAVE = 0x35
',':'36',
'.':'37',
'/':'38',
'caps lock':'39',
'f1':'3a',
'f2':'3b',
'f3':'3c',
'f4':'3d',
'f5':'3e',
'f6':'3f',
'f7':'40',
'f8':'41',
'f9':'42',
'f10':'43',
'f11':'44',
'f12':'45',
'print screen':'46',
'scroll lock':'47',
'pause':'48',
'insert':'49',
'home':'4a',
'page up':'4b',
'delete':'4c',
'end':'4d',
'page down':'4e',
'right':'4f',
'left':'50',
'down':'51',
'up':'52',
'clear':'53',
'num lock':'53',
'/':'54',
'*':'55',
#'-':'56',
'+':'57',
'enter':'58',
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
'ctrl':'e0',
'shift':'e1',
'alt':'e2',
'command':'e3'
#KEYCODE_RIGHT_CTRL = 0xe4
#KEYCODE_RIGHT_SHIFT = 0xe5
#KEYCODE_RIGHT_ALT = 0xe6
#KEYCODE_RIGHT_META = 0xe7
#KEYCODE_MEDIA_PLAY_PAUSE = 0xe8
#KEYCODE_REFRESH = 0xfa
}
