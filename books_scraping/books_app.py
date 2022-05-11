import requests
import logging

from books_scraping.pages.all_books_page import AllBooksPage


logging.basicConfig(format='%(asctime)s %(levelname)s- 8s [%(filename)s:%(lineno)d] %(message)s',
                    datefmt='%d-%m-%Y %H:%M:%S',
                    level=logging.INFO,
                    filename = 'logs.txt')

logger = logging.getLogger('scrapping')
logger.info('Logging book list...')

page_content = requests.get("https://books.toscrape.com/").content
#build page object
page = AllBooksPage(page_content)

books = page.books

for page_num in range(1, page.page_count):
    default_url = f'https://books.toscrape.com/catalogue/page-{page_num+1}.html'
    page_content = requests.get(default_url).content
    page = AllBooksPage(page_content)
    books.extend(page.books)
