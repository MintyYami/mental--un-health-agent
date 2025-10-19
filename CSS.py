CSI = "\x1b["
RESET = CSI + "0m"
BOLD = CSI + "1m"
DIM = CSI + "2m"
FG = {
    'red': CSI + '31m',
    'green': CSI + '32m',
    'yellow': CSI + '33m',
    'blue': CSI + '34m',
    'magenta': CSI + '35m',
    'cyan': CSI + '36m',
    'white': CSI + '37m',
}
def color(text, c): return f"{FG.get(c,'')}{text}{RESET}"
def bold(text): return f"{BOLD}{text}{RESET}"