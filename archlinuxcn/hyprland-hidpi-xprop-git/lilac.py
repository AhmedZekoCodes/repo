#!/usr/bin/python3

from lilaclib import *

def pre_build():
    aur_pre_build(maintainers=['moetayuko', 'q234rty'])
    add_depends(['libdisplay-info.so', 'libhyprlang.so'])
    add_replaces(['hyprland-nvidia-hidpi-git'])

    for line in edit_file('PKGBUILD'):
        if not line.strip().startswith('hyprutils-git'):
            print(line)
