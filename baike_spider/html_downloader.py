#-*- coding: utf-8 -*-
from urllib.request import urlopen

class UrlDownloader(object):
    
    
    def download(self, url):
        if url is None:
            return None
        
        res = urlopen(url)

        if res.getcode() != 200:
            return None
        return res.read()
    
    



