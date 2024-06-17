import requests
import pytest
from datetime import datetime, timedelta

# uniqLIdListDemand = None

currentFullTime = datetime.now()  # whole date
curr_str = datetime.strftime(currentFullTime, "%Y-%m-%d")


print("curr_str::", curr_str)



# note: execute at 12 pm every time because of crone set time.

class TestLegal:
    @pytest.fixture
    def url(self):
        global legalDemandLetter, legalAutoDebit, legalNotice, legalNotice2, legalNotice3, caseAssigned, fillingInProgress_data
        # legalDemandLetter = requests.get("https://chinmayfinserve.com/admin-prod/admin/legal/getAllLegalData",
        #                                  params={"page": 1, "startDate": f"{start_date}T10:00:00.000Z",
        #                                          "endDate": f"{end_date}T10:00:00.000Z", "type": 1, "adminId": 134,
        #                                          "download": "true"})  # date = 6 days before notice sent
        #
        # legalNotice = requests.get("https://chinmayfinserve.com/admin-prod/admin/legal/getAllLegalData",
        #                            params={"page": 1, "startDate": f"{start_date_2}T10:00:00.000Z",
        #                                    "endDate": f"{end_date_2}T10:00:00.000Z", "type": 2, "adminId": 134,
        #                                    "download": "true"})  # current date

        caseAssigned = requests.get("https://chinmayfinserve.com/admin-prod/admin/legal/getAllLegalData",
                                    params={"page": 1, "startDate": f"{curr_str}T10:00:00.000Z",
                                            "endDate": f"{curr_str}T10:00:00.000Z", "type": 11, "adminId": 153,
                                            "download": "true"})


    # @pytest.mark.skip
    def test_case_assign_to_collection_1(self,url):
        global paidPrincipleInterest, principleInterest, cal_less_than_70, case_lid
        case_data = caseAssigned.json()["data"]["rows"]

        # print("case_data::",case_data)

        case_lid = []

        for c in case_data:

            if c["Loan ID"]:
                case_lid.append(c["Loan ID"])


        coll_emi_m_5k = []
        for e in case_lid:
            emiAPI = requests.get("https://chinmayfinserve.com/admin-prod/admin/loan/getEMIDetails",
                                  params={"loanId": e}, verify=False)

            emiAPI_data = emiAPI.json()["data"]["EMIData"]

            for n,ed in enumerate(emiAPI_data):

                emi_amt = ed["totalEmiAmount"]
                paid_emi_amt = ed["paidEmiAmount"]

                outs_emi = emi_amt - paid_emi_amt

                if outs_emi > 5000:
                    coll_emi_m_5k.append(e)


                print(f"lid::{e}")
                print("emi_amt::",emi_amt)
                print("paid_emi_amt::",paid_emi_amt)
                print("out_emi::",outs_emi)

        # print("coll_emi_m_5k::",coll_emi_m_5k)

        if len(coll_emi_m_5k) > 0:
            print(f"collection outstanding EMI amt not below 5k::{coll_emi_m_5k}")
            assert False
        else:
            print("*** collection outstanding EMI amt is below 5k ***")
















        #
        # count_perc_loanId = len(perc_loanId)
        # print("count_perc_loanId :: ", count_perc_loanId)
        #
        # if count_perc_loanId > 0:
        #     print(f"Error:: Paid percentage 100% found in case assigned to collection :: {perc_loanId}")
        #     # assert False
        # else:
        #     print("Paid percentage is below 100% in case assigned to collection")
