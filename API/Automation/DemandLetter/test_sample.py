import pytest
import requests


# curl --location 'https://chinmayfinserve.com/admin-prod/admin/legal/getAllLegalData?page=1&startDate=2023-09-12T10%3A00%3A00.000Z&endDate=2023-09-12T10%3A00%3A00.000Z&type=1&adminId=65'
# curl --location 'https://chinmayfinserve.com/admin-prod/admin/dashboard/todayAutoDebitData?start_date=2023-09-11T10%3A00%3A00.000Z&end_date=2023-09-11T10%3A00%3A00.000Z&status=9&page=1&Download=true'

# FAILED
# AD NOT PLACED


class TestMissedLID:
    @pytest.fixture
    def url(self):
        global response, response2
        # Auto-debit failed
        response = requests.get(
            "https://chinmayfinserve.com/admin-prod/admin/emi/repaymentStatus?fromDate=2024-02-14T10:00:00.000Z&endDate=2024-02-16T10:00:00.000Z&type=TOTAL&page=1&download=true")  # previous date

        # Demand letter (Legal)
        response2 = requests.get("https://chinmayfinserve.com/admin-prod/admin/legal/getAllLegalData?page=1&startDate=2024-02-15T10:00:00.000Z&endDate=2024-02-17T10:00:00.000Z&type=1&adminId=65&download=true&verify=False")  # current date

    def test_getAutoDebitFailAndDemandLetter(self, url):
        global demandLetterLoanId_notSent
        # '''getting loan id of AutoDebitFail'''
        rows = []
        allEMiList = response.json()["data"]['rows']
        for el in allEMiList:
            if el["Today's EMI status"] == 'FAILED' or el["Today's EMI status"] == 'AD NOT PLACED':
                rows.append(el)

        # print('status code of get AutoDebitFail::', response.status_code)
        # print(response.json())

        autoDebitFailNotPlacedLoanId = []

        # ''' adding loan id of AutoDebitFail api into AutoDebitFail list'''
        for i in rows:
            if "Loan ID" in i:
                autoDebitFailNotPlacedLoanId.append(i['Loan ID'])
                # print(i)

        print("autoDebitFailNotPlacedLoanId::", autoDebitFailNotPlacedLoanId)
        print("Count of autoDebitFailNotPlacedLoanId::", len(autoDebitFailNotPlacedLoanId))

        autoDebitNotPlaced = []

        for i in rows:
            if "Today's EMI status" == 'AD NOT PLACED':
                autoDebitNotPlaced.append(i)

        print("Auto Debit not placed::", autoDebitNotPlaced)
        print("Count of auto debit not placed::", len(autoDebitNotPlaced))

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

        for i in autoDebitFailNotPlacedLoanId:
            if i in demandLetterLoanId:
                matchedLID.append(i)
                # print("matchedLID ::",i)

        print("matchedLID::", matchedLID)
        print("count of matchedLID::", len(matchedLID))

        missedLID = []

        for i in autoDebitFailNotPlacedLoanId:
            if i not in demandLetterLoanId:
                missedLID.append(i)
                # print("missed loan id::",i)

        print("missedLID::", missedLID)
        count_of_missed_lid = len(missedLID)
        print("count of missedLID::", count_of_missed_lid)

        if count_of_missed_lid == 0:
            print("All auto-debit failed loan ids are present in demand letter")
        else:
            print(f"Error::Auto-debit failed loan ids are missing in demand letter:: {missedLID}")

        assert count_of_missed_lid == 0, "All auto-debit failed loan ids are present in demand letter"


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
            print("No duplicate found in demand letter")
        else:
            print("Error::Duplicate found in demand letter")

        assert len(duplicateDemandLetter) == 0


    def test_DemandLetter_notsent(self, url):

        if len(demandLetterLoanId_notSent) == 0:
            print("*** All demand letter sent ***")
        else:
            print(f"Error:: demand letter not sent found:: {demandLetterLoanId_notSent}")

        assert len(demandLetterLoanId_notSent) == 0