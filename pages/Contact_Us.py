import streamlit as st
from send_email import send_email

st.header("Contact Me")

with st.form(key="contact_form"):
    user_email = st.text_input("Your email address")
    topic = st.selectbox("What topic would you like to discuss ?", ("Job Inquiries", "Project Proposals", "Other"))
    raw_message = st.text_area("Your message")
    message = f"""\
Subject: New message from your Portfolio App

From: {user_email}
Topic: {topic}
{raw_message}
"""
    submit_button = st.form_submit_button("Submit")
    if submit_button:
        send_email(message)
        st.info("Your email has been sent")
