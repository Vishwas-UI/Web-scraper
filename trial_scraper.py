import bs4 as bs
import urllib.request
import scrapy
from pandas import read_csv
from readability.readability import Document
import time

source = urllib.request.urlopen('https://www.newsnow.co.uk/h/Sport/Football/La+Liga/Real+Madrid/Transfer+News')
soup = bs.BeautifulSoup(source, 'lxml')
count=0
urls=[]
for url in soup.find_all('a', class_="hll"):
    count+=1
    if 0<count<=30:
        a=url.get('href')
        a+='#out'
        urls+=[a]
    elif count>31:
        break

print(urls)
actual_url=[]
for url1 in urls:
    source1=urllib.request.urlopen(url1)
    soup1= bs.BeautifulSoup(source1, 'lxml')

    for url in soup1.find_all('a'):
        actual_url+=[url.get('href')]
print(actual_url)
count1=0
title=[]
for url2 in actual_url:
    if count1<=10:
        try:
            source2=urllib.request.urlopen(url2)
            soup2= bs.BeautifulSoup(source2, 'lxml')
            count1+=1

            title+=[(soup2.title,url2)]
        except:
            continue
    elif count1>11:
        break

print(title)
