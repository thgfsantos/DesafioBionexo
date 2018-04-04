# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By


class NewProductLocators(object):
    NAME_PRODUCT = (By.ID, 'product_name')
    COD_PRODUCT = (By.ID, 'product_code')
    COMPANY_NAME = (By.ID, 'product_manufacturer')
    DESC_PRODUCT = (By.ID, 'product_description')
    PRICE_PRODUCT = (By.ID, 'product_price')
    TYPE_PRODUCT = (By.ID, 'product_kind')
    STATUS_PRODUCT = (By.ID, 'product_status')
    BUTTON_CREATE_PRODUCT = (By.NAME, 'commit')
    BUTTON_ADD_PRODUCT = (By.CSS_SELECTOR, 'div.row > a.btn.btn-primary')
    MESSAGE_SUCCESS = (By.ID, 'flash_notice')

    locator_dictionary = {
        "nome": (By.ID, 'product_name'),
        "codigo": (By.ID, 'product_code'),
        "fabricante": (By.ID, 'product_manufacturer'),
        "descricao": (By.ID, 'product_description'),
        "preco": (By.ID, 'product_price'),
        "tipo": (By.ID, 'product_kind'),
        "status": (By.ID, 'product_status')
    }
