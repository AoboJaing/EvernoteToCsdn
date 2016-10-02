import re

f = open('D:\WorkSpace\python_ws\EvernoteToCsdn\EvernoteToCsdn\install_PCL.md', 'r')
md = f.read()
f.close()

# print md.decode('utf-8')

a = re.findall('!\[Alt text\]\((.*?)\)', md, re.S)
print a

f = open('D:\WorkSpace\python_ws\EvernoteToCsdn\EvernoteToCsdn\yinxiang_online.txt', 'r')
yinxiang_html = f.read()
f.close()

# print yinxiang_html

image_relative_path = re.findall('<p style="margin: 0 0 1.1em;" class="cye-lm-tag"><img x-evernote-mime="image/png" class="en-media" src="(.*?)"', yinxiang_html, re.S)
print image_relative_path
