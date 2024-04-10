import math


class TestLoanAgrDis:
    import pytest
    @pytest.fixture
    def url_agr_dis(self):
        global disAPI, requests
        import requests
        from datetime import datetime, timedelta

        curr = datetime.now()
        curr_str = datetime.strftime(curr, "%Y-%m-%d")
        prev = curr - timedelta(days=1)
        pre_str = datetime.strftime(prev, "%Y-%m-%d")

        disAPI = requests.get("https://chinmayfinserve.com/admin-prod/admin/dashboard/allDisbursedLoans",
                              params={"start_date": f"{curr_str}T10:00:00.000Z",
                                      "end_date": f"{curr_str}T10:00:00.000Z",
                                      "page": 1, "download": "true"})

        # loanAgrAPI = requests.get("https://chinmayfinserve.com/admin-prod/ admin / esign / getLoanAgreement", params={"loanId":726301})

    def test_agr_disb(self, url_agr_dis):
        global loanAmount, app_amt, loanAgrAPI, intRate, int_rate_la, emi_la, totalEMI, loanAgrAPIDataTenure, loanTenure, loan_tenure_la, name_la, name, nbfc, nbfc_la, procFees, procFees_la, sr, loanAgrAPIDataLoanId, dis_lid, riskFees, riskFees_la, docFees, docFees_la, gstAmt, gst_la, a, intRate_disb
        disAPIData = disAPI.json()["data"]["rows"]
        # print("disAPIData::",disAPIData)

        dis_lid = []
        app_amt = []
        loanAmtStr = []
        intRate = []
        totalEMI = []
        loanTenure = []
        name = []
        procFees = []
        docFees = []
        gstAmt = []

        intRate_disb_l = []
        la_int_rate_l = []

        misMatch_lid = []

        for m,dis in enumerate(disAPIData):
            if m == 25:
                break

            if dis["Loan ID"]:
                dis_lid.append(dis["Loan ID"])

        #
            intRate_disb= float(dis["Interest Rate"].replace("%", ""))
            intRate_disb_l.append(intRate_disb)

            # if dis["Interest Rate"]:
            #     intRate_disb = float(dis["Interest Rate"].replace("%", ""))
            #     intRate_disb_l.append(intRate_disb_l)


            # print("intRate_disb::",intRate_disb)
            # print("intRate_disb_type::", type(intRate_disb))

            # if dis["Interest Rate"]:
            #     intRate.append(float(dis["Interest Rate"].replace("%", "")))

        print("intRate_disb_l::",intRate_disb_l)



        global lid

        int_rate_la = []
        emi_la = []
        loan_tenure_la = []
        name_la = []
        proc_fees_str_la = []
        doc_fees_str_la = []
        risk_fees_str_la = []
        sgst_str_la = []
        cgst_str_la = []



        for n,lid in enumerate(dis_lid):
            if n == 25:
                break

            loanAgrAPI = requests.get("https://chinmayfinserve.com/admin-prod/admin/esign/getLoanAgreement",
                                      params={"loanId": lid})

            loanAgrAPIData = loanAgrAPI.json()["data"]["eSign_agree_data"]["emiTotalPrincipal"]

            loanAgrAPIDataLoanId = loanAgrAPI.json()["data"]["eSign_agree_data"]["loanId"]
            loanAgrAPIDataIntRate = loanAgrAPI.json()["data"]["eSign_agree_data"]["interestRatePerDay"]

            loanAgrAPIDataEMI = loanAgrAPI.json()["data"]["eSign_agree_data"]["numberOfEmis"]
            loanAgrAPIDataTenure = loanAgrAPI.json()["data"]["eSign_agree_data"]["loanTenure"]
            loanAgrAPIDataName = loanAgrAPI.json()["data"]["eSign_agree_data"]["borrowerName"]
            loanAgrAPIDataProcAmt = loanAgrAPI.json()["data"]["eSign_agree_data"]["processingAmount"]
            loanAgrAPIDataDoc = loanAgrAPI.json()["data"]["eSign_agree_data"]["documentAmount"]
            loanAgrAPIDataRisk = loanAgrAPI.json()["data"]["eSign_agree_data"]["riskAssessmentCharge"]
            loanAgrAPIDataSGST = loanAgrAPI.json()["data"]["eSign_agree_data"]["sgstCharges"]
            loanAgrAPIDataCGST = loanAgrAPI.json()["data"]["eSign_agree_data"]["cgstCharges"]

            # print(loanAgrAPIDataRisk)

            if loanAgrAPIData:
                loanAmtStr.append(loanAgrAPIData)



            # if loanAgrAPIDataIntRate:
            #     int_rate_la.append(round(float(loanAgrAPIDataIntRate), 2))

            la_int_rate = round(float(loanAgrAPIDataIntRate), 3)
            la_int_rate_l.append(la_int_rate)
            # print("la_int_rate::", la_int_rate)
            # print("la_int_rate_type::", type(la_int_rate))


            # if la_int_rate != intRate_disb:
                # misMatch_lid.append(lid)
                # int_rate_la.append(int_rate_la)

                # print("la_int_rate::",la_int_rate)
                # print("intRate_disb::",intRate_disb)
                # print("lid::",lid)


        # print("misMatch_lid::",misMatch_lid)
        print("la_int_rate_l::",la_int_rate_l)
        print("dis_lid::",dis_lid)
















