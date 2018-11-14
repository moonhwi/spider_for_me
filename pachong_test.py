import re
import urllib.request


def Schedule(a, b, c):
    per = 100.0 * a * b / c
    if per > 100:
        per = 100
        print('完成！')
    print('%.2f%%' % per)


def getHtml(url):
    agent = {'user-agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Mobile Safari/537.36'}
    req = urllib.request.Request(url, headers=agent)
    page = urllib.request.urlopen(req)
    html = page.read()
    return html


def getImg(html):
    html = html.decode('utf-8')
    reg = r'<img src="(https.*?jpg)"'#raw string
    imgre = re.compile(reg)
    imglist = imgre.findall(html)
    x = 0
    print(imglist)
    for imgurl in imglist:
        #  写好你的路径
        urllib.request.urlretrieve(imgurl, 'E:\\test\\%s.jpg' % x, Schedule)
        x += 1


html = getHtml('https://www.zhihu.com/question/49441554/answer/241827437')
print(getImg(html))