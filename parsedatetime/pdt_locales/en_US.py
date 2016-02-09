# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .base import *  # noqa

# don't use an unicode string
localeID = 'en_US'
uses24 = False

dateSep = ['/']
timeSep = [':', '.']
meridian = ['AM', 'PM']
usesMeridian = True
uses24 = True
WeekdayOffsets = {}
MonthOffsets = {}

timeFormats = {
    'full': 'h.mm:ss a z',
    'long': 'h.mm:ss a z',
    'medium': 'h.mm:ss a',
    'short': 'h.mm a',
}

re_values = {
    'specials': 'in|on|of|at',
    'timeseparator': '.',
    'rangeseparator': '-',
    'daysuffix': 'rd|st|nd|th',
    'meridian': 'am|pm|a.m.|p.m.|a|p',
    'qunits': 'h|m|s|d|w|y',
    'now': ['now'],
}
