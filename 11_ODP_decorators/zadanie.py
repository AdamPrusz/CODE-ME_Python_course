# Sprawdźmy czy dzień nie wypada w oficjalne święto, wystarczy nam moduł holidays



import holidays

pl_holidays = holidays.Polish()
>>> '1/1/2019' in pl_holidays
True
>>> '2010-01-06' in pl_holidays
False
>>> '2012-01-06' in pl_holidays
True
>>> pl_holidays.get('2019-01-06')
'Święto Trzech Króli'


today = datetime.date.today()
print(today, 'zajęcia się odbywają:', Student.academic_day(today))

saturday = datetime.datetime.strptime('2019-06-22', '%Y-%m-%d')
print(saturday, 'zajęcia się odbywają:', Student.academic_day(saturday))

sunday = datetime.date.today() - datetime.timedelta(days=1)
print(sunday, 'zajęcia się odbywają:', Student.academic_day(sunday))
