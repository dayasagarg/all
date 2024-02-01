import requests
from datetime import datetime,timedelta

currTime = datetime.now()
currTimeStr = datetime.strftime(currTime, "%Y-%m-%d")

prevTime = currTime - timedelta(days=4)
prevTimeStr = datetime.strftime(prevTime, "%Y-%m-%d")



disAPI = requests.get("https://lendittfinserve.com/admin-prod/admin/dashboard/allDisbursedLoans",
                      params={"start_date": f"{prevTimeStr}T10:00:00.000Z",
                              "end_date": f"{currTimeStr}T10:00:00.000Z",
                              "page": 1, "download": "true"})

# dis_lid = []
# for dis in disAPI:
#     if dis["Loan ID"]:
#         dis_lid.append(dis["Loan ID"])

loanAgrAPI = requests.get("http://lendittfinserve.com/prod/admin/esign/getLoanAgreement",
                      params={"loanId": f"{729602}", "verify": "False"})


print(loanAgrAPI.json()["data"]["eSign_agree_data"]["loanAmount"])





















