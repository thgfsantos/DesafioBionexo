# -*- coding: utf-8 -*-
#language: en
@edit_products
  Feature: Como hospital quero editar os produtos previamente cadastrados.
    Scenario: Editar produtos cadastrados
      Given Usuario logado na Bionexo
      When Eu clico no menu Produtos e seleciono listar produtos
      And Eu devo selecionar um produto e editar todas suas informação
      Then Eu devo editar o produto e verificar se o link Voltar existe na pagina
      |name|code|company|describe|price|type_|status|
      |Seringas 20ml|SE083|FarmaNexo12|Materiais Médicos|40|Materiais Médicos|Ativo|
      And Eu valido a message de produto editado com sucesso