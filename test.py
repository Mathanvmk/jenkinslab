import unittest


class TestApplication(unittest.TestCase):

    def test_application(self):
        name = "VVCEkar"
        self.assertEqual(name, "VVCE")


if __name__ == "__main__":
    unittest.main()
