import requests
import pytest
from datetime import datetime, timedelta

# uniqLIdListDemand = None

currentFullTime = datetime.now()  # whole date
curr_str = datetime.strftime(currentFullTime, "%Y-%m-%d")


print("curr_str::", curr_str)


class TestLegal:
    @pytest.fixture
    def url(self):
        global fillingInProgress, fillingInProgress_data, caseAssigned
        fillingInProgress = requests.get("https://chinmayfinserve.com/admin-prod/admin/legal/getAllLegalData",
                                         params={"page": 1, "startDate": f"{curr_str}T10:00:00.000Z",
                                                 "endDate": f"{curr_str}T10:00:00.000Z", "type": 4, "adminId": 70,
                                                 "download": "true"})

        fillingInProgress_data = fillingInProgress.json()["data"]["rows"]

        caseAssigned = requests.get("https://chinmayfinserve.com/admin-prod/admin/legal/getAllLegalData",
                                    params={"page": 1, "startDate": f"{curr_str}T10:00:00.000Z",
                                            "endDate": f"{curr_str}T10:00:00.000Z", "type": 11, "adminId": 153,
                                            "download": "true"})



    # @pytest.mark.skip
    def test_filling_in_progress_to_collection(self,url):
        global paidPrincipleInterest, principleInterest, cal_less_than_70, case_lid


        filling_in_progress_lid = []

        for c in fillingInProgress_data:

            if c["Loan ID"]:
                filling_in_progress_lid.append(c["Loan ID"])


        filling_in_progress_emi_m_5k = []
        for e in filling_in_progress_lid:
            emiAPI = requests.get("https://chinmayfinserve.com/admin-prod/admin/loan/getEMIDetails",
                                  params={"loanId": e}, verify=False)

            emiAPI_data = emiAPI.json()["data"]["EMIData"]

            for n,ed in enumerate(emiAPI_data):

                emi_amt = ed["totalEmiAmount"]
                paid_emi_amt = ed["paidEmiAmount"]

                outs_emi = emi_amt - paid_emi_amt

                if outs_emi > 5000:
                    filling_in_progress_emi_m_5k.append(e)


                print(f"lid::{e}")
                print("emi_amt::",emi_amt)
                print("paid_emi_amt::",paid_emi_amt)
                print("out_emi::",outs_emi)

        # print("coll_emi_m_5k::",coll_emi_m_5k)

        if len(filling_in_progress_emi_m_5k) > 0:
            print(f"filling_in_progress outstanding EMI amt not below 5k::{filling_in_progress_emi_m_5k}")
            assert False
        else:
            print("*** filling_in_progress outstanding EMI amt is below 5k ***")






