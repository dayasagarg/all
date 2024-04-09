import pytest
import requests
from datetime import datetime

currentFullTime = datetime.now()
currentDate = datetime.strftime(currentFullTime, "%Y-%m-%d")
print("currentDate::",currentDate)


class TestMissedLIDInRepayment:
    @pytest.fixture
    def url(self):
        global response, response2
        # Upcoming EMI
        response = requests.get(
            "https://chinmayfinserve.com/admin-prod/admin/emi/getUpcomingEmi",
            params={"page": 1, "pagesize": 10, "start_date": f"{currentDate}T10:00:00.000Z",
                    "end_date": f"{currentDate}T10:00:00.000Z", "emiStatus": 2, "download": "true"},
            verify=False)  # current date


        response2 = requests.get(
            "https://chinmayfinserve.com/admin-prod/admin/emi/repaymentStatus",
            params={"fromDate":f"{currentDate}T10:00:00.000Z", "endDate":f"{currentDate}T10:00:00.000Z", "type": "TOTAL",
                    "page": 1, "download": "true",
                    "verify": False})  # current date

    def test_getEMIAndRepayment(self, url):
        # '''getting loan id of Upcoming EMI'''
        rows = response.json()["data"]["rows"]
        # print(rows)

        # print('status code of get Upcoming EMI::', response.status_code)
        # print(response.json())
        # print(response.json()["data"]["rows"])

        upcomingEMILoanId = []

        # ''' adding loan id of Upcoming EMI api into upcomingEMILoanId list'''
        for i in rows:
            if "Loan Id" in i:
                upcomingEMILoanId.append(i['Loan Id'])
                # print(i)

        print("UpcomingEMILoanId::", upcomingEMILoanId)
        print("Count of UpcomingEMILoanId::", len(upcomingEMILoanId))

        # # Demand letter (Legal)

        # print('status code of get repayment::', response2.status_code)
        # print('valid::', response2.json())

        # '''getting loan id of repayment api'''
        rows2 = response2.json()["data"]["rows"]
        # print("rows2::",rows2)

        repaymentLoanId = []
        lid_except_rp_comp_fail = []
        ad_not_placed = []


        ''' adding loan id of repayment api into repaymentLoanId list'''
        for j in rows2:
            if "Loan ID" in j:
                repaymentLoanId.append(j['Loan ID'])

            if j["Today's EMI status"] != "Response pending" and j["Today's EMI status"] != "COMPLETED" and j["Today's EMI status"] != "FAILED":
                lid_except_rp_comp_fail.append(j["Loan ID"])

            if j["Today's EMI status"] == "AD NOT PLACED":
                ad_not_placed.append(j["Loan ID"])

        print("RepaymentLoanId::", repaymentLoanId)
        print("Count of repaymentLoanId::", len(repaymentLoanId))

        print("lid_except_rp_comp_fail::",lid_except_rp_comp_fail)
        print("ad_not_placed::",ad_not_placed)
        print("count_lid_except_rp_comp_fail::", len(lid_except_rp_comp_fail))
        print("count_ad_not_placed::", len(ad_not_placed))

        matchedLID = []

        for k in upcomingEMILoanId:
            if k in repaymentLoanId:
                matchedLID.append(k)
                # print("matchedLID ::",k)

        print("matchedLID::", matchedLID)
        print("count of matchedLID::", len(matchedLID))

        missedLID = []

        for l in upcomingEMILoanId:
            if l not in repaymentLoanId:
                missedLID.append(l)
                # print("missed loan id::",l)

        print("missedLID::", missedLID)
        count_of_missed_lid = len(missedLID)
        print("count of missedLID::", count_of_missed_lid)

        if count_of_missed_lid == 0:
            print("All upcoming EMI Loan IDs are present in repayment API")
        else:
            print("Error::Upcoming EMI Loan IDs are missing in repayment API")

        assert count_of_missed_lid == 0, "All upcoming EMI Loan IDs are present in repayment API / auto-debit list"
        print("******************************************************************************")


