import gspread
from typing import Self, Union
# import numpy as np

class Aliases:
    NONE = "_"
    TRANSPARENT = "T"
    INHERIT = "Inherit"


NONE = "KC_NO"
NONE_ALIAS = "_"
TRANSPARENT = "KC_TRNS"
TRANSPARENT_ALIAS = "T"
INHERIT_ALIAS = "Inherit"

def inherit(keys_a, keys_b):
    assert len(keys_a) == len(keys_b)
    for i in range(len(keys_a)):
        assert len(keys_a[i]) == len(keys_b[i])
        for j in range(len(keys_a[i])):
            if keys_a[i][j] == Aliases.INHERIT  and keys_b[i][j] != Aliases.INHERIT:
                keys_a[i][j] = keys_b[i][j]
    return keys_a

class Layout:
    def __init__(self, 
                 name, 
                 keys: list, 
                 priority=0, 
                 inherits: str="", 
                 abstract = False
                 ):
        self.name = name
        self.keys = keys
        self.priority = priority
        self.inherits = inherits
        self.abstract = abstract

    @property
    def enum(self):
        return f"_{self.name.upper()}"

    def register(self, inherited: Union[Self, None] = None):
        if inherited:
            self.keys = inherit(self.keys, inherited.keys)

    def __str__(self) -> str:
        return f"Layout({self.name}, {self.keys}, {self.priority}, {self.inherits})"
    def __repr__(self) -> str:
        return self.__str__()

def read_worksheet_layout(worksheet:gspread.Worksheet) -> Layout:
    values = worksheet.get_all_values("A1:M5")
    header = values[0]
    inherits = header[0] or ""
    abstract = header[1] or False
    keys =  values[1:5]
    keys = [k[:6] + k[7:] for k in keys]


    # print(keys)
    layout = Layout(name=worksheet.title,
                    keys=keys, 
                    priority=worksheet.index,
                    inherits=inherits,
                    abstract=abstract)
    return layout

def render_file(layouts):
    global output
    output = ""
    def format(name, keys, extra=3):
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

    with open("header_template.c", "r") as f:
        header = f.read()


    layout_names = []
    formatted_header = header
    for layout in sorted(layouts.values(), key=lambda x: x.priority):
        if layout.abstract:
            continue
        format(layout.enum, layout.keys, 3)
        # TODO: make it automatic from objects Layout
        layout_names.append(layout.enum)
        replace_word = f"{{%{layout.name}.enum%}}"
        formatted_header = formatted_header.replace(replace_word, layout.enum)
        print(replace_word)

# WRITE TO FILE
    print(layout_names)
    layers_list = ",\n\t".join(layout_names)
    formatted_header = formatted_header.replace("{%layers%}", layers_list)

    print(formatted_header)
    end = f"""{formatted_header}\nconst uint16_t PROGMEM keymaps[][MATRIX_ROWS][MATRIX_COLS] = {{{output}\n}};"""
    with open("keymaps/default/keymap.c", "w+") as f:
        f.write(end)
    print(f"Transpiled {len(layouts)} layers.")

def main():
    gc = gspread.service_account()
    sh = gc.open("ktracergosheets")
    worksheets = sh.worksheets()
    valid_worksheets = [w for w in worksheets if not w.title.startswith("_")]
    layouts = {}
    layout:Layout
    for worksheet in valid_worksheets:
        layout = read_worksheet_layout(worksheet)
        layouts[layout.name] = layout

    for _, layout in layouts.items():
        layout.register(layouts[layout.inherits] if layout.inherits else None)
    # print(layouts)
    render_file(layouts)
    return layouts


main()
