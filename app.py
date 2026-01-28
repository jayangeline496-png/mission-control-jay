import streamlit as st
import pandas as pd
import requests

st.set_page_config(page_title="Mission Control", page_icon="🦞", layout="wide")

st.title("🚀 Mission Control: Jay Angeline Pipeline")

# Logic to fetch data from the tracker sheet (mocked for the POC)
def get_tracker_data():
    # In the real version, this calls the Sheets API using our verified ADC
    return pd.DataFrame([
        {"Task": "Magic Shapes Language Rewrite", "Status": "In Progress", "IP": "Cosmere"},
        {"Task": "Poppins Hub Refactor", "Status": "Backlog", "IP": "Mary Poppins"},
        {"Task": "Voice Interview (David)", "Status": "To Do", "IP": "System"},
        {"Task": "Expanse Faction Split", "Status": "Backlog", "IP": "The Expanse"},
    ])

df = get_tracker_data()

col1, col2, col3 = st.columns(3)

with col1:
    st.header("📋 To Do")
    for _, row in df[df['Status'] == 'To Do'].iterrows():
        st.info(f"**{row['Task']}**\n\n({row['IP']})")

with col2:
    st.header("⏳ In Progress")
    for _, row in df[df['Status'] == 'In Progress'].iterrows():
        st.warning(f"**{row['Task']}**\n\n({row['IP']})")

with col3:
    st.header("✅ Backlog / Finished")
    for _, row in df[df['Status'] == 'Backlog'].iterrows():
        st.success(f"**{row['Task']}**\n\n({row['IP']})")

st.sidebar.markdown("### Strategic Briefing")
st.sidebar.button("Generate New Briefing")
st.sidebar.markdown("---")
st.sidebar.markdown("### Jay Status: **Operational**")
