# coding: utf-8

from icalendar import Calendar, Event
from datetime import datetime, timedelta
import ircalevents
from calverter import Calverter
persiancal = Calverter()
cal = Calendar()
cal['summary'] = u'تقویم اتفاقات تقویم شمسی'

for year in [1397]:
	for month in range(1, 13):
		for day in range(1, 32):
			events = ircalevents.get_day_events(year, month, day)
			jd = persiancal.jalali_to_jd(year, month, day)
			gro = persiancal.jd_to_gregorian(jd)
			print (gro)
			for item in events:
				event = Event()
				event.add('summary', item)
				today = datetime(gro[0], gro[1], gro[2])
				event.add('dtstart', today)
				event.add('dtend', today+timedelta(days=1))
				cal.add_component(event)

#cal['dtstart'] = '20050404T080000'

result = cal.to_ical()
file_ = open('irantaghvim.ical', 'wb')
file_.write(result)
file_.close()
