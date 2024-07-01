# conftest.py

import pytest
import requests
from datetime import datetime, timedelta

@pytest.fixture(scope="module")
def url():
    disb_url = "https://madhurfinance.com"
    endpoint = "/admin-prod/admin/dashboard/allDisbursedLoans"

    currTime = datetime.now()
    currTimeStr = datetime.strftime(currTime, "%Y-%m-%d")

    prevTime = currTime - timedelta(days=4)
    prevTimeStr = datetime.strftime(prevTime, "%Y-%m-%d")

    params = {
        "start_date": f"{prevTimeStr}T10:00:00.000Z",
        "end_date": f"{currTimeStr}T10:00:00.000Z",
        "count": "true",
        "page": 1,
        "download": "false"
    }

    disAPI = requests.get(f"{disb_url}{endpoint}", params=params)
    disbData = disAPI.json()["data"]['rows']

    return disbData





