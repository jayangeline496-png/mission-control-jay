import streamlit as st
import pandas as pd
import json
import os

st.set_page_config(page_title="Mission Control", page_icon="🦞", layout="wide")

st.title("🚀 Mission Control: Jay Angeline Pipeline")

# Communication Hub logic
def load_comms():
    if os.path.exists("comms.json"):
        with open("comms.json", "r") as f:
            return json.load(f)
    return []

def save_comms(comms):
    with open("comms.json", "w") as f:
        json.dump(comms, f)

st.sidebar.title("💬 Jay's Comms")
chat_history = load_comms()

for msg in chat_history[-5:]:
    st.sidebar.write(f"**{msg['sender']}**: {msg['text']}")

user_input = st.sidebar.text_input("Send message to Jay:", key="user_msg")
if st.sidebar.button("Send"):
    if user_input:
        chat_history.append({"sender": "David", "text": user_input})
        save_comms(chat_history)
        st.sidebar.success("Message sent!")
        # In real usage, the AI agent would monitor this file

st.sidebar.markdown("---")
st.sidebar.markdown("### Strategic Briefing")
if st.sidebar.button("Generate New Briefing"):
    st.sidebar.info("Triggering briefing run...")

st.sidebar.markdown("---")
st.sidebar.markdown("### System Status: **Operational**")

# Mock Kanban Data
def get_tracker_data():
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
