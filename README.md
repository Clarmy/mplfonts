[中文文档](./docs/README_zh.md)

[![Python package](https://github.com/Clarmy/mplfonts/actions/workflows/python-package.yml/badge.svg)](https://github.com/Clarmy/mplfonts/actions/workflows/python-package.yml)
[![PyPI version](https://badge.fury.io/py/mplfonts.svg)](https://badge.fury.io/py/mplfonts)
[![contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/Clarmy/mplfonts/issues)


# mplfonts
The mplfonts is a Python package and command-line tool that allows you to manage your Matplotlib fonts. It provides an easy solution to the "tofu" problem that arises when plotting with CJK (Chinese, Japanese, Korean) languages.

## Installation
You can use `pip` to install mplfonts.
```bash
$ pip install mplfonts
```

## Quickstart
You can easily solve the "tofu" problem with a single command:
```bash
$ mplfonts init
```
After that, try using Matplotlib to plot an image with CJK text; it should display normally. 

Now you can enjoy it.

## Usage
This package not only solves the "tofu" problem, but also provides a convenient way to manage Matplotlib fonts. When you install mplfonts, it comes with several open-source CJK fonts, including:
* Noto Sans Mono CJK SC
* Noto Serif CJK SC
* Noto Sans CJK SC
* Source Han Serif SC
* Source Han Mono SC

Once you have finished the initialization step, you can use the following code in your script to switch fonts:

```python
from mplfonts import use_font

use_font('Noto Serif CJK SC')

# write your plotting code below
```

If you want to set up custom fonts, you can install them with the following command:
```bash
$ mplfonts install --update <your font file path>
```
Furthermore, you can install all the fonts in a directory by running the following command:
```bash
$ mplfonts install --update <your directory path>
```

Unsure of which fonts are available? No problem, simply use the command `mplfonts list` to see a list of all available fonts.
```bash
$ mplfonts list
DejaVu Sans Display:
/Users/clarmylee/Miniconda3/envs/mplfonts/lib/python3.6/site-packages/matplotlib-3.3.4-py3.6-macosx-10.9-x86_64.egg/matplotlib/mpl-data/fonts/ttf/DejaVuSansDisplay.ttf
---------------
DejaVu Sans:
/Users/clarmylee/Miniconda3/envs/mplfonts/lib/python3.6/site-packages/matplotlib-3.3.4-py3.6-macosx-10.9-x86_64.egg/matplotlib/mpl-data/fonts/ttf/DejaVuSans-BoldOblique.ttf
---------------
Source Han Mono SC:
/Users/clarmylee/Miniconda3/envs/mplfonts/lib/python3.6/site-packages/matplotlib-3.3.4-py3.6-macosx-10.9-x86_64.egg/matplotlib/mpl-data/fonts/ttf/SourceHanMonoSC-Regular.otf

...
```
This command will show the names and source files of the fonts, which can then be passed as arguments to the `use_font` function.

By default, running `mplfonts init` will generate a new `matplotlibrc` file to replace your current one. This new file will contain cache configuration settings that support CJK rendering. Here is the content of the new `matplotlibrc` file:
```
font.family:  sans-serif
font.sans-serif: Noto Sans CJK SC Regular, 思源等宽, Noto Serif CJK SC, 思源宋体, Noto Sans Mono CJK SC Regularsans-serif
axes.unicode_minus: False
```
By default, `Noto Sans CJK SC Regular` is the preferred font. If you install custom fonts from another source and want them to have first priority, add them to the leftmost end of the `font.sans-serif` list. Then, run `$ mplfonts updaterc <your matplotlibrc path>` to set it as your global cache configuration.

## Fonts Source
You can access some open-source fonts from Google and Adobe. Here are some resources:
* https://github.com/adobe-fonts
* https://fonts.google.com
* https://github.com/googlefonts
