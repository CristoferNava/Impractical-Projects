# car -> arcay
# apple -> appleway

# ixnay on the ottenray
# ixnay -> ixnayway
# on -> onway
# the -> hetay
# ottenray -> ottenrayway

import unittest

from pig_latin import to_pig_latin


class TestPigLatin(unittest.TestCase):
    def test_to_pig_latin(self):
        self.assertEqual(to_pig_latin("car"), "arcay")
        self.assertEqual(to_pig_latin("apple"), "appleway")
        self.assertEqual(to_pig_latin("ixnay"), "ixnayway")
        self.assertEqual(to_pig_latin("on"), "onway")
        self.assertEqual(to_pig_latin("the"), "hetay")
        self.assertEqual(to_pig_latin("ottenray"), "ottenrayway")


if __name__ == "__main__":
    unittest.main()
