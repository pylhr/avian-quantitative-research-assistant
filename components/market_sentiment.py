import streamlit as st
from utils.ai71_client import get_llm_response
from utils.search_client import search_result


def sentiment_analysis(query):
    data_input = search_result(query)
    prompt = (
        f"Based on the following real-time data, provide a precise prediction and market sentiment analysis for the provided company."
        f"Include relevant sources and links if needed.\n\n{data_input}"
    )

    messages = [
        {
            "role": "system",
            "content": "You are a helpful quantitative and financial research assistant. Provide a precise prediction and market sentiment analysis based on the real-time data, including sources like news articles.",
        },
        {"role": "user", "content": prompt},
    ]
    response = get_llm_response("tiiuae/falcon-180B-chat", messages)

    return response


def market_sentiment_page():
    st.markdown(
        '<p class="stSubheader">Market Sentiment Analysis Tool</p>',
        unsafe_allow_html=True,
    )
    st.write("Analyzing news and social media to gauge market sentiment")

    ticker = st.text_input("Enter stock ticker")
    if st.button("Analyze Sentiment", key="sentiment"):
        st.info(f"Analyzing sentiment for {ticker}...")

        response = sentiment_analysis(ticker)
        st.success("Sentiment analysis complete!")
        # st.write(response)
        st.markdown(
            f"<p style='font-size:16px;'>{response}</p>", unsafe_allow_html=True
        )
