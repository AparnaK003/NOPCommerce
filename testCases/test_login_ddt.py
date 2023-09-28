import time

import pytest
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from pageObjects.LoginPage import Login
from utilities import ExcelUtils

class Test_002_DDT_Login:
    baseURL = ReadConfig.getAppURL()
    path=".//TestData//Login_testdata.xlsx"

    logger = LogGen.loggen()

    @pytest.mark.sanity
    def test_login_ddt(self, setup):
        self.logger.info("************* Test_002_DDT_Login ******************")
        self.logger.info("*************Verifying login DDT test******************")
        self.driver = setup
        self.driver.maximize_window()
        self.driver.get(self.baseURL)
        self.lp = Login(self.driver)

        self.rows = ExcelUtils.getRowCount(self.path, "Sheet1" )
        list_status=[]

        for r in range(2,self.rows+1):
            self.email = ExcelUtils.readData(self.path,"Sheet1",r,1)
            self.password = ExcelUtils.readData(self.path,"Sheet1", r,2)
            self.expected = ExcelUtils.readData(self.path,"Sheet1", r,3)

            self.lp.setEmail(self.email)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            time.sleep(5)

            act_title = self.driver.title
            exp_title="Dashboard / nopCommerce administration"

            if act_title == exp_title:
                if self.expected == "Pass":
                    self.logger.info("********** Passed")
                    self.lp.clicklogout()
                    time.sleep(4)
                    list_status.append("Pass")
                elif self.expected == "Fail":
                    self.logger.info("***************Failed")
                    self.lp.clicklogout()
                    time.sleep(4)
                    list_status.append("Fail")

            elif act_title != exp_title:
                if self.expected == "Pass":
                    self.logger.info("********* failed")
                    list_status.append("Fail")
                elif self.expected == "Fail":
                    self.logger.info("***** passed *******")
                    list_status.append("Pass")

        if "Fail" not in list_status:
            self.logger.info("*********** Login DDT test passed *********")
            self.driver.close()
            assert True
        else:
            self.logger.info("*********** Login DDT test failed *********")
            self.driver.close()
            assert False


        self.logger.info("********* End of Login DDT Test ************")
        self.logger.info("******** Completed Test_002_DDT_Login *********")








