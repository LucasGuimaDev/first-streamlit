import streamlit as st

st.set_page_config(page_title="aula teste", layout="wide")
st.title("Armac")
st.write("Olá, armac")
st.header("Cabeçalho")
st.subheader("Subtítulo")
st.text("Texto simples")
st.markdown("**Markdown** _funciona_")
st.write("coringa", 123)
nome = st.text_input("Digite seu nome")
st.write("Olá,", nome)