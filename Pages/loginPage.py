from Locators.locators import Locators

from utilities.BaseClass import BaseClass


class LoginPage(BaseClass):
    def __init__(self, driver):
        self.driver = driver
        self.email_textbox_css = Locators.email_textbox_css
        self.password_textbox_css = Locators.password_textbox_css
        self.email_buttonNext_id= Locators.email_buttonNext_id
        self.password_buttonNext_id = Locators.password_buttonNext_id
        self.basket_link_xpath = Locators.basket_link_xpath

    def enter_email(self, email_id):
        #self.driver=webdriver.Chrome()
        self.driver.find_element_by_css_selector(self.email_textbox_css).clear()
        self.driver.find_element_by_css_selector(self.email_textbox_css).send_keys(email_id)

    def enter_password(self, password):
        self.verify_visibiity_css(self.password_textbox_css)
        self.driver.find_element_by_css_selector(self.password_textbox_css).clear()
        self.driver.find_element_by_css_selector(self.password_textbox_css).send_keys(password)

    def click_email_next(self):
        self.driver.find_element_by_id(self.email_buttonNext_id).click()

    def click_password_next(self):
        self.driver.find_element_by_id(self.password_buttonNext_id).click()
