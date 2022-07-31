from requests_html import HTMLSession
session = HTMLSession()
r= session.get('https://news.cnblogs.com/n/recommend')
# #获取网页上的所有链接
# all_links=r.html.links
# print(all_links)
# #获取网页上所有链接，以绝对路径方式
# all_absolute_links=r.html.absolute_links
# print(all_absolute_links)
# css找新闻标签
news=r.html.find('h2.news_entry>a')
for new in news:
    print(new.text) #获取新闻标题
    print(new.absolute_links) #获取新闻链接