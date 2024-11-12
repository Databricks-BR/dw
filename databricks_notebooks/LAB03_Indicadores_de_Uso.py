# Databricks notebook source
# MAGIC %md
# MAGIC <img src="https://raw.githubusercontent.com/Databricks-BR/dw/main/images/header_dw_notebook.png">

# COMMAND ----------

# MAGIC %md
# MAGIC ## SYSTEM TABLES.  (system.billing.usage)
# MAGIC
# MAGIC * https://docs.databricks.com/en/administration-guide/system-tables/billing.html
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC -- Quantas DBUs de cada SKU foram usadas até agora este mês?
# MAGIC
# MAGIC SELECT
# MAGIC CASE
# MAGIC     WHEN sku_name LIKE '%ALL_PURPOSE%' THEN 'ALL_PURPOSE'
# MAGIC     WHEN sku_name LIKE '%JOBS%' THEN 'JOBS'
# MAGIC     WHEN sku_name LIKE '%DLT%' THEN 'DLT' 
# MAGIC     WHEN sku_name LIKE '%SQL%' THEN 'SQL'
# MAGIC     WHEN sku_name LIKE '%INFERENCE%' THEN 'MODEL_INFERENCE'
# MAGIC     ELSE 'OTHER'
# MAGIC END AS sku,
# MAGIC round(sum(usage_quantity),0) as `DBUs`
# MAGIC
# MAGIC FROM system.billing.usage
# MAGIC WHERE month(usage_date) = month(CURRENT_DATE)
# MAGIC GROUP BY sku
# MAGIC ORDER BY `DBUs` DESC;
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC -- Qual é a tendência diária no consumo de DBU?
# MAGIC
# MAGIC SELECT date(usage_date) as `Date`, 
# MAGIC round(sum(usage_quantity),0) as `DBUs Consumed`
# MAGIC FROM system.billing.usage
# MAGIC GROUP BY date(usage_date)
# MAGIC ORDER BY date(usage_date) ASC;
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC -- Quais Jobs consumiram mais DBUs?
# MAGIC
# MAGIC SELECT usage_metadata.job_id as `Job ID`, 
# MAGIC round(sum(usage_quantity),0) as `DBUs`
# MAGIC FROM system.billing.usage
# MAGIC WHERE usage_metadata.job_id is not null
# MAGIC GROUP BY `Job ID`
# MAGIC ORDER BY `DBUs` DESC;

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC
# MAGIC -- Quantidade de Users ATIVOS por Mes
# MAGIC
# MAGIC SELECT year_month,
# MAGIC active_users,
# MAGIC LAG(active_users, 1)
# MAGIC OVER (ORDER BY year_month)
# MAGIC AS active_users_previous_month,
# MAGIC
# MAGIC CASE
# MAGIC WHEN LAG(active_users, 1)
# MAGIC OVER (ORDER BY year_month)
# MAGIC IS null THEN 0 -- o primeiro mês não tem mês anterior
# MAGIC ELSE active_users - LAG(active_users, 1)
# MAGIC OVER (ORDER BY year_month)
# MAGIC END AS growth,
# MAGIC round(((active_users-active_users_previous_month)*100)/active_users_previous_month, 2) as perc_grow
# MAGIC FROM (
# MAGIC SELECT date_format(event_time, 'MM/yy') as year_month,
# MAGIC count(DISTINCT user_identity.email) as active_users
# MAGIC FROM system.access.audit
# MAGIC WHERE year(event_time) = year(current_date()) AND action_name IS NOT NULL
# MAGIC GROUP BY year_month
# MAGIC
# MAGIC ORDER BY year_month)
