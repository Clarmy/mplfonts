import os
import shutil

import matplotlib
import fire
from mplfonts.util.manage import (
    install_fonts,
    install_font,
    update_custom_rc,
    list_font,
)
from mplfonts.conf import FONT_DIR


def init():
    """To set default cjk fonts and put into use"""
    install_fonts()
    update_custom_rc()
    shutil.rmtree(matplotlib.get_cachedir())


def install(path=None, update=True):
    """
    To install font

    Args:
        path (str): The font file path or directory path
    """
    if not path:
        path = FONT_DIR
    if os.path.isdir(path):
        install_fonts(path)
    elif os.path.isfile(path):
        install_font(path)

    if update:
        updaterc()


def updaterc(rcfp=None):
    """
    To update matplotlibrc by custom file

    Args:
        rcfp (str): The custom matplotlibrc
    """
    update_custom_rc(rcfp)


def cli():
    fire.Fire(
        {"init": init, "install": install, "updaterc": updaterc, "list": list_font}
    )
