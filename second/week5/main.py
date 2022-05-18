#!/usr/bin/env python

import re


def change(name):
    patternn = r"^([\w]+) ([\w)]+)$"
    result = re.search(patternn, name)
    if (result):
        return f"{result[2]} {result[1]}"
    return name


print(change("maryam, gomina"))
