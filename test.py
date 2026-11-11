import unittest


class TestApplication(unittest.TestCase):

    def test_application(self):
        name = "VVCEkarn"
        self.assertEqual(name, "VVCE")


if __name__ == "__main__":
    unittest.main()
