# -*- coding: utf-8 -*-
#language: en
@create_products
Feature: Como hospital quero cadastrar Medicamentos e Materiais Médicos para futuras compras.
  Scenario: Criar novos produtos do tipo Medicamentos e Materiais Médicos
    Given Usuario logado na Bionexo
    When Eu clicar no menu Produtos para adicionar um novo produto
    And Os campos "nome", "codigo", "fabricante", "preco", "descricao", "tipo", "status" devem esta present no formulario
    And O campo tipo deve ter apenas valores de Medicamento e Materiais Médicos
    Then Eu devo criar um novo produto
    |name|code|company|describe|price|type_|status|
    |Alfa25|A235|FarmaNexo2|Medicamento|100|Medicamento|Ativo|
    |Omega25|O235|FarmaNexo3|Medicamento|100|Medicamento|Ativo|
    |Luva 10|L235|FarmaNexo4|Materiais Médicos|100|Materiais Médicos|Ativo|
    |Bacia|BA235|FarmaNexo5|Materiais Médicos|100|Materiais Médicos|Inativo|


