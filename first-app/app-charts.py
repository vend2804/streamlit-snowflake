import streamlit as st
import pandas as pd
import plotly.graph_objects as go



st.title("Hiearchical Data Chars")

df = pd.read_csv("data/employees.csv", header=0).convert_dtypes()

st.dataframe(df)

labels = df[df.columns[0]]
parents = df[df.columns[1]]
children = df[df.columns[2]]

# Write a Treemap from plotly 
fig = go.Figure(go.Treemap(
    ids=labels,
    labels = labels,
    parents = parents,
    root_color = "lightgrey",
    branchvalues = "total"
    ))
st.plotly_chart(fig, use_container_width=True)

#  Generate an Icicle Chart from Plotly 
fig = go.Figure(go.Icicle(
    ids=labels,
    labels = labels,
    parents = parents,
    root_color = "lightgrey",
    branchvalues = "total"
    ))
st.plotly_chart(fig, use_container_width=True)


# generate a subburst chart from plotly 
fig = go.Figure(go.Sunburst(
    ids=labels,
    labels = labels,
    parents = parents,
    root_color = "lightgrey",
    branchvalues = "total"
    ))
st.plotly_chart(fig, use_container_width=True)

# Generate a Sankey chart from plotly 
data = go.Sankey(
    node=dict(label=labels),
    link=dict(
        source=[list(labels).index(x) for x in labels],
        target=[-1 if pd.isna(x) else list(labels).index(x) for x in parents],
        label=labels,
        value=list(range(1, len(labels)))))
fig = go.Figure(data)
st.plotly_chart(fig, use_container_width=True)
# fig = go.Figure(go.Sankey(
#     node = dict(
#       pad = 15,
#       thickness = 20,
#       line = dict(color = "black", width = 0.5),
#       label = labels,
#       color = "blue"
#     ),
#     link = dict(
#       source = [list(labels).index(i) for i in labels],
#       target = [-1 if pd.isna(i) else list(labels).index(i) for i in labels],
#       #labels = labels,
#       value = list(range(1,len(labels)+1))#[1]*len(labels)
#     )))
# st.plotly_chart(fig, use_container_width=True)



