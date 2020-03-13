from Pages.loginPage import LoginPage
from Pages.searchResult import SearchResultPage
from Locators.locators import Locators

from utilities.BaseClass import BaseClass


class HomePage(BaseClass):
    def __init__(self,driver):
        self.driver= driver
        self.login_link_text=Locators.login_link_text
        self.gplus_link_css=Locators.gplus_link_css
        self.search_textbox_id=Locators.search_textbox_id
        self.search_button_css=Locators.search_button_css
        self.basket_link_xpath = Locators.basket_link_xpath
        #self.username_text_xpath=Locators.username_text_path

    def click_Login(self):

        self.verify_visibility_link(self.login_link_text)
        print(self.driver.find_element_by_link_text(self.login_link_text).text)
        self.driver.find_element_by_link_text(self.login_link_text).click()

    def click_Gplus(self):
        #self.driver = webdriver.Chrome()
        self.verify_visibiity_css(self.gplus_link_css)
        self.driver.find_element_by_css_selector(self.gplus_link_css).click()
        login_page=LoginPage(self.driver)
        return login_page

    def enter_search_query(self,search_query):
        #self.driver = webdriver.Chrome()
        self.driver.find_element_by_id(self.search_textbox_id).clear()
        self.driver.find_element_by_id(self.search_textbox_id).send_keys(search_query)

    def click_search_button(self):
        #self.driver = webdriver.Chrome()
        self.driver.find_element_by_css_selector(self.search_button_css).click()
        search_result_page = SearchResultPage(self.driver)
        return search_result_page
'''
    def return_username_after_login(self):
        print("Here")

        wait = WebDriverWait(self.driver, 40)
        wait.until(expected_conditions.visibility_of_element_located((By.XPATH, self.username_text_xpath)))

        user_account=self.driver.find_element_by_xpath(self.username_text_xpath).text
        print(user_account)
        return user_account
'''