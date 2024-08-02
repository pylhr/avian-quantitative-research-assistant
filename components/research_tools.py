# components/research_tools.py
import streamlit as st
from utils.ai71_client import get_llm_response


def research_tools_page():
    st.markdown('<p class="stSubheader">Research Tools</p>', unsafe_allow_html=True)

    tool = st.radio(
        "Select Research Tool",
        ["Quantitative Research Assistant", "Financial Report Summarizer"],
    )

    if tool == "Quantitative Research Assistant":
        st.write("Virtual assistant for quantitative research and analysis")
        research_query = st.text_area("Enter your research query")
        if st.button("Start Research", key="research"):
            st.info("Research assistant activated...")
            messages = [
                {"role": "system", "content": "You are a helpful assistant."},
                {
                    "role": "user",
                    "content": f"Research the following query: {research_query}",
                },
            ]
            response = get_llm_response("tiiuae/falcon-180B-chat", messages)
            st.success("Research complete!")
            st.write(response)

    elif tool == "Financial Report Summarizer":
        st.write("Summarizing financial reports and earnings calls")
        uploaded_file = st.file_uploader("Upload financial report", type="pdf")
        if uploaded_file is not None and st.button("Summarize Report", key="summarize"):
            st.info("Report summarization started...")
            # Assuming the content of the file is extracted and sent directly
            file_content = uploaded_file.read().decode(
                "utf-8"
            )  # Assuming text-based PDF for simplicity
            messages = [
                {"role": "system", "content": "You are a helpful assistant."},
                {
                    "role": "user",
                    "content": f"Summarize the following financial report: {file_content}",
                },
            ]
            response = get_llm_response("tiiuae/falcon-180B-chat", messages)
            st.success("Summarization complete!")
            st.write(response)
