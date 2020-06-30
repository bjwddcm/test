## 请求网页
import requests
import re
import time
import os

headers = {
    'User-Agent':'only老K'# 这里可以随意输入,也可以输入网页上面的User-Agent
}
response = requests.get('https://www.vmgirls.com/12945.html')
# print(response.request.headers)
# print(response.text)
html = response.text
#解析网页
dir_name = re.findall('<h1 class="post-title h3">(.*?)</h1>',html)[-1] #根据网页标题去做我们的文件夹名字
if not os.path.exists(dir_name):
    os.mkdir(dir_name)
urls = re.findall('<a href="(.*?)" alt=".*?" title=".*?">',html) # (.*?) 意思就是匹配这个数据
# print(urls)
# 保存图片
for url in urls:
    time.sleep(1)
    file_name = url.split('/')[-1]
    response = requests.get(url)
    with open(dir_name +'/' + file_name,'wb') as f: #'wb':二进制 file_name：图片名称
        f.write(response.content)
