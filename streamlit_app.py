import streamlit as st

st.set_page_config(page_title="Budgetting App", page_icon='tada', layout='wide')

st.header("Budgetting App For Apartment")

rent1 = (st.input("Monthly Rent Cost")

gas1 = (st.input("Monthly Gas Cost: ")

food1 = (st.input("Monthly Food Cost: ")

girl1 = (st.input("Monthly Girl Cost (If you get no bitches, just throw in a 0): ")

gambling1 = (st.input("Monthly Gambling Cost dont cap: ")

substances1 = (st.input("Monthly Alchohol, Weed, and Nic costs: ")

personal1 = (st.input("Monthly Personal Spending Cost: ")

total = (rent1 + gas1 + food1 + girl1 + gambling1 + substances1 + personal1)
st.header("Total price = " + total)








