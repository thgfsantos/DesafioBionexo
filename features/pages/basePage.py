# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from resources.config import Configuration
import selenium.webdriver.support.ui as UI


class BasePage(object):
    cfg = Configuration().get_config('config.json', 'QA')
    base_url = cfg['base_url']
    driver = webdriver.Firefox(executable_path=cfg['path_geckodriver'])
    driver.implicitly_wait(30)

    def close(self):
        self.driver.quit()

    def visitUrl(self, path=''):
        url = self.base_url + path
        self.driver.get(url)

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def find_element_multi_selector_type(self, label, *locator):
        if label == u'Medicamento':
            UI.Select(self.find_element(*locator)).select_by_value('med')
        else:
            UI.Select(self.find_element(*locator)).select_by_value('mat')

    def find_element_multi_selector_status(self, label, *locator):
        if label == u'Ativo':
            Select(self.find_element(*locator)).select_by_index(0)
        if label == u'Inativo':
            Select(self.find_element(*locator)).select_by_index(1)

    def get_info_to_logging(self):
        email = self.cfg['user_email']
        passw = self.cfg['user_pass']
        return email, passw
