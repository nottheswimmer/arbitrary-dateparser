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
                actual = self.parser(day.format(fmt), False)

                self.assertEqual(expected, actual,
                                 f'fmt = {fmt}, '
                                 f'fmt_str = {day}, '
                                 f'fmtted = {expected_day.format(fmt)}')

    def test_months(self):
        """
        Go through the entire year. For plain months, the current year is
        returned
        """
        start = pendulum.datetime(year=CURRENT_YEAR, month=1, day=1)
        end = start.end_of('year')

        for start_of_month in pendulum.period(start, end).range('months'):
            month = arbitrary_dateparser.MONTH_NAMES[start_of_month.month - 1]

            expected_raw = pendulum.period(start_of_month, start_of_month.end_of('month'))
            actual_full_raw = self.parser(month)
            actual_abbreviated_raw = self.parser(month[:3])

            # TODO: Stop cheating to ignore timezones and fix them in test.
            expected = (expected_raw.start.day_of_year, expected_raw.end.day_of_year)
            actual_full = (actual_full_raw.start.day_of_year, actual_full_raw.end.day_of_year)
            actual_abbreviated = (actual_abbreviated_raw.start.day_of_year,
                                  actual_abbreviated_raw.end.day_of_year)
            self.assertEqual(expected, actual_full,
                             f"For {month}, expected {expected} and got {actual_full}")
            self.assertEqual(expected, actual_abbreviated,
                             f"For {month[:3]}, expected {expected} and got {actual_abbreviated}")

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
