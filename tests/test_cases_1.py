import time
import pytest
from selenium import webdriver
from Pages.cartPage import CartPage
from Pages.homePage import HomePage
from Pages.loginPage import LoginPage
from Pages.searchResult import SearchResultPage
from TestData.LoginData import LoginData
from TestData.SearchProductData import SearchProductData
from utilities.BaseClass import BaseClass


class Testcases(BaseClass):
    added_products = []
    '''@classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Chrome(executable_path="driver/chromedriver.exe")
        cls.driver.get("http://bigbasket.com")
        cls.driver.maximize_window()'''

    def test_a_login(self,get_login_data):
        message = None
        logger = self.getLogger()
        try:

            login_from_home=HomePage(self.driver)
            login_from_home.click_Login()
            logger.info("Login is clicked")
            login_page=login_from_home.click_Gplus()
            print("Gplus is clicked")
            logger.info("Gplus is clicked")


            time.sleep(12)
            childWindow = self.driver.window_handles[1]
            self.driver.switch_to.window(childWindow)
            #login_page=LoginPage(self.driver)
            login_page.enter_email(get_login_data["email"])
            login_page.click_email_next()
            logger.info("email : ")
            logger.info(get_login_data["email"])
            login_page.enter_password(get_login_data["password"])
            login_page.click_password_next()
            logger.info("password : ")
            logger.info(get_login_data["password"])
            self.driver.switch_to.window(self.driver.window_handles[0])
            print(self.driver.title)
            self.driver.refresh()
            message = "Success! to Login"

        except:
            message = "Fail! to Login"

        logger.info(message)
        assert "Success" in message



    def test_add_searched_product_to_basket(self,get_test_data):
        product_name=None
        logger=self.getLogger()
        product_name=self.add_product_in_cart(get_test_data["search_category"],get_test_data["search_product"])

        logger.info("Search category :" + get_test_data["search_category"])
        logger.info("Search product :" + get_test_data["search_product"])

        if len(product_name)!=0:
            assert True
            message = "Success, Product Is  ADDED"
        else:
            message = "Product not added"
            assert False
        logger.info(product_name + message)
        self.driver.refresh()



    def test_view_added_products_in_cart(self):
        #self.add_product_in_cart("Banana","Banana")
        logger=self.getLogger()
        search_result_page=SearchResultPage(self.driver)
        cart_page= search_result_page.click_basket()
        cart_page = search_result_page.click_basket()
        cart_page = CartPage(self.driver)

        #search_result_page.click_basket()
        logger.info("Basket is clicked")
        print("Basket is clicked")


        cart_page.click_cart()
        logger.info("Cart is clicked")
        print("Cart is clicked")
        cart_page.click_LOGIN()

        added_products_from_cart=cart_page.return_added_products()
        logger.info("While adding : ")
        logger.info(self.added_products)
        print("While adding to basket: ",self.added_products)

        logger.info("From cart products are: ")
        logger.info(added_products_from_cart)
        print("From cart : ", added_products_from_cart)

        if len(self.added_products)!=len(added_products_from_cart):
            logger.info("Mismatch between cart and added products")
            assert False
        else:
            logger.info("Added searched products and products in the cart are same")
            logger.info("Cleaning the cart for next test run")
            cart_page.remove_added_products_from_cart()


        '''
        for product_i in self.added_products:
            for product_j in added_products_from_cart:
                if product_i==product_j:
                    assert True
                    break
            assert False
        '''
        #assert "Banana" in added_products_from_cart[0] and "Coffee" in added_products_from_cart[1]

    def add_product_in_cart(self,search_category,search_product):
        logger=self.getLogger()

        driver=self.driver
        search_From_Home=HomePage(driver)
        search_From_Home.enter_search_query(search_category)
        search_result_page=search_From_Home.click_search_button()

        products=search_result_page.return_search_products()
        product_name=None
        selected_product = None
        for product in products:
            selected_product = product
            selected_product_name=search_result_page.return_product_name(selected_product)
            #print(selected_product_name)
            #print("\n")
            #logger.info(selected_product_name+"\n")
            if search_product in selected_product_name.lower():
               break
        time.sleep(5)

        search_result_page.add_selected_product(selected_product)
        product_name=selected_product_name
        self.added_products.append(product_name)
        return product_name

    @pytest.fixture(params= SearchProductData.test_search_product_data )
    def get_test_data(self,request):
        return request.param

    @pytest.fixture(params=LoginData.test_login_data)
    def get_login_data(self, request):
        return request.param
    '''
    
    def test_add_searched_product_to_basket(self):
        self.add_product_in_cart("Coffee","Instant")

       driver=self.driver
        search_From_Home=HomePage(driver)
        search_From_Home.enter_search_query("Coffee")
        search_From_Home.click_search_button()
        search_result_page=SearchResultPage(driver)
        products=search_result_page.return_search_products()

        selected_product = None
        for product in products:
            selected_product = product
            product_name = product.find_element_by_partial_link_text("Coffee").text.lower()
            if "instant" in product_name:
                break


        search_result_page.add_selected_product(selected_product)
        product_name = search_result_page.return_product_name(selected_product)
        self.added_products.append(product_name)
        print(product_name)
        print("ONE PRODUCT IS ADDED")

    def test_view_added_products_in_cart(self):
        self.add_product_in_cart("Banana","Banana")
        print(self.added_products)
        search_result_page=SearchResultPage(self.driver)
        search_result_page.click_basket()
        search_result_page.click_basket()
        print("Basket is clicked")

        cart_page = CartPage(self.driver)
        cart_page.click_cart()
        print("Cart is clicked")
        cart_page.click_LOGIN()
        added_products=cart_page.return_added_products()
        print(added_products)


    def add_product_in_cart(self,search_category,search_product):
        driver=self.driver
        search_From_Home=HomePage(driver)
        search_From_Home.enter_search_query(search_category)
        search_From_Home.click_search_button()
        search_result_page=SearchResultPage(driver)
        products=search_result_page.return_search_products()

        selected_product = None
        for product in products:
            selected_product = product
            product_name = product.find_element_by_partial_link_text(search_category).text

            if search_product in selected_product.text:
                break

        search_result_page.add_selected_product(selected_product)
        product_name=search_result_page.return_product_name(selected_product)
        self.added_products.append(product_name)
        print(product_name)
        print("Product IS successfully ADDED")
        driver.refresh()
'''


