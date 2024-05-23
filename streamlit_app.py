# Import python packages
import streamlit as st
from snowflake.snowpark.functions import col
import requests

st.title('My Parents New Healthy Dinner')

# Write directly to the app
#st.title(":cup_with_straw: Customize Your Smoothie! :cup_with_straw:")
#st.write(    """**Choose the fruits you want in your custom Smoothie!**""")

#name_on_order = st.text_input('Name on Smoothie:')
#st.write('The name on your Smoothie will be:', name_on_order)

#session = get_active_session()
cnx = st.connection("snowflake")
session = cnx.session()

my_cur = session.cursor()
session.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_data_row = session.fetchone()

my_data_row = my_cur.fetchone()
st.text("Hello from Snowflake:")
st.text(my_data_row)
