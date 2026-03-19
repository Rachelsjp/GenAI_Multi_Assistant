import streamlit as st
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from llm import get_llm

def run():
    st.subheader("SQL Assistant")

    task = st.text_area("Describe SQL problem")

    if st.button("Generate SQL") and task:
        llm = get_llm()
        parser = StrOutputParser()

        prompt = PromptTemplate(
            input_variables=["task"],
            template="""
You are an expert SQL developer.

Task:
{task}

Provide:
1. SQL query
2. Explanation
"""
        )

        chain = prompt | llm | parser
        response = chain.invoke({"task": task})

        st.markdown(response)