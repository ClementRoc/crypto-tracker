import unittest

from base import BaseTestCase


class RoutingTest(BaseTestCase):

    def test_home(self):
        response = self.client.get('/home', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_add(self):
        response = self.client.get('/add', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_edit(self):
        response = self.client.get('/edit', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_profit(self):
        response = self.client.get('/profit', content_type='html/text')
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
