from requests_html import HTMLSession
import requests
#保存文件目录
def save_image(url,title):
    img_response=requests.get(url)
    with open('./bg/'+title+'.jpg',wb) as file:
        file.write(img_response.content)
#背景图片地址
url="http://www.win4000.com/wallpaper_2358_0_10_1.html"
session = HTMLSession()
r=session.get(url)
print(r.content)
#查找页面中背景图，找链接，访问大图，并获取大图地址
itmes_img= r.html.find('ul.clearfix > li > a')
print(itmes_img)
for img in itmes_img:
    img_url=img.attrs['href']
    if "/wallpaper_detail" in img_url:
        r= session.get(img_url)
        itme_img=r.html.find('img.pic-large',first=True)
        url = itme_img.attrs['src']
        title= itme_img.attrs['title']
        print(url+title)
        save_image(url,title)