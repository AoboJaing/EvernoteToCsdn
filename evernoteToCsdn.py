import re

f = open('D:\WorkSpace\python_ws\EvernoteToCsdn\EvernoteToCsdn\install_PCL.md', 'r')
md = f.read()
f.close()

# print md.decode('utf-8')

image_local_path = re.findall('!\[Alt text\]\((.*?)\)', md, re.S)
print image_local_path

f = open('D:\WorkSpace\python_ws\EvernoteToCsdn\EvernoteToCsdn\yinxiang_online.txt', 'r')
yinxiang_html = f.read()
f.close()

# print yinxiang_html

image_relative_path = re.findall('<p style="margin: 0 0 1.1em;" class="cye-lm-tag"><img x-evernote-mime="image/png" class="en-media" src="(.*?)"', yinxiang_html, re.S)
print image_relative_path

# print len(image_local_path)
# print len(image_relative_path)

if len(image_local_path)==len(image_relative_path):
    for i in range(len(image_relative_path)):
        image_relative_path[i] = 'https://app.yinxiang.com' + image_relative_path[i]
    print image_relative_path
    for i in range(len(image_relative_path)):
        md = md.replace(image_local_path[i], image_relative_path[i])

print md.decode('utf-8')

f = open('D:\WorkSpace\python_ws\EvernoteToCsdn\EvernoteToCsdn\Final_content.md', 'w')
f.write(md)
f.close()


