from bs4 import BeautifulSoup
import requests
import time
#import json

def getValueList(url, selector):
    htmlValue = requests.get(url)
    htmlValue.encoding = 'gbk'  # 更改字符编码
    soup = BeautifulSoup(htmlValue.text,'html.parser')
    result = soup.select(selector)
    return result

def getAllValue(urlList, selector):
    result = ""
    for zjName in urlList:
        nr = getValueList(zjName['href'], selector)
        result += zjName.text + "\n" + nr[0].text + "\n"
        print(zjName.text)
        
    return result

def saveFile(fileName, fileValue):
    f = open(fileName,'a+',encoding="utf-8")
    f.write(fileValue)
    f.close()

def main():
    url="http://www.huanyue123.com/book/69/69865/"
    zjurl = getValueList(url, 'li > a')
    jzValue = getAllValue(zjurl, '#htmlContent')
    saveFile("天下第九.txt", jzValue)
    
if __name__ == "__main__":
    main()
    
