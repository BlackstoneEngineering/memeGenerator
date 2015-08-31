#!/usr/bin/env python
# h=70,w=300, 
# top left of fortune = 243,130
# bottom left of fortune = 243,210

import os
import sys
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

cookie = Image.open(os.path.join(os.path.abspath("."),"resources\\fortunecookie.jpg"))
# grab text from command line, `meme.py "example text"`
textRaw = sys.argv[1]+", mbed"
fontPath = os.path.join(os.path.abspath("."),"resources\\gilsansalt.TTF")
gilsansalt = ImageFont.truetype(fontPath,20)
textImage = Image.new('RGB',(300,70),(0xFF,0xFF,0xFF))
draw = ImageDraw.Draw(textImage)
draw.text((0,0),textRaw,fill = "black",font=gilsansalt)

cookie.paste(textImage,(243,130))
cookie.save(os.path.join(os.path.abspath("."),"\\output.jpg"))
