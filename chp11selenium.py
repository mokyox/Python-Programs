#!/usr/bin/env python3

from selenium import webdriver
browser = webdriver.Firefox()
browser.get('https://www.google.com/?gws_rd=ssl')
elem = browser.find_element_by_css_selector('#lst-ib')
elem.send_keys('Hello world!')
elem.submit()
#browser.back(), browser.forward() - There are many methods.