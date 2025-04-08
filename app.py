import streamlit as st
from datetime import date

# 🛠️ Configuração da página
st.set_page_config(page_title="Registro de Ações - PESA", layout="centered")

# 🖼️ Logo da empresa
st.image("logo_pesa.jpeg", use_container_width=False, width=200)

# 🔵 Título em branco
st.markdown(
    "<h2 style='color:#FFFFFF;'>📋 Registro de Ações de Sustentabilidade e Inclusão</h2>",
    unsafe_allow_html=True
)

# 📄 Formulário
with st.form("registro_form"):
    nome_acao = st.text_input("Nome da ação")
    descricao = st.text_area("Descrição da ação")

    categorias = st.multiselect(
        "Categoria",
        sorted([
            "Acessibilidade",
            "Ações sociais",
            "Diversidade e equidade",
            "Governança/ética",
            "Inclusão social",
            "Sustentabilidade ambiental"
        ])
    )

    data_acao = st.date_input("Data da ação", value=date.today())
    resultados = st.text_area("Resultados ou impacto")

    enviar = st.form_submit_button("Enviar")

# ✅ Exibe dados após envio
if enviar:
    st.success("✅ Ação registrada com sucesso!")
    st.write("**Nome da ação:**", nome_acao)
    st.write("**Descrição:**", descricao)
    st.write("**Categoria:**", ", ".join(categorias))
    st.write("**Data da ação:**", data_acao.strftime('%d/%m/%Y'))
    st.write("**Resultados/Impacto:**", resultados)
