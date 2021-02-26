import unittest
import orgochemvisualizer.chemanim as ca


class ExampleTest(unittest.TestCase):

    def test_generic(self):
        self.assertTrue(True)
        self.assertFalse(False)
        self.assertEqual(4.31, 4.31)
        self.assertEqual("this is an example test", "this is an example test")


if __name__ == '__main__':
    unittest.main()
