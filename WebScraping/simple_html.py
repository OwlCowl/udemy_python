from bs4 import BeautifulSoup

SIMPLE_HTML = '''<html>
<head></head>
<body>
<h1>This is a title</h1>
<p class="subtitle">Lorem ipsum dolor sit amet. Consectetur edipiscim elit.</p>
<p>Here's another p without a class</p>
<ul>
    <li>Rolf</li>
    <li>Charlie</li>
    <li>Jen</li>
    <li>Jose</li>
</ul>
</body>
</html>'''


class Finder:
    def __init__(self):
        self.soup = BeautifulSoup(SIMPLE_HTML, 'html.parser')

    def find_title(self):
        tag = self.soup.find('title')
        return tag.string

    def find_list_items(self):
        list_items = self.soup.find_all('li')
        items = [item.string for item in list_items]
        return items

    def subtitle(self):
        paragraph = self.soup.find('p', {'class':'subtitle'})
        return paragraph.string

    def find_other_paragraph(self):
        paragraphs = self.soup.find_all('p')
        # print(paragraphs)
        other_paragraphs = [p for p in paragraphs if 'subtitle' not in p.attrs.get('class', [])]
        print(other_paragraphs[0].string)

elements = Finder()

elements.find_other_paragraph()