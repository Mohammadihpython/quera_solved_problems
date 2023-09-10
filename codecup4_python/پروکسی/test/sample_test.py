import unittest
import sys
sys.path.append('../Initial_project')
from proxy import *


class Hi:
    def __init__(self):
        self.number = 0

    def f1(self):
        pass

    def f2(self):
        pass


class Test(unittest.TestCase):
    def test_sample_1(self):
        str_proxy = Proxy("test_string")
        self.assertTrue(isinstance(str_proxy, Proxy))
        t = Hi()
        proxy = Proxy(t)
        proxy.number = 6
        self.assertEqual(6, proxy.number)

    def test_sample_2(self):
        proxy = Proxy("Test String")
        proxy.upper()
        self.assertEqual("upper", proxy.last_invoked_method())
        try:
            proxy.no_such_method()
            self.assertFalse(True)
        except Exception as e:
            self.assertEqual("No Such Method", str(e))

        self.assertEqual(1, proxy.count_of_calls("upper"))
        self.assertEqual(0, proxy.count_of_calls("capitalize"))

    def test_sample_3(self):
        proxy = Proxy(Hi())
        proxy.f1()
        self.assertTrue(proxy.was_called("f1"))
        self.assertFalse(proxy.was_called("f2"))
        proxy.f2()
        self.assertTrue(proxy.was_called("f2"))
        self.assertFalse(proxy.was_called("not valid"))

    def test_sample_4(self):
        t = Hi()
        proxy = Proxy(t)

        try:
            proxy.last_invoked_method()
        except Exception as e:
            self.assertEqual("No Method Is Invoked", str(e))

        proxy.f1()
        proxy.f2()
        self.assertEqual("f2", proxy.last_invoked_method())
        
        
if __name__ == '__main__':
    unittest.main()