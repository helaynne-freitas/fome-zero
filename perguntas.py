# perguntas.py

# --------------------------------------------------
#  IMPORTS
# --------------------------------------------------
import pandas as pd

# --------------------------------------------------
#  CARREGAR O DATASET
# --------------------------------------------------
df = pd.read_csv('dataset/zomato.csv')

# --------------------------------------------------
#  Padronizar nomes de colunas para facilitar
#    (transforma em minúsculas e troca espaço por _)
# --------------------------------------------------
df.columns = df.columns.str.lower().str.replace(' ', '_')

# Agora suas colunas ficam assim:
# restaurant_id, restaurant_name, country_code, city, ...
# price_range, aggregate_rating, rating_color, votes, etc.


# --------------------------------------------------
#  1. Quantos restaurantes únicos estão registrados?
# --------------------------------------------------
restaurantes_unicos = df['restaurant_id'].nunique()


# --------------------------------------------------
#  2. Quantos países únicos estão registrados?
#    (a coluna real é "country_code")
# --------------------------------------------------
paises_unicos = df['country_code'].nunique()


# --------------------------------------------------
#  3. Quantas cidades únicas estão registradas?
# --------------------------------------------------
cidades_unicas = df['city'].nunique()


# --------------------------------------------------
#  4. Qual o total de avaliações feitas?
#    (somatório da coluna "votes")
# --------------------------------------------------
total_avaliacoes = df['votes'].sum()


# --------------------------------------------------
#  5. Quantos tipos de culinária únicos estão registrados?
#    A coluna é "cuisines", e cada linha pode ter várias culinárias
# --------------------------------------------------
lista_culinarias = (
    df['cuisines']
    .dropna()
    .str.split(',')   # separa por vírgula
    .explode()        # transforma em linhas individuais
    .str.strip()      # remove espaços
)

culinarias_unicas = lista_culinarias.nunique()


# --------------------------------------------------
#  MOSTRAR RESULTADOS
# --------------------------------------------------
print("🔎 RESULTADOS GERAIS")
print(f"1. Restaurantes únicos: {restaurantes_unicos}")
print(f"2. Países únicos: {paises_unicos}")
print(f"3. Cidades únicas: {cidades_unicas}")
print(f"4. Total de avaliações feitas: {total_avaliacoes}")
print(f"5. Tipos de culinária únicos: {culinarias_unicas}")


# --------------------------------------------------
#  IMPORTS
# --------------------------------------------------
import pandas as pd

# --------------------------------------------------
#  CARREGAR E PADRONIZAR COLUNAS
# --------------------------------------------------
df = pd.read_csv("dataset/zomato.csv")
df.columns = df.columns.str.lower().str.replace(" ", "_")
# Agora temos: restaurant_id, restaurant_name, country_code, price_range,
# aggregate_rating, votes, has_online_delivery, has_table_booking, etc.

# --------------------------------------------------
#  1. País com mais cidades registradas
# --------------------------------------------------
pais_mais_cidades = (
    df.groupby("country_code")["city"]
    .nunique()
    .idxmax()
)

# --------------------------------------------------
#  2. País com mais restaurantes registrados
# --------------------------------------------------
pais_mais_restaurantes = (
    df.groupby("country_code")["restaurant_id"]
    .nunique()
    .idxmax()
)

# --------------------------------------------------
#  3. País com mais restaurantes com nível de preço = 4
# --------------------------------------------------
pais_mais_preco4 = (
    df[df["price_range"] == 4]
    .groupby("country_code")["restaurant_id"]
    .nunique()
    .idxmax()
)

# --------------------------------------------------
#  4. País com maior quantidade de tipos de culinária distintos
# --------------------------------------------------
# Explodindo a coluna de culinárias
culinarias = (
    df[["country_code", "cuisines"]]
    .dropna()
    .assign(cuisines=df["cuisines"].str.split(","))
    .explode("cuisines")
)
culinarias["cuisines"] = culinarias["cuisines"].str.strip()

pais_mais_culinarias = (
    culinarias.groupby("country_code")["cuisines"]
    .nunique()
    .idxmax()
)

# --------------------------------------------------
#  5. País com maior quantidade de avaliações feitas (soma de votos)
# --------------------------------------------------
pais_mais_avaliacoes = (
    df.groupby("country_code")["votes"]
    .sum()
    .idxmax()
)

# --------------------------------------------------
# 6. País com mais restaurantes que fazem entrega
#    (coluna: has_online_delivery)
# --------------------------------------------------

pais_mais_entrega = (
    df[df["has_online_delivery"] == 1]   # agora usando 1
    .groupby("country_code")["restaurant_id"]
    .nunique()
    .idxmax()
)


# --------------------------------------------------
#  7. País com mais restaurantes que aceitam reservas
#    (coluna: has_table_booking)
# --------------------------------------------------

pais_mais_reservas = (
    df[df["has_table_booking"] == 1]     # agora usando 1
    .groupby("country_code")["restaurant_id"]
    .nunique()
    .idxmax()
)


# --------------------------------------------------
#  8. País com maior média de avaliações feitas
# --------------------------------------------------
pais_maior_media_avaliacoes = (
    df.groupby("country_code")["votes"]
    .mean()
    .idxmax()
)

# --------------------------------------------------
#  9. País com a maior média de notas (aggregate_rating)
# --------------------------------------------------
pais_maior_nota_media = (
    df.groupby("country_code")["aggregate_rating"]
    .mean()
    .idxmax()
)

# --------------------------------------------------
#  10. País com a menor média de notas (aggregate_rating)
# --------------------------------------------------
pais_menor_nota_media = (
    df.groupby("country_code")["aggregate_rating"]
    .mean()
    .idxmin()
)

# --------------------------------------------------
#  11. Média de preço para dois por país
#    (coluna: average_cost_for_two)
# --------------------------------------------------
media_preco_por_pais = (
    df.groupby("country_code")["average_cost_for_two"]
    .mean()
)

# --------------------------------------------------
#  EXIBIR RESULTADOS
# --------------------------------------------------
print("\n🔎 RESULTADOS POR PAÍS\n")

print(f"1. País com mais cidades registradas: {pais_mais_cidades}")
print(f"2. País com mais restaurantes registrados: {pais_mais_restaurantes}")
print(f"3. País com mais restaurantes com preço 4: {pais_mais_preco4}")
print(f"4. País com mais tipos de culinárias distintos: {pais_mais_culinarias}")
print(f"5. País com maior quantidade total de avaliações: {pais_mais_avaliacoes}")
print(f"6. País com mais restaurantes que fazem entrega: {pais_mais_entrega}")
print(f"7. País com mais restaurantes que aceitam reservas: {pais_mais_reservas}")
print(f"8. País com maior média de avaliações: {pais_maior_media_avaliacoes}")
print(f"9. País com maior nota média: {pais_maior_nota_media}")
print(f"10. País com menor nota média: {pais_menor_nota_media}")

print("\n11. Média de preço para dois por país:")
print(media_preco_por_pais)


# --------------------------------------------------
#  IMPORTS
# --------------------------------------------------
import pandas as pd

# --------------------------------------------------
#  CARREGAR E PADRONIZAR
# --------------------------------------------------
df = pd.read_csv("dataset/zomato.csv")
df.columns = df.columns.str.lower().str.replace(" ", "_")


# --------------------------------------------------
#  1. Cidade com mais restaurantes registrados
# --------------------------------------------------
cidade_mais_restaurantes = (
    df.groupby("city")["restaurant_id"]
    .nunique()
    .idxmax()
)


# --------------------------------------------------
#  2. Cidade com mais restaurantes com nota média acima de 4
# --------------------------------------------------
cidade_nota_acima4 = (
    df[df["aggregate_rating"] > 4.0]
    .groupby("city")["restaurant_id"]
    .nunique()
    .idxmax()
)


# --------------------------------------------------
#  3. Cidade com mais restaurantes com nota média abaixo de 2.5
# --------------------------------------------------
cidade_nota_abaixo2_5 = (
    df[df["aggregate_rating"] < 2.5]
    .groupby("city")["restaurant_id"]
    .nunique()
    .idxmax()
)


# --------------------------------------------------
#  4. Cidade com o maior valor médio de um prato para dois
# --------------------------------------------------
cidade_maior_preco_medio = (
    df.groupby("city")["average_cost_for_two"]
    .mean()
    .idxmax()
)


# --------------------------------------------------
#  5. Cidade com maior quantidade de tipos de culinárias distintas
# --------------------------------------------------
culinarias = (
    df[["city", "cuisines"]]
    .dropna()
    .assign(cuisines=df["cuisines"].str.split(","))
    .explode("cuisines")
)
culinarias["cuisines"] = culinarias["cuisines"].str.strip()

cidade_mais_culinarias = (
    culinarias.groupby("city")["cuisines"]
    .nunique()
    .idxmax()
)


# --------------------------------------------------
#  6. Cidade com mais restaurantes que fazem reservas
#     (has_table_booking == 1)
# --------------------------------------------------
cidade_mais_reservas = (
    df[df["has_table_booking"] == 1]
    .groupby("city")["restaurant_id"]
    .nunique()
    .idxmax()
)


# --------------------------------------------------
#  7. Cidade com mais restaurantes que fazem entregas
#     (has_online_delivery == 1)
# --------------------------------------------------
cidade_mais_entregas = (
    df[df["has_online_delivery"] == 1]
    .groupby("city")["restaurant_id"]
    .nunique()
    .idxmax()
)


# --------------------------------------------------
#  8. Cidade com mais restaurantes que aceitam pedidos online
#     (mesma coluna: has_online_delivery == 1)
# --------------------------------------------------
cidade_mais_pedido_online = (
    df[df["has_online_delivery"] == 1]
    .groupby("city")["restaurant_id"]
    .nunique()
    .idxmax()
)


# --------------------------------------------------
#  EXIBIR RESULTADOS
# --------------------------------------------------
print("\n🔎 RESULTADOS POR CIDADE\n")

print(f"1. Cidade com mais restaurantes: {cidade_mais_restaurantes}")
print(f"2. Cidade com mais restaurantes nota > 4: {cidade_nota_acima4}")
print(f"3. Cidade com mais restaurantes nota < 2.5: {cidade_nota_abaixo2_5}")
print(f"4. Cidade com maior preço médio p/ dois: {cidade_maior_preco_medio}")
print(f"5. Cidade com mais tipos de culinária: {cidade_mais_culinarias}")
print(f"6. Cidade com mais restaurantes que fazem reservas: {cidade_mais_reservas}")
print(f"7. Cidade com mais restaurantes que entregam: {cidade_mais_entregas}")
print(f"8. Cidade com mais pedidos online: {cidade_mais_pedido_online}")



# ----------------------------------------------------------
# Restaurantes
# ----------------------------------------------------------
import pandas as pd

# 1. Carregar dataset padronizando colunas
df = pd.read_csv("dataset/zomato.csv")
df.columns = df.columns.str.lower().str.replace(" ", "_")


# ==========================================================
# 1. Restaurante com maior quantidade de avaliações (votes)
# ==========================================================
restaurant_most_votes = df.loc[df['votes'].idxmax(), 'restaurant_name']


# ==========================================================
# 2. Restaurante com maior nota média (aggregate_rating)
# ==========================================================
restaurant_best_rating = df.loc[df['aggregate_rating'].idxmax(), 'restaurant_name']


# ==========================================================
# 3. Restaurante com maior custo para duas pessoas
# ==========================================================
restaurant_highest_cost = df.loc[df['average_cost_for_two'].idxmax(), 'restaurant_name']


# ==========================================================
# 4. Culinária brasileira com menor média de avaliação
# ==========================================================
df_brazilian = df[df['cuisines'].str.contains("Brazilian", case=False, na=False)]

restaurant_brazilian_lowest_rating = (
    df_brazilian.loc[df_brazilian['aggregate_rating'].idxmin(), 'restaurant_name']
    if not df_brazilian.empty else None
)


# ==========================================================
# 5. Culinária brasileira + País Brasil (country_code = 30)
# ==========================================================
df_brazil_brazilian = df[
    (df['country_code'] == 30) &
    (df['cuisines'].str.contains("Brazilian", case=False, na=False))
]

restaurant_brazilian_best_in_brazil = (
    df_brazil_brazilian.loc[df_brazil_brazilian['aggregate_rating'].idxmax(), 'restaurant_name']
    if not df_brazil_brazilian.empty else None
)


# ==========================================================
# 6. Restaurantes com delivery online têm mais avaliações?
# ==========================================================
online_yes = df[df["has_online_delivery"] == 1]['votes'].mean()
online_no  = df[df["has_online_delivery"] == 0]['votes'].mean()

online_more_reviews = "Sim" if online_yes > online_no else "Não"


# ==========================================================
# 7. Restaurantes com reservas têm maior custo médio?
# ==========================================================
booking_yes = df[df["has_table_booking"] == 1]['average_cost_for_two'].mean()
booking_no  = df[df["has_table_booking"] == 0]['average_cost_for_two'].mean()

booking_more_expensive = "Sim" if booking_yes > booking_no else "Não"


# ==========================================================
# 8. Japoneses nos EUA são mais caros que BBQ?
# country_code 216 = EUA
# ==========================================================
df_usa = df[df['country_code'] == 216]

usa_japanese = df_usa[df_usa['cuisines'].str.contains("Japanese", case=False, na=False)]
usa_bbq      = df_usa[df_usa['cuisines'].str.contains("BBQ", case=False, na=False)]

avg_japanese = usa_japanese['average_cost_for_two'].mean()
avg_bbq = usa_bbq['average_cost_for_two'].mean()

japanese_more_expensive = "Sim" if avg_japanese > avg_bbq else "Não"


# ==========================================================
# PRINT FINAL
# ==========================================================
print("\n📝 RESULTADOS – PERGUNTAS DO CEO\n")

print("1. Restaurante com mais avaliações:", restaurant_most_votes)
print("2. Restaurante com maior nota média:", restaurant_best_rating)
print("3. Restaurante com maior custo para 2 pessoas:", restaurant_highest_cost)
print("4. Brasileiro com menor média de avaliação:", restaurant_brazilian_lowest_rating)
print("5. Brasileiro no Brasil com maior média:", restaurant_brazilian_best_in_brazil)
print("6. Delivery online tem mais avaliações?", online_more_reviews)
print("7. Restaurantes com reservas têm maior preço médio?", booking_more_expensive)
print("8. Japoneses nos EUA são mais caros que BBQ?", japanese_more_expensive)


# ----------------------------------------------------------
#  TIPOS DE CULINÁRIA 
# ----------------------------------------------------------
import pandas as pd

# 1. Carregar dataset padronizando colunas
df = pd.read_csv("dataset/zomato.csv")
df.columns = df.columns.str.lower().str.replace(" ", "_")


# ----------------------------------------------------------
# Função auxiliar para evitar repetição
# Retorna nome do restaurante com maior/menor rating dentro de um tipo de cozinha
# ----------------------------------------------------------
def best_restaurant(cuisine):
    subset = df[df["cuisines"].str.contains(cuisine, case=False, na=False)]
    if subset.empty:
        return None
    return subset.loc[subset["aggregate_rating"].idxmax(), "restaurant_name"]

def worst_restaurant(cuisine):
    subset = df[df["cuisines"].str.contains(cuisine, case=False, na=False)]
    if subset.empty:
        return None
    return subset.loc[subset["aggregate_rating"].idxmin(), "restaurant_name"]


# ==========================================================
# 1–10. Melhor e pior restaurante por culinária específica
# ==========================================================

# Italiano
italian_best = best_restaurant("Italian")
italian_worst = worst_restaurant("Italian")

# Americano
american_best = best_restaurant("American")
american_worst = worst_restaurant("American")

# Árabe
arabian_best = best_restaurant("Arabian|Arabic|Middle Eastern")
arabian_worst = worst_restaurant("Arabian|Arabic|Middle Eastern")

# Japonês
japanese_best = best_restaurant("Japanese")
japanese_worst = worst_restaurant("Japanese")

# Caseira (Homemade / Home food / Brazilian Home Style)
caseira_best = best_restaurant("Home|Caseira|Homemade")
caseira_worst = worst_restaurant("Home|Caseira|Homemade")


# ==========================================================
# 11. Tipo de culinária com maior valor médio para duas pessoas
# ==========================================================
df_cuisine_cost = (
    df.assign(cuisine=df["cuisines"].str.split(","))
      .explode("cuisine")
)

df_cuisine_cost["cuisine"] = df_cuisine_cost["cuisine"].str.strip()

cuisine_highest_cost = (
    df_cuisine_cost.groupby("cuisine")["average_cost_for_two"]
    .mean()
    .idxmax()
)


# ==========================================================
# 12. Tipo de culinária com maior nota média
# ==========================================================
cuisine_highest_rating = (
    df_cuisine_cost.groupby("cuisine")["aggregate_rating"]
    .mean()
    .idxmax()
)


# ==========================================================
# 13. Tipo de culinária com mais restaurantes que aceitam pedidos online
#      e fazem entregas (has_online_delivery == 1 e is_delivering_now == 1)
# ==========================================================
df_cuisine_delivery = df_cuisine_cost[
    (df_cuisine_cost["has_online_delivery"] == 1) &
    (df_cuisine_cost["is_delivering_now"] == 1)
]

cuisine_most_online_delivery = (
    df_cuisine_delivery.groupby("cuisine")["restaurant_id"]
    .nunique()
    .idxmax()
)


# ----------------------------------------------------------
# PRINT FINAL
# ----------------------------------------------------------
print("\n🍽️ RESULTADOS – TIPOS DE CULINÁRIA\n")

print(f"1. Italiano – Melhor avaliação: {italian_best}")
print(f"2. Italiano – Pior avaliação: {italian_worst}")

print(f"3. Americano – Melhor avaliação: {american_best}")
print(f"4. Americano – Pior avaliação: {american_worst}")

print(f"5. Árabe – Melhor avaliação: {arabian_best}")
print(f"6. Árabe – Pior avaliação: {arabian_worst}")

print(f"7. Japonês – Melhor avaliação: {japanese_best}")
print(f"8. Japonês – Pior avaliação: {japanese_worst}")

print(f"9. Caseira – Melhor avaliação: {caseira_best}")
print(f"10. Caseira – Pior avaliação: {caseira_worst}")

print(f"11. Culinária com maior custo médio p/ 2 pessoas: {cuisine_highest_cost}")
print(f"12. Culinária com maior nota média: {cuisine_highest_rating}")
print(f"13. Culinária com mais pedidos online + entregas: {cuisine_most_online_delivery}")
