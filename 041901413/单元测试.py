import unittest

from main import test

class MyTestCase(unittest.TestCase):
    def test1(self):
        self.assertEqual(test("./words1.txt", "./org1.txt")[0], "Line1: <二维码> ErWM")

    def test2(self):
        self.assertEqual(test("./words1.txt", "./org2.txt")[0], "Line1: <二维码> 二维码")

    def test3(self):
        self.assertEqual(test("./words1.txt", "./org3.txt")[0], "Line1: <二维码> erweima")

    def test4(self):
        self.assertEqual(test("./words1.txt", "./org4.txt")[0], "Line1: <二维码> 儿为麻")

    def test5(self):
        self.assertEqual(test("./words1.txt", "./org5.txt")[0], "Line1: <二维码> er为M")

    def test6(self):
        self.assertEqual(test("./words1.txt", "./org6.txt")[0], "Line1: <二维码> 二维###!麻")

    def test7(self):
        self.assertEqual(test("./words1.txt", "./org7.txt")[0], "Line1: <二维码> ewm")

    def test8(self):
        self.assertEqual(test("./words1.txt", "./org8.txt")[0], "Line1: <二维码> 二威ma")

    def test9(self):
        self.assertEqual(test("./words1.txt", "./org9.txt")[0], "Line1: <二维码> 二威***m")

    def test10(self):
        self.assertEqual(test("./words1.txt", "./org10.txt")[0], "Line1: <二维码> er为12马")


if __name__ == '__main__':
    unittest.main()
