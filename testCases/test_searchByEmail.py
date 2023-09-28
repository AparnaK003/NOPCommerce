from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from pageObjects.LoginPage import Login
from pageObjects.AddCustomerPage import AddCustomer
from pageObjects.SearchPage import Search
import time
import pytest


class Test_004_SearchByEmail:
    baseURL = ReadConfig.getAppURL()
    email = ReadConfig.getUserEmail()
    password = ReadConfig.getUserPassword()

    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_searchByEmail(self,setup):
        self.logger.info("******* Test_004_SearchByName ********")
        self.logger.info("*************Verifying login test******************")
        self.driver = setup
        self.driver.maximize_window()
        self.driver.get(self.baseURL)
        self.lp = Login(self.driver)
        self.lp.setEmail(self.email)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()

        self.logger.info("******** entering customer page ********")
        self.add = AddCustomer(self.driver)
        self.add.clickOnCustomersMenu()
        self.add.clickOnCustomersMenuItem()

        self.search = Search(self.driver)
        # self.search.bdy_search_class()
        self.search.setSearchEmail("steve_gates@nopCommerce.com")
        self.search.clickSearch()
        self.logger.info("******** clicked search button ********")

        time.sleep(4)


        self.emailid = self.driver.find_element("xpath", "//*[@id='customers-grid']/tbody/tr/td[2]").text

        if self.emailid == "steve_gates@nopCommerce.com":
            assert True == True
            self.logger.info("********** customer search test passed *************")
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_searchByName.png")
            assert True == False
            self.logger.info("********** customer search test failed *************")
            self.driver.close()





