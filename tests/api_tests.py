from api.sentiment import get_sentimet
import unittest


class API_Tests(unittest.TestCase):
    def test_ms_api(self):
        self.assertGreater(get_sentimet("good good"), 0.4)

if __name__ == '__main__':
    unittest.main()