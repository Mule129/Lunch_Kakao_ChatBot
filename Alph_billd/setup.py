from cx_Freeze import setup, Executable
import sys

buildOption = dict(packages = ["datetime","random","requests","re","bs4","PIL"],excludes=[])
exe = [Executable("test_addText.py")]

setup(
    name= 'Filter',
    version = '0.1',
    author = "YJS",
    description = "FIlter Adapter Application",
    options = dict(build_exe = buildOption),
    executables = exe
)
