import datetime

from django.test import TestCase

from portal_core.utils.bank import (get_bank_openday, get_bank_openday_earlier,
                                    get_bank_openday_later)


class BankTests(TestCase):
    """ 銀行営業日関係のユーティリティ """
    def setUp(self):
        self.datelist = [
            (
             datetime.date(2019, 1, 31),
             datetime.date(2019, 1, 31),
             datetime.date(2019, 1, 31),
            ),
            (
             datetime.date(2019, 2, 28),
             datetime.date(2019, 2, 28),
             datetime.date(2019, 2, 28),
            ),
            (
             datetime.date(2019, 3, 31),
             datetime.date(2019, 3, 29),
             datetime.date(2019, 4, 1),
            ),
            (
             datetime.date(2019, 4, 30),
             datetime.date(2019, 4, 26),
             datetime.date(2019, 5, 7),
            ),
            (
             datetime.date(2019, 8, 31),
             datetime.date(2019, 8, 30),
             datetime.date(2019, 9, 2),
            ),
        ]

    def test_get_bank_openday(self):
        for target_date, earlier_date, later_date in self.datelist:
            _earlier_date, _later_date = get_bank_openday(target_date)
            self.assertEqual(_earlier_date, earlier_date)
            self.assertEqual(_later_date, later_date)

    def test_get_bank_openday_earlier(self):
        for target_date, earlier_date, _ in self.datelist:
            _earlier_date = get_bank_openday_earlier(target_date)
            self.assertEqual(_earlier_date, earlier_date)

    def test_get_bank_openday_later(self):
        for target_date, _, later_date in self.datelist:
            _later_date = get_bank_openday_later(target_date)
            self.assertEqual(_later_date, later_date)


