# -*- coding: utf-8 -*-
#language: en
@list_products
  Feature: Como hospital quero listar todos os produtos cadastrados.
    Scenario: Listagem de Produtos
      Given Usuario logado na Bionexo
      When Eu clico no menu Produtos e seleciono listar produtos
      Then Eu visualizo 10 produtos ordenados pelo campo Nome