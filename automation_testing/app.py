from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from pages.quotes_page import QuotesPage, InvalidTagForAuthorError


try:
    author = input("Input the author you want to: ")
    tag = input('Enter your  tag: ')
    s=Service('/Users/yana/Documents/chromdriver/chromedriver')
    chrome = webdriver.Chrome(service=s)
    chrome.get('http://quotes.toscrape.com/search.aspx')
    page = QuotesPage(chrome)

    print(page.search_for_quotes(author, tag))
except InvalidTagForAuthorError as e:
    print(e)
except Exception as e:
    print(e)
    print('Unknown error accure - please repeat')



