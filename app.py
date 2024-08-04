import streamlit as st
from components.overview import overview_page
from components.strategy_analyzer import strategy_analyzer_page
from components.market_sentiment import market_sentiment_page
from components.portfolio_management import portfolio_management_page
from components.research_tools import research_tools_page

# Set page config at the very beginning
st.set_page_config(page_title="Quantitative Research Assistant", layout="wide")

# Initialize session state for page navigation
if "page" not in st.session_state:
    st.session_state.page = "Home"

# Custom CSS to improve the look and feel
st.markdown(
    """
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
""",
    unsafe_allow_html=True,
)

# Sidebar for navigation
st.sidebar.title("Quantitative Research Assistant")
page = st.sidebar.radio(
    "Navigation",
    [
        "Home",
        "Strategy Analyzer",
        "Market Sentiment",
        "Portfolio Management",
        "Research Tools",
    ],
)

# Update session state for page
if page != st.session_state.page:
    st.session_state.page = page

# Display the selected page
if st.session_state.page == "Home":
    overview_page()
elif st.session_state.page == "Strategy Analyzer":
    strategy_analyzer_page()
elif st.session_state.page == "Market Sentiment":
    market_sentiment_page()
elif st.session_state.page == "Portfolio Management":
    portfolio_management_page()
elif st.session_state.page == "Research Tools":
    research_tools_page()
