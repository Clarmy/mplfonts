[中文文档](./README_zh.md)

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
$ mplfonts quickstart
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
If you have finished the `quickstart`, You can shift fonts in you script like:
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

## Fonts Source
You can access some open-source fonts from google and adobe, here is some resource:
* https://github.com/adobe-fonts
* https://fonts.google.com
* https://github.com/googlefonts