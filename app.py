
import streamlit as st
import pandas as pd
import plotly.express as px
from cleaning import clean_data   
from pathlib import Path

# --------------------------------------------------
# CONFIGURAÇÃO INICIAL DA PÁGINA
# --------------------------------------------------
st.set_page_config(
    page_title="Fome Zero",
    layout="wide",
    initial_sidebar_state="expanded"
)


DATA_PATH = Path("dataset/zomato.csv")

df = clean_data(str(DATA_PATH))

# ------------------
# SIDEBAR 
# ------------------

from PIL import Image

with st.sidebar:
    logo = Image.open("image/logo.png")
    st.image(logo, use_container_width=True)
    st.markdown("---")

    # Navegação entre páginas
    page = st.radio(
        "Navegação",
        [
            "Fome Zero (Home)",
            "Visão Países",
            "Visão Cidades",
            "Visão Tipos de Cozinhas"
        ]
    )

    st.markdown("### Filtros Globais")

    # Filtro por país
    countries = ["Todos"] + sorted(df["country"].unique().tolist())
    selected_country = st.selectbox("País", countries)

    # Filtro por faixa de preço
    price_range = st.slider(
        "Faixa de preço",
        int(df["price_range"].min()),
        int(df["price_range"].max()),
        (1, 4)
    )

    # Filtro por nota mínima
    rating_min = st.slider(
        "Nota mínima",
        float(df["aggregate_rating"].min()),
        float(df["aggregate_rating"].max()),
        float(df["aggregate_rating"].min())
    )

    # Filtro por entrega online
    only_delivery = st.checkbox("Apenas com delivery online", False)

    # Filtro por reservas
    only_booking = st.checkbox("Apenas com reservas", False)

    st.markdown("---")
    st.markdown("Use os filtros acima para ajustar o dashboard.")


# --------------------------------------------------
# FUNÇÃO PARA APLICAR FILTROS NO DATASET
# --------------------------------------------------
def apply_filters(df):
    df_f = df.copy()

    if selected_country != "Todos":
        df_f = df_f[df_f["country"] == selected_country]

    df_f = df_f[
        (df_f["price_range"] >= price_range[0]) &
        (df_f["price_range"] <= price_range[1])
    ]

    df_f = df_f[df_f["aggregate_rating"] >= rating_min]

    if only_delivery:
        df_f = df_f[df_f["has_online_delivery"] == 1]

    if only_booking:
        df_f = df_f[df_f["has_table_booking"] == 1]

    return df_f


df_filtered = apply_filters(df)


# ================================================================
#                P Á G I N A   H O M E  
# ================================================================
if page == "Fome Zero (Home)":

    st.title("Fome Zero")
    st.markdown("#### Seu guia para descobrir o restaurante perfeito 🍔✨")

    # ------------------------------
    # CARDS SUPERIORES (MÉTRICAS)
    # ------------------------------
    col1, col2, col3, col4, col5 = st.columns(5)

    col1.metric("Restaurantes", df_filtered["restaurant_id"].nunique())
    col2.metric("Países", df_filtered["country"].nunique())
    col3.metric("Cidades", df_filtered["city"].nunique())
    col4.metric("Avaliações (votos)", int(df_filtered["votes"].sum()))
    col5.metric("Tipos de culinária", df_filtered["cuisines"].nunique())

    st.markdown("---")

    # ------------------------------
    # MAPA
    # ------------------------------
    st.subheader("Localização dos restaurantes (filtro aplicado)")
    try:
        st.map(df_filtered.rename(columns={"latitude": "lat", "longitude": "lon"}))
    except:
        st.info("Este dataset não possui coordenadas suficientes para o mapa.")

    st.markdown("---")

    # ------------------------------
    # TABELA (preview)
    # ------------------------------
    st.subheader("Primeiras entradas da base filtrada")
    st.dataframe(df_filtered.head(50))

# ================================================================
#                      VISÃO PAÍSES
# ================================================================
elif page == "Visão Países":

    st.title("🌎 Visão por Países")

    # --- Gráfico 1 ---
    st.subheader("Quantidade de restaurantes por país")
    fig1 = px.bar(
        df_filtered.groupby("country")["restaurant_id"].nunique().reset_index(),
        x="country",
        y="restaurant_id",
        labels={"restaurant_id": "Restaurantes"}
    )
    st.plotly_chart(fig1, use_container_width=True)

    # --- Gráfico 2 ---
    st.subheader("Quantidade de cidades por país")
    fig2 = px.bar(
        df_filtered.groupby("country")["city"].nunique().reset_index(),
        x="country",
        y="city",
        labels={"city": "Cidades"}
    )
    st.plotly_chart(fig2, use_container_width=True)

    # --- Gráfico 3 ---
    st.subheader("Média de avaliações por país")
    fig3 = px.bar(
        df_filtered.groupby("country")["votes"].mean().reset_index(),
        x="country",
        y="votes",
        labels={"votes": "Média de votos"}
    )
    st.plotly_chart(fig3, use_container_width=True)

    # --- Gráfico 4 ---
    st.subheader("Custo médio para duas pessoas por país")
    fig4 = px.bar(
        df_filtered.groupby("country")["average_cost_for_two"].mean().reset_index(),
        x="country",
        y="average_cost_for_two",
        labels={"average_cost_for_two": "Custo médio"}
    )
    st.plotly_chart(fig4, use_container_width=True)

# ================================================================
#                      VISÃO CIDADES
# ================================================================
elif page == "Visão Cidades":

    st.title("🏙 Visão por Cidades")

    # Top 10 cidades com mais restaurantes
    st.subheader("Top 10 cidades com mais restaurantes")
    top_cities = (
        df_filtered.groupby("city")["restaurant_id"]
        .nunique()
        .sort_values(ascending=False)
        .head(10)
    )
    fig = px.bar(
        top_cities.reset_index(),
        x="city",
        y="restaurant_id",
        labels={"restaurant_id": "Restaurantes"}
    )
    st.plotly_chart(fig, use_container_width=True)

    # Restaurantes com nota alta
    st.subheader("Top 7 restaurantes com nota acima de 4")
    high_rated = df_filtered[df_filtered["aggregate_rating"] >= 4].sort_values(
        "aggregate_rating", ascending=False
    ).head(7)
    st.table(
        high_rated[["restaurant_name", "city", "country", "aggregate_rating", "votes"]]
    )

    # Restaurantes com nota baixa
    st.subheader("Top 7 restaurantes com nota abaixo de 2.5")
    low_rated = df_filtered[df_filtered["aggregate_rating"] < 2.5].sort_values(
        "aggregate_rating"
    ).head(7)
    st.table(
        low_rated[["restaurant_name", "city", "country", "aggregate_rating", "votes"]]
    )

    # Cidades com mais culinárias
    st.subheader("Top 10 cidades com mais tipos de culinária")
    df_exp = (
        df_filtered.assign(cuisines=df_filtered["cuisines"].str.split(","))
        .explode("cuisines")
    )
    df_exp["cuisines"] = df_exp["cuisines"].str.strip()

    top_cul = (
        df_exp.groupby("city")["cuisines"]
        .nunique()
        .sort_values(ascending=False)
        .head(10)
        .reset_index()
    )
    fig_c = px.bar(
        top_cul,
        x="city",
        y="cuisines",
        labels={"cuisines": "Tipos de culinária"}
    )
    st.plotly_chart(fig_c, use_container_width=True)

# ================================================================
#                      VISÃO TIPOS DE COZINHAS
# ================================================================
elif page == "Visão Tipos de Cozinhas":

    st.title("🍽️ Visão por Tipos de Cozinhas")

    # Expansão da coluna cuisines
    df_c = df_filtered.assign(cuisine=df_filtered["cuisines"].str.split(",")).explode("cuisine")
    df_c["cuisine"] = df_c["cuisine"].str.strip()

    st.subheader("Top 10 melhores tipos de culinária (por avaliação)")
    best = (
        df_c.groupby("cuisine")["aggregate_rating"]
        .mean()
        .sort_values(ascending=False)
        .head(10)
        .reset_index()
    )
    fig_b = px.bar(best, x="cuisine", y="aggregate_rating")
    st.plotly_chart(fig_b, use_container_width=True)

    st.subheader("Top 10 piores tipos de culinária (por avaliação)")
    worst = (
        df_c.groupby("cuisine")["aggregate_rating"]
        .mean()
        .sort_values()
        .head(10)
        .reset_index()
    )
    fig_w = px.bar(worst, x="cuisine", y="aggregate_rating")
    st.plotly_chart(fig_w, use_container_width=True)

    st.subheader("Top 10 tipos mais caros (custo médio para 2)")
    cost = (
        df_c.groupby("cuisine")["average_cost_for_two"]
        .mean()
        .sort_values(ascending=False)
        .head(10)
        .reset_index()
    )
    fig_cost = px.bar(cost, x="cuisine", y="average_cost_for_two")
    st.plotly_chart(fig_cost, use_container_width=True)
