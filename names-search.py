import streamlit as st
import panda as pd

st.title("search names")
DATA_URL = "dataset.csv"

@st.cache
def load_data_byname(name):
    data = pd.read_csv(DATA_URL) # read csv
    filtered_data_byname = data[data["name"].st.contains(name)]
    return filtered_data_byname # return the dataframe

byname = st.text.input("nombre :")
if (myname):
    filterbyname = load data byname(myname) # call the functionn
    count_row = filterbyname.shape[0] #
    st.write(f"Total names : {count_row}")

    st.dataframe(filterbyname)
