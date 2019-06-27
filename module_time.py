from datetime import datetime
import calendar

def cal_now():
	c = calendar.TextCalendar(0)
	return c.formatyear(2019)
	return

def time_now():
	return datetime.now()
