import streamlit as st
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from llm import get_llm

def run():
    st.subheader("🎯 Mock Interview Practice")

    job_role = st.text_input("Job Role (e.g., AI Engineer)")
    
    job_description = st.text_area(
        "Job Description",
        height=200
    )

    if st.button("Generate Q&A"):

        if not job_role or not job_description:
            st.warning("Please enter both Job Role and Job Description")
            return

        llm = get_llm()
        parser = StrOutputParser()

        prompt = PromptTemplate(
            input_variables=["role", "jd"],
            template="""
You are an expert interviewer.

Role: {role}

Job Description:
{jd}

Generate:
- 5 interview questions
- Provide strong answers
- Mix technical + behavioral + scenario

Format:

Q1:
Answer:

Q2:
Answer:
"""
        )

        chain = prompt | llm | parser
        response = chain.invoke({
            "role": job_role,
            "jd": job_description
        })

        st.text_area("Interview Questions & Answers", response, height=400)