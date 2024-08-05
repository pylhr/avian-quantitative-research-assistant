import streamlit as st
from utils.ai71_client import get_llm_response
from utils.stock_data import get_stock_data
from utils.search_client import search_result
import json


def portfolio_management_page():
    st.markdown(
        '<p class="stSubheader">Portfolio Management</p>', unsafe_allow_html=True
    )

    # Initialize portfolio in session state if not already present
    if "portfolio" not in st.session_state:
        st.session_state.portfolio = {}

    st.subheader("Enter your portfolio")

    # Input for stock ticker and quantity
    stock = st.text_input("Stock Ticker (e.g., AAPL)", key="stock")
    quantity = st.number_input("Quantity", min_value=0, key="quantity")
    stock_query = []
    if st.button("Add to Portfolio"):
        if stock and quantity > 0:
            # Add or update the stock in the portfolio
            if stock in st.session_state.portfolio:
                st.session_state.portfolio[stock] += quantity

            else:
                st.session_state.portfolio[stock] = quantity
                stock_query.append(stock)
            st.success(f"Added {quantity} shares of {stock} to portfolio")

    def rebalance_portfolio(query, stock):
        # Retrieve market data based on the query
        data_input = search_result(query)

        # Fetch stock data using the provided stock symbol
        stock_data = get_stock_data(stock)

        # Generate a prompt for a more specific rebalancing strategy
        prompt = (
            f"Based on the following real-time market data and specific stock information, provide a detailed and actionable rebalancing strategy for the portfolio '{st.session_state.portfolio}'. "
            f"The portfolio currently holds {stock_data}. Provide specific buy/sell recommendations, including the percentage of the portfolio to allocate to each asset, and any other relevant details.\n\n"
            f"Market Data:\n{data_input}\n\n"
            f"Stock Data for {stock}:\n{stock_data}\n\n"
            f"Consider the following factors: current asset allocation, target allocation, risk tolerance, tax implications, and market conditions. Provide specific actions with percentages for each asset."
        )

        # Structure the messages for the language model
        messages = [
            {
                "role": "system",
                "content": "You are a financial assistant specialized in portfolio management.",
            },
            {"role": "user", "content": prompt},
        ]

        # Get the language model's response
        response = get_llm_response("tiiuae/falcon-180B-chat", messages)

        # Return the rebalancing advice
        return response

    def risk_assessment(query):
        data_input = search_result(query)
        prompt = (
            f"Based on the following real-time data, provide an answer for the query Assess the financial risks for {st.session_state.portfolio} based upon this {get_stock_data(stock)} "
            f"Include relevant sources and links if needed.\n\n{data_input}"
        )
        messages = [
            {"role": "system", "content": "You are a helpful assistant."},
            {
                "role": "user",
                "content": prompt,
            },
        ]
        response = get_llm_response("tiiuae/falcon-180B-chat", messages)
        return response

    st.subheader("Your Portfolio")
    if st.session_state.portfolio:
        st.write(st.session_state.portfolio)

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Portfolio Rebalancing")
        st.write("AI-driven portfolio monitoring and rebalancing")
        if st.button("Rebalance Portfolio", key="rebalance"):
            st.info("Portfolio rebalancing in progress...")
            query = str(list(st.session_state.portfolio.keys()))
            response = rebalance_portfolio(query, stock)
            st.success("Portfolio rebalancing complete!")
            # st.write(response)
            st.markdown(
                f"<p style='font-size:16px;'>{response}</p>", unsafe_allow_html=True
            )

    with col2:
        st.subheader("Risk Management")
        st.write("Assessing and managing financial risks, ensuring compliance")
        if st.button("Assess Risks", key="risks"):
            st.info("Risk assessment initiated...")

            query = str(list(st.session_state.portfolio.keys()))

            response = risk_assessment(query)
            st.success("Risk assessment complete!")
            # st.write(response)
            st.markdown(
                f"<p style='font-size:16px;'>{response}</p>", unsafe_allow_html=True
            )

    st.subheader("Real-time Portfolio Value and Stock Data")
    if st.session_state.portfolio:
        total_value = 0
        for stock, quantity in st.session_state.portfolio.items():
            stock_data = get_stock_data(stock)
            if stock_data:
                price = float(stock_data.get("close", 0))
                total_value += price * quantity
                st.write(f"{stock}: {quantity} shares")
                st.write(f"Latest Data as of {stock_data.get('timestamp', 'N/A')}:")
                st.write(f"Open: ${stock_data.get('open', 'N/A')}")
                st.write(f"High: ${stock_data.get('high', 'N/A')}")
                st.write(f"Low: ${stock_data.get('low', 'N/A')}")
                st.write(f"Close: ${stock_data.get('close', 'N/A')}")
                st.write(f"Volume: {stock_data.get('volume', 'N/A')}")
                st.write(f"Total Value: ${price * quantity:.2f}")
            else:
                st.warning(f"Failed to retrieve data for {stock}")

        st.write(f"Total Portfolio Value: ${total_value:.2f}")
