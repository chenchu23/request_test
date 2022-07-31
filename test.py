import urllib.request
import requests
import urllib.parse
import socket
import urllib.error
import re
#get
# response=urllib.request.urlopen("http://www.baidu.com")
# print(response.read().decode('utf-8'))

#post
# data=bytes(urllib.parse.urlencode({'word':'hello'}),encoding="utf-8")
# response=urllib.request.urlopen("http://httpbin.org/post",data=data)
# print(response.read())

#设置超时时间
# response=urllib.request.urlopen("http://httpbin.org/get",timeout=1)
# print(response.read())

#超过超时时间就抛出异常
# try:
#     response = urllib.request.urlopen("http://httpbin.org/get", timeout=0.1)
# except urllib.error.URLError as e:
#     if isinstance(e.reason,socket.timeout):
#         print('time out')
# files={"file":open(r'D:\Python37\test\guest\request_test\1.txt','rb')}
# headers={
#     "Content-Type": "text/html; charset=utf-8"
# }
# r1=requests.get("http://httpbin.org/post",headers=headers,files=files)
# s=requests.session()
# r1=s.get("http://httpbin.org/cookies/set/number/123456789",headers=headers)
# print(r1.text)
# print(r1.json)
# print(r1.content)
# print(r1.text)

content="Hello 1234567 Wrold_This is a Regex Demo"
# #贪婪匹配
# r=re.match("^He.*?(\d+).*Demo$",content)
# print(r)
# print(r.group(1))
# print(r.span())

# #非贪婪匹配
# result=re.match("^He.*(\d+).*Demo$",content)
# print(result)
# print(result.group(1))
# print(result.span())

# #匹配换行符
# content1="Hello 1234567 Wrold_This " \
#          "is a Regex Demo"
# result1=re.match("^He.*?(\d+).*Demo$",content,re.S)
# print(result1)
# print(result1.group(1))

#转义
# content2='price is $5.00'
# result2=re.match('price is \$5\.00',content2)
# print(result2)
#re.search
# content3='Hello 1234567 Wrold_This is a Regex Demo'
# result3=re.search('Hello.*?(\d+).*?Demo',content3)
# print(result3)
# print(result3.group(1))
#获取豆瓣图书表
