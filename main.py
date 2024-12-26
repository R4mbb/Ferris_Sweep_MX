# HANgeul-Annotated Resoluxe's Efficient, Updated main.py (HAN-AREUm) for Ferris Sweep
# <0부터 시작하는 스플릿 키보드> WikiDocs 가이드에 배포된, Ferris Sweep / KMK 전용 main.py
# https://wikidocs.net/book/9749
# 본인 입맛에 맞게 자유롭게 수정해서 이용하세요!

# Replicates default Ferris keymap from QMK
# Credit: Pierre Chevalier, 2020
# https://github.com/qmk/qmk_firmware/tree/master/keyboards/ferris/keymaps/default

# Original KMK Keymap from:
# https://github.com/KMKfw/kmk_firmware/blob/master/boards/ferris_sweep/main.py

# 키보드의 초기 세팅입니다. 중심 모듈과 기능 모듈을 불러옵니다.
# 다른 기능을 추가하려면 여기에서 import하는 것에서 시작!
import  board

from  kb  import  KMKKeyboard

from kmk.keys import KC

from kmk.modules.holdtap import HoldTap

from kmk.modules.layers import Layers

from kmk.modules.mouse_keys import MouseKeys

from kmk.modules.split import Split

from kmk.extensions.international import International


# KMKKeyboard의 인스턴스를 keyboard라는 이름으로 생성

keyboard  =  KMKKeyboard()


# 불러온 기능들을 구체적인 키맵으로 활용하기 위하여 keyboard.modules 리스트에 추가합니다.
# 현재 사양으로는 split은 무조건 holdtap 다음에 추가되어야 합니다!!
keyboard.modules.append(HoldTap())
keyboard.modules.append(Layers())
keyboard.modules.append(MouseKeys())
split = Split(data_pin=board.D1,use_pio=True)
keyboard.modules.append(split)
keyboard.extensions.append(International())


# 비어있는 키들을 정의하는 부분.
# KC.TRNS는 VIA로 치면 역삼각형과 동일.
# KC.NO는 각 레이어에서 해당 자리를 사용하지 못하게 막는 것.
# (해당 키맵의 원작자는 좀 더 직관적으로 _와 X로 표현한 듯 합니다.)

_______  = KC.TRNS
XXXXXXX  = KC.NO

# 홀드탭 키를 정의하는 부분.
# 맨날 KC.HT 어쩌고 쓰려면 기니까 다른 이름의 변수에 할당합시다.
A_SFT  = KC.HT(KC.A, KC.LSFT,prefer_hold=False)
SCLN_SFT  = KC.HT(KC.SCLN, KC.LSFT,prefer_hold=False)
Z_CTL  = KC.HT(KC.Z, KC.LCTRL,prefer_hold=False)
C_ALT  = KC.HT(KC.C, KC.LALT,prefer_hold=False)
COM_ALT  = KC.HT(KC.COMM, KC.LALT,prefer_hold=False)
SLSH_CTL  = KC.HT(KC.SLSH, KC.LCTRL,prefer_hold=False)
CTL_ALT  = KC.LCTRL(KC.LALT)


# 레이어 키를 정의하는 부분.
L_L5  = KC.LT(5, KC.L)
D_L1  = KC.LT(1, KC.D)
F_L3  = KC.LT(3, KC.F)
J_L4  = KC.LT(4, KC.J)
K_L2  = KC.LT(2, KC.K)
S_L6  = KC.LT(6, KC.S)
#SPC_L7  = KC.LT(7, KC.SPC)
BSPC_L7  = KC.LT(7, KC.BSPC)

# 위에서 불러온 기능과 정의한 키를 이용해, 키매핑을 해 봅시다!

keyboard.keymap = [

[ # 0 QWERTY

KC.Q, KC.W, KC.E, KC.R, KC.T, KC.Y, KC.U, KC.I, KC.O, KC.P,

A_SFT, S_L6, D_L1, F_L3, KC.G, KC.H, J_L4, K_L2, L_L5, SCLN_SFT,

Z_CTL, KC.X, C_ALT, KC.V, KC.B, KC.N, KC.M, COM_ALT, KC.DOT, SLSH_CTL,

KC.HAEN, KC.SPC, BSPC_L7, KC.ENT,

],

[ # 1 MOUSE

_______, _______, _______, _______, _______, _______, KC.MW_UP, KC.MS_UP, KC.MW_DN, _______,

_______, KC.MB_LMB, _______, KC.MB_RMB, _______, _______, KC.MS_LT, KC.MS_DN, KC.MS_RT, _______,

_______, _______, _______, _______, _______, _______, _______, _______, _______, _______,

_______, _______, _______, _______,

],

[ # 2 NAVIGATION

_______, KC.HOME, KC.UP, KC.END, KC.PGUP, _______, _______, _______, _______, _______,

_______, KC.LEFT, KC.DOWN, KC.RGHT, KC.PGDN, _______, KC.LGUI, CTL_ALT, _______, _______,

_______, _______, _______, _______, _______, _______, _______, _______, _______, _______,

_______, _______, _______, _______,

],

[ # 3 RIGHT SYMBOLS

_______, _______, _______, _______, _______, _______, KC.UNDS, KC.PIPE, KC.QUOT, _______,

KC.CIRC, KC.ASTR, KC.AMPR, _______, _______, KC.HASH, KC.TILD, KC.SLSH, KC.DQUO, KC.DLR,

_______, _______, _______, _______, _______, _______, KC.MINS, KC.BSLS, KC.GRV, _______,

_______, _______, _______, _______,

],

[ # 4 LEFT SYMBOLS

_______, KC.COLN, KC.LABK, KC.RABK, KC.SCLN, _______, _______, _______, _______, _______,

KC.LCBR, KC.RCBR, KC.LPRN, KC.RPRN, KC.AT, _______, _______, KC.EQL, KC.PLUS, KC.PERC,

_______, KC.EXLM, KC.LBRC, KC.RBRC, _______, _______, _______, _______, _______, _______,

_______, _______, _______, _______,

],

[ # 5 FUNCTION

_______, KC.F9, KC.F10, KC.F11, KC.F12, _______, _______, _______, _______, _______,

_______, KC.F5, KC.F6, KC.F7, KC.F8, _______, _______, _______, _______, _______,

_______, KC.F1, KC.F2, KC.F3, KC.F4, _______, _______, _______, _______, _______,

_______, _______, _______, _______,

],

[ # 6 NUMBERS

_______, _______, _______, _______, _______, KC.SLSH, KC.N7, KC.N8, KC.N9, KC.PLUS,

_______, _______, _______, _______, _______, KC.ASTR, KC.N4, KC.N5, KC.N6, KC.MINS,

_______, _______, _______, _______, _______, KC.N0, KC.N1, KC.N2, KC.N3, KC.EQL,

_______, _______, _______, _______,

],

[ # 7 ALWAYS AVAILABLE

KC.ESC, _______, KC.COLN, _______, _______, _______, _______, KC.PSCR, _______, KC.DEL,

_______, KC.PERC, KC.SLSH, KC.ENT, _______, _______, KC.LGUI, _______, _______, KC.COLN,

_______, _______, _______, _______, _______, _______, KC.RALT, KC.RCTL, _______, KC.RESET,

_______, KC.TAB, _______, _______,

],

]


# 마지막은 항상 이걸로 끝납니다.
if  __name__  ==  "__main__":
    keyboard.go()
