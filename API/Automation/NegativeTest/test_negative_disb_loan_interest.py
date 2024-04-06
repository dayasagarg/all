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

        disURL = requests.get("https://chinmayfinserve.com/admin-prod/admin/dashboard/allDisbursedLoans",
                              params={"start_date": f"{prevTimeStr}T10:00:00.000Z",
                                      "end_date": f"{currTimeStr}T10:00:00.000Z",
                                      "page": 1, "download": "true"})


    def test_disb_int_rate(self,url):

        disData = disURL.json()["data"]["rows"]

        l_id_intRate_less_85 = []
        l_id_intRate_above_1 = []

        for inte in disData:
            if float(inte["Interest Rate"].replace("%","")) < 0.085:
                # print("intRate",float(inte["Interest Rate"].replace("%","")))
                l_id_intRate_less_85.append(inte["Loan ID"])
            elif float(inte["Interest Rate"].replace("%","")) > 0.1:
                l_id_intRate_above_1.append(inte["Loan ID"])

        count_l_id_intRate_85 = len(l_id_intRate_less_85)
        count_l_id_intRate_1 = len(l_id_intRate_above_1)

        if count_l_id_intRate_85 > 0:
            print(f"Error:: Interest rate below 0.085% found :: l_id :: {count_l_id_intRate_85}")
            assert False
        else:
            print("*** Interest rate is not below 0.085% ***")


        if count_l_id_intRate_1 > 0:
            print(f"Error:: Interest rate above 0.1% found :: l_id :: {count_l_id_intRate_1}")
            assert False
        else:
            print("*** Interest rate is not above 0.1% ***")


        print("*** Test Execution Completed ***")


