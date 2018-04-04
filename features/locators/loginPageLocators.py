# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By


class LoginPageLocators(object):
    EMAIL = (By.ID, 'user_email')
    PASSWORD = (By.ID, 'user_password')
    SUBMIT = (By.ID, 'sign_in')
    MESSAGE_SUCCESS_LOGGED = (By.ID, 'flash_notice')
