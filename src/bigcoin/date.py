import re
import datetime

# Global values
date_y_m_d_pattern = re.compile("^[0-9]{4}-[0-9]{2}-[0-9]{2}$")

# Test if a date format is valid. Format is YYYY-mm-dd
def is_date_format_yyyy_mm_dd_valid(date_string):
	if isinstance(date_string, basestring) and date_y_m_d_pattern.match(date_string):
		return True
	return False


# Return the given datetime as a string date format valid (YYYY-mm-dd). Return today's date if no datetime given
def get_date_string_yyyy_mm_dd_from_datetime(date_time):
	if not isinstance(date_time,datetime.datetime):
		date_time = datetime.datetime.today()
	return date_time.strftime("%Y-%m-%d")
