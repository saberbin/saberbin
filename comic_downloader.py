#!/user/bin/Saberbin python
# -*- coding:utf-8 -*-
#Author:Saberbin
#comic_downloader.py
#version 3.5

#url='http://www.cartoonmad.com/comic/2650.html'

import re
import urllib.request
import requests
import os
from bs4 import BeautifulSoup
from time import sleep
import random


def gethtml(url):
    response=requests.get(url)
    print(response.status_code)
    html=response.text
    return html
'''
def getsoup(html):
    soup=BeautifulSoup(html,'html.parser')
    return soup
    '''

def find_comic_url(html):
    comic_url={}
    a=[]
    roll_page={}
    href=re.findall(r'/(\d+)\.html',html)
    for i in range(len(href)):
        if len(href[i])==15:
            a.append(href[i])
        else:
            continue
    for i in range(len(a)):
        comic_url[i+1]='http://www.cartoonmad.com'+'/comic/'+a[i]+'.html'
        roll_page[i+1]=a[i][9:12]
    return comic_url,roll_page

#创建文件夹存放图片
def creat_folder(folder_path):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        #break
    else:
        print('该文件夹已被创建')
    
def urlprocess(i):
    if i<=9:
        picurl='00'+str(i)
        return picurl
    elif i>=10 and i<=99:
        picurl='0'+str(i)
        return picurl
    else:
        picurl=str(i)
        return picurl

#download manhua
def manhua(manhua_url,page,fpath):
    manhua_html=gethtml(manhua_url)
    li=re.findall(r'src="http://(.*).jpg"',manhua_html)
    pic_url=li[0]
    f_url=pic_url[:41]
    for i in range(int(page)+1):
        if i==0:
            continue
        page=urlprocess(i)
        pic_url='http://'+f_url+page+'.jpg'
        getimg(pic_url,page,fpath)
        print(page)
        print()
        time.sleep(3)

def getimg(pic_url,page,file_path):
    path=file_path+'/'+page+'.jpg'
    urllib.request.urlretrieve(pic_url,path)

def main():
    print('start...')
    url='http://www.cartoonmad.com/comic/2650.html'
    html=gethtml(url)
    #soup=getsoup(html)
    comic_url={}
    roll_page={}
    comic_url,roll_page=find_comic_url(html)
    #print(comic_url)
    #print(roll_page)
    path=os.getcwd()#获取当前文件夹的路径
    comic_path=path+'/'+'comic'
    creat_folder(comic_path)
    f_path=comic_path+'/'
    for i in range(len(comic_url)):
        roll_path=f_path+str(i+1)
        creat_folder(roll_path)
        manhua(comic_url[i+1],roll_page[i+1],roll_path)
        print('one roll download over!')
        sleep(random.randint(5,9))#使程序休眠，休眠时间为5-9的随机数
    print('over!')



main()
print('mission completed!')
    
    
    


