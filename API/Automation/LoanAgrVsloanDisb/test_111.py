import pytest
import requests
from datetime import datetime, timedelta

class TestLoanAgreementDisbursement:
    @pytest.fixture
    def disbursed_loans_data(self):
        try:
            curr = datetime.now()

            curr_str = datetime.strftime(curr, "%Y-%m-%d")
            prev = curr - timedelta(days=1)
            prev_str = datetime.strftime(prev, "%Y-%m-%d")

            response = requests.get(
                "https://chinmayfinserve.com/admin-prod/admin/dashboard/allDisbursedLoans",
                params={
                    "start_date": f"{prev_str}T10:00:00.000Z",
                    "end_date": f"{curr_str}T10:00:00.000Z",
                    "page": 1,
                    "download": "true"
                }
            )

            response.raise_for_status()
            return response.json()["data"]["rows"]

        except requests.RequestException as e:
            pytest.fail(f"Failed to retrieve disbursed loans data: {e}")

    def fetch_loan_agreement(self, loan_id):
        try:
            response = requests.get(
                "https://chinmayfinserve.com/admin-prod/admin/esign/getLoanAgreement",
                params={"loanId": loan_id}
            )
            response.raise_for_status()
            return response.json()["data"]["eSign_agree_data"]

        except requests.RequestException as e:
            pytest.fail(f"Failed to retrieve loan agreement data for Loan ID {loan_id}: {e}")

    def test_loan_amount_matches_approved_amount(self, disbursed_loans_data):
        for loan in disbursed_loans_data:
            approved_amount = loan["Approved amount"]
            loan_amount = loan["Loan amount"]
            assert loan_amount == approved_amount, f"Mismatch for Loan ID {loan['Loan ID']}: {loan_amount} != {approved_amount}"

    def test_interest_rates_match(self, disbursed_loans_data):
        for loan in disbursed_loans_data:
            expected_interest_rate = float(loan["Interest Rate"].replace("%", ""))
            loan_agreement_data = self.fetch_loan_agreement(loan["Loan ID"])
            actual_interest_rate = loan_agreement_data["interestRatePerDay"]
            assert expected_interest_rate == actual_interest_rate, f"Interest rate mismatch for Loan ID {loan['Loan ID']}: {expected_interest_rate} != {actual_interest_rate}"
