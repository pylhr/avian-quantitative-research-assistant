import streamlit as st
from utils.ai71_client import get_llm_response
from utils.stock_data import get_stock_data


def portfolio_management_page():
    st.markdown('<p class="stSubheader">Portfolio Management</p>', unsafe_allow_html=True)

    # Initialize portfolio in session state if not already present
    if "portfolio" not in st.session_state:
        st.session_state.portfolio = {}

    st.subheader("Enter your portfolio")

    # Input for stock ticker and quantity
    stock = st.text_input("Stock Ticker (e.g., AAPL)", key="stock")
    quantity = st.number_input("Quantity", min_value=0, key="quantity")

    if st.button("Add to Portfolio"):
        if stock and quantity > 0:
            # Add or update the stock in the portfolio
            if stock in st.session_state.portfolio:
                st.session_state.portfolio[stock] += quantity
            else:
                st.session_state.portfolio[stock] = quantity
            st.success(f"Added {quantity} shares of {stock} to portfolio")

    st.subheader("Your Portfolio")
    if st.session_state.portfolio:
        st.write(st.session_state.portfolio)

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Portfolio Rebalancing")
        st.write("AI-driven portfolio monitoring and rebalancing")
        if st.button("Rebalance Portfolio", key="rebalance"):
            st.info("Portfolio rebalancing in progress...")
            messages = [
                {"role": "system", "content": "You are a helpful assistant."},
                {
                    "role": "user",
                    "content": f"Following is my portfolio: {st.session_state.portfolio}, rebalance this",
                },
            ]
            response = get_llm_response("tiiuae/falcon-180B-chat", messages)
            st.success("Portfolio rebalancing complete!")
            st.write(response)

    with col2:
        st.subheader("Risk Management")
        st.write("Assessing and managing financial risks, ensuring compliance")
        if st.button("Assess Risks", key="risks"):
            st.info("Risk assessment initiated...")
            messages = [
                {"role": "system", "content": "You are a helpful assistant."},
                {
                    "role": "user",
                    "content": f"Assess the financial risks for {st.session_state.portfolio} based upon this {get_stock_data(stock)}",
                },
            ]
            response = get_llm_response("tiiuae/falcon-180B-chat", messages)
            st.success("Risk assessment complete!")
            st.write(response)

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

