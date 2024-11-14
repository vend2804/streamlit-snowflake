import streamlit as st
import pandas as pd
import plotly.graph_objects as go


# Generate a function makeTreamap pass parameters `labels, parents`
def makeTreemap(labels, parents):
    fig = go.Figure(go.Treemap(
        ids=labels,
        labels=labels,
        parents=parents,
        root_color="lightgrey",
        branchvalues="total"
    ))
    return fig

# Generate a function makeIcicle pass parameters `labels , parents` 
def makeIcicle(labels, parents):
    fig = go.Figure(go.Icicle(
        ids=labels,
        labels=labels,
        parents=parents,
        root_color="lightgrey",
        branchvalues="total"
    ))
    return fig

#Generate a function makeSunburst pass parameters `label, parents`
def makeSunburst(labels, parents):
    fig = go.Figure(go.Sunburst(
        ids=labels,
        labels=labels,
        parents=parents,
        root_color="lightgrey",
        branchvalues="total"
    ))
    return fig

def makeSankey(labels, parents):
    data = go.Sankey(
    node=dict(label=labels),
    link=dict(
        source=[list(labels).index(x) for x in labels],
        target=[-1 if pd.isna(x) else list(labels).index(x) for x in parents],
        label=labels,
        value=list(range(1, len(labels)))))
    fig = go.Figure(data)
    return fig




st.title("Hiearchical Data Chars")

df = pd.read_csv("data/employees.csv", header=0).convert_dtypes()

#st.dataframe(df)

labels, parents = df[df.columns[0]], df[df.columns[1]] 

#Create a tab controler with array kyes of `Treemap, Icicle, Sunburst, Sankey`
tabs = st.tabs(["Treemap", "Icicle", "Sunburst", "Sankey"])


# call the function makeTreemap 
# add and expander to the makeTreeMap function 


with tabs[0]:   #st.expander("Treemap", expanded=True):
    fig = makeTreemap(labels, parents)
    st.plotly_chart(fig, use_container_width=True)

with tabs[1]: #st.expander("Icicle"):
    fig = makeIcicle(labels, parents)
    st.plotly_chart(fig, use_container_width=True)

with tabs[2]:     #st.expander("Sunburst"):
    fig = makeSunburst(labels, parents)
    st.plotly_chart(fig, use_container_width=True)

with tabs[3]:     #st.expander("Sankey"):
    fig = makeSankey(labels, parents)
    st.plotly_chart(fig, use_container_width=True)
