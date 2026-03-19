import streamlit as st
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from llm import get_llm
from urllib.parse import urlparse, parse_qs
from youtube_transcript_api import YouTubeTranscriptApi

def get_video_id(url):
    parsed = urlparse(url)

    if parsed.hostname == 'youtu.be':
        return parsed.path[1:]

    if parsed.hostname in ('www.youtube.com', 'youtube.com'):
        return parse_qs(parsed.query).get('v', [None])[0]

    return None


def run():
    st.subheader("YouTube Summarizer")

    url = st.text_input("Enter URL")

    if st.button("Summarize") and url:

        video_id = get_video_id(url)

        if not video_id:
            st.error("Invalid URL")
            return

        try:
            # ✅ FIXED
            transcript = YouTubeTranscriptApi().fetch(video_id)
            text = " ".join([t.text for t in transcript])

            llm = get_llm()
            parser = StrOutputParser()

            prompt = PromptTemplate(
                input_variables=["text"],
                template="""
Summarize the following YouTube transcript clearly:

{text}
"""
            )

            chain = prompt | llm | parser
            summary = chain.invoke({"text": text})

            st.text_area("Summary", summary, height=300)

        except Exception as e:
            st.error(f"Error: {e}")