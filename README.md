# DesafioBionexo

# Pré-Requisitos
* Ubuntu
* Firefox 54
  * geckodriver>=0.19
* Python 2.7.6
  * pip >= 1.5.4
  * behave >= 1.2.6
  * selenium >= 3.11
  * pyhamcrest >= 1.9.0
  * json


# Estrutura do projeto
* features/
    * locators/ -- Source code  para localizar os elementos da pagina
    * pages/ -- Source code que representa os objetos da pagina
    * steps/ -- Source code que representa as ações de acordo com cenario de teste.
    * *.features -- sao os cenarios de testes descritos 
* resources/ -- Contem executavel do firefox e arquivo python para leiutura da config

# Execução dos Testes
Para execução dos testes e necessario:
* Estar na pasta do projeto
# Outros cenários de Teste

* User Story 1
Como hospital quero deletar produtos previamente cadastrados
Critérios de Aceite:
- Devo acessar o produto pela listagem de produtos
- Após deletar deve aparecer uma mensagem de sucesso
- Deve retornar para listagem de produtos

* User Story 2
Como hospital quero pesquisar pelo nome do produto
Critérios de Aceite:
- Deve acessar o produto pela listagem de produtos
- Deve ter um campo para inserir o nome do produto e fazer a pesquisa
- Deve retornar uma lista de produtos com o nome pesquisado

* User Story 3
Como hospital quero cadastrar produtos com nome e código existentes
Critérios de Aceite:
- Devem existir os campos Código, nome, tipo, preço, Fabricante, Detalhes e status.
- Todos os campos são obrigatórios.
- Deve aparecer uma mensagem de nome e código do produto existente e não cadastrar o produto.

* User Story 4
Como hospital quero diferentes usuários cadastrando 5 novos produtos ao mesmo tempo
Critérios de Aceite:
- Devem existir os campos Código, nome, tipo, preço, Fabricante, Detalhes e status.
- Todos os campos são obrigatórios.
- Deve aparecer uma mensagem de produtos adicionado com sucesso.


# Config.json

* "user_email": "thiago_santos89@gmail.com" -- usera para logar na pagina da bionexo
* "user_pass": "KqE9BSQdbkj7ap" -- senha para logar na pagina da bionexo
* "base_url": "http://qainterview.qa.cloud.bionexo.com.br" -- url default da pagina da bionexo
* "path_geckodriver": "./resources/geckodriver" -- path do geckodriver para os testes executar
