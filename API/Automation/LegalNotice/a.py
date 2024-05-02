import requests
import pytest
from datetime import datetime, timedelta

currentFullTime = datetime.now()  # whole date
curr_str = datetime.strftime(currentFullTime,"%Y-%m-%d")

pre_15 = currentFullTime - timedelta(days=15)
pre_15_DateStr = datetime.strftime(pre_15, "%Y-%m-%d")

pre_5 = currentFullTime - timedelta(days=5) # 4-5
pre_5_DateStr = datetime.strftime(pre_5, "%Y-%m-%d")

pre_10 = pre_5 - timedelta(days=20)
pre_10_DateStr = datetime.strftime(pre_10, "%Y-%m-%d")


fillingInProgress = requests.get("https://chinmayfinserve.com/admin-prod/admin/legal/getAllLegalData",
                                 params={"page": 1, "startDate": f"{pre_10_DateStr}T10:00:00.000Z",
                                         "endDate": f"{pre_5_DateStr}T10:00:00.000Z", "type": 4, "adminId": 70,
                                         "download": "true"})

fillingInProgress_data = fillingInProgress.json()["data"]["rows"]

fillingInProgress_lid = []
for f in fillingInProgress_data:
    if f["Loan ID"]:
        fillingInProgress_lid.append(f["Loan ID"])

print("fillingInProgress_lid::",fillingInProgress_lid)
