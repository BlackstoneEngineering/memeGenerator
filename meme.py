#!/usr/bin/env python
# h=70,w=300, 
# top left of fortune = 243,130
# bottom left of fortune = 243,210

import os
import sys
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont


# function taken from http://python.developermemo.com/6086_7715119/
def wrapText(draw, text,font, fill = "black"):
	import textwrap
	w,h = draw.size
	lines = textwrap.wrap(text, width)
	y_text = h
	for line in lines:
		width, height = font.getsize(line)
		draw.text(((w - width)/2, y_text), line, font = font, fill = FOREGROUND)
		y_text += height


def main():
	cookie = Image.open(os.path.join(os.path.abspath("."),"resources\\fortunecookie.jpg"))
# grab text from command line, `meme.py "example text"`
	textRaw = (sys.argv[1]+", mbed").decode('utf-8')
	fontPath = os.path.join(os.path.abspath("."),"resources\\gilsansalt.TTF")
	gilsansalt = ImageFont.truetype(fontPath,20)
	textImage = Image.new('RGB',(300,70),(0xFF,0xFF,0xFF))
	draw = ImageDraw.Draw(textImage)
#	wrapText(draw = draw, text = textRaw, font = gilsansalt)
	draw.text((0,0),textRaw,fill = "black",font=gilsansalt)
	cookie.paste(textImage,(243,130))
	cookie.save(os.path.join(os.path.abspath("."),"\\output.jpg"))


main()