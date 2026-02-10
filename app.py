import streamlit as st
import pandas as pd

st.set_page_config(page_title="aula teste", layout="wide")

st.title("Home")
st.write("Olá, seja bem vindo, acesse as páginas ao lado para ver os dados!")

# 🔹 Dados
@st.cache_data
def carregar_dados():
    return pd.read_excel(
        r"C:\Users\lucas.barroso\OneDrive - Armac Locação\Área de Trabalho\Doc's guardar\python\projeto\data\dados.xlsx",
        engine="openpyxl"
    )

if "df" not in st.session_state:
    st.session_state.df = carregar_dados()
