import streamlit as st
from main import llm_helper

st.header("AI WebSite summariser :brain:", divider="rainbow")

website_url = st.text_input("Enter your website url to summarise")

if st.button("Summarize :sparkles:"):
    st.write(llm_helper(website_url))


st.write(
    ":warning:  All website entered here are being scrapped by selenium before the AI model summarises it."
)

