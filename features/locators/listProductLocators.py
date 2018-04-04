# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By


class ListProductLocators(object):
    SELECT_FIRST_PRODUCT = (By.CSS_SELECTOR, 'td')
    BUTTON_BACK = (By.LINK_TEXT, 'Voltar')
    BUTTON_UPDATE = (By.NAME, 'commit')
    MESSAGE_SUCCESS_2 = (By.CSS_SELECTOR, 'div.alert.alert-success')
    MESSAGE_SUCCESS = (By.ID, 'flash_notice')
