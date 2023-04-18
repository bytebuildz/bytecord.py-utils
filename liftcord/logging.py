import sys

# Define color codes
RESET = "\033[0m"
BOLD = "\033[1m"
FAINT = "\033[2m"
ITALIC = "\033[3m"
RED = "\033[31m"
GREEN = "\033[32m"
BLUE = "\033[34m"
YELLOW = "\033[33m"
UNDERLINE = "\033[4m"
REVERSE = "\033[7m"
STRIKETHROUGH = "\033[9m"
PURPLE_START = "\033[38;5;57m"
PURPLE_END = "\033[38;5;165m"

# Define gradient function
def gradient(text):
    gradient_text = ""
    color_step = (165 - 57) / (len(text) - 1)
    for i, char in enumerate(text):
        color_code = int(57 + (i * color_step))
        gradient_text += f"\033[38;5;{color_code}m{char}"
    return gradient_text + RESET

# Define logging function
def log(message, level="INFO"):
    level = level.upper()
    if level == "DEBUG":
        color_code = BLUE
    elif level == "INFO":
        color_code = GREEN
    elif level == "WARNING":
        color_code = YELLOW
    elif level == "ERROR":
        color_code = RED
    elif level == "CRITICAL":
        color_code = PURPLE_START
    else:
        color_code = RESET
    prefix = f"{BOLD}{color_code}[{level}]{RESET} "
    print(prefix + gradient(message))

# Test the logging function
log("This is an example debug message", "debug")
log("This is an example info message", "info")
log("This is an example warning message", "warning")
log("This is an example error message", "error")
log("This is an example critical message", "critical")
