import os
import platform
from pathlib import Path

BASE_DIR = os.path.dirname(__file__)

FONT_DIR = os.path.join(BASE_DIR, "fonts")
if platform.system() == "Linux":
    # Linux平台下，matplotlibrc文件的默认路径为~/.config/matplotlib/matplotlibrc
    RC_DIR = str(Path('~/.config/matplotlib').expanduser().resolve())
else:
    RC_DIR = os.path.join(BASE_DIR, "rc")
