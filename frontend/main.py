import streamlit as st
from drive.client import DriveClient
from datasource.csv import CSVCollector
from contract.catalogo import Catalogo
import os

st.title("Portal de dados!!")
drive = DriveClient()

catalogo_de_produtos = CSVCollector(Catalogo, drive, "C11:I211").start()



