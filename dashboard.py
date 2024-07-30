import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import numpy as np

# Set page config at the very beginning
st.set_page_config(page_title="Quantitative Trading Dashboard", layout="wide")

# Custom CSS to improve the look and feel
st.markdown("""
<style>
    .reportview-container {
        background: #f0f2f6;
    }
    .main {
        background: #f0f2f6;
    }
    .stButton>button {
        color: #4F8BF9;
        border-radius: 50px;
        height: 3em;
        width: 100%;
    }
    .stTextInput>div>div>input {
        color: #4F8BF9;
    }
    .stTitle {
        font-size: 42px;
        font-weight: bold;
        color: #0e1117;
    }
    .stSubheader {
        font-size: 24px;
        font-weight: bold;
        color: #0e1117;
    }
</style>
""", unsafe_allow_html=True)

def overview_page():
    st.markdown('<p class="stSubheader">Dashboard Overview</p>', unsafe_allow_html=True)
    
    # Create a sample dataframe for demonstration
    df = pd.DataFrame({
        'Date': pd.date_range(start='2023-01-01', periods=100),
        'Portfolio Value': np.random.randint(10000, 15000, 100)
    })
    
    # Create a line chart using Plotly
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df['Date'], y=df['Portfolio Value'], mode='lines', name='Portfolio Value'))
    fig.update_layout(title='Portfolio Performance', xaxis_title='Date', yaxis_title='Value ($)')
    st.plotly_chart(fig, use_container_width=True)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric(label="Total Return", value="12.5%", delta="3.2%")
    with col2:
        st.metric(label="Sharpe Ratio", value="1.8", delta="0.2")
    with col3:
        st.metric(label="Max Drawdown", value="-5.2%", delta="1.1%", delta_color="inverse")

def strategy_analyzer_page():
    st.markdown('<p class="stSubheader">Quantitative Trading Strategy Analyzer</p>', unsafe_allow_html=True)
    st.write("AI-powered analysis and optimization of trading strategies")
    
    strategy = st.selectbox("Select Strategy", ["Moving Average Crossover", "RSI Oscillator", "MACD"])
    timeframe = st.select_slider("Timeframe", options=["1D", "1W", "1M", "3M", "6M", "1Y"])
    
    if st.button("Analyze Strategy", key="analyze"):
        st.info("Strategy analysis initiated...")
        # Here you would typically call your Falcon LLM API to perform the analysis
        st.success("Analysis complete! Check the results below.")
        
        # Placeholder for results
        st.write("Strategy Performance:")
        st.write("• Win Rate: 62%")
        st.write("• Profit Factor: 1.8")
        st.write("• Sharpe Ratio: 1.5")

def market_sentiment_page():
    st.markdown('<p class="stSubheader">Market Sentiment Analysis Tool</p>', unsafe_allow_html=True)
    st.write("Analyzing news and social media to gauge market sentiment")
    
    ticker = st.text_input("Enter stock ticker")
    if st.button("Analyze Sentiment", key="sentiment"):
        st.info(f"Analyzing sentiment for {ticker}...")
        # Here you would typically call your Falcon LLM API for sentiment analysis
        st.success("Sentiment analysis complete!")
        
        # Placeholder for sentiment results
        sentiment_score = 0.75
        st.progress(sentiment_score)
        st.write(f"Sentiment Score: {sentiment_score:.2f} (Bullish)")

def portfolio_management_page():
    st.markdown('<p class="stSubheader">Portfolio Management</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Portfolio Rebalancing")
        st.write("AI-driven portfolio monitoring and rebalancing")
        if st.button("Rebalance Portfolio", key="rebalance"):
            st.info("Portfolio rebalancing in progress...")
    
    with col2:
        st.subheader("Risk Management")
        st.write("Assessing and managing financial risks, ensuring compliance")
        if st.button("Assess Risks", key="risks"):
            st.info("Risk assessment initiated...")

def research_tools_page():
    st.markdown('<p class="stSubheader">Research Tools</p>', unsafe_allow_html=True)
    
    tool = st.radio("Select Research Tool", ["Quantitative Research Assistant", "Financial Report Summarizer"])
    
    if tool == "Quantitative Research Assistant":
        st.write("Virtual assistant for quantitative research and analysis")
        research_query = st.text_area("Enter your research query")
        if st.button("Start Research", key="research"):
            st.info("Research assistant activated...")
    
    elif tool == "Financial Report Summarizer":
        st.write("Summarizing financial reports and earnings calls")
        uploaded_file = st.file_uploader("Upload financial report", type="pdf")
        if uploaded_file is not None and st.button("Summarize Report", key="summarize"):
            st.info("Report summarization started...")

def main():
    st.markdown('<p class="stTitle">Quantitative Trading Dashboard</p>', unsafe_allow_html=True)

    # Add a sidebar
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ["Overview", "Strategy Analyzer", "Market Sentiment", "Portfolio Management", "Research Tools"])

    if page == "Overview":
        overview_page()
    elif page == "Strategy Analyzer":
        strategy_analyzer_page()
    elif page == "Market Sentiment":
        market_sentiment_page()
    elif page == "Portfolio Management":
        portfolio_management_page()
    elif page == "Research Tools":
        research_tools_page()

if __name__ == "__main__":
    main()