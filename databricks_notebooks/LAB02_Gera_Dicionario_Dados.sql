-- Databricks notebook source
-- MAGIC %md
-- MAGIC
-- MAGIC <img src="https://raw.githubusercontent.com/Databricks-BR/dw/main/images/header_dw_notebook.png">

-- COMMAND ----------

-- MAGIC %md
-- MAGIC | TABELA | descrição |
-- MAGIC | -- | -- |
-- MAGIC | system.**information_schema**.catalogs | Nome e Descrição de TODAS as Catalogos |
-- MAGIC | system.**information_schema**.catalog_privileges | Privilégios de acesso aos catálogos de dados |
-- MAGIC | system.**information_schema**.tables | Nome e Descrição de TODAS as Tabelas do catálogo |
-- MAGIC | system.**information_schema**.table_privileges | Privilégios de acesso das Tabelas |
-- MAGIC | system.**information_schema**.columns | Nome e Descrição de TODAS as Colunas (campos) das Tabelas |
-- MAGIC

-- COMMAND ----------

-- MAGIC %md
-- MAGIC #### Gerando uma LISTA de todas as Tabelas com comentários

-- COMMAND ----------

-- CREATE OR REPLACE TABLE dic_tabelas
-- AS
SELECT table_catalog as catalog_name,
       table_schema as schema_name,
       table_name as table_name,
       table_owner as owner_name,
       table_type as table_type,
       comment as table_comment
    --   CASE 
    --       WHEN comment IS NULL THEN comment 
    --       ELSE ai_translate(comment, 'pt-BR') 
    --   END as table_comment
FROM system.information_schema.tables
WHERE
   table_catalog <> 'system'

-- COMMAND ----------

-- MAGIC %md
-- MAGIC #### Gerando uma LISTA de todas as COLUNAS (Campos) com comentários

-- COMMAND ----------

SELECT table_catalog as catalog_name,
       table_schema as schema_name,
       table_name as table_name,        
       column_name,
      comment as column_comment
FROM system.information_schema.columns
WHERE
   table_catalog <> 'system'
