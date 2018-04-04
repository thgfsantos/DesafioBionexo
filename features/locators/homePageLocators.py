# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By


class HomePageLocators(object):
    PRODUCTS = (By.LINK_TEXT, 'Produtos')
    NEW_PRODUCTS = (By.LINK_TEXT, 'Novo Produto')
    LIST_PRODUCTS = (By.LINK_TEXT, 'Listar Produtos')

