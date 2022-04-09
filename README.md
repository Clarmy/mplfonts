[中文文档](./docs/README_zh.md)

[![Python package](https://github.com/Clarmy/mplfonts/actions/workflows/python-package.yml/badge.svg)](https://github.com/Clarmy/mplfonts/actions/workflows/python-package.yml)
[![PyPI version](https://badge.fury.io/py/mplfonts.svg)](https://badge.fury.io/py/mplfonts)
[![contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/Clarmy/mplfonts/issues)


# mplfonts
Fonts manager for matplotlib

This is a python package and command line tool to manage your matplotlib fonts. You can easily resolve the "tofu" problem when plotting with CJK(Chinese, Japanese, Korean) languages.

## Installation
You can install mplfonts with `pip`
```bash
$ pip install mplfonts
```

## Quickstart
You can just run one command to solve the "tofu" problem:
```bash
$ mplfonts init
```
After that, try to use matplotlib to plot an image with CJK text, it should be normal.

Now you can enjoy it.

## Usage
This package's aim is not only to solve "tofu" problem, but also to manage matplotlib fonts. When you installed mplfonts, there are some open-source CJK fonts already included, they are:
* Noto Sans Mono CJK SC
* Noto Serif CJK SC
* Noto Sans CJK SC
* Source Han Serif SC
* Source Han Mono SC
If you have finished the `init`, You can shift fonts in you script like:
```python
from mplfonts import use_font

use_font('Noto Serif CJK SC')

# write your plotting code below
```

If you want to setup some custom fonts, you can install by command:
```bash
$ mplfonts install --update <your font file path>
```
Also, you can install all fonts in a directory(folder) by:
```bash
$ mplfonts install --update <your directory path>
```

Don't know what fonts is available? Don't worry, you can use `mplfonts list` to list all available fonts.
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
It will show fonts' name and source file, and these names can be argument to pass to  `use_font` function

By default, `mplfonts init` will generate a `matplotlibrc` as the cache configuration, supporting CJK render, to replace your old one, the content of `matplotlibrc` is:
```
font.family:  sans-serif
font.sans-serif: Noto Sans CJK SC Regular, 思源等宽, Noto Serif CJK SC, 思源宋体, Noto Sans Mono CJK SC Regularsans-serif
axes.unicode_minus: False
```
It will preferentially use `Noto Sans CJK SC Regular` as the default font. If you install custom fonts from other source, and want it to be the first priority, you should add it to the leftmost end of `font.sans-serif` list, and then run `$ mplfonts updaterc <your matploblibrc path>` to set it as your global cache rc.

## Fonts Source
You can access some open-source fonts from google and adobe, here is some resource:
* https://github.com/adobe-fonts
* https://fonts.google.com
* https://github.com/googlefonts