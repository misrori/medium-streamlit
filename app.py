import streamlit as st
import plotly.graph_objects as go
from goldhand import *


tw = Tw()
ticker= 'ETH-USD'
t = GoldHand(ticker)
p = t.plotly_last_year(tw.get_plotly_title(ticker))



st.plotly_chart(p, use_container_width=True)
