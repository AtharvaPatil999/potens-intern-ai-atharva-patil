import streamlit as st
import requests

st.set_page_config(page_title="Document Q&A")

st.title("📄 Document Q&A with Citations")

question = st.text_input("Ask a question")

if st.button("Ask"):

    response = requests.post(
        "http://127.0.0.1:8000/ask",
        json={
            "question": question
        }
    )

    result = response.json()

    st.subheader("Answer")

    st.write(result["answer"])

    st.subheader("Citations")

    for citation in result["citations"]:

        st.write(f"📄 {citation['document']}")
        st.write(f"Page: {citation['page']}")
        st.write(citation["snippet"])
        st.divider()