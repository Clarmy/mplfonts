import os

import matplotlib.pyplot as plt

from mplfonts.util.manage import use_font

TEST_DIR = os.path.dirname(os.path.abspath(__file__))
CASE_DIR = os.path.join(TEST_DIR, "case")

FONT_NAMES = {
    "Noto Sans Mono CJK SC": "Noto等宽",
    "Noto Serif CJK SC": "Noto宋体",
    "Noto Sans CJK SC": "Noto黑体",
    "Source Han Serif SC": "思源宋体",
    "Source Han Mono SC": "思源等宽",
    "SimHei": "微软雅黑",
}


def test_chinese():
    for font_name, desc in FONT_NAMES.items():
        fp = font_name.replace(" ", "_") + ".png"
        use_font(font_name)
        fig = plt.figure(figsize=(4, 1))
        fig.text(0.1, 0.6, font_name, fontsize=20)
        fig.text(0.1, 0.2, desc, fontsize=20)

        plt.savefig(fp, format="png")

        right_img = plt.imread(os.path.join(CASE_DIR, fp))
        candidate_img = plt.imread(fp)
        assert (right_img == candidate_img).all()


if __name__ == "__main__":
    test_chinese(debug=True)
