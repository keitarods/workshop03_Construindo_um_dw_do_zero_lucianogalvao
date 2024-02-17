import streamlit as st
from drive.client import DriveClient
from datasource.csv import CSVCollector
from contract.catalogo import Catalogo
import os

st.title("Portal de dados!!")

st.file_uploader("Upload a file", type = "xlsx")

drive = DriveClient()
catalogo_de_produtos = CSVCollector(Catalogo, drive, "C11: I211")


if __name__ == "__main__":
    print(os.getcwd())