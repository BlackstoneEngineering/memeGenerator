#!/usr/bin/env python
# h=70,w=300, 
# top left of fortune = 243,130
# bottom left of fortune = 243,210

import os
from PIL import Image
from PIL import ImageDraw

cookie = Image.open(os.path.join(os.path.abspath("."),"resources\\fortunecookie.jpg"))
textRaw = "Programattically awesome, mbed"
textImage = Image.new('RGB',(300,70),(0xFF,0xFF,0xFF))
draw = ImageDraw.Draw(textImage)
draw.text((50,50),textRaw,fill = "black")

cookie.paste(textImage,(243,130))
cookie.save(os.path.join(os.path.abspath("."),"\\output.jpg"))
