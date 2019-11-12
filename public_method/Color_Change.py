#!/usr/bin/env python
#coding:utf-8
import xlwt
__author__ = 'dingrui'

def color(col):
    # Create the Pattern
    pattern = xlwt.Pattern()
    style = xlwt.XFStyle()

    # May be: NO_PATTERN, SOLID_PATTERN, or 0x00 through 0x12
    pattern.pattern = xlwt.Pattern.SOLID_PATTERN

    # May be: 8 through 63. 0 = Black, 1 = White, 2 = Red, 3 = Green, 4 = Blue, 5 = Yellow, 6 = Magenta, 7 = Cyan, 16 = Maroon,
    # 17 = Dark Green, 18 = Dark Blue, 19 = Dark Yellow , almost brown), 20 = Dark Magenta, 21 = Teal, 22 = Light Gray, 23 = Dark Gray,
    if col == "Red":
        pattern.pattern_fore_colour = 2
        # Add Pattern to Style
        style.pattern = pattern
    if col == "Green":
        pattern.pattern_fore_colour = 3
        # Add Pattern to Style
        style.pattern = pattern
    return style