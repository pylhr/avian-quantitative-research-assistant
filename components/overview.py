# components/overview.py
import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import numpy as np


def overview_page():
    st.markdown('<p class="stSubheader">Dashboard Overview</p>', unsafe_allow_html=True)

    df = pd.DataFrame(
        {
            "Date": pd.date_range(start="2023-01-01", periods=100),
            "Portfolio Value": np.random.randint(10000, 15000, 100),
        }
    )

    fig = go.Figure()
    fig.add_trace(
        go.Scatter(
            x=df["Date"], y=df["Portfolio Value"], mode="lines", name="Portfolio Value"
        )
    )
    fig.update_layout(
        title="Portfolio Performance", xaxis_title="Date", yaxis_title="Value ($)"
    )
    st.plotly_chart(fig, use_container_width=True)

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric(label="Total Return", value="12.5%", delta="3.2%")
    with col2:
        st.metric(label="Sharpe Ratio", value="1.8", delta="0.2")
    with col3:
        st.metric(
            label="Max Drawdown", value="-5.2%", delta="1.1%", delta_color="inverse"
        )
