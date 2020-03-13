import time

from Locators.locators import Locators
from utilities.BaseClass import BaseClass


class CartPage(BaseClass):
    def __init__(self,driver):
        self.driver=driver
        self.view_cart_xpath=Locators.view_cart_xpath
        #self.basket_link_xpath = Locators.basket_link_xpath
        self.LOGIN_link_text= Locators.LOGIN_link_text
        self.gplus_link_css = Locators.gplus_link_css
        self.view_products_added=Locators.view_products_added
        self.remove_added_products_from_cart_cross_xpath=Locators.remove_added_products_from_cart_cross_xpath

    #def click_basket(self):
     #   self.driver.find_element_by_xpath(self.basket_link_xpath).click()


    def click_cart(self):
        self.verify_visibiity_xpath(self.view_cart_xpath)
        self.driver.find_element_by_xpath(self.view_cart_xpath).click()

    def click_LOGIN(self):
        self.verify_visibility_link(self.LOGIN_link_text)
        #self.driver = webdriver.Chrome()
        time.sleep(2)
        self.driver.find_element_by_link_text(self.LOGIN_link_text).click()
        self.driver.find_element_by_css_selector(self.gplus_link_css).click()

    def return_added_products(self):
        logger=self.getLogger()
        logger.info("Returning products from cart")
        self.verify_all_elements_visibiity_xpath(self.view_products_added)
        logger.info("Products in the cart are visible by driver")
        added_products=self.driver.find_elements_by_xpath(self.view_products_added)
        logger.info(str(len(added_products))+ "products are found")
        added_products_from_cart = []

        for product in added_products:
            logger.info(product.text)
            added_products_from_cart.append(product.text)

        return added_products_from_cart

    def remove_added_products_from_cart(self):
        self.verify_all_elements_visibiity_xpath(self.remove_added_products_from_cart_cross_xpath)
        products_to_be_removed=self.driver.find_elements_by_xpath(self.remove_added_products_from_cart_cross_xpath)       #return added_products_read
        time.sleep(2)
        for product in products_to_be_removed:
            product.click()
        logger=self.getLogger()
        logger.info("Products are successfully removed from the cart")