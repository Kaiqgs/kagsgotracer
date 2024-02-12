// Copyright 2023 QMK    
// SPDX-License-Identifier: GPL-2.0-or-later
#include QMK_KEYBOARD_H

enum custom_layers {
    _CDHM,
	_QWERTY,
	_GAME,
	_NVIM,
	_SYMNUM,
	_MOUSE,
	_MEDIA,
	_NUMPAD,
	_FN,
	_SYS
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

#define SPC_NUM LT(_SYMNUM, KC_SPC)
#define CALPAD LT(_NVIM, KC_ENT)
#define TAB_FN LT(_FN, KC_TAB)
#define ENT_NAVI LT(_NVIM, KC_ENT)
#define ESC_NUM LT(_NUMPAD, KC_ESC)
#define DEL_NAVI LT(_MOUSE, KC_DEL)
#define TO_QWERT TO(_QWERTY)
#define TO_CDHM TO(_CDHM)
#define TO_GAME TO(_GAME)
#define MO_MEDIA MO(_MEDIA)
#define MO_SYS MO(_SYS)

const uint16_t PROGMEM keymaps[][MATRIX_ROWS][MATRIX_COLS] = {
	[_CDHM] = LAYOUT(
		        KC_Q,        KC_W,        KC_F,        KC_P,        KC_B,     ESC_NAV,    DEL_NAVI,        KC_J,        KC_L,        KC_U,        KC_Y,     KC_SCLN,
		       CLHRG,       CLHRA,       CLHRC,       CLHRS,        KC_G,   TAB_MOUSE,    MO_MEDIA,        KC_M,       CRHRS,       CRHRC,       CRHRA,       CRHRG,
		        KC_Z,        KC_X,        KC_C,        KC_D,        KC_V,      CALPAD,      MO_SYS,        KC_K,        KC_H,     KC_COMM,      KC_DOT,       KC_NO,
		                  KC_DOWN,       KC_UP,      KC_SPC,     SPC_NUM,                               KC_BSPC,    ENT_NAVI,     KC_LEFT,    KC_RIGHT
	),
	[_QWERTY] = LAYOUT(
		        KC_Q,        KC_W,        KC_E,        KC_R,        KC_T,     ESC_NAV,    DEL_NAVI,        KC_Y,        KC_U,        KC_I,        KC_O,        KC_P,
		        LHRG,        LHRA,        LHRC,        LHRS,        KC_G,   TAB_MOUSE,    MO_MEDIA,        KC_H,        RHRS,        RHRC,        RHRA,        RHRG,
		        KC_Z,        KC_X,        KC_C,        KC_V,        KC_B,      CALPAD,      MO_SYS,        KC_N,        KC_M,     KC_COMM,      KC_DOT,    TD(TDSE),
		                  KC_DOWN,       KC_UP,      KC_SPC,     SPC_NUM,                               KC_BSPC,    ENT_NAVI,     KC_LEFT,    KC_RIGHT
	),
	[_GAME] = LAYOUT(
		     KC_ESC,       KC_1,       KC_2,       KC_3,       KC_4,    ESC_NAV,   DEL_NAVI,       KC_Y,       KC_U,       KC_I,       KC_O,       KC_P,
		    KC_LSFT,       KC_Q,       KC_W,       KC_E,       KC_R,  TAB_MOUSE,   MO_MEDIA,       KC_H,       RHRS,       RHRC,       RHRA,       RHRG,
		    KC_LCTL,       KC_A,       KC_S,       KC_D,       KC_F,     CALPAD,     MO_SYS,       KC_N,       KC_M,    KC_COMM,     KC_DOT,   TD(TDSE),
		                KC_DOWN,      KC_UP,     KC_SPC,     KC_SPC,                            KC_BSPC,   ENT_NAVI,    KC_LEFT,   KC_RIGHT
	),
	[_NVIM] = LAYOUT(
		   KC_1,   KC_2,   KC_3,   KC_4,   KC_5,  KC_NO,  KC_NO,   KC_6,   KC_7,   KC_8,   KC_9,   KC_0,
		  KC_NO,  KC_NO,  KC_NO,  KC_NO,  KC_NO,  KC_NO,  KC_NO,  KC_NO,   KC_H,   KC_J,   KC_K,   KC_L,
		  KC_NO,  KC_NO,  KC_NO,  KC_NO,  KC_NO,  KC_NO,  KC_NO,  KC_NO,  KC_NO,  KC_NO,  KC_NO,  KC_NO,
		          KC_NO,  KC_NO,  KC_NO,  KC_NO,                  KC_NO,  KC_NO,  KC_NO,  KC_NO
	),
	[_SYMNUM] = LAYOUT(
		       KC_1,       KC_2,       KC_3,       KC_4,       KC_5,     KC_DQT,     KC_GRV,       KC_6,       KC_7,       KC_8,       KC_9,       KC_0,
		    KC_MINS,     KC_EQL,    KC_LPRN,    KC_RPRN,    KC_UNDS,   KC_QUOTE,   KC_QUOTE,    KC_ASTR,    KC_RSFT,    KC_RCTL,    KC_RALT,    KC_RGUI,
		    KC_PLUS,    KC_HASH,    KC_LCBR,    KC_RCBR,    KC_PERC,     KC_GRV,     KC_GRV,      KC_AT,    KC_LBRC,    KC_RBRC,    KC_AMPR,    KC_BSLS,
		                KC_CIRC,     KC_DLR,      KC_NO,      KC_NO,                           KC_QUOTE,     KC_DQT,    KC_EXLM,    KC_TILD
	),
	[_MOUSE] = LAYOUT(
		     KC_NO,     KC_NO,     KC_NO,     KC_NO,     KC_NO,     KC_NO,   KC_ACL2,   KC_AGIN,  KC_PASTE,   KC_COPY,    KC_CUT,   KC_UNDO,
		   KC_LGUI,   KC_LALT,   KC_LCTL,   KC_LSFT,     KC_NO,   KC_ACL0,     KC_NO,     KC_NO,   KC_MS_L,   KC_MS_D,   KC_MS_U,   KC_MS_R,
		     KC_NO,     KC_NO,     KC_NO,     KC_NO,     KC_NO,     KC_NO,   KC_BTN1,     KC_NO,   KC_WH_L,   KC_WH_D,   KC_WH_U,   KC_WH_R,
		                KC_NO,     KC_NO,     KC_NO,     KC_NO,                         KC_BTN3,   KC_BTN2,     KC_NO,     KC_NO
	),
	[_MEDIA] = LAYOUT(
		     KC_NO,     KC_NO,     KC_NO,     KC_NO,     KC_NO,     KC_NO,     KC_NO,     KC_NO,     KC_NO,     KC_NO,     KC_NO,     KC_NO,
		   KC_LSFT,   KC_LCTL,   KC_LALT,   KC_LGUI,     KC_NO,     KC_NO,     KC_NO,     KC_NO,   KC_MPRV,   KC_VOLD,   KC_VOLU,   KC_MNXT,
		     KC_NO,     KC_NO,     KC_NO,     KC_NO,     KC_NO,     KC_NO,   KC_MSTP,     KC_NO,     KC_NO,     KC_NO,     KC_NO,     KC_NO,
		                KC_NO,     KC_NO,     KC_NO,     KC_NO,                         KC_MPLY,   KC_MUTE,     KC_NO,     KC_NO
	),
	[_NUMPAD] = LAYOUT(
		     KC_NO,     KC_NO,     KC_NO,     KC_NO,     KC_NO,     KC_NO,     KC_NO,   KC_LBRC,      KC_7,      KC_8,      KC_9,   KC_PPLS,
		   KC_LSFT,   KC_LCTL,   KC_LALT,   KC_LGUI,     KC_NO,     KC_NO,     KC_NO,   KC_SCLN,      KC_4,      KC_5,      KC_6,   KC_PCMM,
		     KC_NO,     KC_NO,     KC_NO,     KC_NO,     KC_NO,     KC_NO,    KC_DOT,   KC_PENT,      KC_1,      KC_2,      KC_3,   KC_PEQL,
		                KC_NO,     KC_NO,     KC_NO,     KC_NO,                            KC_0,   KC_MINS,      KC_0,   KC_PDOT
	),
	[_FN] = LAYOUT(
		        KC_F1,        KC_F2,        KC_F3,        KC_F4,        KC_F5,        KC_NO,        KC_NO,        KC_F6,        KC_F7,        KC_F8,        KC_F9,       KC_F10,
		      CW_TOGG,      KC_PSCR,   LCTL(KC_S),   LCTL(KC_N),       KC_NUM,        KC_NO,        KC_NO,        KC_NO,      KC_RSFT,      KC_RCTL,      KC_RALT,      KC_RGUI,
		      KC_HOME,      KC_PGUP,      KC_PGDN,       KC_END,      KC_CAPS,        KC_NO,        KC_NO,        KC_NO,        KC_NO,        KC_NO,        KC_NO,        KC_NO,
		                     KC_F11,        KC_NO,        KC_NO,        KC_NO,                                    KC_NO,        KC_NO,        KC_NO,       KC_F12
	),
	[_SYS] = LAYOUT(
		   QK_BOOT,   DB_TOGG,    QK_RBT,     KC_NO,     KC_NO,     KC_NO,     KC_NO,   KC_SLEP,   KC_WAKE,     KC_NO,     KC_NO,    KC_PWR,
		     KC_NO,     KC_NO,     KC_NO,     KC_NO,     KC_NO,     KC_NO,     KC_NO,     KC_NO,     KC_NO,     KC_NO,     KC_NO,     KC_NO,
		  TO_QWERT,     KC_NO,   TO_CDHM,   TO_GAME,     KC_NO,     KC_NO,     KC_NO,     KC_NO,     KC_NO,     KC_NO,     KC_NO,     KC_NO,
		                KC_NO,     KC_NO,     KC_NO,     KC_NO,                           KC_NO,     KC_NO,     KC_NO,     KC_NO
	),
};
