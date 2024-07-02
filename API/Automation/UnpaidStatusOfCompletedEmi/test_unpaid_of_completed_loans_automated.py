import requests
from datetime import datetime,timedelta

import json
import math


f_lid = []


currentFullTime = datetime.now() # whole date
currentDateStr = datetime.strftime(currentFullTime,"%Y-%m-%d") # date to string format

currentDateF = datetime.strptime(currentDateStr,"%Y-%m-%d")
print("currentDateStr::",currentDateStr)

currentDateStr_emi = datetime.strftime(currentFullTime,"%d/%m/%Y")
print("currentDateStr_emi::",currentDateStr_emi)


previousDate = currentDateF - timedelta(days=2)
previousDateStr = datetime.strftime(previousDate,"%Y-%m-%d")

previousDate_1 = currentDateF - timedelta(days=1)
previousDateStr_emi_1 = datetime.strftime(previousDate,"%d/%m/%Y")


class TestRepayment:
    def test_getRepayment(self):
        global totalUnpaidAmountForm
        responseAllLoanID = requests.get(
            "https://chinmayfinserve.com/admin-prod/admin/transaction/allRepaidLoans", params={"start_date":f"{previousDateStr}T10:00:00.000Z","end_date":f"{currentDateStr}T10:00:00.000Z","page":1,"pagesize":10,"getTotal":"true","download":"true",
            "verify":"False"})  # current date

        '''getting loan ids from Repayment'''
        loanIDs = responseAllLoanID.json()["data"]["rows"]
        # print(loanIDs)
        match = []
        missMatch = []
        lIDs = []
        for lid in loanIDs:

            if lid["Loan id"]:

                lIDs.append(lid["Loan id"])
                # print(i["Loan id"])

            else:
                pass

        print("lids::", lIDs)
        print('count of unique lids::', len(lIDs))

        unpaid = []
        withoutUnpaid = []
        paid_0 = []
        unpaid_in_p = []
        unpaid_in_p_current_emi_repaym = []

        # Upcoming EMI
        for n,i in enumerate(lIDs):

            response = requests.get(
                "https://chinmayfinserve.com/admin-prod/admin/loan/getEMIDetails", params={"loanId": i},
                verify=False)  # current date

            # print('status code of get Repayment::', response.status_code)
            # print(response.json())
            sData = response.json()
            # jdata = json.dumps(sData,indent=2)
            # print(jdata)

            # print(response.headers)
            # print(response.content)

            '''getting EMIData data of Repayment'''
            emiData = response.json()["data"]["EMIData"]
            # print(emiData)

            # EMI Data
            paymentType = []
            status = []


            for eD in emiData:
                # if "Payment type" in eD:
                #     paymentType.append(eD['Payment type'])
                #     # print(i['EMI date'])
                #
                # if "Paid" in eD:
                #     status.append(eD['Paid'])


                if ((eD["paymentType"] == "FULLPAY") and (eD["status"] == "UNPAID")) or ((eD["paymentType"] == "EMIPAY") and (eD["status"] == "UNPAID")):
                    if eD["unpaidPenalty"] == 0:
                        unpaid.append(i)

                else:
                    withoutUnpaid.append(i)


                if eD["status"] == "PAID":
                    if eD["totalPaidAmount"] == 0 or eD["paidEmiAmount"] == 0:
                        paid_0.append(i)

                    if eD["totalUnpaidAmount"] > 0:
                        unpaid_in_p.append(i)

                    if (eD["emiDate"] == currentDateStr_emi or eD["emiDate"] == previousDateStr_emi_1) or (eD["repaymentDate"] == currentDateStr_emi or eD["repaymentDate"] == previousDateStr_emi_1):
                        if eD["totalUnpaidAmount"] > 0:
                            unpaid_in_p_current_emi_repaym.append(i)


        if len(unpaid_in_p_current_emi_repaym) == 0:
            print("*** No unpaid into paid for current date ***")
        else:
            print(f" E :: unpaid into paid for current date:: {unpaid_in_p_current_emi_repaym} ")


        if len(unpaid_in_p) == 0:
            print("*** No unpaid into paid ***")
        else:
            print(f" E :: unpaid into paid :: {set(unpaid_in_p)} ")


        if len(paid_0) == 0:
            print("*** No paid with 0 found ***")
        else:
            print(f"E:: paid with 0 found::{set(paid_0)}")


        if len(unpaid) == 0:
            print("*** No unpaid found ***")
        else:
            print(f"Error:: unpaid found::{set(unpaid)}")

        assert len(unpaid) == 0

