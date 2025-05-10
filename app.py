import streamlit as st
import pandas as pd

# CONFIG
st.set_page_config(page_title="The Daily Report", layout="wide")
st.title("📰 The Daily Report")
st.markdown("A curated feed of stories worth your time.")

# Load CSV from Google Sheets
csv_url = "https://docs.google.com/spreadsheets/d/YOUR_SHEET_ID/export?format=csv"

try:
    df = pd.read_csv(csv_url)
    for _, row in df.iterrows():
        st.image(row["image"], use_container_width=True)
        st.markdown(f"### [{row['title']}]({row['url']})")
        st.write(row["summary"])
        st.markdown("---")
except Exception as e:
    st.error("⚠️ Couldn't load the news feed. Please check your Google Sheet link.")
    st.write(e)
