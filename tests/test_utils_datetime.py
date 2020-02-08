import datetime

from django.test import TestCase

from portal_core.utils.datetime import (get_nth_weekday, get_month_last,
                                        get_next_year_month, get_prev_year_month)


class DateTimeTests(TestCase):
    """ 日付関係のユーティリティ """

    def test_get_nth_weekday(self):
        test_cases = [
            ({'year': 2017, 'month': 5, 'weekday': 6 ,'n': 2}, datetime.date(2017, 5, 14)),
            ({'year': 2017, 'month': 5, 'weekday': 6 ,'n': 4}, datetime.date(2017, 5, 28)),
            ({'year': 2019, 'month': 11, 'weekday': 5 ,'n': 5}, datetime.date(2019, 11, 30)),
        ]
        test_cases_error = [
            {'year': 2017, 'month': 0, 'weekday': 6 ,'n': 0},
            {'year': 2017, 'month': 13, 'weekday': 6 ,'n': 0},
            {'year': 2017, 'month': 13, 'weekday': 0 ,'n': 0},
            {'year': 2017, 'month': 13, 'weekday': 7 ,'n': 0},
            {'year': 2017, 'month': 5, 'weekday': 6 ,'n': 0},
            {'year': 2017, 'month': 5, 'weekday': 6 ,'n': 6},
        ]

        for kwargs, date_obj in test_cases:
            self.assertEqual(get_nth_weekday(**kwargs), date_obj)

        for kwargs in test_cases_error:
            with self.assertRaises(ValueError):
                self.assertEqual(get_nth_weekday(**kwargs))

    def test_get_month_last(self):
        test_cases = [
            (datetime.date(2019, 2, 1), datetime.date(2019, 2, 28)),
            (datetime.date(2019, 6, 1), datetime.date(2019, 6, 30)),
            (datetime.date(2019, 6, 30), datetime.date(2019, 6, 30)),
            (datetime.date(2019, 12, 1), datetime.date(2019, 12, 31)),
            (datetime.date(2020, 2, 1), datetime.date(2020, 2, 29)),
        ]
        test_cases_error = [
            '2019/12/1',
        ]

        for obj, date_obj in test_cases:
            self.assertEqual(get_month_last(obj), date_obj)

        for obj in test_cases_error:
            with self.assertRaises(ValueError):
                self.assertEqual(get_month_last(obj))


    def test_get_next_year_month(self):
        test_cases = [
            ((2019, 1), (2019, 2)),
            ((2019, 12), (2020, 1)),
        ]
        test_cases_error = [
            ((2019, 13), ValueError),
        ]

        for year_month, next_year_month in test_cases:
            self.assertEqual(get_next_year_month(*year_month), next_year_month)

        for year_month, error in test_cases_error:
            with self.assertRaises(error):
                self.assertEqual(get_next_year_month(*year_month))

    def test_get_prev_year_month(self):
        test_cases = [
            ((2019, 1), (2018, 12)),
            ((2019, 12), (2019, 11)),
        ]
        test_cases_error = [
            ((2019, 13), ValueError),
        ]

        for year_month, prev_year_month in test_cases:
            self.assertEqual(get_prev_year_month(*year_month), prev_year_month)

        for year_month, error in test_cases_error:
            with self.assertRaises(error):
                self.assertEqual(get_prev_year_month(*year_month))
