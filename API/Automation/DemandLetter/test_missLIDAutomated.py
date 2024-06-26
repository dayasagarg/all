import pytest
import requests
from datetime import datetime, timedelta

currentFullTime = datetime.now()  # whole date
currentDateStr = datetime.strftime(currentFullTime, "%Y-%m-%d")  # date to string format
currentDateF = datetime.strptime(currentDateStr, "%Y-%m-%d")  # string to date format

previousDate1 = currentDateF - timedelta(days=15)
previousDateStr1 = datetime.strftime(previousDate1, "%Y-%m-%d")

previousDate2 = currentDateF - timedelta(days=1)
previousDateStr2 = datetime.strftime(previousDate2, "%Y-%m-%d")

previousDate3 = currentDateF - timedelta(days=14)
previousDateStr3 = datetime.strftime(previousDate3, "%Y-%m-%d")


# print("currentDateStr::", currentDateStr)
# print("previousDateStr1::", previousDateStr1)
# print("previousDateStr2::", previousDateStr2)
# print("previousDateStr3::", previousDateStr3)

# curl --location 'https://https://chinmayfinserve.com/admin-prod/admin/legal/getAllLegalData?page=1&startDate=2023-09-12T10%3A00%3A00.000Z&endDate=2023-09-12T10%3A00%3A00.000Z&type=1&adminId=65'
# curl --location 'https://chinmayfinserve.com/admin-prod/admin/dashboard/todayAutoDebitData?start_date=2023-09-11T10%3A00%3A00.000Z&end_date=2023-09-11T10%3A00%3A00.000Z&status=9&page=1&Download=true'

# FAILED
# AD NOT PLACED


class TestMissedLID:
    @pytest.fixture
    def url(self):
        global response, response2
        # Auto-debit failed
        response = requests.get(
            "https://chinmayfinserve.com/admin-prod/admin/emi/repaymentStatus",
            params={"fromDate": f"{previousDateStr1}T10:00:00.000Z", "endDate": f"{previousDateStr2}T10:00:00.000Z",
                    "type": "TOTAL", "page": 1, "download": "true"})  # previous date

        # Demand letter (Legal)
        response2 = requests.get("https://chinmayfinserve.com/admin-prod/admin/legal/getAllLegalData",
                                 params={"page": 1, "startDate": f"{previousDateStr3}T10:00:00.000Z",
                                         "endDate": f"{currentDateStr}T10:00:00.000Z", "type": 1, "adminId": 65,
                                         "download": "true", "verify": False})  # current date

    def test_getAutoDebitFailAndDemandLetter(self, url):
        print("currentDateStr::", currentDateStr)
        print("previousDateStr1::", previousDateStr1)
        print("previousDateStr2::", previousDateStr2)
        print("previousDateStr3::", previousDateStr3)
        global demandLetterLoanId_notSent
        # '''getting loan id of AutoDebitFail'''

        rows = []
        allEMiList = response.json()["data"]['rows']
        for el in allEMiList:
            if el["Today's EMI status"] == 'FAILED' or el["Today's EMI status"] == 'AD NOT PLACED' or el["Today's EMI status"] == 'Response pending':
                rows.append(el)

        # print('status code of get AutoDebitFail::', response.status_code)
        # print(response.json())

        # print("rows::",rows)

        autoDebitFailed_adnotPlaced_LoanId = []

        # '''loan id of AutoDebitFail api into AutoDebitFail list'''  'AD Response date': '-'
        for i in rows:
            if i["Today's EMI status"] == 'FAILED' or i["Today's EMI status"] == 'AD NOT PLACED' or i["Today's EMI status"] == 'Response pending':
                autoDebitFailed_adnotPlaced_LoanId.append(i['Loan ID'])
                # print(i)


        print("autoDebitFailed_adnotPlaced_LoanId::", autoDebitFailed_adnotPlaced_LoanId)
        print("Count of autoDebitFailed_adnotPlaced_LoanId::", len(autoDebitFailed_adnotPlaced_LoanId))

        autoDebitNotPlaced = []
        autoDebitResponsePending = []
        adRespnseDateDash = []

        for j in rows:
            if "Today's EMI status" in j == 'AD NOT PLACED':
                autoDebitNotPlaced.append(j['Loan ID'])

            if j["Today's EMI status"] == 'Response pending':
                autoDebitResponsePending.append(j['Loan ID'])

            if j["AD Response date"] == '-':
                adRespnseDateDash.append(j['Loan ID'])


        print("Auto Debit not placed (AD NOT PLACED status)::", autoDebitNotPlaced)
        print("Count of auto debit not placed (AD NOT PLACED status)::", len(autoDebitNotPlaced))

        print("Auto Debit response pending::", autoDebitResponsePending)
        print("Count of auto debit response pending::", len(autoDebitResponsePending))

        # print("Auto Debit adRespnseDateDash::", adRespnseDateDash)
        # print("Count of auto debit adRespnseDateDash::", len(adRespnseDateDash))

        # print("r-d::",set(autoDebitResponsePending) - set(adRespnseDateDash))
        # print("r-d_count::", len(set(autoDebitResponsePending) - set(adRespnseDateDash)))

        # print('status code of get DemandLetter::', response2.status_code)
        # print('valid::', response2.json())

        # '''getting loan id of DemandLetter api'''
        rows2 = response2.json()["data"]["rows"]
        # print(rows2)

        demandLetterLoanId = []
        demandLetterLoanId_notSent = []

        ''' adding loan id of DemandLetter api into DemandLetterLoanId list'''
        for i in rows2:
            if "Loan ID" in i:
                demandLetterLoanId.append(i['Loan ID'])

            if i["Sent on email"] == "Not sent":
                demandLetterLoanId_notSent.append(i['Loan ID'])

        print("DemandLetterLoanId::", demandLetterLoanId)
        print("Count of DemandLetterLoanId::", len(demandLetterLoanId))

        matchedLID = []

        for i in autoDebitFailed_adnotPlaced_LoanId:
            if i in demandLetterLoanId:
                matchedLID.append(i)
                # print("matchedLID ::",i)

        print("matchedLID::", matchedLID)
        print("count of matchedLID::", len(matchedLID))

        missedLID = []

        for i in autoDebitFailed_adnotPlaced_LoanId:
            if i not in demandLetterLoanId:
                missedLID.append(i)
                # print("missed loan id::",i)

        print("missedLID::", missedLID)
        count_of_missed_lid = len(missedLID)
        print("count of missedLID::", count_of_missed_lid)



        if len(missedLID) == 0:
            print("*** All auto-debit failed are listed in demand letter including ad not placed ***")
        else:
            print(f"Error::Auto-debit failed loan ids are missing in demand letter including ad not placed::{missedLID}")

        assert len(missedLID) == 0, "All auto-debit failed loan ids are not present in demand letter"


        duplicateDemandLetter = []
        uniqDemand = []
        for d in demandLetterLoanId:
            if d not in uniqDemand:
                uniqDemand.append(d)
            else:
                duplicateDemandLetter.append(d)

        print("duplicateDemandLetter::", duplicateDemandLetter)
        print("count_of_duplicateDemandLetter::", len(duplicateDemandLetter))

        if len(duplicateDemandLetter) == 0:
            print("*** No duplicate found in demand letter ***")
        else:
            print("Error::Duplicate found in demand letter")

        assert len(duplicateDemandLetter) == 0


    def test_DemandLetter(self, url):

        if len(demandLetterLoanId_notSent) == 0:
            print("*** All demand letter sent as per api status ***")
        else:
            print(f"Error:: demand letter not sent found :: {demandLetterLoanId_notSent}")

        assert len(demandLetterLoanId_notSent) == 0