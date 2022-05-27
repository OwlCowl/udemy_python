from unittest import TestCase
from unittest.mock import patch
from page import PageRequester

class PageRequester(TestCase):
    def setUp(self):
        self.page = PageRequester("http://google.com")

    def test_make_request(self):
        with patch("request.get") as mocked_get:
            self.page.get()
            mocked_get.assert_called()

    def test_content_return(self):
        fake_content = 'Hello'

        class FakeResponse:
            def __init(self):
                self.content = 'Hello'

        with patch("request.get", return_value=FakeResponse()) as mocked_get:
            result = self.page.get()
            self.assertEqual(result, fake_content)