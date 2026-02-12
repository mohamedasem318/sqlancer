#!/usr/bin/python3
# -*- coding: utf-8 -*-
# pylint: disable=R,W,E,C

"""

Author  : Nasir Khan (r0ot h3x49)
Github  : https://github.com/r0oth3x49
License : MIT


Copyright (c) 2016-2025 Nasir Khan (r0ot h3x49)

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the
Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software,
and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR
ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH 
THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

"""

from sqlancer.common.lib import os, init, Fore, Back, Style

is_nt = bool(os.name == "nt")
init(autoreset=True, convert=is_nt)

# Custom SQLancer color palette from ColorHunt (#005461, #0C7779, #249E94, #3BC1A8)
def rgb_color(r, g, b):
    """Generate ANSI RGB color code"""
    return f"\033[38;2;{r};{g};{b}m"

# SQLancer custom colors
sqlancer_dark_teal = rgb_color(0, 84, 97)      # #005461 - Darkest teal
sqlancer_medium_dark = rgb_color(12, 119, 121) # #0C7779 - Medium dark teal
sqlancer_medium = rgb_color(36, 158, 148)      # #249E94 - Medium teal
sqlancer_light = rgb_color(59, 193, 168)       # #3BC1A8 - Light teal/turquoise

# colors foreground text - mapped to SQLancer palette:
cyan = sqlancer_light            # Was: Fore.CYAN
green = sqlancer_medium          # Was: Fore.GREEN
white = Fore.WHITE               # Keep white for readability
red = Fore.RED                   # Keep red for errors/critical
blue = sqlancer_dark_teal        # Was: Fore.BLUE
yellow = sqlancer_light          # Was: Fore.YELLOW (now light teal for banner/warnings)
magenta = sqlancer_medium_dark   # Was: Fore.MAGENTA
black = Fore.BLACK

bright_cyan = sqlancer_light
bright_green = sqlancer_medium
bright_white = Fore.LIGHTWHITE_EX
bright_red = Fore.LIGHTRED_EX
bright_blue = sqlancer_dark_teal
bright_yellow = sqlancer_light
bright_magenta = sqlancer_medium_dark
bright_black = Fore.LIGHTBLACK_EX


# colors background text:
background_cyan = Back.CYAN
background_green = Back.GREEN
background_white = Back.WHITE
background_red = Back.RED
background_blue = Back.BLUE
background_yellow = Back.YELLOW
background_magenta = Back.MAGENTA
background_black = Back.BLACK
background_reset = Back.RESET

level_map = {
    "INFO": {
        "color": "green",
        "faint": False,
        "bold": False,
        "normal": True,
        "background": "",
    },
    "WARNING": {
        "color": "yellow",
        "faint": False,
        "bold": False,
        "normal": True,
        "background": "",
    },
    "ERROR": {
        "color": "red",
        "faint": False,
        "bold": True,
        "normal": False,
        "background": "",
    },
    "CRITICAL": {
        "color": "white",
        "faint": False,
        "bold": False,
        "normal": True,
        "background": "red",
    },
    "DEBUG": {
        "color": "blue",
        "faint": False,
        "bold": True,
        "normal": False,
        "background": "",
    },
    "SUCCESS": {
        "color": "white",
        "faint": True if is_nt else False,
        "bold": False,
        "normal": False,
        "background": "",
    },
    "NOTICE": {
        "color": "bright_black" if is_nt else "bright_white",
        "faint": False,
        "bold": True if is_nt else False,
        "normal": False,
        "background": "",
    },
    "PAYLOAD": {
        "color": "cyan",
        "faint": False,
        "bold": False,
        "normal": True,
        "background": "",
    },
    "START": {
        "color": "white",
        "faint": True,
        "bold": False,
        "normal": False,
        "background": "",
    },
    "END": {
        "color": "white",
        "faint": True,
        "bold": False,
        "normal": False,
        "background": "",
    },
    "TRAFFIC_IN": {
        "color": "bright_black",
        "faint": True,
        "bold": False,
        "normal": False,
        "background": "magenta",
    },
    "TRAFFIC_OUT": {
        "color": "magenta",
        "faint": True,
        "bold": False,
        "normal": False,
        "background": "",
    },
}

color_map = {
    "white": white,
    "black": black,
    "cyan": cyan,
    "green": green,
    "magenta": magenta,
    "blue": blue,
    "yellow": yellow,
    "red": red,
    "bright_cyan": bright_cyan,
    "bright_green": bright_green,
    "bright_white": bright_white,
    "bright_red": bright_red,
    "bright_blue": bright_blue,
    "bright_yellow": bright_yellow,
    "bright_magenta": bright_magenta,
    "bright_black": bright_black,
}
bgcolor_map = {
    "white": background_white,
    "black": background_black,
    "cyan": background_cyan,
    "green": background_green,
    "magenta": background_magenta,
    "blue": background_blue,
    "yellow": background_yellow,
    "red": background_red,
}


DIM = Style.DIM
BRIGHT = Style.BRIGHT
NORMAL = Style.NORMAL
RESET = Style.RESET_ALL
if is_nt:
    nc = f"{RESET}{bright_black}"
    mc = f"{RESET}{DIM}{white}"
else:
    nc = f"{RESET}{bright_white}"
    mc = f"{RESET}{DIM}{bright_white}"
bw = f"{RESET}{white}"


def colorize(
    string,
    color="white",
    background="",
    bold=False,
    faint=False,
    normal=False,
    reset=True,
):
    if bold:
        style = BRIGHT
    if faint:
        style = DIM
    if normal:
        style = NORMAL
    if not bold and not faint and not normal:
        style = NORMAL

    if color in color_map:
        color = color_map.get(color)
    if background in bgcolor_map:
        background = bgcolor_map.get(background)
        string = f"{background}{string}{RESET}"
    if reset:
        text = f"{color}{style}{string}{RESET}"
    else:
        text = f"{color}{style}{string}"
    return text
