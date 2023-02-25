from datetime import date,timedelta

x = date.today()
y = date.today()-timedelta(days=1)
z = date.today()+timedelta(days=1)

print("Today",x)
print("Yesterday",y)
print("Tomorrow",z)