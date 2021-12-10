# -*- coding: utf-8 -*-
"""
@author: Jack Lee
WebCrawlerLib provides to crawler page by using selenium.
Example:

"""
from selenium import webdriver
import time
import requests
import os
from catch_image import CatchImage

class GoogleCatchImage(CatchImage):
    def __init__(self):
        return
    
    def run(self,url,keyword,headless=False,round=2):
        self.connect_page(url,headless)
        self.download_images(keyword,round)
        self.close()

    def connect_page(self,url,bool_headless):
        if bool_headless:
            options = webdriver.ChromeOptions()
            options.add_argument('--headless')
            self.driver = webdriver.Chrome(options=options)
            self.driver.get(url)
        else:
            self.driver = webdriver.Chrome()
            self.driver.get(url)
    
    def download_images(self,keyword,round):
        picpath = './data/'+keyword
        if not os.path.exists(picpath): os.makedirs(picpath)
        img_url_dic = []

        count = 0 
        pos = 0
        for i in range(round):
            pos += 500
            js = 'var q=document.documentElement.scrollTop=' + str(pos)
            self.driver.execute_script(js)
            time.sleep(1)

            img_elements = self.driver.find_elements_by_tag_name('img')
            #遍历抓到的webElement
            for img_element in img_elements:
                img_url = img_element.get_attribute('src')
                # 前几个图片的url太长，不是图片的url，先过滤掉，爬后面的
                if isinstance(img_url, str):
                    if len(img_url) <= 200:
                        #将干扰的goole图标筛去
                        if 'images' in img_url:
                            #判断是否已经爬过，因为每次爬取当前窗口，或许会重复
                            #实际上这里可以修改一下，将列表只存储上一次的url，这样可以节省开销，不过我懒得写了···
                            if img_url not in img_url_dic:
                                try:
                                    img_url_dic.append(img_url)
                                    #下载并保存图片到当前目录下
                                    filename = picpath+"/" + str(count) + ".jpg"
                                    r = requests.get(img_url)
                                    with open(filename, 'wb') as f:
                                        f.write(r.content)
                                    f.close()
                                    count += 1
                                    print('this is '+str(count)+'st img')
                                    #防止反爬机制
                                    time.sleep(0.2)
                                except:
                                    print('failure')
        
    def close(self):
        try:
            self.driver.close()
            self.driver.quit()
        except Exception as e:
            print(e)