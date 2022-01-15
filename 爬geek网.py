import requests
import re
import os
import parsel

images = 'GEEK图片'  # 创建文件
if not os.path.exists(images):
    os.mkdir(images)
if not os.path.exists("文本"):
    os.mkdir("文本")


def Tools(url):  # 获得请求
    response = requests.get(url)
    response.encoding = 'utf-8'
    return response


response = Tools('http://212.129.245.115/geek#/')
re_temp = '<script type="text/javascript" src="(.*?)">'  # 匹配js地址
result = re.findall(re_temp, response.text)
link = result[2]
reget = Tools(link).text
re_png = re.findall(
    'src:"(.*?)"', reget)  # 匹配图片url地址
for pic_link in re_png:
    picname = picname = pic_link.split('/')[-1]
    pic_content = Tools(pic_link)

    with open(images + '\\' + picname, mode='wb') as file:
        file.write(pic_content.content)
result_word = re.findall(r'\w*[^\x00-\xff]\w*', reget)  # 匹配字母或数字，和双字节字符，
for it in result_word:
    with open("文本\\" + 'GEEK文本.txt', mode='a', encoding='utf-8') as file:
        file.write(it)
        file.write('\n')
