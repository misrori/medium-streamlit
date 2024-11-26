import streamlit as st
import plotly.graph_objects as go

# Create Plotly plot
fig = go.Figure(data=[go.Bar(x=['A', 'B', 'C'], y=[10, 20, 30])])
st.plotly_chart(fig)
