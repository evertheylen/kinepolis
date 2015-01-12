# A bunch of cool functions

import hashlib

# --- TEXT STUFF ---------------------

endc = '\033[0m'  # Resets all ANSI attributes

red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

cyan = (0, 255, 255)
pink = (255, 0, 255)
yellow = (255, 255, 0)

black = (0, 0, 0)
white = (255, 255, 255)


def _rgb(rf,gf,bf,rb=0,gb=0,bb=0):
    # red front, ..., blue back
    return "\033[1;38;2;{};{};{};48;2;{};{};{}m".format(rf,gf,bf,rb,gb,bb)


def rgb(f, b=black):
    return _rgb(f[0], f[1], f[2], b[0], b[1], b[2])


def rgbtext(s, f=red, b=black):
    return rgb(f,b) + s + endc


font = {'d': '      _ \n     | |\n   __| |\n  / _` |\n | (_| |\n  \\__,_|\n        \n        \n',
        'X': ' __   __\n \\ \\ / /\n  \\ V / \n   > <  \n  / . \\ \n /_/ \\_\\\n        \n        \n',
        'W': ' __          __\n \\ \\        / /\n  \\ \\  /\\  / / \n   \\ \\/  \\/ /  \n    \\  /\\  /   \n     \\/  \\/    \n               \n               \n',
        'Q': '   ____  \n  / __ \\ \n | |  | |\n | |  | |\n | |__| |\n  \\___\\_\\\n         \n         \n',
        'g': '        \n        \n   __ _ \n  / _` |\n | (_| |\n  \\__, |\n   __/ |\n  |___/ \n',
        'y': '        \n        \n  _   _ \n | | | |\n | |_| |\n  \\__, |\n   __/ |\n  |___/ \n',
        'e': '       \n       \n   ___ \n  / _ \\\n |  __/\n  \\___|\n       \n       \n',
        'O': '   ____  \n  / __ \\ \n | |  | |\n | |  | |\n | |__| |\n  \\____/ \n         \n         \n',
        'f': '   __ \n  / _|\n | |_ \n |  _|\n | |  \n |_|  \n      \n      \n',
        'H': '  _    _ \n | |  | |\n | |__| |\n |  __  |\n | |  | |\n |_|  |_|\n         \n         \n',
        'h': "  _     \n | |    \n | |__  \n | '_ \\ \n | | | |\n |_| |_|\n        \n        \n",
        'J': '       _ \n      | |\n      | |\n  _   | |\n | |__| |\n  \\____/ \n         \n         \n',
        'U': '  _    _ \n | |  | |\n | |  | |\n | |  | |\n | |__| |\n  \\____/ \n         \n         \n',
        'M': '  __  __ \n |  \\/  |\n | \\  / |\n | |\\/| |\n | |  | |\n |_|  |_|\n         \n         \n',
        'k': '  _    \n | |   \n | | __\n | |/ /\n |   < \n |_|\\_\\\n       \n       \n',
        's': '      \n      \n  ___ \n / __|\n \\__ \\\n |___/\n      \n      \n',
        'a': '        \n        \n   __ _ \n  / _` |\n | (_| |\n  \\__,_|\n        \n        \n',
        'b': "  _     \n | |    \n | |__  \n | '_ \\ \n | |_) |\n |_.__/ \n        \n        \n",
        'j': '    _ \n   (_)\n    _ \n   | |\n   | |\n   | |\n  _/ |\n |__/ \n',
        't': '  _   \n | |  \n | |_ \n | __|\n | |_ \n  \\__|\n      \n      \n',
        'I': '  _____ \n |_   _|\n   | |  \n   | |  \n  _| |_ \n |_____|\n        \n        \n',
        'p': "        \n        \n  _ __  \n | '_ \\ \n | |_) |\n | .__/ \n | |    \n |_|    \n",
        'c': '       \n       \n   ___ \n  / __|\n | (__ \n  \\___|\n       \n       \n',
        'L': '  _      \n | |     \n | |     \n | |     \n | |____ \n |______|\n         \n         \n',
        'A': '          \n    /\\    \n   /  \\   \n  / /\\ \\  \n / ____ \\ \n/_/    \\_\\\n          \n          \n',
        'o': '        \n        \n   ___  \n  / _ \\ \n | (_) |\n  \\___/ \n        \n        \n',
        'r': "       \n       \n  _ __ \n | '__|\n | |   \n |_|   \n       \n       \n",
        'B': '  ____  \n |  _ \\ \n | |_) |\n |  _ < \n | |_) |\n |____/ \n        \n        \n',
        'T': '  _______ \n |__   __|\n    | |   \n    | |   \n    | |   \n    |_|   \n          \n          \n',
        'x': '       \n       \n __  __\n \\ \\/ /\n  >  < \n /_/\\_\\\n       \n       \n',
        'n': "        \n        \n  _ __  \n | '_ \\ \n | | | |\n |_| |_|\n        \n        \n",
        'D': '  _____  \n |  __ \\ \n | |  | |\n | |  | |\n | |__| |\n |_____/ \n         \n         \n',
        'V': ' __      __\n \\ \\    / /\n  \\ \\  / / \n   \\ \\/ /  \n    \\  /   \n     \\/    \n           \n           \n',
        'z': '      \n      \n  ____\n |_  /\n  / / \n /___|\n      \n      \n',
        'Y': ' __     __\n \\ \\   / /\n  \\ \\_/ / \n   \\   /  \n    | |   \n    |_|   \n          \n          \n',
        'w': '           \n           \n __      __\n \\ \\ /\\ / /\n  \\ V  V / \n   \\_/\\_/  \n           \n           \n',
        'F': '  ______ \n |  ____|\n | |__   \n |  __|  \n | |     \n |_|     \n         \n         \n',
        'K': "  _  __\n | |/ /\n | ' / \n |  <  \n | . \\ \n |_|\\_\\\n       \n       \n",
        'N': '  _   _ \n | \\ | |\n |  \\| |\n | . ` |\n | |\\  |\n |_| \\_|\n        \n        \n',
        'S': '   _____ \n  / ____|\n | (___  \n  \\___ \\ \n  ____) |\n |_____/ \n         \n         \n',
        'm': "            \n            \n  _ __ ___  \n | '_ ` _ \\ \n | | | | | |\n |_| |_| |_|\n            \n            \n",
        'v': '        \n        \n __   __\n \\ \\ / /\n  \\ V / \n   \\_/  \n        \n        \n',
        'R': '  _____  \n |  __ \\ \n | |__) |\n |  _  / \n | | \\ \\ \n |_|  \\_\\\n         \n         \n',
        'G': '   _____ \n  / ____|\n | |  __ \n | | |_ |\n | |__| |\n  \\_____|\n         \n         \n',
        'i': '  _ \n (_)\n  _ \n | |\n | |\n |_|\n    \n    \n',
        'E': '  ______ \n |  ____|\n | |__   \n |  __|  \n | |____ \n |______|\n         \n         \n',
        'C': '   _____ \n  / ____|\n | |     \n | |     \n | |____ \n  \\_____|\n         \n         \n',
        'Z': '  ______\n |___  /\n    / / \n   / /  \n  / /__ \n /_____|\n        \n        \n',
        'P': '  _____  \n |  __ \\ \n | |__) |\n |  ___/ \n | |     \n |_|     \n         \n         \n',
        'q': '        \n        \n   __ _ \n  / _` |\n | (_| |\n  \\__, |\n     | |\n     |_|\n',
        'l': '  _ \n | |\n | |\n | |\n | |\n |_|\n    \n    \n',
        'u': '        \n        \n  _   _ \n | | | |\n | |_| |\n  \\__,_|\n        \n        \n'}

def fancytext(s):
    # will return the string in a fancy big ascii art like text
    result = len(font['A'].split("\n"))*[""]
    for char in s:
        if char in font:
            i = 0
            for line in font[char].split("\n"):
                result[i] += line
                i += 1
    
    result_string = ""
    for line in result:
        result_string += line + '\n'
    
    return result_string

        
# --- HASHING ---------------------

# because this has nothing to do with the workings of
# the hashmap itself, we have put this function here
# and not in hashmap.py

def simple_hash(s):
    return int(hashlib.md5(s.encode('utf-8')).hexdigest(), 16)
