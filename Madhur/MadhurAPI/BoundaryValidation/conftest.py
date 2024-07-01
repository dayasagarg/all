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



# Hook to capture screenshots on test failure
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        try:
            driver = item.funcargs['driver']  # Assuming 'driver' fixture is used
            screenshot_name = f"failure_{item.name}.png"
            driver.save_screenshot(screenshot_name)
            print(f"\nScreenshot saved as {screenshot_name}")
        except Exception as e:
            print(f"\nFailed to capture screenshot: {repr(e)}")




# screenshot_util.py

from PIL import ImageGrab
import os

def capture_screenshot(file_name):
    # Capture screenshot using Pillow
    im = ImageGrab.grab()
    im.save(file_name)

# conftest.py

import os
# from screenshot_util import capture_screenshot

@pytest.fixture(scope="function", autouse=True)
def screenshot_on_failure(request):
    yield
    if request.node.rep_call.failed:
        test_name = request.node.name
        screenshot_dir = os.path.join(os.path.dirname(__file__), "screenshots")
        os.makedirs(screenshot_dir, exist_ok=True)
        screenshot_file = os.path.join(screenshot_dir, f"{test_name}.png")
        capture_screenshot(screenshot_file)



