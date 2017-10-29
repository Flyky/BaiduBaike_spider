#-*- coding: utf-8 -*-

from baike_spider import url_manager, html_downloader, html_parser, result_outputer
from urllib.parse import quote


class SpiderMain(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.UrlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = result_outputer.ResultOutputer()
        
    
    def craw(self, rootURL, times, htmlName):
        print(times)
        count = 1
        
        self.urls.add_new_url(rootURL)
        while self.urls.has_next_url():
            try:
                next_url = self.urls.get_next_url()
                print('crawing no.%d: %s' %(count, next_url))
                html_content = self.downloader.download(next_url)
                new_urls, new_data = self.parser.parse(next_url, html_content)
                self.urls.add_new_urls(new_urls)
                self.outputer.collect_data(new_data)
                
                if count == int(times):
                    break
                
                count = count + 1
            except Exception as e:
                print('Error:', e)
                print('crawing failed this time')
            
        self.outputer.output_html(htmlName)
        print('Crawing finished')
    
    



if __name__=='__main__':
    rootURL = 'https://baike.baidu.com/item/'
    searchKey = input('Please input the keyword:')
    rootURL = rootURL+quote(searchKey)
    times = input("Please input the crawing deep times: ")
    outputHTML = input('Please input the name of the output file: ')
    objSpider = SpiderMain()
    objSpider.craw(rootURL, times, outputHTML)