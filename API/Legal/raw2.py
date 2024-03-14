from datetime import datetime, timedelta
import requests


# uniqLIdListDemand = None

currentFullTime = datetime.now()  # whole date
curr_str = datetime.strftime(currentFullTime,"%Y-%m-%d")

end_2 = datetime.strftime(currentFullTime, "%Y-%m-%d")  # date to string format
end_2_F = datetime.strptime(end_2, "%Y-%m-%d")  # string to date format

start_2 = end_2_F - timedelta(days=15)
start_2_DateStr = datetime.strftime(start_2, "%Y-%m-%d")

print("curr_str::",curr_str)
print("start_2_DateStr::",start_2_DateStr)


summons = requests.get("https://lendittfinserve.com/admin-prod/admin/legal/getAllLegalData",params={"page":1,"startDate":f"{start_2_DateStr}T10:00:00.000Z","endDate":f"{curr_str}T10:00:00.000Z","type":6,"adminId":70,"download":"true"})
summons_data = summons.json()["data"]["rows"]
summons_data_count = summons.json()["data"]["count"]


# print("summons_data::",summons_data_count)
# print("summons_data::",summons_data)






