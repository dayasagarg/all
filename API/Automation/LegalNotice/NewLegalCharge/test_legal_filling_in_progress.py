import requests
import pytest
from datetime import datetime, timedelta

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

        case_data = caseAssigned.json()["data"]["rows"]

        # print("case_data::",case_data)

        case_lid = []

        for c in case_data:

            if c["Loan ID"]:
                case_lid.append(c["Loan ID"])

        print("case_lid::",case_lid)


        filling_in_progress_lid = []

        for c in fillingInProgress_data:

            if c["Loan ID"]:
                filling_in_progress_lid.append(c["Loan ID"])


        filling_in_progress_emi_m_5k = []
        for e in filling_in_progress_lid:
            emiAPI = requests.get("https://chinmayfinserve.com/admin-prod/admin/loan/getEMIDetails",
                                  params={"loanId": e}, verify=False)

            emiAPI_data = emiAPI.json()["data"]["EMIData"]

            emi_amt_e = []
            paid_emi_amt_e = []
            for n,ed in enumerate(emiAPI_data):

                emi_amt = ed["totalEmiAmount"]
                emi_amt_e.append(emi_amt)
                paid_emi_amt = ed["paidEmiAmount"]
                paid_emi_amt_e.append(paid_emi_amt)

            print(f"lid::{e}")
            print("emi_amt_l::",emi_amt_e)
            print("paid_emi_amt_l::",paid_emi_amt_e)


            emi_amt_l = sum(emi_amt_e)
            paid_emi_amt_l = sum(paid_emi_amt_e)

            print("emi_amt_l::",emi_amt_l)
            print("paid_emi_amt_l::",paid_emi_amt_l)

            outs_emi_l = emi_amt_l - paid_emi_amt_l
            print("outs_emi_l::", outs_emi_l)

            if outs_emi_l < 5000:
                filling_in_progress_emi_m_5k.append(e)

        # print("coll_emi_m_5k::",coll_emi_m_5k)

        filling_in_progress_emi_m_5k_drop_coll_lid = set(filling_in_progress_emi_m_5k) - set(case_lid)

        if len(filling_in_progress_emi_m_5k_drop_coll_lid) > 0:
            print(f"filling_in_progress outstanding EMI amt below 5k cases not assign to collection::{filling_in_progress_emi_m_5k_drop_coll_lid}")
            assert False
        else:
            print("*** filling_in_progress outstanding EMI amt below 5k cases are assigned to collection ***")

