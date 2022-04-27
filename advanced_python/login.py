import logging

logging.basicConfig(format='%(asctime)s,%(msecs)d %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
    datefmt='%Y-%m-%d:%H:%M:%S',
    level=logging.DEBUG,
                    filename = 'logs.txt')
logger = logging.getLogger('books')

#childlogger of books, config from books will be inherit
logger = logging.getLogger('books.database')

logger.info('This will not show up')
logger.warning('This will')

"""
DEBUG
INFO
WARNING
ERROR
CRITICAL
"""