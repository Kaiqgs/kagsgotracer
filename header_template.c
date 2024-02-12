// Copyright 2023 QMK    
// SPDX-License-Identifier: GPL-2.0-or-later
#include QMK_KEYBOARD_H

enum custom_layers {
    {%layers%}
};
enum custom_keycodes {
};

enum tapdance{
        TDSE,
};
//void keyboard_post_init_user(void) {
// Customise these values to desired behaviour
// debug_enable=true;
// debug_matrix=true;
// debug_keyboard=true;
// debug_mouse=true;
//}

bool process_record_user(uint16_t keycode, keyrecord_t *record) {
    switch (keycode) {
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

#define SPC_NUM LT({%symnum.enum%}, KC_SPC)
#define CALPAD LT({%nvim.enum%}, KC_ENT)
#define TAB_FN LT({%fn.enum%}, KC_TAB)
#define ENT_NAVI LT({%nvim.enum%}, KC_ENT)
#define ESC_NUM LT({%numpad.enum%}, KC_ESC)
#define DEL_NAVI LT({%mouse.enum%}, KC_DEL)
#define TO_QWERT TO({%qwerty.enum%})
#define TO_CDHM TO({%cdhm.enum%})
#define TO_GAME TO({%game.enum%})
#define MO_MEDIA MO({%media.enum%})
#define MO_SYS MO({%sys.enum%})
