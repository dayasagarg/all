import pytest
import requests
class TestGetRecovery:
    @pytest.fixture
    def rec_rate(self):
        global ep, ei, epp, te, pp, pi, p_pen, tp, dis, wo, wp, wi, wpen, ppp, ppi, tppa, unpp, unpi, unpp, tun, rr, ppr
        recResponse = requests.get("http://144.24.112.239/api/admin/report/getRecoveryRate")
        # print(recResponse.json())
        ep = recResponse.json()["data"]["Jan-24"]["expectedPrincipal"]
        ei = recResponse.json()["data"]["Jan-24"]["expectedInterest"]
        epp = recResponse.json()["data"]["Jan-24"]["expectedPenalty"]
        te = recResponse.json()["data"]["Jan-24"]["totalExpected"]

        pp = recResponse.json()["data"]["Jan-24"]["paidPrincipal"]
        pi = recResponse.json()["data"]["Jan-24"]["paidInterest"]
        p_pen = recResponse.json()["data"]["Jan-24"]["paidPenalty"]
        tp = recResponse.json()["data"]["Jan-24"]["totalPaid"]

        dis = recResponse.json()["data"]["Jan-24"]["discount"]
        wo = recResponse.json()["data"]["Jan-24"]["waivedOff"]
        wp = recResponse.json()["data"]["Jan-24"]["waiverPrincipal"]
        wi = recResponse.json()["data"]["Jan-24"]["waiverInterest"]
        wpen = recResponse.json()["data"]["Jan-24"]["waiverPenalty"]

        ppp = recResponse.json()["data"]["Jan-24"]["prePaidPrinciple"]
        ppi = recResponse.json()["data"]["Jan-24"]["prePaidInterest"]
        tppa = recResponse.json()["data"]["Jan-24"]["totalPrePaidAmount"]

        unpp = recResponse.json()["data"]["Jan-24"]["unPaidPrincipal"]
        unpi = recResponse.json()["data"]["Jan-24"]["unPaidInterest"]
        unpp = recResponse.json()["data"]["Jan-24"]["unpaidPenalty"]
        tun = recResponse.json()["data"]["Jan-24"]["totalUnpaid"]

        rr = recResponse.json()["data"]["Jan-24"]["recoveryRate"]
        ppr = recResponse.json()["data"]["Jan-24"]["prePaidRate"]
        return ep, ei, epp, te, pp, pi, p_pen, tp, dis, wo, wp, wi, wpen, ppp, ppi, tppa, unpp, unpi, unpp, tun, rr, ppr

    def test_expected(self, rec_rate):
        print("*** TEST EXECUTION STARTED ***")
        ef = ep + ei + epp

        if ef == te:
            print("Total expected amount is correct")

        else:
            print("Error :: Total expected amount is incorrect")
            assert False

        print(ef)
        print(te)

    def test_paid(self,rec_rate):
        pf = pp + pi + p_pen

        if pf == tp:
            print("Total paid is correct")
        else:
            print("Error :: Total paid is incorrect")
            assert False


    def test_pre_paid(self,rec_rate):
        ppf = ppp + ppi

        if ppf == tppa:
            print("Pre paid is correct")
        else:
            print("Error :: Pre paid is incorrect")
            assert False

        # print(ppf)









