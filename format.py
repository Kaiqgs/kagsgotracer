class Aliases:
    NONE = "_"
    TRANSPARENT = "T"
    INHERIT = None


NONE = "KC_NO"
NONE_ALIAS = "_"

TRANSPARENT = "KC_TRNS"
TRANSPARENT_ALIAS = "T"

INHERIT_ALIAS = None


def inherit(keys_a, keys_b):
    assert len(keys_a) == len(keys_b)
    for i in range(len(keys_a)):
        assert len(keys_a[i]) == len(keys_b[i])
        for j in range(len(keys_a[i])):
            if keys_a[i][j] == None and keys_b[i][j] is not None:
                keys_a[i][j] = keys_b[i][j]
    return keys_a


output = ""


def format(name, keys, extra=0):
    global output
    ksize = 0
    count = 0
    for groupkey in keys:
        for key in groupkey:
            if key != "":
                count += 1
                ksize = len(key) + 1 if len(key) > ksize else ksize
    ksize += extra

    strout = ""
    for groupkey in keys:
        newgroup = [""]
        for key in groupkey:
            if key == TRANSPARENT_ALIAS:
                key = TRANSPARENT
            if key == NONE_ALIAS:
                key = NONE

            if key != "":
                key = f"{key},"

            kformat = f"{key:>{ksize}}"
            if key != "":
                newgroup.append(kformat)
            elif len(newgroup) > 0:
                newgroup[-1] += kformat
        # print(newgroup)
        strout += "\n\t\t" + "".join(newgroup)
    strout = strout[::-1]
    first = strout.index(",")
    strout = strout[first + 1 :]
    strout = strout[::-1]
    print(f"// {count}x Keys")
    output += f"\n\t[{name}] = LAYOUT({strout}\n\t),"


header = """
// Copyright 2023 QMK
// SPDX-License-Identifier: GPL-2.0-or-later
#include QMK_KEYBOARD_H

enum custom_layers {
    _BASECDHM,
    _BASE,
    _GAME,
    _NVIM,
    _DHVIM,
    _NAVIM,
    _SYMNUM,
    _NAV,
    _MOUSE,
    _MEDIA,
    _NUM,
    _FN,
    _SYS,
};

enum custom_keycodes {
        ESCTOCOLE = SAFE_RANGE,
        ESCTOVIM,
};

enum tapdance{
        TDSE,
};
//void keyboard_post_init_user(void) {
  // Customise these values to desired behaviour
  // debug_enable=true;
  // debug_matrix=true;
  //debug_keyboard=true;
  //debug_mouse=true;
//}

bool process_record_user(uint16_t keycode, keyrecord_t *record) {
    switch (keycode) {
        case ESCTOCOLE:
            if (record->event.pressed) {
                layer_off(_NVIM);
                layer_on(_DHVIM);
                return false;
            }
            break;
        case ESCTOVIM:
            if (record->event.pressed) {
                layer_on(_NVIM);
                layer_off(_DHVIM);
                return false;
            }
            break;
    }
    return true;
};



tap_dance_action_t tap_dance_actions[] = {
    [TDSE] = ACTION_TAP_DANCE_DOUBLE(KC_SLSH, KC_ENT),
};

// Home Row Mods
#define LHRG MT(MOD_LGUI, KC_A)
#define LHRA MT(MOD_LALT, KC_S)
#define LHRC MT(MOD_LCTL, KC_D)
#define LHRS MT(MOD_LSFT, KC_F)

#define RHRG MT(MOD_RGUI, KC_L)
#define RHRA MT(MOD_RALT, KC_K)
#define RHRC MT(MOD_RCTL, KC_J)
#define RHRS MT(MOD_RSFT, KC_H)

// Home Row CDHM Mods
#define CLHRG MT(MOD_LGUI, KC_A)
#define CLHRA MT(MOD_LALT, KC_R)
#define CLHRC MT(MOD_LCTL, KC_S)
#define CLHRS MT(MOD_LSFT, KC_T)

#define CRHRG MT(MOD_RGUI, KC_O)
#define CRHRA MT(MOD_RALT, KC_I)
#define CRHRC MT(MOD_RCTL, KC_E)
#define CRHRS MT(MOD_RSFT, KC_N)

#define SPC_NUM LT(_SYMNUM, KC_SPC)
#define CALPAD LT(_NAVIM, KC_ENT)
#define TAB_FN LT(_FN, KC_TAB)
#define ENT_NAVI LT(_NAVIM, KC_ENT)
#define ESC_NUM LT(_NUM, KC_ESC)
#define DEL_NAVI LT(_MOUSE, KC_DEL)

"""

# fmt: off
right_gacs = ["KC_RSFT", "KC_RCTL", "KC_RALT", "KC_RGUI"]
left_gacs = ["KC_LSFT", "KC_LCTL", "KC_LALT", "KC_LGUI"]
keys = [
    ["_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_"],
    ["_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_"],
    ["_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_"],
    ["", "_", "_", "_", "_", "", "", "_", "_", "_", "_", ""],
]

fn_keys = [
    [None, None, None, None, None, "ESC_NUM",  "DEL_NAVI",        None, None, None, None, None],
    [None, None, None, None, None, "TAB_FN",  "MO(_MEDIA)",  None, None, None, None, None],
    [None, None, None, None, None, "CALPAD", "MO(_SYS)",        None, None, None, None, None],
    ["", "KC_DOWN", "KC_UP", "KC_SPC", "SPC_NUM", "",       "", "KC_BSPC", "ENT_NAVI", "KC_LEFT", "KC_RIGHT", ""],
]

base_keys = \
inherit([
    ["KC_Q", "KC_W", "KC_E", "KC_R", "KC_T", None, None, "KC_Y", "KC_U", "KC_I", "KC_O", "KC_P"],
    ["LHRG", "LHRA", "LHRC", "LHRS", "KC_G", None, None, "KC_H", "RHRS", "RHRC", "RHRA", "RHRG"],
    ["KC_Z", "KC_X", "KC_C", "KC_V", "KC_B", None, None, "KC_N", "KC_M", "KC_COMM", "KC_DOT", "TD(TDSE)"],
    ["", None, None, None, None, "",   "", None, None, None, None, ""],
],
fn_keys)

cdhmbase_keys = \
inherit(
    [
        ["KC_Q", "KC_W", "KC_F", "KC_P", "KC_B", None,     None, "KC_J", "KC_L", "KC_U", "KC_Y", "KC_SCLN"],
        ["CLHRG", "CLHRA", "CLHRC", "CLHRS", "KC_G", None, None, "KC_M","CRHRS", "CRHRC", "CRHRA", "CRHRG"],
        ["KC_Z", "KC_X", "KC_C", "KC_D", "KC_V", None,     None, "KC_K", "KC_H", "KC_COMM", "KC_DOT", None],
        ["", None, None, None, None, "",                   "", None, None, None, None, ""],
    ],
    base_keys
)

cdhmvim_keys = \
inherit(
    [
        [None, None, None, None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, "ESCTOVIM", None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None, None, None, None],
    ],
    cdhmbase_keys
)



gamebase_keys = \
inherit(
    [
        ["KC_ESC", "KC_1", "KC_2", "KC_3", "KC_4", None,  None,None,None,None,None,None],
        ["KC_LSFT","KC_Q", "KC_W", "KC_E", "KC_R", None,  None,None,None,None,None,None],
        ["KC_LCTL", "KC_A", "KC_S", "KC_D", "KC_F", None, None,None,None,None,None,None],
        [None, None, None, "KC_SPC", "KC_SPC", None,   None, None, None, None, None, None],
    ],
base_keys
)


# nav_keys = [
#     ["_", "_", "_", "_", "_", "_",                         "_", "KC_AGIN", "KC_PASTE", "KC_COPY", "KC_CUT", "KC_UNDO"],
#     ["KC_LGUI", "KC_LALT", "KC_LCTL", "KC_LSFT", "_", "_", "KC_ESC", "KC_LEFT", "KC_DOWN", "KC_UP", "KC_RIGHT", "_"],
#     ["_", "_", "_", "_", "_", "_",                         "KC_ENT", "KC_HOME", "KC_PGDN", "KC_PGUP", "KC_END", "KC_INS"],
#     ["", "_", "_", "_", "_", "",                           "", "KC_BSPC", "KC_DEL", "_", "_", ""],
# ]

mouse_keys =inherit([
    [None, None, None, None, None, None, "KC_ACL2", "KC_AGIN", "KC_PASTE", "KC_COPY", "KC_CUT", "KC_UNDO"],
    ["KC_LGUI", "KC_LALT", "KC_LCTL", "KC_LSFT", None, "KC_ACL0", None, None,"KC_MS_L", "KC_MS_D", "KC_MS_U", "KC_MS_R"],
    [None, None, None, None, None, None, "KC_BTN1", None, "KC_WH_L", "KC_WH_D", "KC_WH_U", "KC_WH_R"],
    [None, None, None, None, None, None, None, "KC_BTN3", "KC_BTN2", None, None, None],
    ], keys)

nvim_keys = inherit(
    [
        [None, None, None, None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, "ESCTOCOLE", None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None, None, None, None],
    ],
    base_keys
)

navim_keys = inherit(
    [
        ["KC_1", "KC_2", "KC_3", "KC_4", "KC_5", None, None, None, None, None, "KC_I", None],
        [None, None, None, None, None, None, None, None, "KC_H", "KC_J", "KC_K", "KC_L"],
        [None, None, None, None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None, None, None, None],
    ],
    base_keys
)



media_keys = inherit([
    [None, None, None, None, None, None, None, None, None, None, None, None],
    [*left_gacs, None, None, None, None, "KC_MPRV", "KC_VOLD", "KC_VOLU", "KC_MNXT"],
    [None, None, None, None, None, None, "KC_MSTP", None, None, None, None, None],
    [None, None, None, None, None, None, None, "KC_MPLY", "KC_MUTE", None, None, None]
    ], keys
                     )

num_keys = inherit([
    [None, None, None, None, None, None, None,                         "KC_LBRC","KC_7", "KC_8", "KC_9", "KC_PPLS"],
    [*left_gacs, None, None, None,                                     "KC_SCLN","KC_4", "KC_5", "KC_6", "KC_PCMM"],
    [None, None, None, None, None, None, "KC_DOT",                "KC_PENT",    "KC_1", "KC_2", "KC_3", "KC_PEQL"],
    [None, None, None, None, None, None,                       None, "KC_0", "KC_MINS", "KC_0", "KC_PDOT", None],
    ], keys)

rowfn_keys = inherit([
    ["KC_F1", "KC_F2", "KC_F3", "KC_F4", "KC_F5", "_", "_", "KC_F6", "KC_F7", "KC_F8", "KC_F9", "KC_F10"],
    ["CW_TOGG", "KC_PSCR", "LCTL(KC_S)", "LCTL(KC_N)", "KC_NUM", None, None, None, *right_gacs],
    ["KC_HOME", "KC_PGUP", "KC_PGDN", "KC_END", "KC_CAPS", None, None, None, None, None, None, None],
    [None, "KC_F11", None, None, None, None, None, None, None, None, "KC_F12", None],
],  keys)

sys_keys = inherit([
    ["QK_BOOT", "DB_TOGG", "QK_RBT", None, None, None, None, "KC_SLEP", "KC_WAKE", None, None, "KC_PWR"],
    [None, None, None, None, None, None, None, None, None, None, None, None],
    ["TO(_BASE)","TO(_NVIM)", "TO(_BASECDHM)", "TO(_GAME)", None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None, None, None, None],
    ], keys)

symnum_keys = inherit([
    [ "KC_1", "KC_2", "KC_3", "KC_4", "KC_5", "KC_DQT",                "KC_GRV", "KC_6", "KC_7", "KC_8", "KC_9", "KC_0"],
    ["KC_MINS", "KC_EQL", "KC_LPRN", "KC_RPRN", "KC_UNDS", "KC_QUOTE",  "KC_QUOTE", "KC_ASTR", *right_gacs ],
    ["KC_PLUS", "KC_HASH", "KC_LCBR", "KC_RCBR", "KC_PERC", "KC_GRV",    "KC_GRV", "KC_AT", "KC_LBRC", "KC_RBRC", "KC_AMPR", "KC_BSLS"],
    [None, "KC_CIRC", "KC_DLR", None, None, None,                       None, "KC_QUOTE", "KC_DQT", "KC_EXLM", "KC_TILD", None],
],            keys
)
# fmt: on

symbols = [
    "KC_EXLM",
    "KC_AT",
    "KC_HASH",
    "KC_DLR",
    "KC_PERC",
    "KC_CIRC",
    "KC_AMPR",
    "KC_ASTR",
    "KC_LPRN",
    "KC_RPRN",
    "KC_UNDS",
    "KC_PLUS",
    "KC_LCBR",
    "KC_RCBR",
    # "KC_PIPE",
    "KC_GRV",
    "KC_DQT",
    "KC_QUOTE",
    "KC_LBRC",
    "KC_RBRC",
    "KC_LPRN",
    "KC_RPRN",
    "KC_LCBR",
]

conditions = [any([symbol in row for row in symnum_keys]) for symbol in symbols]
assert all(
    conditions
), f"Not all symbols are in the symnum layer {symbols[conditions.index(False)]}"

format("_BASECDHM", cdhmbase_keys, 1)
format("_BASE", base_keys, 1)
format("_GAME", gamebase_keys, 1)
format("_NVIM", nvim_keys, 1)
format("_DHVIM", cdhmvim_keys, 1)
format("_NAVIM", navim_keys, 1)
format("_SYMNUM", symnum_keys, 1)
format("_MOUSE", mouse_keys, 1)
format("_MEDIA", media_keys, 1)
format("_NUM", num_keys, 1)
format("_FN", rowfn_keys, 1)
format("_SYS", sys_keys, 1)
# WRITE TO FILE
end = f"""{header}\nconst uint16_t PROGMEM keymaps[][MATRIX_ROWS][MATRIX_COLS] = {{{output}\n}};"""
with open("keymaps\\default\\keymap.c", "w+") as f:
    f.write(end)
print(end)
