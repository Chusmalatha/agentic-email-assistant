import streamlit as st
from agent import agent 

st.set_page_config(
    page_title="AI Email Agent",
    page_icon="📧"
)

st.title("📧 AI Email Assistant Agent")

st.write(
    "Enter an instruction and let the AI draft and save the email."
)

user_input = st.text_area(
    "What should the email do?",
    height=150,
    placeholder="Reply accepting the internship offer politely..."
)

if st.button("Generate Email"):
    if user_input.strip():

        with st.spinner("Agent working..."):

            result = agent.run_sync(user_input)

        st.success("Done!")

        st.subheader("Agent Response")

        st.write(result.output)

    else:
        st.warning("Please enter instructions.")