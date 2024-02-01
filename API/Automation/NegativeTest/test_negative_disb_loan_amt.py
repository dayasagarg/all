class TestAppAmt:
    import pytest
    @pytest.fixture
    def url(self):
        print("*** Test execution started ***")

        global disAPI
        import requests
        from datetime import datetime,timedelta

        currTime = datetime.now()
        currTimeStr = datetime.strftime(currTime,"%Y-%m-%d")

        prevTime = currTime - timedelta(days=4)
        prevTimeStr = datetime.strftime(prevTime, "%Y-%m-%d")



        disAPI = requests.get("https://lendittfinserve.com/admin-prod/admin/dashboard/allDisbursedLoans",
                              params={"start_date": f"{prevTimeStr}T10:00:00.000Z",
                                      "end_date": f"{currTimeStr}T10:00:00.000Z",
                                      "page": 1, "download": "true"})

    def test_dis_loan_amt_lower(self, url):

        global disbData
        disbData = disAPI.json()["data"]['rows']
        # print(disbData)

        loanID = []
        for d in disbData:
            # print(d)
            if d["Approved amount"] <= 5000:
                loanID.append(d["Loan ID"])
        # print(loanID)

        count_loan = len(loanID)

        if count_loan > 0:
            print(f"Error::Approved amount is below Rs.5000 found :: loanID :: {loanID}")
            assert False
        else:
            print("Approved amount is above Rs.5000")

    def test_dis_loan_amt_upper(self):

        l_Id_upper = []
        for da in disbData:
            if da["Approved amount"] > 100000:
                l_Id_upper.append(da["Loan ID"])

        count_l_Id_upper = len(l_Id_upper)

        if count_l_Id_upper > 0:
            print(f"Error:: Approved amount is above Rs.100000 (1 lac) found :: l_Id_upper :: {l_Id_upper}")
            assert False
        else:
            print("Approved amount is below Rs.100000 (1 lac)")

        print("*** Test execution completed ***")
