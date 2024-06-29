import time

from playwright.sync_api import sync_playwright, Page


def test_a():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)

        try:
            context = browser.new_context()
            context.grant_permissions(["geolocation", "notifications", "camera"],
                                      origin="https://devuatapi.com/web-test/")

            page = context.new_page()
            page.goto('https://devuatapi.com/web-test/')
            page.wait_for_timeout(3000)

        except Exception as e:
            print(f"Error occurred: {str(e)}")

        # Add a delay of 3 seconds using Playwright's wait_for_timeout method

        # page.get_by_test_id("flt-semantic-node-13").click()
        # page.get_by_role("button", name="Login").click()
        # page.get_by_label("Login").click()
        # page.get_by_text("Login").click()

        page.locator("//flt-semantics[@id='flt-semantic-node-13']").click()

        page.wait_for_timeout(3000)
        # page.get_by_role("checkbox", name="checkbox").click()
        page.locator("//flt-semantics[@role='checkbox']").click()
        page.wait_for_timeout(3000)
        page.locator("//flt-semantics[@role='button']").click()
        page.wait_for_timeout(3000)
        # page.locator("//flt-semantics[@id='flt-semantic-node-13']").click()
        page.wait_for_timeout(3000)
        page.locator("//textarea[@data-semantics-role='text-field']").fill("0123456784")
        page.wait_for_timeout(3000)
        page.locator("//flt-semantics[@aria-label='Yes']").click()
        page.wait_for_timeout(3000)
        page.locator("//flt-semantics[@aria-label='NEFT']").click()
        page.wait_for_timeout(5000)
        page.locator("//flt-semantics//textarea[@aria-label='Enter monthly in-hand salary']").fill("999789")
        page.wait_for_timeout(7000)
        page.locator("//flt-semantics[@aria-label='Continue']").click()

        page.wait_for_timeout(3000)
        page.locator("//flt-semantics//input[@id='one-time-code']").fill("1111")
        page.wait_for_timeout(4000)



        page.locator("//textarea[@aria-label='Enter Email ID']").fill("abxscxs@gmail.com")
        page.wait_for_timeout(3000)
        page.locator("//textarea[@aria-label='Enter PAN number']").fill("sadpl1111q")
        page.wait_for_timeout(3000)
        page.locator("//flt-semantics[@aria-label='Loan purpose']").click()
        page.wait_for_timeout(3000)
        page.locator("//flt-semantics[@aria-label='Education']").click()
        page.wait_for_timeout(3000)
        # page.locator("//flt-semantics[@aria-label='Communication Language']").click()
        # page.wait_for_timeout(3000)
        # page.locator("//flt-semantics[@aria-label='Communication Language English']").click()
        page.wait_for_timeout(3000)
        page.locator("//flt-semantics[@aria-label='Are you politically exposed?']").click()
        page.wait_for_timeout(3000)
        page.locator("//flt-semantics[@aria-label='No']").click()
        page.wait_for_timeout(4000)
        cont = page.locator("//flt-semantics[@aria-label='Continue']")
        page.wait_for_timeout(4000)
        cont.scroll_into_view_if_needed()
        page.wait_for_timeout(4000)
        # cont.click()
        page.wait_for_timeout(4000)
        page.locator("//flt-semantics[@aria-label='Employment status']").click()
        page.wait_for_timeout(4000)
        page.locator("//flt-semantics[@aria-label='Salaried']").click()
        page.wait_for_timeout(4000)
        page.locator("//flt-semantics[@aria-label='Marital status']").click()
        page.wait_for_timeout(4000)

        page.locator("//flt-semantics[@aria-label='Single']").click()
        page.wait_for_timeout(4000)
        page.locator("//textarea[@aria-label='Enter mother name']").fill("qewqr")
        page.wait_for_timeout(5000)
        # hle = page.locator("//flt-semantics[@aria-label='Continue']")
        # page.wait_for_timeout(4000)
        # hle.scroll_into_view_if_needed()
        # page.wait_for_timeout(4000)
        # page.locator("//flt-semantics[@aria-label='Do you own a vehicle?']").click()
        page.get_by_label("Do you own a vehicle?").click()
        page.wait_for_timeout(4000)
        w_2 = page.locator("//flt-semantics[@aria-label='2 Wheeler']").click()

        page.wait_for_timeout(4000)
        # page.locator("//flt-semantics[@aria-label='Do you own a vehicle?']").click()
        # page.get_by_label("Do you own a vehicle?").click()
        page.locator("//textarea[@aria-label='Enter mother name']").click()
        page.wait_for_timeout(1000)
        # page.locator("//flt-semantics[@aria-label="Highest level of education").click()
        page.get_by_label("Highest level of education").click()

        page.wait_for_timeout(7000)
        # page.locator("//flt-semantics[@aria-label='Masters Degree']").click()
        page.get_by_label("Masters Degree").click()

        page.wait_for_timeout(7000)
        page.get_by_label("Your residential status").click()

        page.wait_for_timeout(7000)
        page.get_by_label("Owned").click()

        page.wait_for_timeout(7000)
        # page.locator("//flt-semantics[@aria-label='Select salary bankWe only support the banks listed here']").click()
        page.get_by_label("Select salary bank We only support the banks listed here").click()

        page.locator('flt-semantics').nth(2).click()
        # page.wait_for_timeout(7000)
        # try:
        #     page.evaluate("document.getElementsByTagName('flt-semantics')[31].click()")
        #     page.wait_for_timeout(7000)
        # except Exception as e:
        #     print(f"Error: {e}")

        # page.get_by_label("Bank of India").click()
        # page.get_by_text("Bank of India").click()
        # page.evaluate("document.getElementsByTagName('flt-semantics')[31].click()")
        # page.wait_for_timeout(7000)
        # page.locator('flt-semantics').nth(3).click()
        page.wait_for_timeout(7000)


        page.locator("//flt-semantics[@aria-label='Continue']").click()
        page.wait_for_timeout(3000)

        # Take a screenshot
        # page.screenshot(path='example.png')

        # Close the browser
        # browser.close()






