
import unittest
import bigcoin.date as bcdate
import datetime

class TestDate(unittest.TestCase):

    def test_is_date_format_yyyy_mm_dd_valid(self):
		self.assertTrue(bcdate.is_date_format_yyyy_mm_dd_valid("2011-05-22"))
		self.assertFalse(bcdate.is_date_format_yyyy_mm_dd_valid("2011.05.22"))
		self.assertFalse(bcdate.is_date_format_yyyy_mm_dd_valid("2011_05_22"))
		self.assertFalse(bcdate.is_date_format_yyyy_mm_dd_valid("11-05-22"))
		self.assertFalse(bcdate.is_date_format_yyyy_mm_dd_valid("2011-5-22"))
		self.assertFalse(bcdate.is_date_format_yyyy_mm_dd_valid("2011-05-2"))
		self.assertFalse(bcdate.is_date_format_yyyy_mm_dd_valid("201-05-2"))
		self.assertFalse(bcdate.is_date_format_yyyy_mm_dd_valid(""))
		self.assertFalse(bcdate.is_date_format_yyyy_mm_dd_valid(54))

    def test_get_date_string_yyyy_mm_dd_from_datetime(self):
        today_string = datetime.datetime.today().strftime("%Y-%m-%d")
        self.assertEquals(bcdate.get_date_string_yyyy_mm_dd_from_datetime(datetime.datetime(2018,2,18)),"2018-02-18")
        self.assertEquals(bcdate.get_date_string_yyyy_mm_dd_from_datetime(None),today_string)
if __name__ == "__main__":
    unittest.main()
