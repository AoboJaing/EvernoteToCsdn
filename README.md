# ��дһ�� �� .md �ļ�ת�� CSDN ����Դ���� ��Python�ű� --- Ŀ�ģ�Ϊ�˽��CSDN��д�����Ǵӱ����ϴ�ͼƬ��CSDN�������ٶ��������� --- ����������������������� --- ���յõ��İ취����Github�ϴ���ͣ���������CSDN��ʹ��GIthub������ͼƬ��URL���� --- 2016��10��2�� ������


## ��дһ�� �� .md �ļ�ת�� CSDN ����Դ���� ��Python�ű�


��ʹ�õ�IDE����� **PyCharm 2016 04**
��ʹ�õ�Python�汾��**Python2.7.10**

���̱�������·����**D:\WorkSpace\python_ws\EvernoteToCsdn**
��������**EvernoteToCsdn**
����������ļ���
**evernoteToCsdn.py** �� ���� .md �ļ����������ת�� CSDN ����Դ����
Դ�������ڣ�https://github.com/AoboJaing/EvernoteToCsdn


����ͳһ�� **PyCharm** ����е� **Run** ���������С�


---

## Python ��һ���ı��ļ�

**��һ�� `.md` �ļ���**

```python
f = open('D:\WorkSpace\python_ws\EvernoteToCsdn\EvernoteToCsdn\install_PCL.md', 'r')
md = f.read()
f.close()

print md.decode('utf-8')

```

> ע�⣬��ʹ�� **Pycharm** �������� **Run** ���ڵ�ʱ���ڳ�����������Ҫ�����õ��ļ�������·��������Ҫд����·���������д�������·������ **Run** ���������нű��ͻᱨ������ **Terminal** �����оͲ��������������⣬�����Ǿ���·���������·�������򶼿���ʹ�á���

������������� **Run** �����У�

![Alt text](./img/1475380236844.png)

> ����ͬ���ĳ����� **Terminal** ���������о��Ǵ���ģ���Ҳ��֪��Ϊʲô��
> ```
> > C:\Python27\python.exe -i EvernoteToCsdn\evernoteToCsdn.py
> ```
> 
> ![Alt text](./img/1475380326494.png)
>  
>  �Ȳ���������⡣

---

## Python�е�ת���ַ� ʹ��������ʽ�õ� `.md` �ļ���  `![Alt text](xxx)` ������ӵ��ַ����е�`xxx` �ַ���

��Ϊ���ģ�壺 `![Alt text](xxx)` ���� `()` �� `[]` �������ַ�����Ȼ������Python�����в���ת���ַ���������Ϊ��������ʽ�У��������ַ����Ǳ�ʹ�õĹ��ߣ����ԣ����ģ���ַ��������������ַ���������Ҫ���������ַ�ǰ����� ��б�ܣ�`\` ��

```python
a = re.findall('!\[Alt text\]\((.*?)\)', md, re.S)
print a
```

���������
```
['./1475185523275.png', './1475185542021.png', './1475291577407.png', './1475291600927.png', './1475185222317.png', ....]
```

> Python �е�ת���ַ�����Щ���뿪������ͣ�http://www.cnblogs.com/allenblogs/archive/2011/04/28/2031477.html

---


## ��ȡ ��ӡ��ʼ��������߱ʼǵ�Դ�����txt�ļ�

�� **Chrome** �������Դ���������

```
<p style="margin: 0 0 1.1em;"><img class="en-media" src="/shard/s53/res/2f08130e-d47e-4fc2-b6be-0256abbaf3dd" data-en-resource-reference="resource-43" style="height: auto;"></p>
```
![Alt text](./img/1475382711908.png)

������Դ���븴�Ƶ�`txt` �ļ���������Դ��������ӣ�

```
<p style="margin: 0 0 1.1em;" class="cye-lm-tag"><img x-evernote-mime="image/png" class="en-media" src="/shard/s53/res/2f08130e-d47e-4fc2-b6be-0256abbaf3dd" style="border: 0; vertical-align: middle; max-width: 100%;" hash="ae5482e2a9b9e7bce8f5f77c76877d39" type="image/png" title="" alt="Alt text" longdesc="./1475185329838.png"></p>
```

![Alt text](./img/1475382904244.png)


---

��ӡ��ʼ��бʼǵ�������ҳ��Դ���뿽����һ��txt�ļ����棬������Python�������ȡ���txt�ļ���

```
f = open('D:\WorkSpace\python_ws\EvernoteToCsdn\EvernoteToCsdn\yinxiang_online.txt', 'r')
yinxiang_html = f.read()
f.close()

print yinxiang_html
```

���У�

![Alt text](./img/1475385702731.png)


---

## ʹ��������ʽ�� `yinxiang_online.txt` �ļ���������Ϣ��ȡ����

ͬһ��ͼƬ�������������������Ϣ��

---

��**Chrome** ������У�ӡ�����߱ʼ�����ҳ��Դ�����У�ͼƬ��Դ���룺

```
<img class="en-media" src="/shard/s53/res/d6ae5c20-56e4-4e3b-ab3c-c80acec89859" data-en-resource-reference="resource-47" style="height: auto;">
```

ͼƬ��վ��URL���ӣ�

```
https://app.yinxiang.com/shard/s53/res/d6ae5c20-56e4-4e3b-ab3c-c80acec89859
```

��`yinxiang_online.txt` �ļ���

```
<p style="margin: 0 0 1.1em;" class="cye-lm-tag"><img x-evernote-mime="image/png" class="en-media" src="/shard/s53/res/d6ae5c20-56e4-4e3b-ab3c-c80acec89859" style="border: 0; vertical-align: middle; max-width: 100%;" hash="8669b92dc685fdf38ea62d929b70d827" type="image/png" title="" alt="Alt text" longdesc="./1475185222317.png"></p>
```

�� `install_PCL.md` �ļ��У�

```
![Alt text](./img/1475185222317.png)
```

---

����ͨ���۲췢�֡����ǵ�Ŀ����Ҫ�õ����յ�ͼƬ**URL**���ӡ�

������Ҫͨ���� `yinxiang_online.txt` �ļ� �������Ϣ������ ����ͼƬ��**URL**���ӡ����գ����Ƿ���ͼƬ������**URL**����Ϊ��

������ͼƬ**URL**���� = `https://app.yinxiang.com` + `yinxiang_online.txt` �ļ�����ӦͼƬ��`src` 

���磺

![Alt text](./img/1475387545436.png)

---

ʹ��������ʽ�� `yinxiang_online.txt` �ļ���������Ϣ��ȡ�������������£�

```python
image_relative_path = re.findall('<p style="margin: 0 0 1.1em;" class="cye-lm-tag"><img x-evernote-mime="image/png" class="en-media" src="(.*?)"', yinxiang_html, re.S)
print image_relative_path
```

���У�

![Alt text](./img/1475387809022.png)

---

## �� ͼƬ�����**URL**���� ��� ����**URL**����


```python
if len(a)==len(image_relative_path):
    for i in range(len(image_relative_path)):
        image_relative_path[i] = 'https://app.yinxiang.com' + image_relative_path[i]

print image_relative_path
```


---

## ��`.md` �ļ��е� `![Alt text](xxx)` �е�`xxx`  **�滻** �ɶ�ӦͼƬ��**URL**�������ӡ�

�ο���վ��http://www.cnblogs.com/wanpython/archive/2010/05/31/1748387.html

```python
if len(image_local_path)==len(image_relative_path):
    for i in range(len(image_relative_path)):
        md = md.replace(image_local_path[i], image_relative_path[i])

print md.decode('utf-8')
```

---

## �����յõ��� `.md` �ļ�������������Ϊ�� `Final_content.md` �ļ����档 

```python
f = open('D:\WorkSpace\python_ws\EvernoteToCsdn\EvernoteToCsdn\Final_content.md', 'w')
f.write(md)
f.close()
```

���нű��󣬵õ���

![Alt text](./img/1475419335474.png)


---

�����������Դ���Ĺ��ܾͶ�ʵ���ˡ�

---

# ��ϧ�������ַ����Ѿ�����ʹ����

��Ϊ��
��Ϊ��ЩͼƬ��URL����ֻ���ҵ�¼��ӡ��ʼǵ��˺ţ��Ҳ��ܿ�����Ҳ����˵����ЩͼƬ��Ȼ�������û������ҵ���վ�Ļ��������ǿ�����ͼƬ�ġ�

![Alt text](./img/1475419565965.png)

---

���������һ���ֻ�ܼ��������������ͼƬ�ϴ���CSDN�Ƚϱ��գ�����CSDN���ϴ��ٶ�ʵ����̫���ˣ��Ҹ���ô�졣�ѵ���Ҫ�Լ���һ����������


---

## ���¾�

ӡ��ʼ�����˽�˵Ŀռ䣬����Ҫ���û�����������ܹ����ʵģ���ô������ǽ�ͼƬ�����һ�����еĿռ��У���ô��ʹ�����ͼƬ��**URL**���ӷ������ҵ�CSDN���Ͳ������棬���Ϳ��Ը������˿�����

�������ڵ������ǣ��ҵ�һ�����Դ��ͼƬ�����̡����������������Ϊ���пռ䡣û�����Ǿ�ʹ��**�ٶ���**��

�ٶ����̣��ϴ��ٶȿ졣

---

���������ҵİٶ��������洴�������·����

![Alt text](./img/1475420676923.png)

�Ժ����Ǿͽ�ͼƬ�ļ�������������档

�����ڽ���� `img` �ļ��й�������
http://pan.baidu.com/s/1eSPtP8e


���ǣ����һ�������г�����1���ļ��Ļ�����ô�������������ҳ����һ����̬��ҳ�������ֻ����һ���ļ��Ļ�����ô�����������������ҳ����һ����̬��ҳ��

���ڶ�̬��ҳ�����޷�ֱ�ӵõ�ÿ���ļ����ڵ�**URL**���ӡ�
�����ھ�̬��ҳ����Ȼ���ǿ��Եõ��ļ�������**URL**���ӣ��������һ��һ���ļ����ϴ��Ļ�������Ч����ʵ�ͽ�ͼƬ�ϴ���CSDN��վ��һ���ġ�

---

���ԣ����ڵ�����ͱ���ˣ���λ�ȡ **�ٶ���** ������ҳ�����ļ�������**URL**���ӡ�

����������⣬�Ҹ����Ҳ�������취����û�а취������**�ٶ���** ����Դ�л�ȡ����ͼƬ��Դ��URL���ӣ�Ȼ��ʹ����**CSDN**�Ĳ����С�



---

## �ٴ���ٽ��·�� --- ���� ʹ�� ����԰ ������ʹ��CSDN

**����԰**

�ŵ㣺
1 . ͼƬ�����ϴ�������ֱ��ճ������ק�Ϳ��Խ�ͼƬ���������ڱ༭�Ĳ����У������ٶȷǳ��졣
2 . û�й��
3 . ���͵�ҳ�����
ȱ��
1 . ʹ��MarkDown��д���͵�ʱ��û��Ԥ������
2 . ʹ��**Markdown**��д�Ĵ����û���к�
3 . ��Baidu�����ϵ��ƹ�û��CSDNǿ��

**CSDN**

�ŵ�
1 . ʹ�õ��˶�
2 . ��Baidu�����ϵ��ƹ����ĺ�
3 . ���������ܣ����Թ�������д����
4 . �в���ר������
5 . Mardown��д������Ԥ���Ĺ���
6 . Markdown��д�����п�ݼ��Ĺ���
7 . Makdown��д���͵Ĵ�������к�
ȱ��
1 . ���̫��
2 . д���͵Ļ����ϴ�ͼƬ̫���������鷳��ͼƬ�ϴ���ʱ������Ҫ�������һ��������ҳ����������

---

����������������ʵ�������е��뷨���Ǽ��ʹ��**CSDN**�ġ���������ϴ�ͼƬʵ����̫���ˡ�����Ҫ�������������ⲻ����Ļ������ҵĹ���Ч�ʻ���������Ӱ�졣���صĶ��ҵĹ���Ч�������ȡ�

---

������ֻʣ��һ��Ψһ�Ľ���취�����ǣ�ʹ���������棬���������ں�̨�ϴ�ͼƬ����ֻ����ô���ˡ�

---


## ��ͻȻ��������һ��������������д��Github Page�ϰ�

�԰�������ô�����ˡ�������������������������ĺô��ǳ����Ķࡣ

1 . �ҿ��Խ����ҵĲ���д��һ���Լ�������վ�㣬
2 . ���ҿ��Խ���ϴ���ͼƬ������
3 . Github�а汾����Ĺ��ܣ��һ����Բſ��ҵ���ҳ����ʱ�޸ĵĺۼ�
4 . ��д�ľ��Ǽ�����Ĳ��ͣ�Ҳ����˵�����ĺͳ�����������ϵ��һ��

���ң��������� **Github For Windows** ��GUI����������ϴ��͸�����ҳ���ٶȶ��ǳ��Ŀ죬������GUI���棬����Ҳ�Ƿǳ��ļ򵥣��ҿ���ȫ��Ͷ�뵽д�����ϣ�������Ҫȥ�����������顣�������͵�����ͽ���**Github**ȥ��������ֻ��Ҫ��д���͡���


---

���ԣ���������Ҫ֪��һ�㣺

**Q��** **Github ** �Ƿ��ж��û��Ĵ洢�ռ������ƣ�

**A��**  ����������Ƕ����ˣ�**GitHub ** �����е��û�����û�д洢�ռ����޵ģ��������޵Ĵ洢�ռ䡣Ҳ����˵���������**Github Page**����д�����Ĳ��ġ�����㻹�ǲ��������Ҹ�����̫ͻȻ������Բ鿴**GitHub Help**�����[��ƪ����](https://help.github.com/articles/what-is-my-disk-quota/)��

---

���ԣ������ھ�Ҳ��������
���ڣ���**GitHub** �ϴ���͡�Ȼ�󽫲��Ͷ�д��**Github** �ϣ����ţ��ҿ��Խ�**Github** �ϵĲ��ͣ�ת�Ƶ�**CSDN**�����ϣ������ҾͲ���Ҫ��**ͼƬ**�ϴ���**CSDN**���������ˣ������ϴ����ҵ�**GIthub**�û��Ŀռ��ϣ�Ȼ����**CSDN**��������ʹ��ʹ��**Github**���������ͼƬ��**URL**���ӡ�
������




