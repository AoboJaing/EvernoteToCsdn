import re

f = open('D:\WorkSpace\python_ws\EvernoteToCsdn\EvernoteToCsdn\install_PCL.md', 'r')
md = f.read()
f.close()

# print md.decode('utf-8')

a = re.findall('!\[Alt text\]\((.*?)\)', md, re.S)
print a

