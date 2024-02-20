import requests

class TestRefund:
    def test_ref_url(self):
        global allRepay, refund_compl, refund_pend, emiRepaymentStatus

        emiRepaymentStatus = requests.get(
            "https://lendittfinserve.com/prod/admin/emi/repaymentStatus?fromDate=2024-02-03T10:00:00.000Z&endDate=2024-02-07T10:00:00.000Z&type=TOTAL&page=1&download=true")

        allRepay = requests.get(
            "https://lendittfinserve.com/admin-prod/admin/transaction/allRepaidLoans?start_date=2024-02-04T10:00:00.000Z&end_date=2024-02-07T10:00:00.000Z&page=1&pagesize=10&getTotal=true&download=true")
        # print(allRepay.json())

        headers = {"adminid": "37"}
        # refund_compl = requests.get("https://lendittfinserve.com/stag/admin/transaction/getRefundableData",params={"startDate":"2024-02-01T10:00:00.000Z","endDate":"2024-02-05T10:00:00.000Z","status":1},headers=headers,verify=False)
        refund_compl = requests.get(
            "https://lendittfinserve.com/stag/admin/transaction/getRefundableData?startDate=2024-02-04T10:00:00.000Z&endDate=2024-02-08T10:00:00.000Z&status=1",
            headers=headers)

        refund_pend = requests.get(
            "https://lendittfinserve.com/stag/admin/transaction/getRefundableData?startDate=2024-02-01T10:00:00.000Z&endDate=2024-02-04T10:00:00.000Z&status=-1",
            headers=headers)

    def test_refund_amt_allRepay(self):
        global dupl_repay_lid,match_app_auto

        allRepay_data = allRepay.json()["data"]["rows"]

        # un_repay_lid = []
        # dupl_repay_lid = []

        app = []
        web = []
        auto = []

        full_pay_1 = []
        full_pay_2 = []
        full_pay_3 = []
        full_pay_4 = []
        fullpay = []

        emi1 = []
        emi2 = []
        emi3 = []
        emi4 = []

        for r in allRepay_data:
            if (r["EMI Types"] == "EMIPAY 1"):
                emi1.append(r["Loan id"])

            if (r["EMI Types"] == "EMIPAY 2"):
                emi2.append(r["Loan id"])

            if (r["EMI Types"] == "EMIPAY 3"):
                emi3.append(r["Loan id"])

            if (r["EMI Types"] == "EMIPAY 4"):
                emi4.append(r["Loan id"])


            if ((r["EMI Types"] == "EMIPAY 1") and (r["EMI Types"] == "EMIPAY 1")):

                if r["Repayment via"] == "APP":
                    app.append(r["Loan id"])

                elif r["Repayment via"] == "WEB":
                    web.append(r["Loan id"])

                elif r["Repayment via"] == "AUTODEBIT":
                    auto.append(r["Loan id"])


            if ((r["EMI Types"] == "EMIPAY 2") and (r["EMI Types"] == "EMIPAY 2")):

                    if r["Repayment via"] == "APP":
                        app.append(r["Loan id"])

                    elif r["Repayment via"] == "WEB":
                        web.append(r["Loan id"])

                    elif r["Repayment via"] == "AUTODEBIT":
                        auto.append(r["Loan id"])
                #

            if ((r["EMI Types"] == "EMIPAY 3") and (r["EMI Types"] == "EMIPAY 3")):

                    if r["Repayment via"] == "APP":
                        app.append(r["Loan id"])

                    elif r["Repayment via"] == "WEB":
                        web.append(r["Loan id"])

                    elif r["Repayment via"] == "AUTODEBIT":
                        auto.append(r["Loan id"])


            if ((r["EMI Types"] == "EMIPAY 4") and (r["EMI Types"] == "EMIPAY 4")):

                    if r["Repayment via"] == "APP":
                        app.append(r["Loan id"])

                    elif r["Repayment via"] == "WEB":
                        web.append(r["Loan id"])

                    elif r["Repayment via"] == "AUTODEBIT":
                        auto.append(r["Loan id"])


            if ("FULLPAY" in r["EMI Types"]):
                if "1" in r["EMI Types"]:
                    full_pay_1.append(r["Loan id"])

                if "2" in r["EMI Types"]:
                    full_pay_2.append(r["Loan id"])

                if "3" in r["EMI Types"]:
                    full_pay_3.append(r["Loan id"])

                if "4" in r["EMI Types"]:
                    full_pay_4.append(r["Loan id"])







        # for i in  full_pay_1:
        #     if i not in emi1:
        #         print(i)







        # print("fullpay::", fullpay)
        # print("emi1::", emi1)
        # print("emi2::", emi2)
        # print("emi3::", emi3)
        # print("emi4::", emi4)








        match_app_auto = []
        for ap in app:
            if ap in auto:
                match_app_auto.append(ap)

        match_web_auto = []
        for wb in web:
            if wb in auto:
                match_web_auto.append(wb)

        match_app_auto_FULLPAY = []
        for ap in app:
            if ap in auto:
                match_app_auto_FULLPAY.append(ap)




        # print("match_app_auto_FULLPAY::",match_app_auto_FULLPAY)




        print("match_app_auto::", match_app_auto)
        print("match_web_auto::", match_web_auto)



    # def test_ref_completed(self):
    #     refund_compl_data = refund_compl.json()["data"]["rows"]
    #
    #     refund_comp_loan_ids = []
    #     for rc in refund_compl_data:
    #         if rc["loanId"]:
    #             refund_comp_loan_ids.append(rc["loanId"])
    #
    #     ref_miss_compl = []
    #
    #     for dut in match_app_auto:
    #
    #         if dut not in refund_comp_loan_ids:
    #             ref_miss_compl.append(dut)
    #
    #     print("refund_comp_loan_ids::", refund_comp_loan_ids)
    #     print("ref_miss_compl::", ref_miss_compl)
    #
    #     # print("un_repay_lid",un_repay_lid)
    #     # print("dupl_repay_lid:: ", dupl_repay_lid)




