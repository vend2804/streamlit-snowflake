import streamlit as st

st.title("Session State Example")

if "count" not in st.session_state:
    st.session_state["count"] = 0

st.write(st.session_state)

st.write(f"Current count: {st.session_state['count']}")

if st.button("Button", key="my-button"):
    st.session_state["count"] += 1
    st.write("you Clicked the button")

if st.toggle("Toggle", key="my-toggle"):
    st.write("you toggled")

st.write(st.session_state)
