import requests
import pytest
from datetime import datetime, timedelta


class TestRefund:
    def test_ref_url(self):
        global allRepay, refund_compl, refund_pend, emiRepaymentStatus

        currTime = datetime.now()
        currTimeStr = datetime.strftime(currTime, "%Y-%m-%d")
        preTime = currTime - timedelta(days=5)
        preTimeStr = datetime.strftime(preTime, "%Y-%m-%d")
        print("currTimeStr::",currTimeStr)
        print("preTimeStr::",preTimeStr)

        emiRepaymentStatus = requests.get(
            "https://chinmayfinserve.com/admin-prod/admin/emi/repaymentStatus?fromDate=2024-02-18T10:00:00.000Z&endDate=2024-02-23T10:00:00.000Z&type=TOTAL&page=1&download=true")

        allRepay = requests.get(
            "https://chinmayfinserve.com/admin-prod/admin/transaction/allRepaidLoans",
            params={"start_date": f"{preTimeStr}T10:00:00.000Z", "end_date": f"{currTimeStr}T10:00:00.000Z", "page": 1,
                    "pagesize": 10, "getTotal": "true", "download": "true"})
        # print(allRepay.json())

        headers = {"adminid": "37"}

        refund_compl = requests.get("https://chinmayfinserve.com/admin-prod/admin/transaction/getRefundableData",
                                    params={"skipPageLimit": "true", "endDate": f"{currTimeStr}T10:00:00.000Z",
                                            "startDate": f"{preTimeStr}T10:00:00.000Z", "status": 1}, headers=headers)
        headers_2 = {"adminid": "164"}
        refund_pend = requests.get(
            "https://chinmayfinserve.com/admin-prod/admin/transaction/getRefundableData",params={"skipPageLimit":"true","endDate":f"{currTimeStr}T10:00:00.000Z","startDate":f"{preTimeStr}T10:00:00.000Z","status":-1},
            headers=headers_2)

    def test_refund_amt_allRepaid(self):
        global dupl_repay_lid, match_app_auto, all_refund, all_refund_unique

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

        autodebit_miss_match_razorpay = []
        cashfree_miss_match_ICICI_UPI = []

        for r in allRepay_data:
            if r["Repayment via"] == "AUTODEBIT":
                if r["Payment mode"] != "RAZORPAY":
                    autodebit_miss_match_razorpay.append(r["Loan id"])

            if r["Repayment via"] == "APP":
                if r["Payment mode"] != "ICICI_UPI":
                    cashfree_miss_match_ICICI_UPI.append(r["Loan id"])

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

        # print("autodebit_miss_match_razorpay::",autodebit_miss_match_razorpay)
        # print("cashfree_miss_match_ICICI_UPI::", cashfree_miss_match_ICICI_UPI)

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

        all_refund = match_app_auto_1 + match_web_auto_2 + match_app_auto_3 + match_app_auto_4 + match_web_auto_1 + match_web_auto_2 + match_web_auto_3 + match_web_auto_4 + match_app_auto_1_f + match_app_auto_2_f + match_app_auto_3_f + match_app_auto_4_f
        all_refund_unique = []
        [all_refund_unique.append(i) for i in all_refund if i not in all_refund_unique]

        # print("all_refund::",all_refund)
        print("all_refund_unique::", all_refund_unique)

        # print("match_app_auto_1::", match_app_auto_1)
        # print("match_app_auto_2::", match_app_auto_2)
        # print("match_app_auto_3::", match_app_auto_3)
        # print("match_app_auto_4::", match_app_auto_4)
        #
        # print("match_app_auto_1_f::::" ,match_app_auto_1_f)
        # print("match_app_auto_2_f::::", match_app_auto_2_f)
        # print("match_app_auto_3_f::::", match_app_auto_3_f)
        # print("match_app_auto_4_f::::", match_app_auto_4_f)
        #
        #
        # print("match_web_auto_1::", match_web_auto_1)
        # print("match_web_auto_2::", match_web_auto_2)
        # print("match_web_auto_3::", match_web_auto_3)
        # print("match_web_auto_4::", match_web_auto_4)

        # print("full_pay_1::",full_pay_1)
        # print("full_pay_2::", full_pay_2)
        # print("full_pay_3::", full_pay_3)
        # print("full_pay_4::", full_pay_4)
        #
        # print("emi_1::",emi_1)
        # print("emi_2::", emi_2)
        # print("emi_3::", emi_3)
        # print("emi_4::", emi_4)

    def test_ref_completed(self):
        global uniqRefund_compl,ref_miss_compl
        refund_compl_data = refund_compl.json()["data"]["rows"]
        refund_compl_data_count = refund_compl.json()["data"]["count"]

        # print("refund_compl_data::",refund_compl_data)
        print("refund_compl_data_count::", refund_compl_data_count)

        refund_comp_loan_ids = []
        ref_source_wrong = []

        for rc in refund_compl_data:
            if rc["loanId"]:
                refund_comp_loan_ids.append(rc["loanId"])

            if rc["source"] != "RAZORPAY":
                ref_source_wrong.append(rc["loanId"])

        print("refund_comp_loan_ids::", refund_comp_loan_ids)
        print("ref_source_wrong::", ref_source_wrong)

        if len(ref_source_wrong) == 0:
            print("*** No ref_source_wrong found in refund completed ***")
        else:
            print("Error::ref_source_wrong found in refund completed")  # it should be razorpay only not ICICI_UPI
            # assert False, "ref_source_wrong found in refund completed"

        duplicateRefund_compl = []
        uniqRefund_compl = []

        for d in refund_comp_loan_ids:
            if d not in uniqRefund_compl:
                uniqRefund_compl.append(d)
            else:
                duplicateRefund_compl.append(d)

        if len(duplicateRefund_compl) == 0:
            print("*** No duplicate found in refund completed ***")
        else:
            print("Error::Duplicate found in refund completed")

        assert len(duplicateRefund_compl) == 0

        ref_miss_compl = []
        for dut in all_refund_unique:
            if dut in refund_comp_loan_ids:
                continue
            else:
                ref_miss_compl.append(dut)

            # if dut not in refund_comp_loan_ids:
            #     ref_miss_compl.append(dut)

        # print("refund_comp_loan_ids::", refund_comp_loan_ids)
        # print("refund_miss_in_compl::", ref_miss_compl)

        if len(ref_miss_compl) > 0:
            print(f"refund missed found:: {ref_miss_compl}")
            assert False, "refund missed found"
        else:
            print("*** refund not missed with refund completed ***")


    def test_refund_pending(self):
        refund_pend_data = refund_pend.json()["data"]["filteredData"]
        # refund_pend_data = refund_pend.json()
        # print("refund_pend_data::",refund_pend_data)

        pend_lid = []
        for p in refund_pend_data:
            if p["loanId"]:
                pend_lid.append(p["loanId"])

        miss_with_pend = []
        for m in ref_miss_compl:
            if m not in pend_lid:
                miss_with_pend.append(m)

        if len(miss_with_pend) > 0:
            print(f"Error:: refund miss_with_pend found::{miss_with_pend}")
            assert False, "refund miss_with_pend found"
        else:
            print("*** No refund miss_with_pend found ***")

        # print("miss_with_pend::",miss_with_pend)





    @pytest.mark.skip
    def test_ref_amt_emi_check(self):

        for r in uniqRefund_compl:
            trans = requests.get("https://chinmayfinserve.com/admin-prod/admin/transaction/getTransactionDetails",
                                 params={"loanId": r})

            transData = trans.json()["data"]

            repayAmt = []
            for td in transData:
                if td["Status"] == "COMPLETED":
                    if td["Pay type"] == "REFUND":
                        if td["Repay Amount"]:
                            repayAmt.append(td["Repay Amount"])


                if "AUTODEBIT" or "APP" in td["Source"]:
                    if td["Repay Amount"] == td["Repay Amount"]:
                        print("ra::",td["Repay Amount"])


            # print(transData)

    #
    # @pytest.mark.skip
    # def test_refund_repay_status(self):
    #     repayStatus = emiRepaymentStatus.json()["data"]["rows"]
    #     # print("repayStatus::",repayStatus)
    #
    #     emi_1_r = []
    #     emi_2_r = []
    #     emi_3_r = []
    #     emi_4_r = []
    #
    #     app_emi_1_r = []
    #     web_emi_1_r = []
    #     auto_emi_1_r = []
    #
    #     app_emi_2_r = []
    #     web_emi_2_r = []
    #     auto_emi_2_r = []
    #
    #     app_emi_3_r = []
    #     web_emi_3_r = []
    #     auto_emi_3_r = []
    #
    #     app_emi_4_r = []
    #     web_emi_4_r = []
    #     auto_emi_4_r = []
    #
    #     for rr in repayStatus:
    #         if rr["Emi number"] == 1:
    #             emi_1_r.append(rr["Loan ID"])
    #
    #         if rr["Emi number"] == 2:
    #             emi_2_r.append(rr["Loan ID"])
    #
    #         if rr["Emi number"] == 3:
    #             emi_3_r.append(rr["Loan ID"])
    #
    #         if rr["Emi number"] == 4:
    #             emi_4_r.append(rr["Loan ID"])
    #
    #
    #
    #         if ((rr["Emi number"] == 1) and (rr["Emi number"] == 1)):
    #
    #             if rr["Payment type"] == "APP":
    #                 app_emi_1_r.append(rr["Loan ID"])
    #
    #             elif rr["Payment type"] == "WEB":
    #                 web_emi_1_r.append(rr["Loan ID"])
    #
    #             elif rr["Payment type"] == "AUTODEBIT":
    #                 auto_emi_1_r.append(rr["Loan ID"])
    #
    #
    #         if ((rr["Emi number"] == 2) and (rr["Emi number"] == 2)):
    #
    #             if rr["Payment type"] == "APP":
    #                 app_emi_2_r.append(rr["Loan ID"])
    #
    #             elif rr["Payment type"] == "WEB":
    #                 web_emi_2_r.append(rr["Loan ID"])
    #
    #             elif rr["Payment type"] == "AUTODEBIT":
    #                 auto_emi_2_r.append(rr["Loan ID"])
    #
    #         if ((rr["Emi number"] == 3) and (rr["Emi number"] == 3)):
    #
    #             if rr["Payment type"] == "APP":
    #                 app_emi_3_r.append(rr["Loan ID"])
    #
    #             elif rr["Payment type"] == "WEB":
    #                 web_emi_3_r.append(rr["Loan ID"])
    #
    #             elif rr["Payment type"] == "AUTODEBIT":
    #                 auto_emi_3_r.append(rr["Loan ID"])
    #
    #         if ((rr["Emi number"] == 4) and (rr["Emi number"] == 4)):
    #
    #             if rr["Payment type"] == "APP":
    #                 app_emi_4_r.append(rr["Loan ID"])
    #
    #             elif rr["Payment type"] == "WEB":
    #                 web_emi_4_r.append(rr["Loan ID"])
    #
    #             elif rr["Payment type"] == "AUTODEBIT":
    #                 auto_emi_4_r.append(rr["Loan ID"])
    #
    #
    #
    #     # APP
    #     match_app_auto_1_r = []
    #     for ap1_r in app_emi_1_r:
    #         if ap1_r not in auto_emi_1_r:
    #             continue
    #         else:
    #             match_app_auto_1_r.append(ap1_r)
    #
    #
    #     match_app_auto_2_r = []
    #     for ap2_r in app_emi_2_r:
    #         if ap2_r in auto_emi_2_r:
    #             match_app_auto_2_r.append(ap2_r)
    #
    #     match_app_auto_3_r = []
    #     for ap3_r in app_emi_3_r:
    #         if ap3_r in auto_emi_3_r:
    #             match_app_auto_3_r.append(ap3_r)
    #
    #     match_app_auto_4_r = []
    #     for ap4_r in app_emi_4_r:
    #         if ap4_r in auto_emi_4_r:
    #             match_app_auto_4_r.append(ap4_r)
    #
    #
    #
    #     # WEB
    #     match_web_auto_1_r = []
    #     for wb1_r in web_emi_1_r:
    #         if wb1_r in auto_emi_1_r:
    #             match_web_auto_1_r.append(wb1_r)
    #
    #     match_web_auto_2_r = []
    #     for wb2_r in web_emi_2_r:
    #         if wb2_r in auto_emi_2_r:
    #             match_web_auto_2_r.append(wb2_r)
    #
    #     match_web_auto_3_r = []
    #     for wb3_r in web_emi_3_r:
    #         if wb3_r in auto_emi_3_r:
    #             match_web_auto_3_r.append(wb3_r)
    #
    #     match_web_auto_4_r = []
    #     for wb4_r in web_emi_4_r:
    #         if wb4_r in auto_emi_4_r:
    #             match_web_auto_4_r.append(wb4_r)
    #
    #
    #     #
    #     print("app_emi_1_r::",app_emi_1_r)
    #     print("auto_emi_1_r::", auto_emi_1_r)
    #
    #     print("app_emi_2_r::", app_emi_2_r)
    #     print("auto_emi_2_r::", auto_emi_2_r)
    #
    #     print("app_emi_3_r::", app_emi_3_r)
    #     print("auto_emi_3_r::", auto_emi_3_r)
    #
    #     print("app_emi_4_r::", app_emi_4_r)
    #     print("auto_emi_4_r::", auto_emi_4_r)
    #
    #
    #
    #     print("match_app_auto_1_r::", match_app_auto_1_r)
    #     print("match_app_auto_2_r::", match_app_auto_2_r)
    #     print("match_app_auto_3_r::", match_app_auto_3_r)
    #     print("match_app_auto_4_r::", match_app_auto_4_r)
    #
    #
    #     print("match_web_auto_1_r::", match_web_auto_1_r)
    #     print("match_web_auto_2_r::", match_web_auto_2_r)
    #     print("match_web_auto_3_r::", match_web_auto_3_r)
    #     print("match_web_auto_4_r::", match_web_auto_4_r)
    #
