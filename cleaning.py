# cleaning.py

import pandas as pd

df = pd.read_csv("dataset/zomato.csv")

print(df.head())


import pandas as pd
import inflection

# ====================================================
# 1. Funções fornecidas pelo Cientista de Dados pleno
# ====================================================

COUNTRIES = {
    1: "India",
    14: "Australia",
    30: "Brazil",
    37: "Canada",
    94: "Indonesia",
    148: "New Zeland",
    162: "Philippines",
    166: "Qatar",
    184: "Singapure",
    189: "South Africa",
    191: "Sri Lanka",
    208: "Turkey",
    214: "United Arab Emirates",
    215: "England",
    216: "United States of America",
}

def country_name(country_id):
    return COUNTRIES.get(country_id, "Unknown")

def create_price_type(price_range):
    if price_range == 1:
        return "cheap"
    elif price_range == 2:
        return "normal"
    elif price_range == 3:
        return "expensive"
    else:
        return "gourmet"

COLORS = {
    "3F7E00": "darkgreen",
    "5BA829": "green",
    "9ACD32": "lightgreen",
    "CDD614": "orange",
    "FFBA00": "red",
    "CBCBC8": "darkred",
    "FF7800": "darkred",
}

def color_name(color_code):
    return COLORS.get(color_code, "unknown")

def rename_columns(dataframe):
    df = dataframe.copy()
    title = lambda x: inflection.titleize(x)
    snakecase = lambda x: inflection.underscore(x)
    spaces = lambda x: x.replace(" ", "")
    cols_old = list(df.columns)
    cols_old = list(map(title, cols_old))
    cols_old = list(map(spaces, cols_old))
    cols_new = list(map(snakecase, cols_old))
    df.columns = cols_new
    return df

# ===============================================
# 2. Função principal de limpeza do DataFrame
# ===============================================

def clean_data(path_to_csv: str):
    """
    Carrega, limpa e prepara o DataFrame para análise.
    """

    # ---- Carregar dados ----
    df = pd.read_csv(path_to_csv)

    # ---- Remover duplicados ----
    df = df.drop_duplicates()

    # ---- Remover valores nulos ----
    df = df.dropna()

    # ---- Renomear colunas ----
    df = rename_columns(df)

    # ---- Categorizar a culinária (usar somente o 1° tipo) ----
    df["cuisines"] = df["cuisines"].apply(lambda x: x.split(",")[0])

    # ---- Adicionar nome do país ----
    df["country"] = df["country_code"].apply(country_name)

    # ---- Criar categoria de preço ----
    df["price_type"] = df["price_range"].apply(create_price_type)

    # ---- Traduzir código de cor para nome ----
    df["rating_color_name"] = df["rating_color"].apply(color_name)

    return df


# ====================================================
# Execução de teste
# ====================================================

if __name__ == "__main__":
    df = clean_data("dataset/zomato.csv")
    print(df.head())
