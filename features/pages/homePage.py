# -*- coding: utf-8 -*-
from features.pages.basePage import BasePage
from features.locators.homePageLocators import HomePageLocators
from features.pages.newFormProductPage import CreateNewProducts


class HomePage(BasePage):

    def enter_menu_product(self):
        self.find_element(*HomePageLocators.PRODUCTS).click()

    def enter_new_product(self):
        self.enter_menu_product()
        self.find_element(*HomePageLocators.NEW_PRODUCTS).click()
        return CreateNewProducts()

    def enter_list_products(self):
        self.enter_menu_product()
        self.find_element(*HomePageLocators.LIST_PRODUCTS).click()
