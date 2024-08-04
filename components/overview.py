import streamlit as st


def overview_page():
    st.title("Home")

    # Create a 2x2 grid layout
    col1, col2 = st.columns(2)

    with col1:
        # Card for Strategy Analyzer
        with st.container():
            st.markdown(
                """
                <div style="
                    background-color: #ffffff;
                    border-radius: 12px;
                    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
                    padding: 20px;
                    margin: 10px;
                    text-align: center;
                ">
                    <h3 style="color: #0e1117;">Strategy Analyzer</h3>
                    <p style="color: #555555;">Analyze and refine your trading strategies.</p>
                    <a href="javascript:void(0);" onclick="window.location.href='/strategy_analyzer';" 
                       style="
                       display: inline-block;
                       padding: 10px 20px;
                       font-size: 16px;
                       color: white;
                       background-color: #4F8BF9;
                       border-radius: 8px;
                       text-decoration: none;
                       box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
                       ">Go to Strategy Analyzer</a>
                </div>
            """,
                unsafe_allow_html=True,
            )

    with col2:
        # Card for Market Sentiment
        with st.container():
            st.markdown(
                """
                <div style="
                    background-color: #ffffff;
                    border-radius: 12px;
                    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
                    padding: 20px;
                    margin: 10px;
                    text-align: center;
                ">
                    <h3 style="color: #0e1117;">Market Sentiment</h3>
                    <p style="color: #555555;">Get insights into market trends and sentiment.</p>
                    <a href="javascript:void(0);" onclick="window.location.href='/market_sentiment';"
                       style="
                       display: inline-block;
                       padding: 10px 20px;
                       font-size: 16px;
                       color: white;
                       background-color: #4F8BF9;
                       border-radius: 8px;
                       text-decoration: none;
                       box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
                       ">Go to Market Sentiment</a>
                </div>
            """,
                unsafe_allow_html=True,
            )

    col3, col4 = st.columns(2)

    with col3:
        # Card for Portfolio Management
        with st.container():
            st.markdown(
                """
                <div style="
                    background-color: #ffffff;
                    border-radius: 12px;
                    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
                    padding: 20px;
                    margin: 10px;
                    text-align: center;
                ">
                    <h3 style="color: #0e1117;">Portfolio Management</h3>
                    <p style="color: #555555;">Manage and optimize your investment portfolio.</p>
                    <a href="javascript:void(0);" onclick="window.location.href='/portfolio_management';"
                       style="
                       display: inline-block;
                       padding: 10px 20px;
                       font-size: 16px;
                       color: white;
                       background-color: #4F8BF9;
                       border-radius: 8px;
                       text-decoration: none;
                       box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
                       ">Go to Portfolio Management</a>
                </div>
            """,
                unsafe_allow_html=True,
            )

    with col4:
        # Card for Research Tools
        with st.container():
            st.markdown(
                """
                <div style="
                    background-color: #ffffff;
                    border-radius: 12px;
                    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
                    padding: 20px;
                    margin: 10px;
                    text-align: center;
                ">
                    <h3 style="color: #0e1117;">Research Tools</h3>
                    <p style="color: #555555;">Explore tools for in-depth research and analysis.</p>
                    <a href="javascript:void(0);" onclick="window.location.href='/research_tools';"
                       style="
                       display: inline-block;
                       padding: 10px 20px;
                       font-size: 16px;
                       color: white;
                       background-color: #4F8BF9;
                       border-radius: 8px;
                       text-decoration: none;
                       box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
                       ">Go to Research Tools</a>
                </div>
            """,
                unsafe_allow_html=True,
            )

    # Optional: Add some spacing at the bottom
    st.markdown("<br>", unsafe_allow_html=True)
