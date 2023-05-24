import os
import shutil
from glob import glob

import matplotlib
import matplotlib.font_manager
from fontmeta import FontMeta

from mplfonts.conf import FONT_DIR, RC_DIR

MPL_FONT_PATH = os.path.join(matplotlib.get_data_path(), "fonts/ttf")


def use_font(font="Noto Sans CJK SC"):
    """To choose the font that you want to use

    Args:
        font (str, optional): The font name that you want to use.
                              Defaults to 'Noto Sans CJK SC'.
    """
    matplotlib.rcParams["font.family"] = "sans-serif"
    matplotlib.rcParams["font.sans-serif"] = [font, "sans-serif"]
    matplotlib.rcParams["axes.unicode_minus"] = False


def update_custom_rc(custom_rc=None):
    """To update matplotlibrc by custom one

    Args:
        custom_rc (str, optional): The file path of matplotlibrc.
                                   Defaults to None.
    """
    install_fonts()
    if not custom_rc:
        custom_rc = os.path.join(RC_DIR, "matplotlibrc")
    cache_rc_fp = os.path.join(matplotlib.get_cachedir(), "matplotlibrc")
    if os.path.exists(cache_rc_fp):
        backup_fp = cache_rc_fp + ".backup"
        if os.path.exists(backup_fp):
            os.remove(cache_rc_fp)
            print(
                f"Warning: The {matplotlib.matplotlib_fname()} "
                f"already exists, renamed it to {backup_fp}"
            )

    shutil.copy(custom_rc, cache_rc_fp)


def reset_rc():
    """To reset your matplotlibrc"""
    cache_rc_fp = os.path.join(matplotlib.get_cachedir(), "matplotlibrc")
    backup_rc_fp = cache_rc_fp + ".backup"
    if os.path.exists(backup_rc_fp):
        if os.path.exists(cache_rc_fp):
            os.remove(cache_rc_fp)
            os.rename(backup_rc_fp, cache_rc_fp)
    else:
        print("Sorry, no backup rc file to reset.")


def get_font_name(font_fp):
    """Get font's name

    Args:
        font_fp (str): The font file path

    Returns:
        str: font name
    """
    meta_instance = FontMeta(font_fp)
    return meta_instance.get_data()["full_font_name"]


def update_rc_font_list(font_names, rcfp=None):
    if not rcfp:
        rcfp = os.path.join(RC_DIR, "matplotlibrc")

    with open(rcfp, encoding="utf-8", errors="ignore") as f:
        content = f.readlines()

    font_list_text = "font.sans-serif: " + ", ".join(font_names) + "sans-serif\n"
    for n, line in enumerate(content):
        if line.startswith("font.sans-serif"):
            break

    content[n] = font_list_text

    with open(rcfp, "w", encoding="utf-8") as f:
        f.write("".join(content))


def install_fonts(font_dir=None):
    """To install all fonts in a specific directory

    Args:
        font_dir (str, optional): The directory that storing font files.
                                  Defaults to None.
    """
    if not font_dir:
        font_dir = FONT_DIR
    font_fps = glob(os.path.join(font_dir, "*.[ot]tf"))
    font_names = []
    for src_font_fp in font_fps:
        mpl_font_fp = os.path.join(MPL_FONT_PATH, os.path.basename(src_font_fp))
        if not os.path.exists(mpl_font_fp):
            shutil.copy(src_font_fp, mpl_font_fp)
            matplotlib.font_manager.fontManager.addfont(mpl_font_fp)
        font_names.append(get_font_name(mpl_font_fp))

    update_rc_font_list(font_names)


def install_font(font_fp):
    """To install one font by specific font file(otf)

    Args:
        font_fp (str): The font file's path.
    """
    mpl_font_fp = os.path.join(MPL_FONT_PATH, os.path.basename(font_fp))
    if not os.path.exists(mpl_font_fp):
        shutil.copy(font_fp, mpl_font_fp)
        matplotlib.font_manager.fontManager.addfont(mpl_font_fp)


def list_font() -> list:
    """To list font names for choosing

    Returns:
        list: Font names
    """
    result = []
    for font in matplotlib.font_manager.fontManager.ttflist:
        print(f"{font.name}:\n{font.fname}\n---------------")

    return result


if __name__ == "__main__":
    pass
