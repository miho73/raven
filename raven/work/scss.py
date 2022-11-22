import os

"""
mode: SCSS compile mode
0: for build
1: for export
"""
def compileScss(mode):
    if mode == 0:
        os.system("npm run scss-build")
    elif mode == 1:
        os.system("npm run scss-compile")
