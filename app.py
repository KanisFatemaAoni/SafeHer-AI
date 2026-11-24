import streamlit as st

# Page configuration
st.set_page_config(
    page_title="SafeHer AI",
    page_icon="💙",
    layout="wide"
)

# Session state
if "alerts" not in st.session_state:
    st.session_state.alerts = 0

if "contacts" not in st.session_state:
    st.session_state.contacts = []

if "journey" not in st.session_state:
    st.session_state.journey = False

# Header
st.title("💙 SafeHer AI")
st.subheader("Intelligent Personal Safety & Emergency Assistance")

st.write("Your Safety. Your Voice. Your Power.")

st.divider()

# Dashboard metrics
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Trusted Contacts", len(st.session_state.contacts))

with col2:
    st.metric("Emergency Alerts", st.session_state.alerts)

with col3:
    status = "Active" if st.session_state.journey else "Inactive"
    st.metric("Journey Status", status)

st.divider()

# Emergency SOS
st.header("🆘 Emergency SOS")

if st.button("ACTIVATE SOS", type="primary"):
    st.session_state.alerts += 1
    st.warning("Demo alert activated! No real emergency message was sent.")

st.divider()

# Trusted Contacts
st.header("👥 Trusted Contacts")

with st.form("contact_form"):
    name = st.text_input("Contact Name")
    phone = st.text_input("Phone Number")

    submitted = st.form_submit_button("Add Contact")

    if submitted:
        if name.strip() and phone.strip():
            st.session_state.contacts.append({
                "Name": name.strip(),
                "Phone": phone.strip()
            })
            st.success("Contact added successfully!")
        else:
            st.error("Please enter both fields.")

if st.session_state.contacts:
    st.table(st.session_state.contacts)

st.divider()

# Safety Journey
st.header("⏱️ Safety Journey")

if not st.session_state.journey:
    if st.button("Start Journey"):
        st.session_state.journey = True
        st.rerun()
else:
    if st.button("End Journey"):
        st.session_state.journey = False
        st.rerun()

st.write(
    "Your journey is currently being demonstrated "
    "within this application."
)

st.divider()

# AI Assistant
st.header("🤖 AI Safety Assistant")

question = st.text_input("What safety guidance do you need?")

if st.button("Get Guidance"):
    if question.strip():
        st.info(
            "This is an AI assistant demo. "
            "AI-powered responses will be implemented in a later stage."
        )
    else:
        st.warning("Please enter a question.")

st.divider()

st.caption("SafeHer AI | Version 2.0 | Built with Python")