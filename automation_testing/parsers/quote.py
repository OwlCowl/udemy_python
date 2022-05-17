from locators.quote_locators import QuoteLocators


class QuoteParser:
    """ Given one of the specific quote divs,
     find out the data about quote"""

    def __init__(self, parent):
        self.parent = parent

    def __repr__(self):
        return f'Quote {self.content}, by {self.author}'

    @property
    def content(self):
        locator = QuoteLocators.CONTENT_LOCATOR
        return self.parent.find_element_by_css_selector(locator).text


    @property
    def author(self):
        locator = QuoteLocators.AUTHOR_LOCATOR
        return self.parent.find_element_by_css_selector(locator).text

    @property
    def tags(self):
        locator = QuoteLocators.TAGS_LOCATOR
        return self.parent.find_element_by_css_selectors(locator)

