import streamlit as st
from utils.ai71_client import get_llm_response
from utils.stock_data import get_stock_data


def portfolio_management_page():
    st.markdown(
        '<p class="stSubheader">Portfolio Management</p>', unsafe_allow_html=True
    )

    st.subheader("Enter your portfolio")
    portfolio = {}
    stock = st.text_input("Stock Ticker (e.g., AAPL)", key="stock")
    quantity = st.number_input("Quantity", min_value=0, key="quantity")

    if st.button("Add to Portfolio"):
        if stock and quantity > 0:
            portfolio[stock] = quantity
            st.success(f"Added {quantity} shares of {stock} to portfolio")

    st.subheader("Your Portfolio")
    if portfolio:
        st.write(portfolio)

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Portfolio Rebalancing")
        st.write("AI-driven portfolio monitoring and rebalancing")
        if st.button("Rebalance Portfolio", key="rebalance"):
            st.info("Portfolio rebalancing in progress...")
            messages = [
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": f"Rebalance my portfolio: {portfolio}"},
            ]
            response = get_llm_response("tiiuae/falcon-180B-chat", messages)
            st.success("Portfolio rebalancing complete!")
            st.write(response["choices"][0]["message"]["content"])

    with col2:
        st.subheader("Risk Management")
        st.write("Assessing and managing financial risks, ensuring compliance")
        if st.button("Assess Risks", key="risks"):
            st.info("Risk assessment initiated...")
            messages = [
                {"role": "system", "content": "You are a helpful assistant."},
                {
                    "role": "user",
                    "content": f"Assess the financial risks of my portfolio: {portfolio}",
                },
            ]
            response = get_llm_response("tiiuae/falcon-180B-chat", messages)
            st.success("Risk assessment complete!")
            st.write(response["choices"][0]["message"]["content"])

    st.subheader("Real-time Portfolio Value and Stock Data")
    if portfolio:
        total_value = 0
        for stock, quantity in portfolio.items():
            stock_data = get_stock_data(stock)
            price = float(stock_data["close"])
            total_value += price * quantity
            st.write(f"{stock}: {quantity} shares")
            st.write(f"Latest Data as of {stock_data['timestamp']}:")
            st.write(f"Open: ${stock_data['open']}")
            st.write(f"High: ${stock_data['high']}")
            st.write(f"Low: ${stock_data['low']}")
            st.write(f"Close: ${stock_data['close']}")
            st.write(f"Volume: {stock_data['volume']}")
            st.write(f"Total Value: ${price * quantity:.2f}")

        st.write(f"Total Portfolio Value: ${total_value:.2f}")
