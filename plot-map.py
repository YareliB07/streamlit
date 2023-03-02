import streamlit as st
import numpy as np
import pandas as pd

map_data=pd.DataFrame(
        np.random.randn(10,2)/[100,100]+[18.803333,-97.180833],
        columns=['lat','lon'])

st.map(map_data)
st.dataframe(map_data)
