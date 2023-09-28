import pytest

from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from pageObjects.LoginPage import Login

class Test_001_Login:
    baseURL = ReadConfig.getAppURL()
    email = ReadConfig.getUserEmail()
    password = ReadConfig.getUserPassword()

    logger = LogGen.loggen()

    @pytest.mark.sanity
    def test_homePageTitle(self,setup):
        self.logger.info("************* Test_001_Login ***************")
        self.logger.info("************* Verifying Home Page Title ***************")
        self.driver = setup
        self.driver.maximize_window()
        self.driver.get(self.baseURL)
        act_title = self.driver.title

        if act_title == "Your store. Login":
            assert True
            self.driver.close()
            self.logger.info("************* Home Page Title Test is Passed ***************")
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_homePageTitle.png")
            self.logger.info("************* Home page title test Failed ***************")
            assert False
            self.driver.close()

    @pytest.mark.regression
    def test_login(self, setup):
        self.logger.info("*************Verifying login test******************")
        self.driver = setup
        self.driver.maximize_window()
        self.driver.get(self.baseURL)
        self.lp = Login(self.driver)
        self.lp.setEmail(self.email)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title = self.driver.title

        if act_title == "Dashboard / nopCommerce administration":
            self.logger.info("************* Login test Passed ***************")
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_login.png")
            self.logger.error("************* Login test Failed ***************")
            assert False
            self.driver.close()

