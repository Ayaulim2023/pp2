from datetime import datetime, time

date1 = datetime.strptime('2015-01-01 01:00:00', '%Y-%m-%d %H:%M:%S')

date2 = datetime.now()
result = date2 - date1
print(result.days * 24 * 3600 + result.seconds,"seconds")
print()
