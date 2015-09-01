# h=70,w=300, 
# top left of fortune = 243,130
# bottom left of fortune = 243,210

import os
import sys
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

transparent = (0,0,0,0)

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
	cookie = Image.open(os.path.join(os.path.abspath("."),"resources/fortunecookie.jpg"))
# grab text from command line, `meme.py "example text"`
	textRaw = (sys.argv[1]+", mbed")
	fontPath = os.path.join(os.path.abspath("."),"resources/gilsansalt.TTF")
	gilsansalt = ImageFont.truetype(fontPath,20)
	mask = Image.new('1', (300,70))
	trans = Image.new('RGBA', (300, 70),transparent)
	draw = ImageDraw.Draw(trans)
#	wrapText(draw = draw, text = textRaw, font = gilsansalt)
	draw.text((0,0),textRaw,fill = "black",font=gilsansalt)
	cookie.paste(mask,(243,130),trans)
	cookie.save(os.path.join(os.path.abspath("."),"output.png"),'PNG')


main()