import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

# ============================================
# CONFIGURAÇÃO DA PÁGINA
# ============================================
st.set_page_config(
    page_title="MatFuturo - Equação do 2º Grau",
    page_icon="📐",
    layout="centered"
)

# ============================================
# CORES DA ESCOLA (AZUL ESCURO) - MATFUTURO
# ============================================
VERDE_ESCURO = "#0D1B3E"   # azul quase marinho (fundo)
VERDE_MEDIO = "#1E3A8A"    # azul médio (botões, destaques)
VERDE_CLARO = "#60A5FA"    # azul claro (detalhes/raízes no gráfico)
VERDE_FUNDO = "#0A1128"    # fundo geral do app (azul bem escuro)
TEXTO_CLARO = "#F1F5F9"    # texto claro para contraste no fundo escuro

# ============================================
# ESTILO PERSONALIZADO (TEMA AZUL ESCURO DA ESCOLA)
# ============================================
st.markdown(
    f"""
    <style>
    .stApp {{
        background-color: {VERDE_FUNDO};
        color: {TEXTO_CLARO};
    }}
    h1, h2, h3 {{
        color: {TEXTO_CLARO} !important;
    }}
    p, label, span, .stMarkdown, .stAlert, div[data-testid="stMetricValue"] {{
        color: {TEXTO_CLARO} !important;
    }}
    div[data-testid="stNumberInput"] input {{
        color: {VERDE_ESCURO};
        background-color: {TEXTO_CLARO};
    }}
    div.stButton > button {{
        background-color: {VERDE_MEDIO};
        color: {TEXTO_CLARO};
        font-weight: bold;
        border-radius: 8px;
        border: 2px solid {VERDE_CLARO};
    }}
    div.stButton > button:hover {{
        background-color: {VERDE_CLARO};
        color: {VERDE_ESCURO};
        border: 2px solid {VERDE_CLARO};
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# ============================================
# CAMINHO DA PASTA DO PROGRAMA
# ============================================
PASTA_APP = Path(__file__).parent

# ============================================
# CAMINHO DA LOGOMARCA
# ============================================
CAMINHO_LOGO = PASTA_APP / "gabriel.jpg"

# ============================================
# LOGOMARCA
# ============================================
if CAMINHO_LOGO.exists():
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.image(
            str(CAMINHO_LOGO),
            use_container_width=True
        )
else:
    st.warning("⚠️ A imagem gabriel.jpg não foi encontrada.")

# ============================================
# CABEÇALHO DA ESCOLA
# ============================================
st.markdown(
    f"<h3 style='text-align:center; color:{VERDE_CLARO};'>Escola MatFuturo</h3>",
    unsafe_allow_html=True
)

# ============================================
# TÍTULO
# ============================================
st.title("📐 Equação do 2º Grau")
st.write("Equação no formato:")
st.latex(r"ax^2 + bx + c = 0")

# ============================================
# ENTRADA DOS VALORES
# ============================================
a = st.number_input(
    "Digite o valor de a",
    value=1,
    step=1
)

b = st.number_input(
    "Digite o valor de b",
    value=0,
    step=1
)

c = st.number_input(
    "Digite o valor de c",
    value=0,
    step=1
)

# ============================================
# BOTÃO CALCULAR
# ============================================
if st.button("Calcular", use_container_width=True):

    # ========================================
    # VERIFICA SE A EQUAÇÃO É REALMENTE DO 2º GRAU
    # ========================================
    if a == 0:
        st.error(
            "O valor de 'a' não pode ser zero em uma equação do 2º grau. "
            "Se a = 0, a equação passa a ser do 1º grau."
        )
    else:
        # ====================================
        # MOSTRA A EQUAÇÃO
        # ====================================
        def monta_equacao(a, b, c):
            termo_b = f"+ {b}x" if b >= 0 else f"- {abs(b)}x"
            termo_c = f"+ {c}" if c >= 0 else f"- {abs(c)}"
            return f"{a}x^2 {termo_b} {termo_c} = 0"

        st.subheader("Equação")
        st.latex(monta_equacao(a, b, c))

        # ====================================
        # CALCULA O DISCRIMINANTE (DELTA)
        # ====================================
        delta = (b ** 2) - (4 * a * c)

        st.subheader("Resolução")
        st.latex(r"\Delta = b^2 - 4ac")
        st.latex(f"\\Delta = ({b})^2 - 4({a})({c})")
        st.latex(f"\\Delta = {delta}")

        # ====================================
        # ANALISA O DISCRIMINANTE
        # ====================================
        st.subheader("✅ Resultado")

        if delta < 0:
            st.error(
                "A equação não possui raízes reais, pois Δ < 0."
            )
            x1 = None
            x2 = None
        elif delta == 0:
            x1 = -b / (2 * a)
            x2 = x1
            st.latex(r"x = \frac{-b}{2a}")
            st.latex(f"x = \\frac{{-({b})}}{{2({a})}}")
            st.success(f"A equação possui uma única raiz real: x = {x1:.2f}")
        else:
            raiz_delta = np.sqrt(delta)
            x1 = (-b + raiz_delta) / (2 * a)
            x2 = (-b - raiz_delta) / (2 * a)
            st.latex(r"x = \frac{-b \pm \sqrt{\Delta}}{2a}")
            st.latex(f"x = \\frac{{-({b}) \\pm \\sqrt{{{delta}}}}}{{2({a})}}")
            st.success(f"A equação possui duas raízes reais: x' = {x1:.2f} e x'' = {x2:.2f}")

        # ====================================
        # GRÁFICO
        # ====================================
        st.subheader("📊 Gráfico da função")

        # Define um intervalo adequado para o gráfico
        if delta >= 0 and x1 is not None:
            centro = (x1 + x2) / 2
            largura = max(abs(x1 - x2), 5) + 5
        else:
            centro = -b / (2 * a)
            largura = 10

        x = np.linspace(centro - largura, centro + largura, 500)
        y = a * (x ** 2) + b * x + c

        fig, ax = plt.subplots(figsize=(8, 5))
        fig.patch.set_facecolor(VERDE_FUNDO)
        ax.set_facecolor(VERDE_FUNDO)

        # Desenha a parábola
        ax.plot(
            x, y,
            linewidth=2,
            color=VERDE_CLARO,
            label=f"y = {a}x² + {b}x + {c}"
        )

        # Eixo X
        ax.axhline(y=0, linewidth=1, color=TEXTO_CLARO)
        # Eixo Y
        ax.axvline(x=0, linewidth=1, color=TEXTO_CLARO)

        # Marca o vértice da parábola
        x_vertice = -b / (2 * a)
        y_vertice = a * (x_vertice ** 2) + b * x_vertice + c
        ax.scatter(
            [x_vertice], [y_vertice],
            s=80, zorder=5, color="#FBBF24",
            label=f"Vértice ({x_vertice:.2f}, {y_vertice:.2f})"
        )

        # Marca as raízes reais, se existirem
        if delta >= 0:
            ax.scatter(
                [x1, x2], [0, 0],
                s=100, zorder=5, color=TEXTO_CLARO,
                edgecolor=VERDE_CLARO,
                label="Raízes"
            )

        ax.set_xlabel("x", color=TEXTO_CLARO)
        ax.set_ylabel("y", color=TEXTO_CLARO)
        ax.set_title("Gráfico da Função do 2º Grau", color=TEXTO_CLARO)
        ax.tick_params(colors=TEXTO_CLARO)
        for spine in ax.spines.values():
            spine.set_color(TEXTO_CLARO)
        ax.grid(True, color=VERDE_MEDIO, alpha=0.4)
        legend = ax.legend(facecolor=VERDE_FUNDO, edgecolor=TEXTO_CLARO)
        for text in legend.get_texts():
            text.set_color(TEXTO_CLARO)

        st.pyplot(fig)
        plt.close(fig)

# ============================================
# RODAPÉ
# ============================================
st.divider()
st.markdown(
    f"<p style='text-align:center; color:{VERDE_CLARO};'>"
    "📚 Escola MatFuturo — Calculadora de Equação do 2º Grau</p>",
    unsafe_allow_html=True
)
