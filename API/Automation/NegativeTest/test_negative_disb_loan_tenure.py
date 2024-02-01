class TestLoanTenure:
    import pytest
    @pytest.fixture
    def url(self):
        global dApi
        import requests
        from datetime import datetime,timedelta
        currTime = datetime.now()
        currTimeStr = datetime.strftime(currTime, "%Y-%m-%d")

        prevTime = currTime - timedelta(days=4)
        prevTimeStr = datetime.strftime(prevTime, "%Y-%m-%d")


        dApi = requests.get("https://lendittfinserve.com/admin-prod/admin/dashboard/allDisbursedLoans",
                            params={"start_date": f"{prevTimeStr}T10:00:00.000Z",
                                    "end_date": f"{currTimeStr}T10:00:00.000Z",
                                    "page": 1, "download": "true"})

    def test_loan_tenure(self,url):
        l_data = dApi.json()["data"]["rows"]

        loan_id_tenure = []
        for lt in l_data:
            if  (lt["Loan Tenure (Days)"] < 90 or lt["Loan Tenure (Days)"]>120):
                loan_id_tenure.append(lt["Loan ID"])


        count_l_data = len(loan_id_tenure)

        if count_l_data > 0:
            print(f"Errors::loan tenure more than 120 days and less than 90 days found :: loan_id_tenure :: {loan_id_tenure}")
            assert False
        else:
            print("loan tenure is within 90 to 120 days")



