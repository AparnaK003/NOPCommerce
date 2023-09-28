
from selenium.webdriver import Chrome



class Login:
    textbox_email_id = "Email"
    textbox_password_id = "Password"
    button_login_xpath = "//button[@class='button-1 login-button']"
    link_logout_xpath = "//a[contains(text(),'Logout')]"


    def __init__(self,driver):
        self.driver = driver


    def setEmail(self,email):
        self.driver.find_element("id",self.textbox_email_id).clear()
        self.driver.find_element("id", self.textbox_email_id).send_keys(email)


    def setPassword(self,password):
        self.driver.find_element("id", self.textbox_password_id).clear()
        self.driver.find_element("id", self.textbox_password_id).send_keys(password)


    def clickLogin(self):
        self.driver.find_element("xpath", self.button_login_xpath).click()


    def clicklogout(self):
        self.driver.find_element("xpath", self.link_logout_xpath).click()


