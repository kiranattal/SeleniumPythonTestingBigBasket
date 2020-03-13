import inspect
import logging

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures("setup")
class BaseClass:
    def verify_visibility_link(self,link_text):
        wait = WebDriverWait(self.driver, 40)
        wait.until(expected_conditions.visibility_of_element_located((By.LINK_TEXT, link_text)))


    def verify_visibiity_css(self,css_path):
        wait = WebDriverWait(self.driver, 40)
        wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, css_path)))

    def verify_visibiity_xpath(self,xpath_path):
        wait = WebDriverWait(self.driver, 40)
        wait.until(expected_conditions.visibility_of_element_located((By.XPATH, xpath_path)))

    def verify_all_elements_visibiity_xpath(self, xpath_path):
        wait = WebDriverWait(self.driver, 40)
        wait.until(expected_conditions.presence_of_all_elements_located((By.XPATH, xpath_path)))

    def getLogger(self):
        testcasename=inspect.stack()[1][3]
        logger=logging.getLogger(testcasename)
        filehandler=logging.FileHandler("C:/Users/attal/PycharmProjects/Bigbasket/utilities/logFile.log")
        formatter=logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")
        filehandler.setFormatter(formatter)
        logger.addHandler(filehandler)
        logger.setLevel(logging.DEBUG)
        return logger
