
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carregar os dados
file_path = 'data/Análise de Desempenho Financeiro Empório do Mármore 2025.xlsx'
balanco_patimonial = pd.read_excel(file_path, sheet_name='Balanço Patrimonial')
dre = pd.read_excel(file_path, sheet_name='DRE')
indicadores_faturamento = pd.read_excel(file_path, sheet_name='Indicadores de Faturamento')

# Título do Dashboard
st.title("Análise de Desempenho Financeiro - Empório do Mármore")

# Descrição do dashboard
st.write(""" 
Este dashboard oferece uma visão detalhada dos indicadores financeiros e contábeis da Empório do Mármore. 
Utilize as opções abaixo para explorar as diferentes análises financeiras, como Balanço Patrimonial, DRE, 
indicadores de faturamento, e muito mais.
""")

# Seleção de indicador
indicador = st.selectbox(
    "Escolha o indicador financeiro:",
    ("Ativo Circulante", "Passivo Circulante", "Receitas", "Lucro Líquido", "Indicadores de Liquidez", "Projeções")
)

# Gráfico do Ativo Circulante (exemplo)
if indicador == "Ativo Circulante":
    # Extraindo dados do Ativo Circulante
    ativo_circulante = balanco_patimonial.iloc[1, 1:8].values
    anos = balanco_patimonial.columns[1:8]

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.bar(anos, ativo_circulante, color='skyblue')
    ax.set_title("Evolução do Ativo Circulante (2019-2025)", fontsize=14)
    ax.set_xlabel('Ano', fontsize=12)
    ax.set_ylabel('Valor (R$)', fontsize=12)
    st.pyplot(fig)

# Gráfico do Passivo Circulante (exemplo)
elif indicador == "Passivo Circulante":
    # Extraindo dados do Passivo Circulante
    passivo_circulante = balanco_patimonial.iloc[2, 1:8].values
    anos = balanco_patimonial.columns[1:8]

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.bar(anos, passivo_circulante, color='lightcoral')
    ax.set_title("Evolução do Passivo Circulante (2019-2025)", fontsize=14)
    ax.set_xlabel('Ano', fontsize=12)
    ax.set_ylabel('Valor (R$)', fontsize=12)
    st.pyplot(fig)

# Gráfico de Receita Líquida (exemplo)
elif indicador == "Receitas":
    receita_liquida = indicadores_faturamento.iloc[1, 1:8].values
    anos = indicadores_faturamento.columns[1:8]

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(anos, receita_liquida, marker='o', color='green', label="Receita Líquida")
    ax.set_title("Evolução da Receita Líquida (2019-2025)", fontsize=14)
    ax.set_xlabel('Ano', fontsize=12)
    ax.set_ylabel('Valor (R$)', fontsize=12)
    st.pyplot(fig)

# Seção de Indicadores de Rentabilidade
elif indicador == "Lucro Líquido":
    lucro_liquido = dre.iloc[3, 1:8].values
    anos = dre.columns[1:8]

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(anos, lucro_liquido, marker='o', color='orange', label="Lucro Líquido")
    ax.set_title("Evolução do Lucro Líquido (2019-2025)", fontsize=14)
    ax.set_xlabel('Ano', fontsize=12)
    ax.set_ylabel('Valor (R$)', fontsize=12)
    st.pyplot(fig)

# Gráficos adicionais ou widgets podem ser adicionados aqui conforme necessidade

# Fim do dashboard
st.write("Obrigado por usar o dashboard!")
