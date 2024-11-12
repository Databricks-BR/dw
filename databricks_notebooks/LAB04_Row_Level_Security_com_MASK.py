# Databricks notebook source
# MAGIC %md
# MAGIC <img src="https://raw.githubusercontent.com/Databricks-BR/dw/main/images/header_dw_notebook.png">

# COMMAND ----------

# MAGIC %md
# MAGIC <img src="https://raw.githubusercontent.com/Databricks-BR/lab_sql/main/images/lab01_uc.png">

# COMMAND ----------

# MAGIC %md
# MAGIC #### Referências:
# MAGIC
# MAGIC * https://docs.databricks.com/en/data-governance/unity-catalog/row-and-column-filters.html#column-mask-examples

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE FUNCTION cpf_mask(cpf STRING)
# MAGIC   RETURN CASE WHEN is_member('HumanResourceDept') THEN cpf ELSE '***-**-****' END;

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC CREATE TABLE users (
# MAGIC   name STRING,
# MAGIC   cpf STRING MASK cpf_mask);
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC #### outra alternativa (se a tabela já estiver criada)

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE TABLE users
# MAGIC   (name STRING, cpf STRING);
# MAGIC
# MAGIC ALTER TABLE users ALTER COLUMN cpf SET MASK cpf_mask;
# MAGIC
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC -- pra retirar a MASK
# MAGIC
# MAGIC ALTER TABLE users ALTER COLUMN cpf DROP MASK;
# MAGIC
