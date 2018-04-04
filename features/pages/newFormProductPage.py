# -*- coding: utf-8 -*-
from features.pages.basePage import BasePage
from features.locators.createNewProductLocators import NewProductLocators
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select


class CreateNewProducts(BasePage):
    ADD_PRODUCT = '/products/new'

    def enter_product_name(self, name):
        self.find_element(*NewProductLocators.NAME_PRODUCT).click()
        self.find_element(*NewProductLocators.NAME_PRODUCT).clear()
        self.find_element(*NewProductLocators.NAME_PRODUCT).send_keys(name)

    def enter_cod_product(self, cod):
        self.find_element(*NewProductLocators.COD_PRODUCT).click()
        self.find_element(*NewProductLocators.COD_PRODUCT).clear()
        self.find_element(*NewProductLocators.COD_PRODUCT).send_keys(cod)

    def enter_company_name(self, company):
        self.find_element(*NewProductLocators.COMPANY_NAME).click()
        self.find_element(*NewProductLocators.COMPANY_NAME).clear()
        self.find_element(*NewProductLocators.COMPANY_NAME).send_keys(company)

    def enter_desc_product(self, desc):
        self.find_element(*NewProductLocators.DESC_PRODUCT).click()
        self.find_element(*NewProductLocators.DESC_PRODUCT).clear()
        self.find_element(*NewProductLocators.DESC_PRODUCT).send_keys(desc)

    def enter_price_product(self, price):
        self.find_element(*NewProductLocators.PRICE_PRODUCT).click()
        self.find_element(*NewProductLocators.PRICE_PRODUCT).clear()
        self.find_element(*NewProductLocators.PRICE_PRODUCT).send_keys(price)

    def enter_type_product(self, type_):
        self.find_element_multi_selector_type(type_, *NewProductLocators.TYPE_PRODUCT)

    def enter_status_product(self, status):
        self.find_element_multi_selector_status(status, *NewProductLocators.STATUS_PRODUCT)

    def click_create_product_button(self):
        self.find_element(*NewProductLocators.BUTTON_CREATE_PRODUCT).click()

    def do_fillin_form_create_product(self, name, cod, company, desc, price, type_, status):
        self.enter_product_name(name)
        self.enter_cod_product(cod)
        self.enter_company_name(company)
        self.enter_desc_product(desc)
        self.enter_price_product(price)
        self.enter_type_product(type_)
        self.enter_status_product(status)
        self.click_create_product_button()

    def is_field_present(self, element_field_name):
        try:
            self.driver.find_element(*NewProductLocators.locator_dictionary[element_field_name])
        except NoSuchElementException as e:
            return False
        return True

    def click_button_add_product(self):
        self.visitUrl(self.ADD_PRODUCT)

    def get_message_success_new_product(self):
        result = self.driver.find_element(*NewProductLocators.MESSAGE_SUCCESS).is_displayed()
        if result is True:
            msg = self.find_element(*NewProductLocators.MESSAGE_SUCCESS).text
        return msg

    def validate_field_tipo(self):
        result_element = ()
        options = Select(self.find_element(*NewProductLocators.TYPE_PRODUCT))
        for opt in options.options:
            result_element += (opt.text,)
        return result_element
