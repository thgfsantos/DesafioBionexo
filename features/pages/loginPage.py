from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from features.pages.basePage import BasePage
from features.pages.homePage import HomePage
from features.locators.loginPageLocators import LoginPageLocators


class LoginPage(BasePage):

    PAGE_LOGIN = '/users/sign_in'

    def enter_email(self, username):
        self.find_element(*LoginPageLocators.EMAIL).clear()
        self.find_element(*LoginPageLocators.EMAIL).send_keys(username)

    def enter_password(self, password):
        self.find_element(*LoginPageLocators.PASSWORD).clear()
        self.find_element(*LoginPageLocators.PASSWORD).send_keys(password)

    def click_login_button(self):
        self.find_element(*LoginPageLocators.SUBMIT).click()

    def do_login(self, username, password):
        self.visitUrl(self.PAGE_LOGIN)
        self.enter_email(username)
        self.enter_password(password)
        self.click_login_button()
        return HomePage()

    def get_message_success_logged_in(self):
        result = self.driver.find_element(*LoginPageLocators.MESSAGE_SUCCESS_LOGGED).is_displayed()
        if result is True:
            msg = self.find_element(*LoginPageLocators.MESSAGE_SUCCESS_LOGGED).text
            return msg
