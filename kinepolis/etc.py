# A bunch of cool functions

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


def rgb(rf,gf,bf,rb=0,gb=0,bb=0):
    # red front, ..., blue back
    return "\033[1;38;2;{};{};{};48;2;{};{};{}m".format(rf,gf,bf,rb,gb,bb)

def rgbtext(s, f=red, b=black):
    return rgb(f[0],f[1],f[2],b[0],b[1],b[2]) + s + endc


