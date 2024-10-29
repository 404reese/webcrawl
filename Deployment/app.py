import pickle
from PIL import Image
import streamlit as st

# Importing the smaller apps
from ml_app import run_ml_app
from eda_app import run_eda_app

def main():
    st.title("Super legal NEVIL system")

    # Data Analysis section
    st.subheader("Data Analysis")
    run_eda_app()

    # Prediction section
    st.subheader("Prediction")
    run_ml_app()

    # Map section (or other relevant data)
    st.subheader("Data points which are working on the project:")
    path_to_html = "IMG/mumbai_property.html"
    with open(path_to_html, 'r') as f:
        html_data = f.read()
    st.components.v1.html(html_data, height=500)

if __name__ == "__main__":
    main()
