import time
from selenium.webdriver.support.ui import Select

class AddCustomer:
    # Add customer page
    linkCustomers_menu_xpath="//a[@href='#']//p[contains(text(),'Customers')]"
    linkCustomers_menuitem_xpath = "//a[@href='/Admin/Customer/List']"
    btnAddNew_xpath= "//a[@href='/Admin/Customer/Create']"

    txt_Email_name="Email"
    txtPassword_name="Password"
    txtFirstName_name="FirstName"
    txtLastName_name="LastName"
    rdMaleGender_id="Gender_Male"
    rdFemaleGender_id="Gender_Female"
    txtDOB_name="DateOfBirth"
    txtCompanyName_name="Company"
    chkbxTaxExempt_name="IsTaxExempt"

    txtNewsletter="//*[@id='customer-info']/div[2]/div[9]/div[2]/div/div[1]/div/div"
    listitem_newsOp1="//option[contains(text(),'Your storename')]"
    listitem_newsOp2 = "//option[contains(text(),'Test store 2')]"

    txtCustomerRole_xpath="//*[@id='customer-info']/div[2]/div[10]/div[2]/div/div[1]/div/div"
    listitem_Administrators_xpath="//li[contains(text(), 'Administrators')]"
    listitem_ForumModerator_xpath="//li[contains(text(), 'Forum Moderator')]"
    listitem_Guests_xpath="//li[contains(text(), 'Guests')]"
    listitem_Registered_xpath="//li[contains(text(), 'Registered')]"
    listitem_Vendors_xpath="//li[contains(text(), 'Vendors')]"

    txtVendor_name = "VendorId"
    option_NotVendor_xpath="//option[contains(text(),'Not a vendor')]"
    option_Vendor1_xpath = "//option[contains(text(),'Vendor 1')]"
    option_Vendor2_xpath = "//option[contains(text(),'Vendor 2')]"

    chkbx_active_name="Active"
    txtarea_Admincmt_name="AdminComment"
    btn_Save_name="save"


    def __init__(self,driver):
        self.driver = driver

    def clickOnCustomersMenu(self):
        self.driver.find_element("xpath", self.linkCustomers_menu_xpath).click()

    def clickOnCustomersMenuItem(self):
        self.driver.find_element("xpath", self.linkCustomers_menuitem_xpath).click()

    def clickOnAddNew(self):
        self.driver.find_element("xpath", self.btnAddNew_xpath).click()

    def setEmail(self,email):
        self.driver.find_element("name", self.txt_Email_name).clear()
        self.driver.find_element("name", self.txt_Email_name).send_keys(email)

    def setPassword(self,password):
        self.driver.find_element("name", self.txtPassword_name).clear()
        self.driver.find_element("name", self.txtPassword_name).send_keys(password)


    def setFirstName(self,firstname):
        self.driver.find_element("name", self.txtFirstName_name).clear()
        self.driver.find_element("name",self.txtFirstName_name).send_keys(firstname)

    def setLastName(self, lastname):
        self.driver.find_element("name",self.txtLastName_name).clear()
        self.driver.find_element("name", self.txtLastName_name).send_keys(lastname)

    def setGender(self,gender):
        if gender == "female":
            self.driver.find_element("id", self.rdFemaleGender_id).click()
        elif gender == "male":
            self.driver.find_element("id", self.rdMaleGender_id).click()

    def setDOB(self,dob):
        self.driver.find_element("name", self.txtDOB_name).clear()
        self.driver.find_element("name", self.txtDOB_name).send_keys(dob)

    def setCompany(self, company):
        self.driver.find_element("name", self.txtCompanyName_name).clear()
        self.driver.find_element("name", self.txtCompanyName_name).send_keys(company)

    def setTaxExempt(self):
        self.driver.find_element("name", self.chkbxTaxExempt_name).click()

    def setActive(self):
        self.driver.find_element("name", self.chkbx_active_name).click()

    def addComment(self,comment):
        self.driver.find_element("name", self.txtarea_Admincmt_name).clear()
        self.driver.find_element("name", self.txtarea_Admincmt_name).send_keys(comment)

    def setManagerofVendor(self,manager):
        self.driver.find_element("name", self.txtVendor_name).click()

        if manager == "option1":
            self.driver.find_element("xpath", self.option_Vendor1_xpath).click()
        elif manager == "option2":
            self.driver.find_element("xpath", self.option_Vendor2_xpath).click()
        else:
            self.driver.find_element("xpath", self.option_NotVendor_xpath).click()

    def setCustomerRole(self,role):
        self.driver.find_element("xpath", self.txtCustomerRole_xpath).click()

        if role == "admin":
            self.driver.find_element("xpath", self.listitem_Administrators_xpath).click()
        elif role == "forum moderator":
            self.driver.find_element("xpath", self.listitem_ForumModerator_xpath).click()
        elif role == "vendor":
            self.driver.find_element("xpath", self.listitem_Vendors_xpath).click()
        elif role == "guest":
            self.driver.find_element("xpath", self.listitem_Registered_xpath).click()
            self.driver.find_element("xpath", self.listitem_Guests_xpath).click()



    def clickSave(self):
        self.driver.find_element("name", self.btn_Save_name).click()
