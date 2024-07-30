# components/strategy_analyzer.py
import streamlit as st
from utils.ai71_client import get_llm_response


def strategy_analyzer_page():
    st.markdown(
        '<p class="stSubheader">Quantitative Trading Strategy Analyzer</p>',
        unsafe_allow_html=True,
    )
    st.write("AI-powered analysis and optimization of trading strategies")

    strategy = st.selectbox(
        "Select Strategy", ["Moving Average Crossover", "RSI Oscillator", "MACD"]
    )
    timeframe = st.select_slider(
        "Timeframe", options=["1D", "1W", "1M", "3M", "6M", "1Y"]
    )

    if st.button("Analyze Strategy", key="analyze"):
        st.info("Strategy analysis initiated...")
        messages = [
            {"role": "system", "content": "You are a helpful assistant."},
            {
                "role": "user",
                "content": f"Analyze the {strategy} strategy for the {timeframe} timeframe.",
            },
        ]
        response = get_llm_response("tiiuae/falcon-180B-chat", messages)
        st.success("Analysis complete! Check the results below.")
        st.write(response)
