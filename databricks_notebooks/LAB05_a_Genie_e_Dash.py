# Databricks notebook source
# MAGIC %md
# MAGIC <img src="https://raw.githubusercontent.com/Databricks-BR/dw/main/images/header_dw_notebook.png">

# COMMAND ----------

# MAGIC %md
# MAGIC # Sobre a base de dados que será utilizada
# MAGIC
# MAGIC <img src="http://assets.pokemon.com/assets/cms2/img/pokedex/full/001.png" width="100px">
# MAGIC <img src="http://assets.pokemon.com/assets/cms2/img/pokedex/full/002.png" width="100px">
# MAGIC <img src="http://assets.pokemon.com/assets/cms2/img/pokedex/full/003.png" width="100px">
# MAGIC <img src="http://assets.pokemon.com/assets/cms2/img/pokedex/full/004.png" width="100px">
# MAGIC <img src="http://assets.pokemon.com/assets/cms2/img/pokedex/full/005.png" width="100px">
# MAGIC <img src="http://assets.pokemon.com/assets/cms2/img/pokedex/full/006.png" width="100px">
# MAGIC <img src="http://assets.pokemon.com/assets/cms2/img/pokedex/full/007.png" width="100px">
# MAGIC <img src="http://assets.pokemon.com/assets/cms2/img/pokedex/full/008.png" width="100px">
# MAGIC <img src="http://assets.pokemon.com/assets/cms2/img/pokedex/full/009.png" width="100px">
# MAGIC <img src="http://assets.pokemon.com/assets/cms2/img/pokedex/full/010.png" width="100px">
# MAGIC <img src="http://assets.pokemon.com/assets/cms2/img/pokedex/full/011.png" width="100px">
# MAGIC <img src="http://assets.pokemon.com/assets/cms2/img/pokedex/full/012.png" width="100px">
# MAGIC
# MAGIC ## Você já ouviu falar sobre Pokémons?
# MAGIC Pokémon é uma franquia de mídia originária do Japão que gira em torno de criaturas fictícias chamadas "Pokémons" (abreviação de "Pocket Monsters", ou "Monstros de Bolso"). A ideia central é que os Pokémons são seres com habilidades especiais, como a capacidade de lançar ataques elementares ou de evoluir para formas mais poderosas. Eles podem ser capturados, treinados e usados em batalhas contra outros Pokémons.
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC <!-- Tipos de Pokémons -->
# MAGIC
# MAGIC ## Tipos de Pokémons
# MAGIC
# MAGIC Os Pokémons são classificados em diferentes tipos, cada um com suas próprias características e habilidades. Abaixo estão alguns dos tipos mais comuns:
# MAGIC
# MAGIC | Fogo | Água | Planta | Elétrico |
# MAGIC | --- | --- | --- | --- |
# MAGIC | <img src="http://assets.pokemon.com/assets/cms2/img/pokedex/full/004.png" width="100px"> <img src="http://assets.pokemon.com/assets/cms2/img/pokedex/full/005.png" width="100px"> <img src="http://assets.pokemon.com/assets/cms2/img/pokedex/full/006.png" width="100px"> | <img src="http://assets.pokemon.com/assets/cms2/img/pokedex/full/007.png" width="100px"> <img src="http://assets.pokemon.com/assets/cms2/img/pokedex/full/008.png" width="100px"> <img src="http://assets.pokemon.com/assets/cms2/img/pokedex/full/009.png" width="100px"> | <img src="http://assets.pokemon.com/assets/cms2/img/pokedex/full/001.png" width="100px"> <img src="http://assets.pokemon.com/assets/cms2/img/pokedex/full/002.png" width="100px"> <img src="http://assets.pokemon.com/assets/cms2/img/pokedex/full/003.png" width="100px"> | <img src="http://assets.pokemon.com/assets/cms2/img/pokedex/full/025.png" width="100px"> <img src="http://assets.pokemon.com/assets/cms2/img/pokedex/full/026.png" width="100px"> |
# MAGIC
# MAGIC | Pedra | Voador | Fantasma | Psíquico |
# MAGIC | --- | --- | --- | --- |
# MAGIC | <img src="http://assets.pokemon.com/assets/cms2/img/pokedex/full/074.png" width="100px"> <img src="http://assets.pokemon.com/assets/cms2/img/pokedex/full/075.png" width="100px"> <img src="http://assets.pokemon.com/assets/cms2/img/pokedex/full/076.png" width="100px"> | <img src="http://assets.pokemon.com/assets/cms2/img/pokedex/full/016.png" width="100px"> <img src="http://assets.pokemon.com/assets/cms2/img/pokedex/full/017.png" width="100px"> <img src="http://assets.pokemon.com/assets/cms2/img/pokedex/full/018.png" width="100px"> | <img src="http://assets.pokemon.com/assets/cms2/img/pokedex/full/092.png" width="100px"> <img src="http://assets.pokemon.com/assets/cms2/img/pokedex/full/093.png" width="100px"> <img src="http://assets.pokemon.com/assets/cms2/img/pokedex/full/094.png" width="100px"> | <img src="http://assets.pokemon.com/assets/cms2/img/pokedex/full/063.png" width="100px"> <img src="http://assets.pokemon.com/assets/cms2/img/pokedex/full/064.png" width="100px"> <img src="http://assets.pokemon.com/assets/cms2/img/pokedex/full/065.png" width="100px"> |
# MAGIC
# MAGIC | Inseto | Lutador | Veneno | Terra |
# MAGIC | --- | --- | --- | --- |
# MAGIC | <img src="http://assets.pokemon.com/assets/cms2/img/pokedex/full/010.png" width="100px"> <img src="http://assets.pokemon.com/assets/cms2/img/pokedex/full/011.png" width="100px"> <img src="http://assets.pokemon.com/assets/cms2/img/pokedex/full/012.png" width="100px"> | <img src="http://assets.pokemon.com/assets/cms2/img/pokedex/full/066.png" width="100px"> <img src="http://assets.pokemon.com/assets/cms2/img/pokedex/full/067.png" width="100px"> <img src="http://assets.pokemon.com/assets/cms2/img/pokedex/full/068.png" width="100px"> | <img src="http://assets.pokemon.com/assets/cms2/img/pokedex/full/023.png" width="100px"> <img src="http://assets.pokemon.com/assets/cms2/img/pokedex/full/024.png" width="100px"> | <img src="http://assets.pokemon.com/assets/cms2/img/pokedex/full/027.png" width="100px"> <img src="http://assets.pokemon.com/assets/cms2/img/pokedex/full/028.png" width="100px"> |
# MAGIC
# MAGIC | Gelo | Dragão | Fada | Aço |
# MAGIC | --- | --- | --- | --- |
# MAGIC | <img src="http://assets.pokemon.com/assets/cms2/img/pokedex/full/087.png" width="100px"> <img src="http://assets.pokemon.com/assets/cms2/img/pokedex/full/091.png" width="100px"> | <img src="http://assets.pokemon.com/assets/cms2/img/pokedex/full/147.png" width="100px"> <img src="http://assets.pokemon.com/assets/cms2/img/pokedex/full/148.png" width="100px"> <img src="http://assets.pokemon.com/assets/cms2/img/pokedex/full/149.png" width="100px"> | <img src="http://assets.pokemon.com/assets/cms2/img/pokedex/full/035.png" width="100px"> <img src="http://assets.pokemon.com/assets/cms2/img/pokedex/full/036.png" width="100px"> | <img src="http://assets.pokemon.com/assets/cms2/img/pokedex/full/081.png" width="100px"> <img src="http://assets.pokemon.com/assets/cms2/img/pokedex/full/082.png" width="100px"> |

# COMMAND ----------

# MAGIC %md
# MAGIC # Atividade 1: Criando a tabela <img src="http://assets.pokemon.com/assets/cms2/img/pokedex/full/004.png" width="100px">
# MAGIC
# MAGIC 1 -  Faça o download do arquivo https://github.com/Databricks-BR/dw/blob/main/dados/pokemon.csv
# MAGIC
# MAGIC 2 - Clique em ***New*** no canto superior esquedo e selecione ***Add or upload data***
# MAGIC
# MAGIC <img src="https://raw.githubusercontent.com/Databricks-BR/dw/refs/heads/main/images/addNewDataLab4.jpeg" width="600px">
# MAGIC
# MAGIC 3 - Clique em ***Create or modify table***
# MAGIC
# MAGIC <img src="https://raw.githubusercontent.com/Databricks-BR/dw/refs/heads/main/images/CreateTableLab4.jpeg" width="600px">
# MAGIC
# MAGIC 4 - Arraste o arquivo que você fez o download para a área indicada
# MAGIC
# MAGIC <img src="https://raw.githubusercontent.com/Databricks-BR/dw/refs/heads/main/images/ChooseFileLab4.jpeg" width="600px">
# MAGIC
# MAGIC 5 - Seleciono o catálogo e o schema que você irá utilizar neste laboratório. Para finalizar, clique em ***Create table*** no canto inferior direito
# MAGIC
# MAGIC <img src="https://raw.githubusercontent.com/Databricks-BR/dw/refs/heads/main/images/newTableLab4.jpeg" width="600px">
# MAGIC
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC # Atividade 2: Teste se a tabela foi criada corretamente <img src="http://assets.pokemon.com/assets/cms2/img/pokedex/full/005.png" width="100px">
# MAGIC
# MAGIC Para testar iremos usar SQL. 
# MAGIC
# MAGIC Na Query abaixo, substitua <SEU_CATALOGO> e <SEU_SCHEMA>  pelas respectivas informações, que foram definidas no passo anterior para pa tabela pokemon

# COMMAND ----------

# MAGIC %sql
# MAGIC -- Testando se a tabela foi criada corretamente
# MAGIC
# MAGIC
# MAGIC select * from <SEU_CATALOGO>.<SEU_SCHEMA>.pokemon
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC # Atividade 3:  Criando uma Genie <img src="http://assets.pokemon.com/assets/cms2/img/pokedex/full/001.png" width="100px">
# MAGIC
# MAGIC 1 - No menu esquedo, clique em ***Genie***
# MAGIC
# MAGIC 2 - Clique em ***New*** no canto superior direito
# MAGIC
# MAGIC 3 - Dê um em **Title**
# MAGIC
# MAGIC 4 - Selecione seu cluster SQL serverless no campo **Default warehouse**
# MAGIC
# MAGIC 5 - Clique em **Add Table** e selecione a sua tabela **pokemon**
# MAGIC
# MAGIC 6 - Clique em **Save**
# MAGIC
# MAGIC <img src="https://raw.githubusercontent.com/Databricks-BR/dw/refs/heads/main/images/GenieLab4.jpeg" width="600">
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC # Atividade 4:  Explorando dados com linguagem natural <img src="http://assets.pokemon.com/assets/cms2/img/pokedex/full/009.png" width="100px">
# MAGIC
# MAGIC 1 - Faça as seguintes perguntas:
# MAGIC - Qual o pokemon com maior poder de ataque?
# MAGIC - Qual pokemon possui a melhor defesa?
# MAGIC - Poderia me trazer um gráfico de barras com a quantidade de pokemons por tipo?
# MAGIC   - Alguns pokemons tem mais de um tipo separado por virgula. Resolva isso pra mim. 
# MAGIC   - Traduza o tipo para português
# MAGIC   - Traduza novamente ignorando maiusculas e minúsculas
# MAGIC
# MAGIC
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC #Atividade 5: Criando um AI/BI Dashboard. <img src="http://assets.pokemon.com/assets/cms2/img/pokedex/full/007.png" width="100px">
# MAGIC
# MAGIC
# MAGIC 1 - Clique em **Dashboards** no menu esquerdo
# MAGIC
# MAGIC 2 - Clique em **New dashboard** no canto superior direito
# MAGIC
# MAGIC 3 - Na tela que abrirá, clique em **Data** e em seguida em **Create from SQL**
# MAGIC
# MAGIC <img src="https://github.com/Databricks-BR/dw/blob/main/images/newDashboardLab4.png?raw=true" width="300px">
# MAGIC
# MAGIC 4 - Cole a query abaixo no editor de SQL que abrirá. Não esqueça de mudar o catálogo e schema
# MAGIC
# MAGIC SELECT
# MAGIC   <br>link_url
# MAGIC   <br>,pokemon_name
# MAGIC   <br>,total
# MAGIC   <br>,hp
# MAGIC   <br>,attack
# MAGIC   <br>,defense
# MAGIC   <br>,special_attack
# MAGIC   <br>,speed
# MAGIC   <br>,pokemon_type
# MAGIC   <br>,generation
# MAGIC   <br>,Average_CP
# MAGIC   <br>,Average_HP
# MAGIC   <br>,Max_HP
# MAGIC   <br>,Tier
# MAGIC <br>FROM {SEU_CATALOGO}.{SEU_SCHEMA}.pokemon
# MAGIC
# MAGIC
# MAGIC 5 - Clique em **Canvas**
# MAGIC  
# MAGIC 6 - Na barra inferior azul, clique em **Add visualization**
# MAGIC
# MAGIC 7 - Repita o passo 6 para cada linha abaixo
# MAGIC   - Qual Distribuição por tier?
# MAGIC   - Qual a quantidade total?
# MAGIC   - Traga uma tabela com todas as colunas
# MAGIC
# MAGIC
# MAGIC
# MAGIC
# MAGIC
