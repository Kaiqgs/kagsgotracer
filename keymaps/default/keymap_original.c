// Copyright 2023 QMK
// SPDX-License-Identifier: GPL-2.0-or-later

#include QMK_KEYBOARD_H

enum custom_layers {
    _BASE,
    // _BASECDHM,
    _TEST,
    _SYS, // Additional features
    _MEDIA,
    _NAV,
    _MOUSE,
    _NUM,
    _BUTTON,
    _SYM,
    _FN,
};


// Home Row Mods
#define LHRG MT(MOD_LGUI, KC_A)
#define LHRA MT(MOD_LALT, KC_S)
#define LHRC MT(MOD_LCTL, KC_D)
#define LHRS MT(MOD_LSFT, KC_F)

#define RHRG MT(MOD_RGUI, KC_SCLN)
#define RHRA MT(MOD_RALT, KC_L)
#define RHRC MT(MOD_RCTL, KC_K)
#define RHRS MT(MOD_RSFT, KC_J)

#define SPACE_NAV MT(MO(_NAV), KC_SPC)
#define ESC_MEDIA MT(MO(_MEDIA), KC_ESC)
#define BSPC_NUM MT(MO(_NUM), KC_BSPC)
#define TAB_MOUSE MT(MO(_MOUSE), KC_TAB)
#define ENT_SYM MT(MO(_SYM), KC_ENT)
#define DEL_FN MT(MO(_FN), KC_DEL)
// #define TAB_MOUSE


const uint16_t PROGMEM keymaps[][MATRIX_ROWS][MATRIX_COLS] = {
    [_BASE] = LAYOUT(
            KC_Q,        KC_W,        KC_E,        KC_R,        KC_T,   ESC_MEDIA,        KC_0,        KC_Y,        KC_U,        KC_I,        KC_O,        KC_P,
            LHRG,        LHRA,        LHRC,        LHRS,        KC_G,    MO(_SYS), MO(_BUTTON),        KC_H,        RHRS,        RHRC,        RHRA,        RHRG,
            KC_Z,     KC_LEFT,        KC_C,        KC_V,        KC_B,   TAB_MOUSE,     ENT_SYM,        KC_N,        KC_M,     KC_COMM,      KC_DOT,      KC_ENT,
                        KC_UP,     KC_DOWN,   SPACE_NAV,    BSPC_NUM,                                DEL_FN,        KC_0,     KC_LEFT,    KC_RIGHT
    ),
    [_NAV] = LAYOUT(
         KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS,    REDO,   PASTE,    COPY,     CUT,    UNDO,
         KC_LGUI, KC_LALT, KC_LCTL, KC_LSFT, KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS, KC_LEFT, KC_DOWN,   KC_UP,KC_RIGHT,
         KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS,  KC_ENT,  KC_INS, KC_HOME, KC_PGDN, KC_PGUP,  KC_END,
                  KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS,                   KC_BSPC,  KC_DEL, KC_TRNS, KC_TRNS
    ),

    [_TEST] = LAYOUT(
        KC_A, KC_B, KC_C, KC_D, KC_E, KC_F, KC_G, KC_H, KC_I, KC_J, KC_K, KC_L,
        KC_M, KC_N, KC_O, KC_P, KC_Q, KC_R, KC_S, KC_T, KC_U, KC_V, KC_W, KC_X"KC_RSFT", "KC_RCTL", "KC_RALT", "KC_RGUI",
        KC_Y, KC_Z, KC_1, KC_2, KC_3, KC_4, KC_5, KC_6, KC_7, KC_8, KC_9, KC_0,
         KC_DOT, KC_COMM, KC_SLSH, KC_MINS,  KC_GRV, KC_BSLS, KC_QUOT, KC_ENT
    ),
    [_SYS] = LAYOUT(
        QK_BOOT, DB_TOGG, QK_RBT, KC_R, KC_T, KC_Y, KC_U, KC_I, KC_O, KC_P, KC_0, KC_0,
        KC_A, KC_S, KC_D, KC_F, KC_G, KC_H, KC_J, KC_K, KC_L, KC_QUOT, KC_QUOT, KC_X,
        KC_Y, KC_Z, KC_1, KC_2, KC_3, KC_4, KC_5, KC_6, KC_7, KC_8, KC_9, KC_0,
         KC_DOT, KC_COMM, KC_SLSH, KC_MINS,  KC_GRV, KC_BSLS, KC_QUOT, KC_ENT
    ),
};
void keyboard_post_init_user(void) {
  // Customise these values to desired behaviour
  debug_enable=true;
  debug_matrix=true;
  //debug_keyboard=true;
  //debug_mouse=true;
}
// void keyboard_post_
