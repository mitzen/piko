import unittest
from unittest.mock import patch
from sqsprovider import SqsProvider

@patch('sqsprovider.SqsProvider.send', return_value=[1,2])
class TestStringMethods(unittest.TestCase):

    def test_upper(self, target):
        result = SqsProvider.send("test")
        self.assertTrue(result == [1,2])

if __name__ == '__main__':
    unittest.main()