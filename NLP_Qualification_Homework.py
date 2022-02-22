#!/usr/bin/python
#-*- coding: utf-8 -*-
import requests
import os
import time
import random
from bs4 import BeautifulSoup
from ckiptagger import WS, POS, NER
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options

options = Options()
options.add_argument("headless")

class googleNews:
    def __init__(self,id,url,meida,headlines):
        self.url = url
        self.meida = meida
        self.headlines = headlines
        self.id = id

    def __repr__(self):
        return f'news{self.id:04d}\t{self.url}\t{self.meida}\t{self.headlines}\n'
    
    def loadingNewsContents(self):
        if (self.meida =="台灣蘋果日報"):
            driver = webdriver.Edge(options = options)
            driver.get(self.url)
            time.sleep(random.randint(5,10))  
            element = driver.find_element(By.ID, 'articleBody')
            self.contents = element.text
            driver.quit()
            return
        if (self.meida =="Yahoo奇摩新聞"):
            driver = webdriver.Edge(options = options)
            driver.get(self.url)
            time.sleep(random.randint(5,10))    
            element = driver.find_element(By.CLASS_NAME, 'caas-body')
            self.contents = element.text
            driver.quit()
            return
        if (self.meida =="新頭殼"):
            driver = webdriver.Edge(options = options)
            driver.get(self.url)
            time.sleep(random.randint(5,10))    
            element = driver.find_elements(By.XPATH,'//*[@id="news_content"]/div/div[2]')
            self.contents = element[0].text
            driver.quit()
            return
        if (self.meida =="自由時報電子報"):
            page = requests.get(self.url)
            soup = BeautifulSoup(page.text, "html.parser")
            article=soup.select_one('div[class^="text boxTitle boxText"]')
            if (article is None):
                article=soup.select_one('div[class^="whitecon"]')
            if (not article is None):
                self.contents = article.text
                return
        if (self.meida == "ETtoday新聞雲"):
            page = requests.get(self.url)
            soup = BeautifulSoup(page.text, "html.parser")
            article=soup.select_one('div[class^="story"]')
            if (not article is None):
                self.contents = article.text
                return
        if (self.meida == "UDN 聯合新聞網"):
            page = requests.get(self.url)
            soup = BeautifulSoup(page.text, "html.parser")
            article=soup.select_one('section[class^="article-content__editor"]')
            if (not article is None):
                self.contents = article.text
                return
        
        self.contents = ""
        page = requests.get(self.url)
        soup = BeautifulSoup(page.text, "html.parser")
        p_tag = soup.find_all('p')
        if (p_tag != []):
            for p in p_tag:
                self.contents += p.text
        
        if (self.contents ==""):
            driver = webdriver.Edge(options = options)
            driver.get(self.url)
            time.sleep(random.randint(5,10))    
            element = driver.find_elements(By.XPATH, '//*[@id="description"]/yt-formatted-string')
            if element != []:
                self.contents= element[0].text
            driver.quit()
            
        #print(self.contents)
    
if __name__ == '__main__':
    os.chdir('.')
    [os.remove(f) for f in os.listdir() if f.endswith(".txt")]
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
        ws_result = ws([g.contents])[0]
        
        print(f'news{g.id:04d}.txt')
        print(ws_result)
        fp = open(f'news{g.id:04d}.txt',"w", encoding='utf-8')
        for w in ws_result:
            fp.write(f'{w} ')
        fp.close()
        time.sleep(random.randint(3,5))   