# components/market_sentiment.py
import streamlit as st
from utils.ai71_client import get_llm_response


def market_sentiment_page():
    st.markdown(
        '<p class="stSubheader">Market Sentiment Analysis Tool</p>',
        unsafe_allow_html=True,
    )
    st.write("Analyzing news and social media to gauge market sentiment")

    ticker = st.text_input("Enter stock ticker")
    if st.button("Analyze Sentiment", key="sentiment"):
        st.info(f"Analyzing sentiment for {ticker}...")
        messages = [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f"Analyze the market sentiment for {ticker}."},
        ]
        response = get_llm_response("tiiuae/falcon-180B-chat", messages)
        st.success("Sentiment analysis complete!")
        st.write(response)
