import math


class TestLoanAgrRisk:
    import pytest
    @pytest.fixture
    def url_agr_dis_risk(self):
        global disAPI, requests
        import requests
        from datetime import datetime, timedelta

        curr = datetime.now()
        curr_str = datetime.strftime(curr, "%Y-%m-%d")
        prev = curr - timedelta(days=1)
        pre_str = datetime.strftime(prev, "%Y-%m-%d")

        disAPI = requests.get("https://lendittfinserve.com/stag/admin/dashboard/allDisbursedLoans",
                              params={"start_date": f"{pre_str}T10:00:00.000Z",
                                      "end_date": f"{curr_str}T10:00:00.000Z",
                                      "page": 1, "download": "true"})

        # loanAgrAPI = requests.get("http: // lendittfinserve.com / prod / admin / esign / getLoanAgreement", params={"loanId":726301})

    def test_disb_risk(self, url_agr_dis_risk):
        print("*** Test execution started ***")
        global cibil_800_lid_mis_match_count, cibil_700_799_lid_mis_match_count, cibil_less_than_700_mis_match_count
        global cibil_800_lid_mis_match,cibil_700_799_lid_mis_match,cibil_less_than_700_mis_match

        disAPIData = disAPI.json()["data"]["rows"]


        cibil_800_lid_match = []
        cibil_800_lid_mis_match = []

        cibil_700_799_lid_match = []
        cibil_700_799_lid_mis_match = []

        cibil_less_than_700_match = []
        cibil_less_than_700_mis_match = []

        # print(disAPIData)
        for r in disAPIData:

            if r["Cibil Score"] >= 800:

                if 0.01 * r["Approved amount"] == r["Risk assessment fees"]:
                    cibil_800_lid_match.append(r["Loan ID"])

                elif 0.01 * r["Approved amount"] != r["Risk assessment fees"]:
                    cibil_800_lid_mis_match.append(r["Loan ID"])

                else:
                    print("something went wrong with 800 cs")

            elif 799 >= r["Cibil Score"] >= 700:

                if (math.ceil(0.025 * r["Approved amount"]) == math.ceil(r["Risk assessment fees"])):
                    cibil_700_799_lid_match.append(r["Loan ID"])

                elif (math.ceil(0.025 * r["Approved amount"]) != math.ceil(r["Risk assessment fees"])):
                    cibil_700_799_lid_mis_match.append(r["Loan ID"])

                else:
                    print("something went wrong with 700 to 799 cs")

            elif r["Cibil Score"] < 700:

                if 0.04 * r["Approved amount"] == r["Risk assessment fees"]:
                    cibil_less_than_700_match.append(r["Loan ID"])

                elif 0.04 * r["Approved amount"] != r["Risk assessment fees"]:
                    cibil_less_than_700_mis_match.append(r["Loan ID"])

                else:
                    print("something went wrong with less than 700 cs")




        cibil_800_lid_match_count = len(cibil_800_lid_match)
        cibil_800_lid_mis_match_count = len(cibil_800_lid_mis_match)

        cibil_700_799_lid_match_count = len(cibil_700_799_lid_match)
        cibil_700_799_lid_mis_match_count = len(cibil_700_799_lid_mis_match)

        cibil_less_than_700_match_count = len(cibil_less_than_700_match)
        cibil_less_than_700_mis_match_count = len(cibil_less_than_700_mis_match)

        print("cibil_800_lid_match_count ::",cibil_800_lid_match_count)
        print("cibil_800_lid_mis_match_count ::",cibil_800_lid_mis_match_count)
        print("cibil_700_799_lid_match_count ::",cibil_700_799_lid_match_count)
        print("cibil_700_799_lid_mis_match_count ::",cibil_700_799_lid_mis_match_count)
        print("cibil_less_than_700_match_count ::",cibil_less_than_700_match_count)
        print("cibil_less_than_700_mis_match_count ::",cibil_less_than_700_mis_match_count)



    def test_cs_800(self):
        if cibil_800_lid_mis_match_count > 0:
            print(f"cibil_800_lid_mis_match_count found :: {cibil_800_lid_mis_match}")
            assert False
        else:
            print("cibil_800 criteria match with 1%")


    def test_cs_700_799(self):
        if cibil_700_799_lid_mis_match_count > 0:
            print(f"cibil_700_799_lid_mis_match found :: {cibil_700_799_lid_mis_match}")
            assert False
        else:
            print("cibil_700_799 criteria match with 2.5%")


    def test_cs_less_than_700(self):
        if cibil_less_than_700_mis_match_count > 0:
            print(f"cibil_less_than_700_mis_match_count found :: {cibil_less_than_700_mis_match}")
            assert False
        else:
            print("cibil_less_than_700 criteria match with 4%")


        print("*** Test execution completed ***")








