from PIL import Image
import math
img=Image.open('tyan.png')

img=img.resize((71,67))
imgl=img.convert('L')
table=['\033[30m ','.',':',"'",',','-',';','_','"','+','°','•','^','=','1','|','(','[','{',"∆",'©','®','&',"$",'O',"@",'%','\033[37m#','\033[37m¶']
def convert(L):
	return table[round((len(table)-1)/255*L)]
for i in range(0,imgl.height):
	print('')
	for j in range(0,imgl.width):
		print(convert(imgl.getpixel((j,i))),end='')
