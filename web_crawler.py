from abc import ABC,abstractclassmethod

class WebCrawler(ABC):
    @abstractclassmethod
    def __init__(self):
        pass
    
    @abstractclassmethod
    def connect_page(self):
        pass
    
    @abstractclassmethod
    def close(self):
        pass