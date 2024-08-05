import streamlit as st
from utils.ai71_client import get_llm_response


def strategy_analyzer_page():
    st.markdown(
        '<p class="stSubheader">Quantitative Trading Strategy Analyzer</p>',
        unsafe_allow_html=True,
    )
    st.write("AI-powered analysis and optimization of trading strategies")

    # Strategy selection
    strategy_option = st.selectbox(
        "Select Strategy",
        [
            "Moving Average Crossover",
            "RSI Oscillator",
            "MACD",
            "Mean Reversion",
            "Momentum",
            "Custom",
        ],
    )

    # Common input for timeframe
    timeframe = st.select_slider(
        "Timeframe", options=["1D", "1W", "1M", "3M", "6M", "1Y"]
    )

    # Inputs for predefined strategies
    if strategy_option == "Moving Average Crossover":
        short_ma = st.number_input(
            "Short-term Moving Average (days)", min_value=1, value=50
        )
        long_ma = st.number_input(
            "Long-term Moving Average (days)", min_value=1, value=200
        )
        signals = st.selectbox("Signals", ["Buy", "Sell", "Both"])
        strategy_details = f"Short-term Moving Average: {short_ma} days, Long-term Moving Average: {long_ma} days, Signals: {signals}"

    elif strategy_option == "RSI Oscillator":
        rsi_period = st.number_input("RSI Period (days)", min_value=1, value=14)
        overbought_level = st.number_input(
            "Overbought Level", min_value=0, max_value=100, value=70
        )
        oversold_level = st.number_input(
            "Oversold Level", min_value=0, max_value=100, value=30
        )
        strategy_details = f"RSI Period: {rsi_period} days, Overbought Level: {overbought_level}, Oversold Level: {oversold_level}"

    elif strategy_option == "MACD":
        short_ema = st.number_input("Short-term EMA (days)", min_value=1, value=12)
        long_ema = st.number_input("Long-term EMA (days)", min_value=1, value=26)
        signal_line = st.number_input("Signal Line (days)", min_value=1, value=9)
        strategy_details = f"Short-term EMA: {short_ema} days, Long-term EMA: {long_ema} days, Signal Line: {signal_line} days"

    elif strategy_option == "Mean Reversion":
        mean_period = st.number_input("Mean Period (days)", min_value=1, value=30)
        threshold = st.number_input("Deviation Threshold (%)", min_value=0.1, value=5.0)
        strategy_details = (
            f"Mean Period: {mean_period} days, Deviation Threshold: {threshold}%"
        )

    elif strategy_option == "Momentum":
        momentum_period = st.number_input(
            "Momentum Period (days)", min_value=1, value=14
        )
        holding_period = st.number_input("Holding Period (days)", min_value=1, value=7)
        strategy_details = f"Momentum Period: {momentum_period} days, Holding Period: {holding_period} days"

    elif strategy_option == "Custom":
        st.subheader("Custom Strategy Input")
        custom_name = st.text_input("Strategy Name", "Enter custom strategy name")
        custom_description = st.text_area(
            "Strategy Description",
            "Provide a detailed description of the custom strategy including parameters and logic.",
        )
        strategy_details = (
            f"Custom Strategy Name: {custom_name}, Description: {custom_description}"
        )

    # Additional inputs for user thoughts and plan
    st.subheader("Additional Details")
    tickers = st.text_area(
        "Stock Tickers (comma-separated, e.g., AAPL, MSFT, TSLA)",
        "Enter stock tickers here",
    )
    user_plan = st.text_area(
        "Your Plan", "Describe your plan for implementing this strategy."
    )
    thoughts = st.text_area(
        "Your Thoughts",
        "Share any additional thoughts or considerations regarding this strategy.",
    )

    if st.button("Analyze Strategy", key="analyze"):
        st.info("Strategy analysis initiated...")
        tickers_list = [ticker.strip() for ticker in tickers.split(",")]

        messages = [
            {"role": "system", "content": "You are a helpful assistant."},
            {
                "role": "user",
                "content": f"Analyze the {strategy_option} strategy for the {timeframe} timeframe with the following details: {strategy_details}. The user is planning to implement this strategy on the following stocks: {', '.join(tickers_list)}. Here is the user's plan: {user_plan}. Additional thoughts: {thoughts}.",
            },
        ]
        response = get_llm_response("tiiuae/falcon-180B-chat", messages)
        st.success("Analysis complete! Check the results below.")
        st.write(response)
