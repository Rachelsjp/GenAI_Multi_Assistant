import streamlit as st
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from llm import get_llm

def run():
    st.subheader("Email Writer")

    points = st.text_area("Enter email points")

    if st.button("Generate Email") and points:
        llm = get_llm()
        parser = StrOutputParser()

        prompt = PromptTemplate(
            input_variables=["points"],
            template="""
Write a professional email using:
{points}

Include subject, greeting, body, closing.
"""
        )

        chain = prompt | llm | parser
        response = chain.invoke({"points": points})

        st.markdown(response)