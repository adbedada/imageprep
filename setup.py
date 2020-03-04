from setuptools import setup

REQUIRED = [
    'click>=7.0',
    'Pillow==7.0.0'
]
setup(
    name='imprep',
    version=0.1,
    entry_points='''
        [console_scripts]
        imprep=imcli:commands
        ''',
    py_modules=['imprep','imcli'],
    install_requires=REQUIRED
)