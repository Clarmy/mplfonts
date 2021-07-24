[English Documentation](./README_en.md)

[![Build Status](https://api.travis-ci.com/Clarmy/mplfonts.svg?branch=main)](https://travis-ci.com/github/Clarmy/mplfonts)
[![PyPI version](https://badge.fury.io/py/mplfonts.svg)](https://badge.fury.io/py/mplfonts)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/Clarmy/mplfonts/issues)

# mplfonts
matplotlib 字体管理工具

这是一个用于管理你的matplotlib字体的python模块包/命令行工具。它可以帮助你快速解决matplotlib渲染亚洲字体时出现“豆腐块”的问题。

## 安装
你可以使用`pip`来安装
```bash
$ pip install mplfonts
```

## 快速设置
安装完成之后，你只需要执行一条简单的命令就可以快速解决亚洲字体渲染出现“豆腐块”的问题：
```bash
$ mplfonts quickstart
```
执行完之后，试试在matplotlib的程序中渲染亚洲字体，结果应该会正常显示了。

请享用。

## 使用
其实该模块包的目标不仅仅是解决“豆腐块”这么简单的问题而已，它将致力于管理matploblib的字体库，在你安装mplfonts时，一些开源的字体就已经一起下载了，它们是：
* Noto Sans Mono CJK SC：Noto等宽黑体
* Noto Serif CJK SC：Noto宋体
* Noto Sans CJK SC：Noto黑体
* Source Han Serif SC：思源宋体
* Source Han Mono SC：思源等宽宋体
当你完成了上述的`mplfonts quickstart`命令以后，你就可以在程序中指定你想要的使用的字体
```python
from mplfonts import use_font

use_font('Noto Serif CJK SC')

# 编写你的绘图程序
```

如果你想要安装自定义的字体，可以执行命令：
```bash
$ mplfonts install --update <your font file path>
```
此外，你还可以直接对存有字体文件的字体目录（文件夹）进行安装：
```bash
$ mplfonts install --update <your directory path>
```

不知道有哪些可用的字体？不用担心，你可以使用`mplfonts list`命令将当前可用的字体罗列出来
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
它显示的是当前可用的字体的名称及字体源文件，这些字体名称是可以直接作为参数传入`use_font`使用的。

默认情况下，`mplfonts quickstart`会为你生成一个默认的支持亚洲字体的`matplotlibrc`文件来替代你的默认缓存配置，这个`matplotlibrc`文件的默认内容如下：
```
font.family:  sans-serif
font.sans-serif: Noto Sans CJK SC Regular, 思源等宽, Noto Serif CJK SC, 思源宋体, Noto Sans Mono CJK SC Regularsans-serif
axes.unicode_minus: False
```
它会优先使用`Noto Sans CJK SC Regular`字体作为你的默认字体，如果你安装了其他源的字体文件，想要让字体在全局生效，成为默认的首选字体，那么就需要将你的字体名称添加到`font.sans-serif`参数的最左端，然后执行`$ mplfonts updaterc <your matploblibrc path>`将配置写入全局缓存文件。

## 字体源
你可以从google和adobe获取一些开源的字体，这里有一些资源：
* https://github.com/adobe-fonts
* https://fonts.google.com
* https://github.com/googlefonts