# -*- coding: utf-8 -*-

from albert import *
import os
from time import sleep

import base64


__title__ = "base64 encoder/decoder"
__version__ = "0.1.0"
__triggers__ = ["encode ", "decode "]
__authors__ = "vykio"

iconPath = iconLookup("albert")


# Can be omitted
def initialize():
    pass


# Can be omitted
def finalize():
    pass

def makeItem(text: str, subtext: str):
    return Item(
        id=__title__,
        icon=iconPath,
        text=text,
        subtext=subtext,
        actions=[ClipAction("Copy to clipboard", text)]
    )

def encode(text: str):
    return base64.b64encode(bytes(text, 'utf-8'))

def decode(text: str):
    return base64.b64decode(bytes(text, 'utf-8'))

def convert(trigger, value):
    if trigger == 'encode ':
        return [encode(value), "Convert text to base64"]
    else:
        return [decode(value), "Convert base64 to text"]


def handleQuery(query):
    if query.isTriggered:

        fields = query.string.split()

        txt = " ".join(fields[:])

        result = convert(query.trigger, txt)

        return makeItem(result[0] if result[0] else result[1] , result[1] if result[0] else "by Vykio")
