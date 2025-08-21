import streamlit as st
from pathlib import Path

st.set_page_config(page_title="Login - Grupo Maroni", layout="wide")

# Lê os arquivos
BASE = Path(__file__).resolve().parent
html_file = BASE / "LoginMCD.html"
css_file = BASE / "LoginMCD.css"

html_code = html_file.read_text(encoding="utf-8")
css_code = css_file.read_text(encoding="utf-8")

# Injeta CSS no HTML
final_html = f"""
<style>
{css_code}
</style>
{html_code}
"""

# Exibe no Streamlit
st.components.v1.html(final_html, height=800, scrolling=True)