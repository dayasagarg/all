from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import pytest
import time



class TestCardTPP:
    @pytest.fixture()
    def setup_teardown(self):
        global driver
        ser = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service = ser)
        driver.maximize_window()
        driver.implicitly_wait(5)
        driver.get("http://144.24.112.239/lenditt/#/dashboard")
        # time.sleep(1)
        driver.find_element(By.XPATH, "//input[@type='email']").send_keys("dayasagar.ghodake@lenditt.com") #email
        # time.sleep(1)
        driver.find_element(By.XPATH, "/html/body/app-root/app-auth/div/div[2]/div/div/form/div/button").click()
        # time.sleep(1)
        driver.find_element(By.XPATH, "//input[@type='password']").send_keys("Dsg@9373") #password
        # time.sleep(1)
        driver.find_element(By.XPATH, "/html/body/app-root/app-auth/div/div[2]/div/div/form/div[2]/button").click()
        # time.sleep(1)
        driver.find_element(By.XPATH, "//input[@type='text']").send_keys("1111") #otp
        # time.sleep(1)
        element = driver.find_element(By.XPATH, "/html/body/app-root/app-auth/div/div[2]/div/div/form/div[2]/button")
        # time.sleep(1)
        driver.execute_script("arguments[0].scrollIntoView();", element)
        # time.sleep(1)
        driver.find_element(By.CSS_SELECTOR,"body > app-root > app-auth > div > div:nth-child(2) > div > div > form > div.submit-btn.margin-top-bottom.d-flex.justify-content-center.ng-star-inserted > button").click()
        time.sleep(1)
        yield
        time.sleep(1)
        driver.close()
        driver.quit()
        print("test execution completed")


    def test_count(self,setup_teardown):
        time.sleep(2)
        oCount = driver.find_element(By.CSS_SELECTOR,"body > app-root > app-layout > div.ng-star-inserted > mat-drawer-container > mat-drawer-content > div > app-dashboard > div > div > app-dashboard-cards > div > div:nth-child(9) > a > div.mx-2.sub-dashboard-card > div:nth-child(1) > div.font-weight-bold.text-dark.d-flex.flex-row.fnt-size-12").text
        print(f"oCount:{oCount}")
        time.sleep(2)
        driver.find_element(By.XPATH,"(// div[text() = ' Count '])[2]").click() #count
        time.sleep(2)
        time.sleep(2)
        iCount = driver.find_element(By.XPATH,"//div[@class='mat-paginator-range-label']").text
        time.sleep(2)
        print(f"iCount:{iCount[4]}")

        if oCount != iCount:
            print("Error::oCount and iCount of todays part payment not matched")

        assert oCount == iCount, "oCount and iCount matched"


    def test_amount(self,setup_teardown):
        time.sleep(2)
        oAmount = driver.find_element(By.CSS_SELECTOR,"body > app-root > app-layout > div.ng-star-inserted > mat-drawer-container > mat-drawer-content > div > app-dashboard > div > div > app-dashboard-cards > div > div:nth-child(9) > a > div.mx-2.sub-dashboard-card > div.w-100.d-flex.flex-row.justify-content-between.align-items-center.px-2.mt-2.card-row-bg > div.font-weight-bold.text-dark.d-flex.flex-row.fnt-size-12").text
        time.sleep(2)
        print(f"oAmount:{oAmount}")
        driver.find_element(By.XPATH,"(// div[text() = ' Amount '])[3]").click()
        time.sleep(2)
        onTimeUsersAmount = driver.find_element(By.XPATH,"(//div[text() = 'Amount'])[1]//ancestor::div[1]//div[2]").text
        time.sleep(2)
        print(f"onTimeUsersAmount:{onTimeUsersAmount}")
        time.sleep(2)
        delayUsersAmount = driver.find_element(By.XPATH,"(//div[text() = 'Amount'])[2]//ancestor::div[1]//div[2]").text
        time.sleep(2)
        print(f"delayUsersAmount:{delayUsersAmount}")

        if int(oAmount) != int(onTimeUsersAmount) + int(delayUsersAmount):
            print("Error::oAmount not matches with onTimeUsersAmount and delayUsersAmount")

        assert int(oAmount) == int(onTimeUsersAmount) + int(delayUsersAmount), "oAmount matches with onTimeUsersAmount and delayUsersAmount"











