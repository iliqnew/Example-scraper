import scrapy
from selenium import webdriver
import time
import json

class MidiSatinSkirtSpider(scrapy.Spider):
    name = 'midi_satin_skirt'
    allowed_domains = ['shop.mango.com']
    start_urls = [
        'https://shop.mango.com/gb/women/skirts-midi/midi-satin-skirt_17042020.html?c=99',
    ]

    

    def parse(self, response):
        self.driver = webdriver.Firefox()
        self.driver.get(response.request.url)
        time.sleep(1)
        self.driver.find_element_by_id('onetrust-accept-btn-handler').click()
        time.sleep(1.5)
        self.driver.find_element_by_class_name('icon.closeModal.icon__close.desktop.confirmacionPais').click()
        
        name = self.driver.find_element_by_class_name('product-name').text
        price = float(self.driver.find_element_by_class_name('product-sale').text[1:])
        color = self.driver.find_element_by_class_name('colors-info-name').text
        size_selector_list = self.driver.find_element_by_class_name('selector-list')
        size_choices = size_selector_list.find_elements_by_xpath('span')
        sizes = [e.get_attribute("data-size") for e in size_choices]
        
        yield {
            'name': name,
            'price': price,
            'color': color,
            'size': sizes
        }
        