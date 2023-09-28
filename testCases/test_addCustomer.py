import string
import time
import random
import pytest

from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from pageObjects.LoginPage import Login
from pageObjects.AddCustomerPage import AddCustomer


class Test_003_AddCustomer:
    baseURL = ReadConfig.getAppURL()
    email = ReadConfig.getUserEmail()
    password = ReadConfig.getUserPassword()

    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_AddNew(self,setup):
        self.logger.info("************* Test_003_AddCustomer ******************")
        self.logger.info("*************Logging in ******************")
        self.driver = setup
        self.driver.maximize_window()
        self.driver.get(self.baseURL)
        self.lp = Login(self.driver)
        self.lp.setEmail(self.email)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()

        self.logger.info("******** Verifying Add New Customer ********")
        self.add = AddCustomer(self.driver)
        self.add.clickOnCustomersMenu()
        self.add.clickOnCustomersMenuItem()
        self.add.clickOnAddNew()
        time.sleep(5)

        self.emailid=random_generator()+ "@gmail.com"
        self.add.setEmail(self.emailid)
        self.add.setPassword(self.password)
        self.add.setFirstName("Veronica")
        self.add.setLastName("Dumbling")
        self.add.setGender("female")
        self.add.setDOB("9/27/2023")
        self.add.setCompany("Company")
        self.add.setTaxExempt()
        self.add.setActive()
        self.add.addComment("good comments only")
        self.add.setManagerofVendor("option1")
        self.logger.info("****** Adding customer role *******")
        self.add.setCustomerRole("vendor")
        self.logger.info("****** clicking save *******")
        self.add.clickSave()


        self.logger.info("******** add customer validation started  ************")

        self.msg = self.driver.find_element("xpath", "//div[@class='alert alert-success alert-dismissable']").text
        print(self.msg)

        exp_msg ="The new customer has been added successfully."
        if exp_msg in self.msg:
            assert True == True
            self.logger.info("Add customer test passed")
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_addCustomer.png")
            self.logger.error("Add customer test failed")
            assert True == False
            self.driver.close()


def random_generator(size=8, chars= string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))


