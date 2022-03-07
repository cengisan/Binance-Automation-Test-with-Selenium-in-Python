from selenium import webdriver
import unittest
import HtmlTestRunner
import time

class BitcoinTestCase(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path='../drivers/chromedriver.exe')
        cls.driver.implicitly_wait(5)
        cls.driver.maximize_window()

    def test_entrance_binance(self):
        driver = self.driver
        driver.get("https://google.com")
        driver.find_element_by_name("q").send_keys("Binance")
        driver.find_element_by_name("btnK").click()

        driver.find_element_by_partial_link_text(
            "Bitcoin, Ether ve Altcoin Al/Sat | Kripto Para Borsası | Binance").click()
        time.sleep(3)

        driver.find_element_by_xpath("//*[@id='__APP']/div/header/div[4]/div[2]/div[2]").click()
        time.sleep(3)

        driver.find_element_by_xpath("// *[ @ id = 'fiatlngdialog_ba-Currency-USD']").click()
        time.sleep(3)

        driver.find_element_by_xpath("// *[ @ id = 'header_menu_ba-tableMarkets'] / div").click()
        time.sleep(3)

        driver.find_element_by_xpath("//*[@id='markets_main_search']").send_keys("Bitcoin")
        time.sleep(3)
        
        driver.find_element_by_xpath("//*[@id='tabContainer']/div[2]/div[2]/div/div[2]/div[1]/div/div[6]/a").click()
        time.sleep(5)

        time.sleep(5)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="C:/Users/ASUS/AppData/Roaming/JetBrains"
                                                                  "/PyCharmCE2021.3/scratches/selenium/Reports"))
