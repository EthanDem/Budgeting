import streamlit as st

st.set_page_config(page_title="Budgetting App", page_icon='tada', layout='wide')

st.header("Budgetting App For Apartment")

rent1 = st.number_input("Monthly Rent Cost", step = 1)

gas1 = st.number_input("Monthly Gas Cost: ", step = 1)

food1 = st.number_input("Monthly Food Cost: ", step = 1)

girl1 = st.number_input("Monthly Girl Cost (If you get no bitches, just throw in a 0): ", step = 1)

gambling1 = st.number_input("Monthly Gambling Cost dont cap: ", step = 1)

substances1 = st.number_input("Monthly Alchohol, Weed, and Nic costs: ", step = 1)

personal1 = st.number_input("Monthly Personal Spending Cost: ", step = 1)

total = (rent1 + gas1 + food1 + girl1 + gambling1 + substances1 + personal1)

if st.button("Submit Calculations"):
  time.sleep(0.5)
  st.header("Your total monthly cost is:")
  st.header(total)







