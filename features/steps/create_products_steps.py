# -*- coding: utf-8 -*-
from behave import given, when, then, use_step_matcher
from features.environment import *
from hamcrest import *


@given(u'Usuario logado na Bionexo')
def step_do_login_bionexo(context):
    context.basepage.visitUrl('/')
    context.login.do_login(context.basepage.get_info_to_logging()[0],
                           context.basepage.get_info_to_logging()[1])
    assert_that(context.login.get_message_success_logged_in(), equal_to("Autenticado com sucesso."))


@when(u'Eu clicar no menu Produtos para adicionar um novo produto')
def step_click_in_link_new_product(context):
    context.home.enter_new_product()


@when(
    u'Os campos "{nome}", "{codigo}", "{fabricante}", "{preco}", "{descricao}", "{tipo}", "{status}" devem esta present no formulario')
def step_validate_fields_presents(context, nome, codigo, fabricante, preco, descricao, tipo, status):
    assert_that(context.newProducts.is_field_present(nome) is True)
    assert_that(context.newProducts.is_field_present(codigo) is True)
    assert_that(context.newProducts.is_field_present(fabricante) is True)
    assert_that(context.newProducts.is_field_present(descricao) is True)
    assert_that(context.newProducts.is_field_present(preco) is True)
    assert_that(context.newProducts.is_field_present(tipo) is True)
    assert_that(context.newProducts.is_field_present(status) is True)

@when(u'O campo tipo deve ter apenas valores de Medicamento e Materiais Médicos')
def step_impl(context):
    assert_that(context.newProducts.validate_field_tipo()[0], equal_to('Medicamento'))
    assert_that(context.newProducts.validate_field_tipo()[1], starts_with('Mat'))


@then(u'Eu devo criar um novo produto')
def step_do_create_new_product(context):
    for row in context.table:
        context.newProducts.do_fillin_form_create_product((row['name']), (row['code']), (row['company']),
                                                          (row['describe']), (row['price']), (row['type_']),
                                                          (row['status']))

        assert_that(context.newProducts.get_message_success_new_product(),
                    equal_to("Produto criado com sucesso."))

        context.newProducts.click_button_add_product()