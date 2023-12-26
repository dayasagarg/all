import pytest
import requests

response1 = requests.get(
    "https://lendittfinserve.com/prod/admin/dashboard/allDisbursedLoans?start_date=2023-12-22T10%3A00%3A00.000Z&end_date=2023-12-22T10%3A00%3A00.000Z&page=1&download=true")  # current date

# print(response1.json())

data = response1.json()["data"]["rows"]

# print(data)

for dis in data:
    # dis["Loan ID"]
    app_amt = dis['Approved amount']
    disb_amt = dis['Disbursed Amount']
    pro_fees_amt = dis['Processing fees']
    # print(pro_fees_amt,end="")

    pro_fees_form = 0.065 * app_amt
    # print(pro_fees_form)
    # print(pro_fees_amt)



    # print(dis)


