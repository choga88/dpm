import datetime
now = datetime.datetime.now()
print(now) 

nowdate = now.strftime('%Y-%m-%d')
print(nowdate)

nowtime = now.strftime('%H:%M:%S')
print(nowtime)

nowdatetime = now.strftime('%Y-%m-%d %H:%M:%S')
print(nowdatetime)

print(nowdate +" "+ nowtime) 
