import unittest

from entities.mechanics.stack import CardStack


class MyTestCase(unittest.TestCase):

    def test_stack_generation(self):
        test = CardStack()
        #print(test.getStack())

        self.assertEqual(len(test.getStack()), 32)


if __name__ == '__main__':
    unittest.main()
