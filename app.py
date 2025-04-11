import streamlit as st
from datetime import date
import pandas as pd
import os

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
    if not nome_acao or not descricao or not categorias or not resultados:
        st.error("❌ Por favor, preencha todos os campos obrigatórios.")
    else:
        st.success("✅ Ação registrada com sucesso!")
        st.write("**Nome da ação:**", nome_acao)
        st.write("**Descrição:**", descricao)
        st.write("**Categoria:**", ", ".join(categorias))
        st.write("**Data da ação:**", data_acao.strftime('%d/%m/%Y'))
        st.write("**Resultados/Impacto:**", resultados)

        # 🔄 Salvando em Excel
        arquivo_excel = "registros_acoes.xlsx"
        novo_registro = {
            "Nome da ação": nome_acao,
            "Descrição": descricao,
            "Categoria": ", ".join(categorias),
            "Data da ação": data_acao.strftime('%d/%m/%Y'),
            "Resultados/Impacto": resultados
        }

        if os.path.exists(arquivo_excel):
            df_existente = pd.read_excel(arquivo_excel)
            df_novo = pd.concat([df_existente, pd.DataFrame([novo_registro])], ignore_index=True)
        else:
            df_novo = pd.DataFrame([novo_registro])

        df_novo.to_excel(arquivo_excel, index=False)
        st.info("📁 Registro salvo em *registros_acoes.xlsx*")
