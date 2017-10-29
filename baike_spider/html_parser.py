#-*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import re
from urllib.parse import urljoin, quote

class HtmlParser(object):
    
    
    def _get_new_urls(self, page_url, soup):
        new_urls = set()
        #/item/abc...
        links = soup.find_all('a', href=re.compile(r'/item/.*'))
        for link in links:
            new_url = link['href']
            new_full_url = urljoin(page_url, new_url)
            new_urls.add(new_full_url)
        return new_urls
    
    
    def _get_new_data(self, page_url, soup):
        res_data = {}
        
        #url
        res_data['url'] = page_url
        
        '''
        <dd class="lemmaWgt-lemmaTitle-title">
        <h1>Python</h1>
        <h2>xxx</h2>
        '''
        
        title_node = soup.find('dd', class_="lemmaWgt-lemmaTitle-title").find('h1')
        title_small_node = soup.find('dd', class_="lemmaWgt-lemmaTitle-title").find('h2')
        
        title = title_node.get_text()
        if title_small_node != None:
            title = title + title_small_node.get_text()
        res_data['title'] = title
        
        '''
        <div class="lemma-summary" label-module="lemmaSummary">
        <div class="para" label-module="para">Python��һ���������Ľ�����......</div
        '''
        summary_node = soup.find('div', class_='lemma-summary')
        res_data['summary'] = summary_node.get_text()
        return res_data
    
    def parse(self, page_url, html_content):
        if page_url is None or html_content is None:
            return 
        
        soup = BeautifulSoup(html_content, 'lxml', from_encoding='utf-8')
        new_urls = self._get_new_urls(page_url, soup)
        new_data = self._get_new_data(page_url, soup)
        return new_urls, new_data
        
    
    



