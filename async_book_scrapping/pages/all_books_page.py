import re
import logging

from bs4 import BeautifulSoup

from books_scraping.locators.all_books_page import AllBooksPageLocators
from books_scraping.parsers.book_parser import BookParser

logger = logging.getLogger('scrapping.all_books_page')


class AllBooksPage:
    def __init__(self, page_content):
        logger.debug('Parsing page with BeautifulSoup HTML parser')
        self.soup = BeautifulSoup(page_content, 'html.parser')

    @property
    def books(self):
        logger.debug(f'Here we have all books using "{AllBooksPageLocators.BOOKS}"')
        return [BookParser(e) for e in self.soup.select(AllBooksPageLocators.BOOKS)]

    @property
    def page_count(self):
        logger.debug(f'Finding all catalog books available...')
        content = self.soup.select_one(AllBooksPageLocators.PAGER).string
        logger.info(f'Find number of catalog available "{content}"')
        pattern = 'Page [0-9]+ of ([0-9]+)'
        matcher = re.search(pattern, content)
        pages = int(matcher.group(1))
        logger.debug(f'We extracted "{pages}" such amount of pages')
        return pages

