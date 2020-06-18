import unittest
from features import *


class TestAtmNew(unittest.TestCase):
    def setUp(self):
        self.atm = Atm()
        self.balance = 10000
        self.attempts = 2
        self.pin = 777


    def test_rise_money(self):
        self.assertEqual(self.atm.rise_money(0), 10000)
        self.assertEqual(self.atm.rise_money(500), 10500)
        self.assertEqual(self.atm.rise_money(99999999999999999999), 100000000000000009999)
        self.assertEqual(self.atm.rise_money(0.01), 10000.01)

