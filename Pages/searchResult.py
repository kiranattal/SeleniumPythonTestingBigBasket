from Pages.cartPage import CartPage
from Locators.locators import Locators
from utilities.BaseClass import BaseClass


class SearchResultPage(BaseClass):
    def __init__(self,driver):
        self.driver=driver
        self.search_products_xpath=Locators.search_products_xpath
        self.selected_product=None
        self.add_selected_product_in_cart=Locators.add_selected_product_in_cart
        self.basket_link_xpath = Locators.basket_link_xpath
        self.add_product_name_xpath=Locators.add_product_name_xpath

    def return_search_products(self):
        self.verify_all_elements_visibiity_xpath(self.search_products_xpath)
        products=self.driver.find_elements_by_xpath(self.search_products_xpath)
        return products

    def add_selected_product(self,selected_product):
        self.selected_product = selected_product
        self.verify_visibiity_xpath(self.add_selected_product_in_cart)
        self.selected_product.find_element_by_xpath(self.add_selected_product_in_cart).click()


    def click_basket(self):
        self.verify_visibiity_xpath(self.basket_link_xpath)
        self.driver.find_element_by_xpath(self.basket_link_xpath).click()
        print("Inside basket clicking")


    def return_product_name(self,selected_product):
        self.selected_product = selected_product
        return self.selected_product.find_element_by_xpath(self.add_product_name_xpath).text
