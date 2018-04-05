# DesafioBionexo

## Escreva a respeito da abordagem que você usou para testar essa aplicação;
A abordagem usada para realizar os testes desta aplicação foi BDD com selenium webdriver com Python: 
* BDD: 
 * por que com bdd é possível escrever cenários/exemplos baseados nos critérios de aceitação e são possíveis testá-los
 * a escrita dos cenários/exemplos são de fácil compreensão
 * permiti focar no que deve ser desenvolvido ou validado. 
 * tem diversos frameworks para diversas linguagem de programação, para esta aplicação utilizei o framework behave do python. 

* Selenium Webdriver: O selenium webdriver permitir realizar as interações do usuário na página web. Utilizando o selenium webdriver permitir utilizar o conceito de pattern page objects, que para esta apliação foi baseado nos menus e sub-menus da mesma.

* Python: 
 * por que é uma linguagem mais fácil de aprender a programar e desenvolver testes automatizado.
 * por que possui suporte a orientação a objeto e possui bastante lib open source e bom suporte pela comunidade python.

## Use a ferramenta de controle de bugs (embutida na aplicação) para o cadastro dos problemas que você encontrar;
* Os bugs foram cadastrados manualmente. Fiquei na dúvida se deveriam ser automatizados.

## Nos demonstre os casos de testes que você criar (caso haja). Se você tiver escrito qualquer outro tipo de documentação, ou código gostaríamos de ver também. Todos os arquivos que você enviar devem ser enviados em somente um zip ou no github.

* Os cenarios de testes que crie estão na seções: Outros Cenário de Testes. 

## Nos entregue anotações, questões ou qualquer coisa que possa ter surgido enquanto você fazia seus testes.
 * Como não tinha uma forma de deletar os dados inseridos, a listagem ficou com bastantes informações.
 * Obtive problemas de encode ao obter o nome "Materiais Médicos" do campo Tipo.


# Pré-Requisitos
* Ubuntu
* Firefox 54 ou superior
  * geckodriver>=0.19 ou superior
* Python 2.7.6
  * pip >= 1.5.4
  * behave >= 1.2.6 ou superior
  * selenium >= 3.10 ou superior
  * pyhamcrest >= 1.8 ou superior
  * json


# Estrutura do projeto
* features/
    * locators/ -- Source code  para localizar os elementos da pagina
    * pages/ -- Source code que representa os objetos da pagina
    * steps/ -- Source code que representa as ações de acordo com cenario de teste.
    * *.features -- sao os cenarios de testes descritos
* resources/ -- Contem executavel do firefox e arquivo python para leiutura da config

# Execução dos Testes
Para execução dos testes é necessário:
* Estar na pasta do projeto "DesafioBionexo" e executar:
 * behave -t "tage_feature"
    * tag_feature: pode ser (create_products, edit_products, list_products) estes são colocadas em cada arquivo *.feature

# Outros cenários de Teste

* User Story 1:Como hospital quero deletar produtos previamente cadastrados
 * Critérios de Aceite:
  Devo acessar o produto pela listagem de produtos
  Após deletar deve aparecer uma mensagem de sucesso
  Deve retornar para listagem de produtos

* User Story 2: Como hospital quero pesquisar pelo nome do produto
 * Critérios de Aceite:
  Deve acessar o produto pela listagem de produtos
  Deve ter um campo para inserir o nome do produto e fazer a pesquisa
  Deve retornar uma lista de produtos com o nome pesquisado

* User Story 3: Como hospital quero cadastrar produtos com nome e código existentes
 * Critérios de Aceite:
  Devem existir os campos Código, nome, tipo, preço, Fabricante, Detalhes e status.
  Todos os campos são obrigatórios.
  Deve aparecer uma mensagem de nome e código do produto existente e não cadastrar o produto.

* User Story 4:Como hospital quero diferentes usuários cadastrando 5 novos produtos ao mesmo tempo
 * Critérios de Aceite:
  Devem existir os campos Código, nome, tipo, preço, Fabricante, Detalhes e status.
  Todos os campos são obrigatórios.
  Deve aparecer uma mensagem de produtos adicionado com sucesso.


# Config.json

* "user_email": "thiago_santos89@gmail.com" -- usera para logar na pagina da bionexo
* "user_pass": "KqE9BSQdbkj7ap" -- senha para logar na pagina da bionexo
* "base_url": "http://qainterview.qa.cloud.bionexo.com.br" -- url default da pagina da bionexo
* "path_geckodriver": "./resources/geckodriver" -- path do geckodriver para os testes executar
