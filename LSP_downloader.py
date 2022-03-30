import requests
from bs4 import BeautifulSoup
import re
import urllib.request
import list

Base_URL = "xxxx"
Login_URL = "xxxx"

def get_html(url):
    response = requests.get(url)
    first_cookie = response.cookies.get_dict()
    return response.text,first_cookie


def login(url,cookie):

    data= {
        "username":"ssssgradman",
        "pass":"zxcvbnm",
        "action":"login",
        "email_link":"https://www.xxxxx.com/email/",
        "format":"json",
        "mode":"async"
    }
    response = requests.post(url,data=data)
    print(response.status_code)
    cookie = response.cookies.get_dict()
    # cookie.update(second_cookie)
    return cookie

Html,Cookie = get_html(Base_URL)
Cookie = login(Login_URL,Cookie)

imgName = 0

#Get HTML file
def getHtml(url):
    for i in range(0,4):
        try:
            page = requests.get(url,cookies=Cookie,timeout = 5)
            html = page
            print("start")
            return html
        except Exception as e:
            print("wow")

    #Get image url 
def getImg(html):
    #Match picture address
    reg = r'href="([.*\S]*\.jpg/)"'
    imgre = re.compile(reg)
    imglist = re.findall(imgre, html)
    return imglist


def download(urllll):
    global imgName
    print(urllll)
    html = getHtml(urllll)
    
    html = html.text

    imgList = getImg(html)

    for imgPath in imgList:
        try:
            f = open('data/'+ str(imgName)+".jpg", 'wb')
            f.write((urllib.request.urlopen(imgPath, timeout = 30)).read())
            print("got a image: " + str(imgName))
            f.close()
        except Exception as e:
            print(imgPath+" error")
        
        imgName += 1

    print("All Done!")

for url_num in list.urllist:
    download(url_num)