import streamlit as st


def overview_page():
    # Main Header
    st.title("Avian Quantitative Research Assistant")
    st.markdown("## Empower your quantitative research with data-driven insights")

    # Introduction to the dashboard
    st.markdown(
        """
        Welcome to your one-stop platform for quantitative research and analysis. 
        Explore various tools designed to help you analyze market sentiment, optimize trading strategies, manage your portfolio, and conduct in-depth research.
        """
    )

    # Horizontal sections with cards or boxes for each feature
    st.markdown("---")
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown(
            """
            <div style="
                background-color: #f8f9fa; 
                border-radius: 10px; 
                padding: 20px;
                box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1); 
                text-align: center;">
                <h3 style="color: #0e1117;">Strategy Analyzer</h3>
                <p>Analyze and optimize your trading strategies across different market conditions.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col2:
        st.markdown(
            """
            <div style="
                background-color: #f8f9fa; 
                border-radius: 10px; 
                padding: 20px;
                box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1); 
                text-align: center;">
                <h3 style="color: #0e1117;">Market Sentiment</h3>
                <p>Get insights into market trends and sentiment to stay ahead of the curve.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col3:
        st.markdown(
            """
            <div style="
                background-color: #f8f9fa; 
                border-radius: 10px; 
                padding: 20px;
                box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1); 
                text-align: center;">
                <h3 style="color: #0e1117;">Portfolio Management</h3>
                <p>Manage and optimize your investment portfolio for better returns.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    # Another row for more features or tools
    st.markdown("---")
    col4, col5, col6 = st.columns(3)

    with col4:
        st.markdown(
            """
            <div style="
                background-color: #f8f9fa; 
                border-radius: 10px; 
                padding: 20px;
                box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1); 
                text-align: center;">
                <h3 style="color: #0e1117;">Research Tools</h3>
                <p>Conduct in-depth research and analysis with our powerful tools.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col5:
        st.markdown(
            """
            <div style="
                background-color: #f8f9fa; 
                border-radius: 10px; 
                padding: 20px;
                box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1); 
                text-align: center;">
                <h3 style="color: #0e1117;">Coming Soon</h3>
                <p>Stay tuned for new features and tools to enhance your trading experience.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    # Footer section or additional information
    st.markdown("---")
    st.markdown(
        """
        <div style="text-align: center; padding: 20px;">
            <p style="color: #0e1117;">Use the sidebar to navigate through different tools and features.</p>
            <p>Developed by <a href="https://pylhr.vercel.app/" target="_blank">PYLHR</a> &copy <a href="https://www.linkedin.com/in/pylhr" target="_blank">Priyanshu Lohar</a> </p>
            
        </div>
        """,
        unsafe_allow_html=True,
    )
