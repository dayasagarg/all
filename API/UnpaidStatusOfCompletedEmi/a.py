from datetime import datetime,timedelta

currentFullTime = datetime.now() # whole date
currentDateStr = datetime.strftime(currentFullTime,"%Y-%m-%d") # date to string format
currentDateF = datetime.strptime(currentDateStr,"%Y-%m-%d")
# print("currentDateStr::",currentDateStr)



previousDate = currentDateF - timedelta(days=3)
previousDateStr = datetime.strftime(previousDate,"%Y-%m-%d")

# print("previousDateStr::",previousDateStr)