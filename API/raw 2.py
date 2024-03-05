import requests

from datetime import datetime, timedelta

# curr = datetime.now()
# curr_str = datetime.strftime(curr, "%Y-%m-%d")
#
# prev_1 = curr - timedelta(days=1)
# prev_2 = curr - timedelta(days=2)
#
# pre_str_1 = datetime.strftime(prev_1, "%Y-%m-%d")
# pre_str_2 = datetime.strftime(prev_2, "%Y-%m-%d")
#
# autoDebitFailedAPI = requests.get(
#     "https://lendittfinserve.com/admin-prod/admin/dashboard/todayAutoDebitData",
#     params={"start_date": f"{pre_str_2}T10:00:00.000Z", "end_date": f"{pre_str_1}T10:00:00.000Z", "status": 4,
#             "page": 1, "skipPageLimit": "true"})
#
# autoDebitData = autoDebitFailedAPI.json()["data"]["finalData"]
# # print(autoDebitData)
# bounceChMissed_LId = []
# aut_failed_loan_ids = []
#
# for ad in autoDebitData:
#
#     # if ad["AD Response date"] == "05-02-2024":
#
#     if ad["Today's EMI status"] == "FAILED":
#         if ad["Loan ID"]:
#             aut_failed_loan_ids.append(ad["Loan ID"])
#         # print(ad)
#
# # print("aut_failed_loan_ids::", aut_failed_loan_ids)
#
# for e in aut_failed_loan_ids:
emiAPI = requests.get("https://lendittfinserve.com/admin-prod/admin/loan/getEMIDetails",
                      params={"loanId": 716678}, verify=False)
# print(emiAPI.json())
emiAPI_data = emiAPI.json()["data"]["EMIData"]

print("emiAPI_data::",emiAPI_data)

    # for ed in emiAPI_data:
    #     if ed["penaltyDays"] > 0:
    #         if ed["status"] == "UNPAID":
    #             # if ed["emiDate"] == "08/02/2024":
    #
    #             if ed["bounceCharge"] == 0:
    #                 bounceChMissed_LId.append(e)







    # bounceChMissed_LId_unique = []
    #
    # [bounceChMissed_LId_unique.append(ul) for ul in bounceChMissed_LId if ul not in bounceChMissed_LId_unique]
    #
    # # print("bounceChMissed_LId::",bounceChMissed_LId)
    # # print("bounceChMissed_LId_unique::", bounceChMissed_LId_unique)
    #
    # if len(bounceChMissed_LId_unique) > 0:
    #     print(f"bounce charge missing found for bounceChMissed_LId_unique::{bounceChMissed_LId_unique}")
    #     assert False, "bounce charge missing found"
    # else:
    #     print("No bounce charge missed for bounceChMissed_LId_unique")
    #
    #
    #




