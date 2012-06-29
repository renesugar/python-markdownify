import unittest
from markdownify import markdownify as md


class BasicTests(unittest.TestCase):

    def test_single_tag(self):
        self.assertEqual(md('<span>Hello</span>'), 'Hello')

    def test_soup(self):
        self.assertEqual(md('<div><span>Hello</div></span>'), 'Hello')


class EscapeTests(unittest.TestCase):

    def test_underscore(self):
        self.assertEqual(md('_hey_dude_'), '\_hey\_dude\_')


class ConversionTests(unittest.TestCase):

    def test_b(self):
        self.assertEqual(md('<b>Hello</b>'), '**Hello**')

    def test_em(self):
        self.assertEqual(md('<em>Hello</em>'), '*Hello*')

    def test_h1(self):
        self.assertEqual(md('<h1>Hello</h1>'), 'Hello\n=====\n\n')

    def test_h2(self):
        self.assertEqual(md('<h2>Hello</h2>'), 'Hello\n-----\n\n')

    def test_hn(self):
        self.assertEqual(md('<h3>Hello</h3>'), '### Hello\n\n')
        self.assertEqual(md('<h6>Hello</h6>'), '###### Hello\n\n')

    def test_i(self):
        self.assertEqual(md('<i>Hello</i>'), '*Hello*')

    def test_ol(self):
        self.assertEqual(md('<ol><li>a</li><li>b</li></ol>'), '1. a\n2. b\n')

    def test_p(self):
        self.assertEqual(md('<p>hello</p>'), 'hello\n\n')

    def test_strong(self):
        self.assertEqual(md('<strong>Hello</strong>'), '**Hello**')

    def test_ul(self):
        self.assertEqual(md('<ul><li>a</li><li>b</li></ul>'), '* a\n* b\n')