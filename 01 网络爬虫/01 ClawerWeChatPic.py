import csv
import urllib
from re import findall
from urllib.request import urlopen


url = 'https://mp.weixin.qq.com/s/YOBr48asF3LJjisJWyyB0w'

with urllib.request.urlopen(url) as fp:
    content = fp.read().decode()
    # print(content)

pattern = 'data-croporisrc="(.+?)"'
result = findall(pattern, content)
print(result)


for index, item in enumerate(result):
    with urlopen(str(item)) as fp:
        with open(str(index)+'.png', 'wb') as fp1:
            fp1.write(fp.read())
