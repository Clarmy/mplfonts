import os

import matplotlib.pyplot as plt

from mplfonts.util.manage import use_font
from mplfonts.util.common import calc_md5

TEST_DIR = os.path.dirname(os.path.abspath(__file__))
CASE_DIR = os.path.join(TEST_DIR, 'case')

FONT_NAMES = {
    'Noto Sans Mono CJK SC': 'Noto等宽',
    'Noto Serif CJK SC': 'Noto宋体',
    'Noto Sans CJK SC': 'Noto黑体',
    'Source Han Serif SC': '思源宋体',
    'Source Han Mono SC': '思源等宽',
    'SimHei': '微软雅黑'
}


def test_chinese(debug=False):
    for font_name, desc in FONT_NAMES.items():
        fp = font_name.replace(' ', '_') + '.png'
        use_font(font_name)
        fig = plt.figure(figsize=(4, 1))
        fig.text(.1, .6, font_name, fontsize=20)
        fig.text(.1, .2, desc, fontsize=20)

        plt.savefig(fp, format='png')

if __name__ == '__main__':
    test_chinese(debug=True)
