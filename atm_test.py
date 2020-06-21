import unittest
from features import *


class TestAtmNew(unittest.TestCase):
    def setUp(self):
        self.atm = Atm()
        self.balance = 10000
        self.attempts = 2
        self.atm.client_can_get_money = True


    def test_rise_money(self):
        self.assertEqual(self.atm.rise_money(500), 10500, "User can't add 500 money")

    def test_rise_money_boundary_values(self):
        self.assertEqual(self.atm.rise_money(99999999999999999999), 100000000000000009999, "User can't add much money")
        self.assertEqual(self.atm.rise_money(0.01), 10000.01, "User can't add tight money")
        self.assertEqual(self.atm.rise_money(0), 10000, "User can't add 0 money")

    def test_rise_money_negative_meaning(self):
        self.assertEqual(self.atm.rise_money(-1), 10000, "User can't rise negative meaning")

    def test_rise_money_twice(self):
        first_add = self.atm.rise_money(300)
        second_add = first_add + 400
        self.assertEqual(self.atm.rise_money(700), 10700, "User can't added money twice")

    def test_get_money(self):
        self.assertEqual(self.atm.get_money(1000), 1000, "User can't get 1000 money")

    def test_get_money_boundary_values(self):
        self.assertEqual(self.atm.get_money(0.01), 0.01, "User can't get tight money")
        self.assertEqual(self.atm.get_money(9999.99), 9999.99, "User can't get money")
        self.assertEqual(self.atm.get_money(0), 0, "User can't get zero money")

    def test_negative_meaning(self):
        self.assertEqual(self.atm.get_money(-1), 0, "User can't get negative value")

    def test_get_money_withdraw_more_money_than_on_the_account(self):
        self.assertEqual(self.atm.get_money(10500), self.balance)

    def test_get_money_withdraw_more_money_than_on_the_account_boundary_values(self):
        self.assertEqual(self.atm.get_money(10000.01), self.balance)

    def test_check_balance(self):
        self.assertEqual(self.atm.check_balance(), 10000, "User can't check balance")


























