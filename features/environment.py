# -*- coding: utf-8 -*-

from features.pages.basePage import BasePage
from features.pages.loginPage import LoginPage
from features.pages.homePage import HomePage
from features.pages.newFormProductPage import CreateNewProducts
from features.pages.listProductPage import ListProductsPage

from selenium import webdriver


def before_all(context):
    context.basepage = BasePage()
    context.login = LoginPage()
    context.home = HomePage()
    context.newProducts = CreateNewProducts()
    context.listProducts = ListProductsPage()


def after_all(context):
    context.basepage.close()

