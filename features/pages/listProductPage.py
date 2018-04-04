# -*- coding: utf-8 -*-

from features.pages.basePage import BasePage
from features.locators.listProductLocators import ListProductLocators
from features.pages.newFormProductPage import CreateNewProducts
from selenium.common.exceptions import NoSuchElementException
import collections


class ListProductsPage(BasePage):

    def select_product(self):
        self.find_element(*ListProductLocators.SELECT_FIRST_PRODUCT).click()

    def do_update_info_product(self, name, cod, company, desc, price, type_, status):
        product = CreateNewProducts()
        product.do_fillin_form_create_product(name, cod, company, desc, price, type_, status)

    def click_go_back_button(self):
        self.find_element(*ListProductLocators.BUTTON_BACK)

    def get_message_success_update(self):
        message = self.find_element(*ListProductLocators.MESSAGE_SUCCESS).text
        return message

    def is_link_goback_present(self):
        try:
            self.driver.find_element(*ListProductLocators.BUTTON_BACK)
        except NoSuchElementException as e:
            return False
        return True

    def get_products_items(self):
        body = self.driver.find_element_by_tag_name('tbody')
        data_table = body.find_elements_by_tag_name('td')
        qtde_data = body.find_elements_by_tag_name('tr')
        data_element = self.get_data_from_table(data_table, qtde_data)
        return data_element

    def get_data_from_table(self, data_table, qtde_data):
        dict_element = {}
        for i in range(0, qtde_data.__len__() - 1):
            if i <= 10:
                str_value = ''
                key = data_table[0].text
                value = data_table[2:5]
                for j in range(0, value.__len__()):
                    str_value += value[j].text + ','
                    dict_element[key] = str_value
                del data_table[0:5]
            else:
                break
        order_elements = collections.OrderedDict(sorted(dict_element.items()))
        return order_elements
