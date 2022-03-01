import unittest
from nomadapp_front import send_filters_to_api as grt


class TestSpreadsheetApi(unittest.TestCase):
    def test_hello(self):
        grt.hello()
        self.assertEqual(True, True, "I leave Python!")


if __name__ == "__main__":
    unittest.main()
