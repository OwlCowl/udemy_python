import requests
import logging
import aiohttp
import asyncio
import async_timeout
import time

from books_scraping.pages.all_books_page import AllBooksPage


logging.basicConfig(format='%(asctime)s %(levelname)s- 8s [%(filename)s:%(lineno)d] %(message)s',
                    datefmt='%d-%m-%Y %H:%M:%S',
                    level=logging.INFO,
                    filename = 'logs.txt')

logger = logging.getLogger('scrapping')
logger.info('Logging book list...')

page_content = requests.get("https://books.toscrape.com/").content
page = AllBooksPage(page_content)
books = page.books
loop = asyncio.get_event_loop()


async def fetch_page(session, url):
    page_start = time.time()
    async with async_timeout.timeout(10):
        async with session.get(url, ssl=False) as response:
            print(f'Page took {time.time() - page_start}')
            return await response.text()


async def get_multiple_pages(loop, *urls):
    tasks = []
    async with aiohttp.ClientSession(loop=loop, trust_env=True) as session:
        for url in urls:
            tasks.append(fetch_page(session, url))
        grouped_tasks = asyncio.gather(*tasks)
        return await grouped_tasks


urls = [f'https://books.toscrape.com/catalogue/page-{page_num+1}.html' for page_num in range(1, page.page_count)]

start = time.time()
pages = loop.run_until_complete(get_multiple_pages(loop, *urls))

print(f'All page request took {time.time() - start}')

for page_content in pages:
    page = AllBooksPage(page_content)
    books.extend(page.books)


