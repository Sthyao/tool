from PIL import Image, ImageDraw, ImageFont

string = input("输入文字：")
#string = "我是憨批"

n = 18
lenght = len(string)

img = 'data/index2.png'
new_img = string + '.png'

font_type = 'C:/Windows/Fonts/微软雅黑/msyhbd.ttc'
font = ImageFont.truetype(font_type, 18)
color = "#000000"

image = Image.open(img)
draw = ImageDraw.Draw(image)
width, height = image.size

text_x = 135
text_y = 374

draw.text((text_x-lenght*n/2, text_y), u'%s'  % string , color, font)
image.save(new_img, 'png')