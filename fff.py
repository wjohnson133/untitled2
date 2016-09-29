from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# import openpyxl
import requests
from lxml import html


page = requests.get('http://econpy.pythonanywhere.com/ex/001.html')
tree = html.fromstring(page, base_url="http://econpy.pythonanywhere.com/ex/001.html")
print treea

