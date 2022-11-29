import unittest
from unittest.mock import patch
from sqsprovider import SqsProvider

#@patch('sqsprovider.SqsProvider.send', return_value=[1,2])
@patch('sqsprovider.SqsProvider')
class TestStringMethods(unittest.TestCase):

    def test_upper(self, target):
        target.send.return_value = [1,2]
        result = target.send("test")
        self.assertTrue(result == [1,2])
        target.send.assert_called_once_with("test")
        target.receive.assert_not_called()
    
if __name__ == '__main__':
    unittest.main()