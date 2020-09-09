import requests
import re

av = input('请输入哔哩哔哩的AV号：')
# url = 'https://m.bilibili.com/video/{}.html'
url = f'https://m.bilibili.com/video/{str(av)}.html'
headers = {
    'User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1'
}

url2 = re.compile(r"video_url: '(.*)',")
html = requests.get(url,headers=headers).text
url2 = url2.findall(html)[0]
print(url2)
url2 = 'http:'+url2
print(url2)
html = requests.get(url2,headers=headers).content
with open('11.mp4','ab+') as f:
    f.write(html)
print('下载完了')
