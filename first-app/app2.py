import streamlit as st
import pandas as pd

st.title("Hierachical Date Visualization")

# write a header 
st.header("this is a heder")

# write a subheader 
st.subheader("this is a subheader")

# write a caption 
st.caption("this is a caption")

# write 
st.write("this is some text")

# write a text 
st.text("this is some text")

# write a markdown 
st.markdown("this is some markdown **bold**")
# write code 
st.code("this is some code")

# write a code block 
st.code("v= variable()\nanother_call()", language='python')

# write  a divider 
st.divider()

# write a latex formula
st.latex(r'''
a^2 + b^2 = c^2
''')

# write error 
st.error("this is an error")

# write warning 
st.warning("this is a warning")

# write info 
st.info("this is an info")

# write success 
st.success("this is a success")

#write balloons 
st.balloons()

# write Snow 
st.snow()

#write linkbutton   
st.link_button("Go to Google", "https://www.google.com")

#write checkbox 
checkbox_value = st.checkbox("Check me")
st.write(f"Checkbox value: {checkbox_value}")

#write radio button
radio_value = st.radio("Choose one:", ["Option A", "Option B", "Option C"])
st.write(f"Radio value: {radio_value}")

#write selectbox
selectbox_value = st.selectbox("Select one:", ["Option A", "Option B", "Option C"])
st.write(f"Selectbox value: {selectbox_value}")

#write multiselect
multiselect_value = st.multiselect("Select multiple:", ["Option A", "Option B", "Option C"])
st.write(f"Multiselect value: {multiselect_value}")

#write slider
slider_value = st.slider("Slide me:", 0, 100, 50)
st.write(f"Slider value: {slider_value}")

#write number input
number_input_value = st.number_input("Enter a number:", value=0)
st.write(f"Number input value: {number_input_value}")

#write text input
text_input_value = st.text_input("Enter some text:")
st.write(f"Text input value: {text_input_value}")

#write text area
text_area_value = st.text_area("Enter some text:")
st.write(f"Text area value: {text_area_value}")

#write date input
date_input_value = st.date_input("Enter a date:")
st.write(f"Date input value: {date_input_value}")

#write time input
time_input_value = st.time_input("Enter a time:")
st.write(f"Time input value: {time_input_value}")

#write color picker
color_picker_value = st.color_picker("Pick a color:")
st.write(f"Color picker value: {color_picker_value}")

#write file uploader
file_uploader_value = st.file_uploader("Upload a file:")
st.write(f"File uploader value: {file_uploader_value}")

#write camera input
camera_input_value = st.camera_input
st.button("Click me")

# write table 
data = {'col1': [1, 2, 3], 'col2': [4, 5, 6], 'col3': [7, 8, 9]}
df = pd.DataFrame(data)
st.table(df)

# generate graphviz chart 
edges = ""

for _, row in df.iterrows():
    if not pd.isna(row.iloc[1]):
        edges += f'\t"{row.iloc[0]}" -> "{row.iloc[1]}";\n'

d = f'digraph G {{\n{edges}\n}}'

st.graphviz_chart(d)

# GEnerate interactive map 
st.map(df)

# Generate altair chart 
import altair as alt


# Create a sample DataFrame
data = {'x': [1, 2, 3, 4, 5], 'y': [10, 20, 15, 25, 30]}
df = pd.DataFrame(data)

# Create an Altair chart
chart = alt.Chart(df).mark_line().encode(
    x='x',
    y='y'
)

# Display the chart in Streamlit
st.altair_chart(chart, use_container_width=True)

# Generate Ploty chart 
import plotly.graph_objects as go

fig = go.Figure(data=[go.Bar(y=[2, 1, 3])])
st.plotly_chart(fig, use_container_width=True)







