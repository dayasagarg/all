class TestSalAmt:
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



        disAPI = requests.get("https://chinmayfinserve.com/admin-prod/admin/dashboard/allDisbursedLoans",
                              params={"start_date": f"{prevTimeStr}T10:00:00.000Z",
                                      "end_date": f"{currTimeStr}T10:00:00.000Z",
                                      "page": 1, "download": "true"})

    def test_dis_salary_amt_lower(self, url):

        global disbData
        disbData = disAPI.json()["data"]['rows']
        # print(disbData)

        loanID_sal = []
        for s in disbData:
            # print(d)
            if s["Approved salary"] < 20000:
                loanID_sal.append(s["Loan ID"])
        # print(loanID)

        count_loan_sal = len(loanID_sal)

        if count_loan_sal > 0:
            print(f"Error:: Loan accepted if Approved Salary is below Rs.20000 found :: loanID :: {loanID_sal}")
            assert False
        else:
            print("*** Approved Salary for loan is above Rs.20000 / Loan rejected if Approved Salary is below Rs.20000 ***")

