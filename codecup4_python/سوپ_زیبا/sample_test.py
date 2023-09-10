from bs4 import BeautifulSoup
import unittest
import sys

# sys.path.append('../Initial_project')
from HTMLParser import *


class Test(unittest.TestCase):
    def setUp(self):
        with open("test/html-doc.txt", 'r') as file:
            doc = file.read()
        self.parser = BeautifulSoup(doc, "html.parser")
        self.test_obj = HTMLParser(doc)

    def test_find_first_simple(self):
        values = {
            "class": "section"
        }
        tag_name = self.test_obj.find_first("name", **values)
        self.assertEqual(tag_name, self.parser.find(**values).name)
        tag_string = self.test_obj.find_first("string", name="ul")
        self.assertEqual(tag_string, self.parser.find(name="ul").get_text())

    def test_find_first_advance(self):
        values = {
            "name": "div",
            "class": "section",
            "id": "navigating-the-tree"
        }
        tag_string = self.test_obj.find_first("string", **values)
        self.assertEqual(tag_string, self.parser.find(**values).get_text())

    def test_find_all(self):
        values = {
            'name': 'p',
        }
        test__list = self.test_obj.find_all(10, 'string', **values)
        results= self.parser.find_all(**values, limit=10)
        real_list = [res.get_text()for res in results]
        self.assertEqual(test__list, real_list)

if __name__ == '__main__':
    unittest.main()