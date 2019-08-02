import unittest

import pendulum

import arbitrary_dateparser

START = pendulum.datetime(2018, 6, 1)
END = pendulum.datetime(2019, 6, 1)
CURRENT_YEAR = pendulum.today().now().year
DATE_FORMATS = arbitrary_dateparser.DateParser().date_formats


class TestDateParser(unittest.TestCase):
    def setUp(self):
        self.parser = arbitrary_dateparser.DateParser()

    def test_single_day(self):
        for fmt in DATE_FORMATS:
            for day in pendulum.period(START, END).range('days'):
                if 'YY' not in fmt:
                    try:
                        expected_day = pendulum.parse(str(day)).set(year=CURRENT_YEAR)
                    except ValueError:
                        # This should only happen for leap years
                        self.assertTrue(day.is_leap_year())
                        continue
                else:
                    expected_day = pendulum.parse(str(day))
                expected = pendulum.period(expected_day,
                                           expected_day.end_of('day'))
                actual = self.parser(day.format(fmt))

                self.assertEqual(expected, actual,
                                 f'fmt = {fmt}, '
                                 f'fmt_str = {day}, '
                                 f'fmtted = {expected_day.format(fmt)}')

    def test_period_phrases(self):
        expected_dates = self.parser.period_phrases
        actual_dates = dict()
        for key in expected_dates.keys():
            actual_dates[key] = self.parser(key)
        for key in expected_dates.keys():
            self.assertEqual((key, expected_dates[key]), (key, actual_dates[key]))


class TestDateParserWithoutPeriods(unittest.TestCase):
    def setUp(self):
        self.parser = arbitrary_dateparser.DateParser(support_periods=False)

    def test_date_phrases(self):
        expected_dates = self.parser.date_phrases

        # Runtime sensitivity. Test elsewhere.
        expected_dates.pop('now')

        actual_dates = dict()
        for key in expected_dates.keys():
            actual_dates[key] = self.parser(key)
        for key in expected_dates.keys():
            self.assertEqual((key, expected_dates[key]), (key, actual_dates[key]))


if __name__ == '__main__':
    unittest.main()
