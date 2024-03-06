import requests
emi = requests.get("https://lendittfinserve.com/admin-prod/admin/loan/getEMIDetails", params={"loanId": 728731})
emi_data = emi.json()["data"]["EMIData"]

for d in emi_data:
    print(d)




