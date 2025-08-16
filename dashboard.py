# dashboard.py
import streamlit as st
import pandas as pd
import plotly.express as px
from src.data.loader import DataLoader
from src.analysis.returns import calculate_daily_returns
from src.analysis.risk import calculate_rolling_volatility

def main():
    st.title("Financial Analysis Dashboard")
    
    # File upload
    uploaded_file = st.file_uploader("Upload your financial data (CSV)", type="csv")
    
    if uploaded_file is not None:
        # Load and process data
        loader = DataLoader(uploaded_file)
        df = loader.load_data()
        
        # Display raw data
        st.subheader("Raw Data")
        st.dataframe(df.head())
        
        # Calculate returns
        if 'Close' in df.columns:
            returns = calculate_daily_returns(df['Close'])
            
            # Plot returns
            st.subheader("Daily Returns")
            fig = px.line(returns, title="Daily Returns")
            st.plotly_chart(fig)
            
            # Calculate and plot volatility
            st.subheader("Rolling Volatility (21-day)")
            volatility = calculate_rolling_volatility(returns)
            fig = px.line(volatility, title="21-day Rolling Volatility")
            st.plotly_chart(fig)

if __name__ == "__main__":
    main()
    