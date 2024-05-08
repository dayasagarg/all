import math

class TestDisbMonthlyLoanFigure:
    import pytest
    @pytest.fixture
    def url_dis(self):
        global disAPI, requests
        import requests
        from datetime import datetime, timedelta

        curr = datetime.now()
        curr_str = datetime.strftime(curr, "%Y-%m-%d")
        prev = curr - timedelta(days=30)
        pre_str = datetime.strftime(prev, "%Y-%m-%d")

        disAPI = requests.get("https://chinmayfinserve.com/admin-prod/admin/dashboard/allDisbursedLoans",
                              params={"start_date": f"{pre_str}T10:00:00.000Z",
                                      "end_date": f"{curr_str}T10:00:00.000Z",
                                      "page": 1, "download": "true"})


    def test_disb_cibil_new_user(self, url_dis):
        print("*** Test execution started ***")
        global disData


        disData = disAPI.json()["data"]["rows"]


        # print(disData)

        new_users = []
        repeat_users = []

        disb_amt = []
        int_amt = []

        for d in disData:
            if d["Completed loans"] == 0:
                new_users.append(d["Loan ID"])

            if d["Completed loans"] > 0:
                repeat_users.append(d["Loan ID"])

            if d["Disbursed Amount"]:
                disb_amt.append(d["Disbursed Amount"])

            if d["Total Interest Amount"]:
                int_amt.append(d["Total Interest Amount"])

            if d["Total Interest Amount"]:
                int_amt.append(d["Total Interest Amount"])


        new_users_count = len(new_users)
        repeat_users = len(repeat_users)

        total_disb_loans_count = new_users_count + repeat_users

        print("new_users_count_disb::",new_users_count)
        print("repeat_users_disb::",repeat_users)
        print("total/approved_disb_loans_count::",total_disb_loans_count)

        print("disb_amt::",disb_amt)
        total_disb_amt = sum(disb_amt)
        total_int_amt = sum(int_amt)

        print("total_disb_amt::",total_disb_amt)
        print("total_int_amt::",total_int_amt)




