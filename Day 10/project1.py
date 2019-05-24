# -*- coding: utf-8 -*-
"""
Created on Fri May 17 17:54:42 2019

@author: Tarun Joshi
"""


from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

name=input("Enter your name: ")
img = Image.open("image.jpg")
draw = ImageDraw.Draw(img)
font = ImageFont.truetype("C:\Windows\Fonts\Arial.ttf", 16)
draw.text( (100,40), "Forsk Technologies", (255,0,0),font=font)
font = ImageFont.truetype("C:\Windows\Fonts\Arial.ttf", 14)
draw.text( (110,80), "This is to certify that", (255,0,0),font=font)
draw.text( (30,120), "has successfully completed Summer Training", (255,0,0),font=font)
font = ImageFont.truetype("C:\Windows\Fonts\Arial.ttf", 14)
draw.text( (120,100), name, (255,255,0),font=font)
img.save('certi.jpg')
