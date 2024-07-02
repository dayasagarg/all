import requests
import json
import math
from datetime import datetime




currentFullTime = datetime.now() # whole date
currentDateStr = datetime.strftime(currentFullTime,"%Y-%m-%d") # date to string format


class TestRepayment:
    def test_getRepayment(self):
        print("currentDateStr::", currentDateStr)
        global userStuck
        userStuck = requests.get(
            "https://chinmayfinserve.com/admin/analysis/getUserStuckData", params={"stage":"IN_PROGRESS","page":1,"start_date":f"{currentDateStr}T10:00:00.000Z","end_date":f"{currentDateStr}T10:00:00.000Z","download":"true",
            })  # current date

        # print("userStuck::", userStuck)

        userStuckD = userStuck.json()["data"]["rows"]
        print("userStuckD::",userStuckD)


        # user_id = []

        # for uid in userStuckD:
        #
        #     if uid["userId"]:
        #
        #         user_id.append(uid["userId"])
        #         # print(i["Loan id"])
        #
        #     else:
        #         pass


        # print("uids::", user_id)

        #
        # for u in user_id:
        #
        #     response = requests.get(
        #         "https://chinmayfinserve.com/v4/user/routeDetails", params={"id":u,"isRefresh":"true"},
        #         verify=False)  # current date
        #
        #
        #     print(response.json())
        #
        #     rot = response.json()["data"]