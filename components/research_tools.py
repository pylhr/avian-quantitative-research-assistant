# components/research_tools.py
import streamlit as st
from utils.ai71_client import get_llm_response
from utils.search_client import search_result
import PyPDF2


def extract_text_from_pdf(pdf_file):
    reader = PyPDF2.PdfReader(pdf_file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text


def chunk_text(text, chunk_size=1000):
    # Splits the text into chunks of specified size
    for i in range(0, len(text), chunk_size):
        yield text[i : i + chunk_size]


def summarize_chunk(chunk, model):
    messages = [
        {
            "role": "system",
            "content": "You are a knowledgeable quantitative and finance research assistant.",
        },
        {"role": "user", "content": f"Summarize the following text: {chunk}"},
    ]
    response = get_llm_response(model, messages)
    return response


def research_assistant(query):
    data_input = search_result(query)
    prompt = (
        f"Based on the following real-time data, provide an answer for the query "
        f"Include relevant sources and links if needed.\n\n{data_input}"
    )
    messages = [
        {
            "role": "system",
            "content": "You are a helpful quantitative and financial research assistant.",
        },
        {"role": "user", "content": prompt},
    ]
    response = get_llm_response("tiiuae/falcon-180B-chat", messages)
    return response


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

            response = research_assistant(research_query)
            st.success("Research complete!")
            # st.write(response)
            st.markdown(
                f"<p style='font-size:16px;'>{response}</p>", unsafe_allow_html=True
            )

    elif tool == "Financial Report Summarizer":
        st.write(
            "Summarizing financial reports and earnings calls or any dossier you need help with."
        )
        uploaded_file = st.file_uploader("Upload financial report", type="pdf")
        if uploaded_file is not None and st.button("Summarize Report", key="summarize"):
            st.info("Report summarization started...")
            file_content = extract_text_from_pdf(uploaded_file)

            summarized_chunks = []
            chunk_size = 1000  # Adjust chunk size based on model and API limits
            for i, chunk in enumerate(chunk_text(file_content, chunk_size)):
                summary = summarize_chunk(chunk, "tiiuae/falcon-180B-chat")
                # st.markdown(f"### Summary of Chunk {i + 1}")
                st.markdown(
                    f"<p style='font-size:16px;'>{summary}</p>", unsafe_allow_html=True
                )
            st.success("Summarization complete!")
            # final_summary = " ".join(summarized_chunks)
            # st.success("Summarization complete!")
        # st.write(final_summary)
