import streamlit as st
from pathlib import Path

# Design
st.set_page_config(page_title="MyPortfolio",
                   page_icon="bar_chart:",
                   layout="wide")

# Hide hamburger menu
hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden;}
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)

# Print .md file
result=st.experimental_get_query_params() #Get params of url

filename=result['file'][0]

md=Path(filename).read_text()
st.markdown(md, unsafe_allow_html=True)
