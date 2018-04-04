# -*- coding: utf-8 -*-
from behave import given, when, then
from features.environment import *
from hamcrest import *


@when(u'Eu clico no menu Produtos e seleciono listar produtos')
def step_click_link_list_product(context):
    context.home.enter_list_products()


@then(u'Eu visualizo 10 produtos ordenados pelo campo Nome')
def step_show_list_of_products(context):
    list_product = context.listProducts.get_products_items()

    assert_that(list_product.__len__(), greater_than_or_equal_to(10))

    for k, v in list_product.iteritems():
        print 'Nome do Produto: ' + k +'|'+' Fabricante: ' + v.split(',')[0] +'|'+ ' Tipo do Produto: ' + v.split(',')[
            1] +'|'+ ' Status do Produto: ' + v.split(',')[2]+'\n'


