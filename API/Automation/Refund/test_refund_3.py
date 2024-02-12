import requests


class TestRefund:
    def test_ref_url(self):
        global allRepay, refund_compl, refund_pend, emiRepaymentStatus

        emiRepaymentStatus = requests.get(
            "https://lendittfinserve.com/prod/admin/emi/repaymentStatus?fromDate=2024-02-10T10:00:00.000Z&endDate=2024-02-12T10:00:00.000Z&type=TOTAL&page=1&download=true")

        allRepay = requests.get(
            "https://lendittfinserve.com/admin-prod/admin/transaction/allRepaidLoans?start_date=2024-02-10T10:00:00.000Z&end_date=2024-02-12T10:00:00.000Z&page=1&pagesize=10&getTotal=true&download=true")
        # print(allRepay.json())

        headers = {"adminid": "37"}
        # refund_compl = requests.get("https://lendittfinserve.com/stag/admin/transaction/getRefundableData",params={"startDate":"2024-02-01T10:00:00.000Z","endDate":"2024-02-05T10:00:00.000Z","status":1},headers=headers,verify=False)
        refund_compl = requests.get(
            "https://lendittfinserve.com/stag/admin/transaction/getRefundableData?startDate=2024-02-04T10:00:00.000Z&endDate=2024-02-08T10:00:00.000Z&status=1",
            headers=headers)
        refund_pend = requests.get(
            "https://lendittfinserve.com/stag/admin/transaction/getRefundableData?startDate=2024-02-01T10:00:00.000Z&endDate=2024-02-04T10:00:00.000Z&status=-1",
            headers=headers)

    def test_refund_amt(self):
        global dupl_repay_lid, match_app_auto

        allRepay_data = allRepay.json()["data"]["rows"]

        # un_repay_lid = []
        # dupl_repay_lid = []

        emi_1 = []
        emi_2 = []
        emi_3 = []
        emi_4 = []

        app_emi_1 = []
        web_emi_1 = []
        auto_emi_1 = []

        app_emi_2 = []
        web_emi_2 = []
        auto_emi_2 = []

        app_emi_3 = []
        web_emi_3 = []
        auto_emi_3 = []

        app_emi_4 = []
        web_emi_4 = []
        auto_emi_4 = []

        full_pay_1 = []
        full_pay_2 = []
        full_pay_3 = []
        full_pay_4 = []

        lid = []

        for r in allRepay_data:
            if r["EMI Types"] == "EMIPAY 1":
                emi_1.append(r["Loan id"])

            if (r["EMI Types"] == "EMIPAY 2"):
                emi_2.append(r["Loan id"])

            if (r["EMI Types"] == "EMIPAY 3"):
                emi_3.append(r["Loan id"])

            if (r["EMI Types"] == "EMIPAY 4"):
                emi_4.append(r["Loan id"])


            if ((r["EMI Types"] == "EMIPAY 1") and (r["EMI Types"] == "EMIPAY 1")):

                if r["Repayment via"] == "APP":
                    app_emi_1.append(r["Loan id"])

                elif r["Repayment via"] == "WEB":
                    web_emi_1.append(r["Loan id"])

                elif r["Repayment via"] == "AUTODEBIT":
                    auto_emi_1.append(r["Loan id"])

            if ((r["EMI Types"] == "EMIPAY 2") and (r["EMI Types"] == "EMIPAY 2")):

                if r["Repayment via"] == "APP":
                    app_emi_2.append(r["Loan id"])

                elif r["Repayment via"] == "WEB":
                    web_emi_2.append(r["Loan id"])

                elif r["Repayment via"] == "AUTODEBIT":
                    auto_emi_2.append(r["Loan id"])
            #

            if ((r["EMI Types"] == "EMIPAY 3") and (r["EMI Types"] == "EMIPAY 3")):

                if r["Repayment via"] == "APP":
                    app_emi_3.append(r["Loan id"])

                elif r["Repayment via"] == "WEB":
                    web_emi_3.append(r["Loan id"])

                elif r["Repayment via"] == "AUTODEBIT":
                    auto_emi_3.append(r["Loan id"])

            if ((r["EMI Types"] == "EMIPAY 4") and (r["EMI Types"] == "EMIPAY 4")):

                if r["Repayment via"] == "APP":
                    app_emi_4.append(r["Loan id"])

                elif r["Repayment via"] == "WEB":
                    web_emi_4.append(r["Loan id"])

                elif r["Repayment via"] == "AUTODEBIT":
                    auto_emi_4.append(r["Loan id"])

            if "FULLPAY" in r["EMI Types"]:
                if "1" in r["EMI Types"]:
                    full_pay_1.append(r["Loan id"])

                if "2" in r["EMI Types"]:
                    full_pay_2.append(r["Loan id"])

                if "3" in r["EMI Types"]:
                    full_pay_3.append(r["Loan id"])

                if "4" in r["EMI Types"]:
                    full_pay_4.append(r["Loan id"])


        # APP
        match_app_auto_1 = []
        for ap1 in app_emi_1:
            if ap1 in auto_emi_1:
                match_app_auto_1.append(ap1)



        match_app_auto_2 = []
        for ap2 in app_emi_2:
            if ap2 in auto_emi_2:
                match_app_auto_2.append(ap2)

        match_app_auto_3 = []
        for ap3 in app_emi_3:
            if ap3 in auto_emi_3:
                match_app_auto_3.append(ap3)

        match_app_auto_4 = []
        for ap4 in app_emi_4:
            if ap4 in auto_emi_4:
                match_app_auto_4.append(ap4)




        # WEB
        match_web_auto_1 = []
        for wb1 in web_emi_1:
            if wb1 in auto_emi_1:
                match_web_auto_1.append(wb1)

        match_web_auto_2 = []
        for wb2 in web_emi_2:
            if wb2 in auto_emi_2:
                match_web_auto_2.append(wb2)

        match_web_auto_3 = []
        for wb3 in web_emi_3:
            if wb3 in auto_emi_3:
                match_web_auto_3.append(wb3)

        match_web_auto_4 = []
        for wb4 in web_emi_4:
            if wb4 in auto_emi_4:
                match_web_auto_4.append(wb4)


        # full pay
        match_app_auto_1_f = []
        for ap1f in emi_1:
            if ap1f in full_pay_1:
                match_app_auto_1_f.append(ap1f)

        match_app_auto_2_f = []
        for ap2f in emi_2:
            if ap2f in full_pay_2:
                match_app_auto_2_f.append(ap2f)

        match_app_auto_3_f = []
        for ap3f in emi_3:
            if ap3f in full_pay_3:
                match_app_auto_3_f.append(ap3f)

        match_app_auto_4_f = []
        for ap4f in emi_4:
            if ap4f in full_pay_4:
                match_app_auto_4_f.append(ap4f)


        print("match_app_auto_1::", match_app_auto_1)
        print("match_app_auto_2::", match_app_auto_2)
        print("match_app_auto_3::", match_app_auto_3)
        print("match_app_auto_4::", match_app_auto_4)

        print("match_app_auto_1_f::::" ,match_app_auto_1_f)
        print("match_app_auto_2_f::::", match_app_auto_2_f)
        print("match_app_auto_3_f::::", match_app_auto_3_f)
        print("match_app_auto_4_f::::", match_app_auto_4_f)


        print("match_web_auto_1::", match_web_auto_1)
        print("match_web_auto_2::", match_web_auto_2)
        print("match_web_auto_3::", match_web_auto_3)
        print("match_web_auto_4::", match_web_auto_4)

        print("full_pay_1::",full_pay_1)
        print("full_pay_2::", full_pay_2)
        print("full_pay_3::", full_pay_3)
        print("full_pay_4::", full_pay_4)

        print("emi_1::",emi_1)
        print("emi_2::", emi_2)
        print("emi_3::", emi_3)
        print("emi_4::", emi_4)










