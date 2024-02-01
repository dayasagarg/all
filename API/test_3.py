import requests
import json

class TestDisbInt:
    def test_interest(self):

        response = requests.get("https://lendittfinserve.com/prod/admin/dashboard/allDisbursedLoans?start_date=2023-12-26T10%3A00%3A00.000Z&end_date=2023-12-26T10%3A00%3A00.000Z&page=1&download=true")
        data = response.json()['data']['rows']
        # print(data,indent=2)
        # print(json.dumps(data, indent=2))




