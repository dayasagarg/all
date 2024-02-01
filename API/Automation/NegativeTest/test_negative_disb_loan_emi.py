durl = None
class TestEMI:
    import pytest
    @pytest.fixture
    def url(self):
        print("### Test Execution Started ###")
        global durl
        import requests
        from datetime import datetime,timedelta
        currTime = datetime.now()
        currTimeStr = datetime.strftime(currTime, "%Y-%m-%d")

        prevTime = currTime - timedelta(days=4)
        prevTimeStr = datetime.strftime(prevTime, "%Y-%m-%d")

        durl = requests.get("https://lendittfinserve.com/admin-prod/admin/dashboard/allDisbursedLoans",
                            params={"start_date": f"{prevTimeStr}T10:00:00.000Z",
                                    "end_date": f"{currTimeStr}T10:00:00.000Z",
                                    "page": 1, "download": "true"})

    def test_emi_limit(self,url):

        durl_data = durl.json()["data"]["rows"]

        lIdEMI = []
        for d in durl_data:
            if (d["Total Emi"] < 3 or d["Total Emi"] > 4):
                lIdEMI.append(d["Loan ID"])


        count_lIdEMI = len(lIdEMI)

        if count_lIdEMI > 0:
            print(f"Error:: EMI not between 3 to 4 limit :: lIdEMI :: {lIdEMI}")
            assert False
        else:
            print("EMI's are within limit of 3 to 4")

        print("### Test Execution Completed ###")


