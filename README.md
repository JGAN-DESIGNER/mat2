# Escola MatFuturo — Equação do 2º Grau (App)

App em Streamlit que resolve equações do 2º grau (`ax² + bx + c = 0`),
seguindo a identidade visual da escola **MatFuturo** (cores verdes).

## Arquivos

- `equa2.py` — código principal do app (Streamlit)
- `gabriel.jpg` — imagem exibida no topo do app
- `requirements.txt` — dependências do projeto

## O que o app faz

1. Recebe os coeficientes **a**, **b** e **c**.
2. Calcula o discriminante (Δ = b² − 4ac).
3. Mostra a equação formatada e o passo a passo da resolução.
4. Informa se a equação tem:
   - duas raízes reais (Δ > 0)
   - uma raiz real (Δ = 0)
   - nenhuma raiz real (Δ < 0)
5. Exibe o gráfico da parábola, com o vértice e as raízes destacadas.

## Como executar

1. Instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```

2. Execute o app:

   ```bash
   streamlit run equa2.py
   ```

3. O navegador abrirá automaticamente em `http://localhost:8501`.

## Personalização

As cores da escola estão definidas no início do arquivo `equa2.py`:

```python
VERDE_ESCURO = "#1B5E20"
VERDE_MEDIO  = "#2E7D32"
VERDE_CLARO  = "#66BB6A"
VERDE_FUNDO  = "#E8F5E9"
```

Basta trocar os valores hexadecimais para ajustar a identidade visual.
