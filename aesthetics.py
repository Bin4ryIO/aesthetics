#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import sys

def aesthetics(s):
    exp = r"""[a-zA-Z0-9!\?\.'";:\]\[}{\)\(@#\$%\^&\*\-_=\+`~><]"""
    c = ''.join(chr(0xFEE0 + ord(i)) for i in s)
    c = re.sub(r" ", "", c)
    return re.sub(exp, s, c)

print(aesthetics(sys.argv[1]))
