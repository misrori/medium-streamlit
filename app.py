import streamlit as st
import plotly.graph_objects as go
from goldhand import *


tw = Tw()
ticker= 'ETH-USD'
t = GoldHand(ticker)
p = t.plotly_last_year(tw.get_plotly_title(ticker))



# Create Plotly plot
#fig = go.Figure(data=[go.Bar(x=['A', 'B', 'C'], y=[10, 20, 30])])
st.plotly_chart(p)
