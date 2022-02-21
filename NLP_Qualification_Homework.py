#!/usr/bin/python
#-*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import time
import random
from ckiptagger import WS, POS, NER
    
#caas-content-wrapper

class googleNews:
    def __init__(self,id,url,meida,headlines):
        self.url = url
        self.meida = meida;
        self.headlines = headlines;
        self.id = id;

    def __repr__(self):
        return f'news{self.id:04d}\t{self.url}\t{self.meida}\t{self.headlines}\n'
    
    def loadingNewsContents(self):
        page = requests.get(self.url)
        soup = BeautifulSoup(page.text, "html.parser")
        p_tag = soup.find_all('p')
        self.contents = ""
        for p in p_tag:
            self.contents += p.text
        #print(self.contents)
    
if __name__ == '__main__':
    #CKIP initial
    ws = WS("./data")
    # scraping news form google_news_url
    google_news_url = "https://news.google.com/topstories?hl=zh-TW&gl=TW&ceid=TW:zh-Hant"
    page = requests.get(google_news_url)
    soup = BeautifulSoup(page.text, "html.parser")
    
    news = soup.find_all(class_="ipQwMb ekueJc RD0gLb")
    media = soup.find_all(class_="wEwyrc AVN2gc uQIVzc Sksgp")
    g_news = []
    for n,m in zip(news,media):
        a = n.findChildren('a',recuresive=False)[0]
        url = (a['href'])
        g_news.append(googleNews(len(g_news)+1,"https://news.google.com/"+url,m.contents[0], a.contents[0]))
    # output news to newslist.txt 
    fp = open("newslist.txt", "w",encoding='utf-8')
    for n in g_news:
        fp.writelines(n.__repr__())
        print(n.__repr__())
    fp.close()
    
    # loading news contents
    for g in g_news:
        g.loadingNewsContents()
        ws_result = ws([g.contents])[0];
        print(f'news{g.id:04d}.txt')
        print(ws_result)
        fp = open(f'news{g.id:04d}.txt',"w", encoding='utf-8')
        for w in ws_result:
            fp.write(f'{w} ')
        fp.close()
        time.sleep(random.randint(10,30))
        