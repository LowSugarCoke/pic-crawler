# -*- coding: utf-8 -*-
"""
@author: Jack Lee
Reference: https://www.cxymm.net/article/qq_34687559/106340929

How to use:

import google_catch_image

crawler_lib = google_catch_image.GoogleCatchImage()   
keyword = 'cat'
url = 'https://www.google.com.hk/search?q='+keyword+'&tbm=isch'
round = 70  #download image numbers
headless = False #(default is False, don't show by setting True) 

crawler_lib.run(url,keyword,headless=headless,round=round)

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

            #catch "img" label
            img_elements = self.driver.find_elements_by_tag_name('img')
            
            for img_element in img_elements:
                img_url = img_element.get_attribute('src')
                # insinstance(img_url,str) -> make sure type is str
                # len(img_url)<=200 -> url too long is not image
                # 'images' in img_url -> filter google logo
                # img_url not in img_url_dic -> make sure image not to download repeatly
                if isinstance(img_url, str) and len(img_url)<=200 and 'images' in img_url and img_url not in img_url_dic:
                    #download picture to local
                    try:
                        img_url_dic.append(img_url)
                        filename = picpath+"/" + str(count) + ".jpg"
                        r = requests.get(img_url)
                        with open(filename, 'wb') as f:
                            f.write(r.content)
                            f.close()
                        count += 1
                        print('this is '+str(count)+'st img')
                        
                        time.sleep(0.2)
                    except:
                        print('failure')
        
    def close(self):
        try:
            self.driver.close()
            self.driver.quit()
        except Exception as e:
            print(e)