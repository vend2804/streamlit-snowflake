import webbrowser
import urllib.parse
import pandas as pd
import streamlit as st

st.title("Hierachical Date Visualization")


df = pd.read_csv("data/employees.csv", header=0).convert_dtypes()

st.dataframe(df)

edges = ""

for _, row in df.iterrows():
    if not pd.isna(row.iloc[2]):
        edges += f'\t"{row.iloc[0]}" -> "{row.iloc[2]}";\n'

d = f'digraph G {{\n{edges}\n}}'

st.graphviz_chart(d)


#print(d)
