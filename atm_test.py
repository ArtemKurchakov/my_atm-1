import unittest
from features import *


class TestAtmNew(unittest.TestCase):
    def setUp(self):
        self.atm = Atm()
        self.balance = 10000
        self.attempts = 2
        # self.client_can_get_money = False


    def test_rise_money(self):
        self.assertEqual(self.atm.rise_money(0), 10000, "User can't add 0 money")
        self.assertEqual(self.atm.rise_money(500), 10500, "User can't add 500 money")
        self.assertEqual(self.atm.rise_money(99999999999999999999), 100000000000000009999, "User can't add much money")
        self.assertEqual(self.atm.rise_money(0.01), 10000.01, "User can't add tight money")

    def test_rise_money_twice(self):
        self.first_add = self.atm.rise_money(300)
        self.second_add = self.first_add + 400
        self.assertEqual(self.atm.rise_money(700), 10700, "User can't added money twice")

    def test_get_money(self):
        self.assertEqual(self.atm.get_money(0.01), 0.01, "User can't get tight money")
        self.assertEqual(self.atm.get_money(9999.99), 9999.99, "User can't get money")
        self.assertEqual(self.atm.get_money(0), 0, "User can't get zero money")

    def test_negative_meaning(self):
        self.assertEqual(self.atm.get_money(-1), 0, "User can't get negative value")

    def test_check_balance(self):
        self.assertFalse(self.atm.check_balance(), "User can't check balance")







