from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import pytest
import time


class TestCardLD:
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


    def test_newUserMap(self,setup_teardown):
        time.sleep(2)
        oNewUser = driver.find_element(By.XPATH,"/html/body/app-root/app-layout/div[3]/mat-drawer-container/mat-drawer-content/div/app-dashboard/div/div/app-dashboard-cards/div/div[1]/div[2]/div[1]/div[1]/div[2]/span").text
        time.sleep(2)
        print(f"oNewUser:{oNewUser}")
        time.sleep(2)
        driver.find_element(By.XPATH, "(//div[text()=' Current month '])[1]").click()  # current month
        time.sleep(2)
        iNewUser = driver.find_element(By.XPATH, "/html/body/app-root/app-layout/div[3]/mat-drawer-container/mat-drawer-content/div/app-dashboard-table/div/div[3]/div/app-dashboard-tables/div[2]/div[2]/div[1]/div[1]/span[2]").text
        time.sleep(2)
        print(f"iNewUser:{iNewUser}")
        time.sleep(2)

        if oNewUser != iNewUser:
            print("Error::new user card not matched")

        assert oNewUser == iNewUser, "new user card matched"


    def test_repeatedUserMap(self,setup_teardown):
        time.sleep(2)
        oRepeatedUser = driver.find_element(By.XPATH,"/html/body/app-root/app-layout/div[3]/mat-drawer-container/mat-drawer-content/div/app-dashboard/div/div/app-dashboard-cards/div/div[1]/div[2]/div[1]/div[1]/div[3]/span").text
        time.sleep(2)
        print(f"oRepeatedUser:{oRepeatedUser}")
        time.sleep(2)
        driver.find_element(By.XPATH, "(//div[text()=' Current month '])[1]").click()  # current month
        time.sleep(2)
        iRepeatedUser = driver.find_element(By.XPATH, "/html/body/app-root/app-layout/div[3]/mat-drawer-container/mat-drawer-content/div/app-dashboard-table/div/div[3]/div/app-dashboard-tables/div[2]/div[2]/div[2]/div[1]/span[2]").text
        time.sleep(2)
        print(f"iRepeatedUser:{iRepeatedUser}")
        time.sleep(2)

        if oRepeatedUser != iRepeatedUser:
            print("Error::repeated user card not matched")
        time.sleep(2)
        assert oRepeatedUser == iRepeatedUser,"repeated user card matched"



    def test_inNewAndRepUserToAllMap(self,setup_teardown):
        time.sleep(2)
        driver.find_element(By.XPATH, "(//div[text()=' Current month '])[1]").click()  # current month
        time.sleep(2)
        iNewUser = driver.find_element(By.XPATH,"/html/body/app-root/app-layout/div[3]/mat-drawer-container/mat-drawer-content/div/app-dashboard-table/div/div[3]/div/app-dashboard-tables/div[2]/div[2]/div[1]/div[1]/span[2]").text
        time.sleep(2)
        print(f"iNewUser:{iNewUser}")
        time.sleep(2)
        iRepeatedUser = driver.find_element(By.XPATH,"/html/body/app-root/app-layout/div[3]/mat-drawer-container/mat-drawer-content/div/app-dashboard-table/div/div[3]/div/app-dashboard-tables/div[2]/div[2]/div[2]/div[1]/span[2]").text
        time.sleep(2)
        print(f"iRepeatedUser:{iRepeatedUser}")
        time.sleep(2)
        AllRecord = driver.find_element(By.XPATH,"/html/body/app-root/app-layout/div[3]/mat-drawer-container/mat-drawer-content/div/app-dashboard-table/div/div[3]/div/app-mat-paginator/div/mat-paginator/div/div/div[2]/div").text
        time.sleep(2)
        print(f"AllRecord:{AllRecord[4]}")
        time.sleep(2)
        if int(iNewUser) + int(iRepeatedUser) != AllRecord[4]:
            print("Error::iNewUser and iRepeatedUser not matched with all record on page")

        assert int(iNewUser) + int(iRepeatedUser) == AllRecord[4],"iNewUser and iRepeatedUser matched with all record on page"


