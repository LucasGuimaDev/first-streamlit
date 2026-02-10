import streamlit as st
import pandas as pd

st.set_page_config(page_title="Validação e Correção de Dados", layout="wide")

st.title("🧹 Validação e Correção de Base de Dados")

# =========================
# 1. BASE DE DADOS INICIAL
# =========================
if "df" not in st.session_state:
    st.session_state.df = pd.DataFrame({
        "id": [1, 2, 3, 4],
        "valor": [100, -50, 200, -10],
        "status": ["", "", "", ""]
    })

df = st.session_state.df

# =========================
# 2. VALIDAÇÃO DOS DADOS
# =========================
df["status"] = df["valor"].apply(
    lambda x: "ERRO" if x < 0 else "OK"
)

st.subheader("📊 Base de dados atual")
st.dataframe(df, use_container_width=True)

# =========================
# 3. FILTRO DE ERROS
# =========================
erros = df[df["status"] == "ERRO"]

st.subheader("⚠️ Registros com erro")

if erros.empty:
    st.success("Nenhum erro encontrado 🎉")
else:
    st.dataframe(erros, use_container_width=True)

    # =========================
    # 4. SELETOR DE REGISTRO
    # =========================
    registro_selecionado = st.selectbox(
        "Selecione o ID para correção",
        erros["id"].tolist()
    )

    # =========================
    # 5. AÇÃO (EXECUTA CÓDIGO)
    # =========================
    if st.button("🔄 Corrigir registro selecionado"):
        st.session_state.df.loc[
            st.session_state.df["id"] == registro_selecionado, "valor"
        ] = 0

        st.success(f"Registro {registro_selecionado} corrigido com sucesso!")

        # Força atualização visual
        st.rerun()

# =========================
# 6. LOG (OPCIONAL)
# =========================
st.divider()
st.caption("Exemplo de app Streamlit reativo para validação e correção de dados")
