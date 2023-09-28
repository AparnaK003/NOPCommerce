
class Search:
    bdy_search_class="row search-row"
    txt_email_name ="SearchEmail"
    txt_FirstName_name ="SearchFirstName"
    txt_LastName_name ="SearchLastName"
    table_xpath ="//table[@id='customers-grid']"
    tableRows_xpath = "//table[@id='customers-grid']//tbody/tr"
    tableCols_xpath = "//table[@id='customers-grid']//tbody/tr/td"

    btn_Search_id ="search-customers"

    def __init__(self, driver):
        self.driver = driver

    def clickSearchBody(self):
        self.driver.find_element("class", self.bdy_search_class).click()

    def setSearchEmail(self ,email):
        self.driver.find_element("name", self.txt_email_name).send_keys(email)

    def setSearchFirstName(self ,firstname):
        self.driver.find_element("name", self.txt_FirstName_name).send_keys(firstname)
        return firstname

    def setSearchLastName(self ,lastname):
        self.driver.find_element("name", self.txt_LastName_name).send_keys(lastname)
        return lastname

    def clickSearch(self):
        self.driver.find_element("id", self.btn_Search_id).click()




