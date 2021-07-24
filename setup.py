import setuptools
import os

FILE_PATH = os.path.dirname(os.path.realpath(__file__))

with open(os.path.join(FILE_PATH, 'README.md'), 'r') as fh:
    long_description = fh.read()

requirements_path = os.path.join(FILE_PATH, 'requirements.txt')
with open(requirements_path) as f:
    required = f.read().splitlines()

setuptools.setup(
    name='mplfonts',
    version='0.0.1',
    author='Wentao Li',
    author_email='clarmylee92510@gmail.com',
    description='Fonts manager for matplotlib',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/Clarmy/mplfonts',
    include_package_data=True,
    package_data={'': ['rc/matplotlibrc','fonts/*.otf']},
    packages=setuptools.find_packages(),
    install_requires=required,
    classifiers=[
        'Programming Language :: Python :: 3',
    ],
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
            'mplfonts = mplfonts.bin.cli:cli'
        ]
    }
)