# -*- coding: utf-8 -*-
from behave import given, when, then
from features.environment import *
from hamcrest import *


@when(u'Eu devo selecionar um produto e editar todas suas informação')
def step_click_link_list_of_products(context):
    context.home.enter_list_products()


@then(u'Eu devo editar o produto e verificar se o link Voltar existe na pagina')
def step_do_edit_products_info(context):
    context.listProducts.select_product()

    assert_that(context.listProducts.is_link_goback_present() is True)

    for row in context.table:
        context.listProducts.do_update_info_product((row['name']), (row['code']), (row['company']),
                                                    (row['describe']), (row['price']), (row['type_']),
                                                    (row['status']))


@then(u'Eu valido a message de produto editado com sucesso')
def step_validate_products_edited_success(context):
    assert_that(context.listProducts.get_message_success_update(), equal_to("Produto atualizado com sucesso."))
