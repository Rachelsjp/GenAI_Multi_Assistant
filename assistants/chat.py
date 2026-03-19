import streamlit as st
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from llm import get_llm

def run():
    st.subheader("Chat Assistant")

    user_input = st.text_input("Ask anything")

    if st.button("Send") and user_input:
        llm = get_llm()
        parser = StrOutputParser()

        prompt = PromptTemplate(
            input_variables=["q"],
            template="""
You are a helpful AI assistant.

Question:
{q}

Answer clearly with examples.
"""
        )

        chain = prompt | llm | parser
        response = chain.invoke({"q": user_input})

        st.markdown(response)