from bs4 import BeautifulSoup
import requests
import time
#import json


url="http://www.huanyue123.com/book/49/49865/"
wb_data = requests.get(url)
wb_data.encoding = 'gbk'  # 更改字符编码
soup = BeautifulSoup(wb_data.text,'html.parser')
#print(wb_data.text)
name = soup.select('li > a')
f = open("天下第九.txt",'a+',encoding="utf-8")

for zj in name:
    zj_data=requests.get(zj['href'])
    zj_data.encoding = 'gbk'
    soup1=BeautifulSoup(zj_data.text,'html.parser')
    nr = soup1.select('#htmlContent')
    f.write(zj.text+"\n"+nr[0].text+"\n")
    print(zj.text)
    #print(nr[0].text)

f.close()
