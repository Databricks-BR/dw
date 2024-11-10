## PRÉ-REQUISITOS para o Treinamento:

* Ter acesso a um ambiente Databricks
* Ter o Genie Spaces HABILITADO no Menu
* Ter o Unity Catalog Instalado no Ambiente
* Os participantes já precisam ter seus acessos concedidos
* Sugerimos criar um novo catálogo para essa finalidade:    "academy"
* Os participantes precisam ter direitos de criação de "schemas" e de "tabelas" debaixo deste catálogo. ("academy"), além de poder executar Queries.
* Disponibilizar um SQL Warehouse EndPoint (SERVERLESS) com tamanho de 2XSmall.

</br></br>

## Habilitando Genie Spaces:

Para verificar se a "GENIE" está habilitada, verifique a sessão SQL no menu esquerdo do seu workspace.
Caso não esteja habilitado, com o usuário de ADMIN do Databricks, seguir as instruções:

* [AZURE - Habilitando o GENIE](https://learn.microsoft.com/en-us/azure/databricks/genie/#enable-genie)
* [AWS/GCP - Habilitando o GENIE](https://docs.databricks.com/en/genie/index.html#enable-genie-spaces-in-your-workspace)

</br>

## Referências:

* [Create CATALOG](https://docs.databricks.com/en/sql/language-manual/sql-ref-syntax-ddl-create-catalog.html)
* [Criando um End-point Serverless](https://docs.databricks.com/en/compute/sql-warehouse/create.html)
* [Habilitando o Unity Catalog](https://docs.databricks.com/en/data-governance/unity-catalog/enable-workspaces.html)



