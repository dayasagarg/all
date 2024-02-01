class TestNegInterest:
    import pytest
    @pytest.fixture
    def url(self):
        print("*** Test Execution Started ***")
        global disURL
        import requests
        from datetime import datetime,timedelta
        currTime = datetime.now()
        currTimeStr = datetime.strftime(currTime,"%Y-%m-%d")

        prevTime = currTime - timedelta(days=4)
        prevTimeStr = datetime.strftime(prevTime, "%Y-%m-%d")

        disURL = requests.get("https://lendittfinserve.com/admin-prod/admin/dashboard/allDisbursedLoans",
                              params={"start_date": f"{prevTimeStr}T10:00:00.000Z",
                                      "end_date": f"{currTimeStr}T10:00:00.000Z",
                                      "page": 1, "download": "true"})


    def test_disb_int_rate(self,url):

        disData = disURL.json()["data"]["rows"]

        l_id_int = []
        for inte in disData:
            if (inte["Interest Rate"] > 0.1 or inte["Interest Rate"] < 0.1):
                l_id_int.append(inte["Loan ID"])

        count_l_id_int = len(l_id_int)

        if count_l_id_int > 0:
            print(f"Error:: Interest rate above/below 0.1% found :: l_id_int :: {l_id_int}")
            assert False
        else:
            print("Interest rate is 0.1%")


        print("*** Test Execution Completed ***")


