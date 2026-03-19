import streamlit as st
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from llm import get_llm
from utils.file_reader import extract_text

def run():
    st.subheader("Cover Letter Generator")

    file = st.file_uploader("Upload Resume", type=["pdf", "docx", "txt"])
    role = st.text_input("Job Title")
    company = st.text_input("Company Name")

    if st.button("Generate Cover Letter"):
        if file and role:
            resume_text = extract_text(file)

            llm = get_llm()
            parser = StrOutputParser()

            prompt = PromptTemplate(
                input_variables=["resume", "role", "company"],
                template="""
Create a professional cover letter.

Role: {role}
Company: {company}

Resume:
{resume}
"""
            )

            chain = prompt | llm | parser
            response = chain.invoke({
                "resume": resume_text,
                "role": role,
                "company": company
            })

            st.text_area("Cover Letter", response, height=400)