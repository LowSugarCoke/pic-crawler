from abc import ABC,abstractclassmethod
from web_crawler import WebCrawler

class CatchImage(WebCrawler):
    @abstractclassmethod
    def __init__(self):
        pass
    
    @abstractclassmethod
    def connect_page(self):
        pass
    
    @abstractclassmethod
    def close(self):
        pass
    
    @abstractclassmethod
    def download_images(self):
        pass
    
    @abstractclassmethod
    def run(self):
        pass