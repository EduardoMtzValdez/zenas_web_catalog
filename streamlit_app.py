# Import python packages
import streamlit as st
from snowflake.snowpark.functions import col
import requests
import pandas

st.title('Zena\'s Amazing Athleisure Catalog')

# connect to snowflake
cnx = st.connection("snowflake")
session = cnx.session()

# put the data into a dataframe
#my_dataframe = session.table("ZENAS_ATHLEISURE_DB.PRODUCTS.CATALOG_FOR_WEBSITE").select(col('COLOR_OR_STYLE'), col('DIRECT_URL'))
my_dataframe = session.table("ZENAS_ATHLEISURE_DB.PRODUCTS.CATALOG_FOR_WEBSITE")
my_list = session.table("ZENAS_ATHLEISURE_DB.PRODUCTS.CATALOG_FOR_WEBSITE").select(col('COLOR_OR_STYLE'))
color_list = my_list.to_pandas()                                                                                    
#Convert df to pandas
df = my_dataframe.to_pandas()
option = st.selectbox('Pick a sweatsuit color or style:', color_list)

## We'll build the image caption now, since we can
product_caption = "Our warm, comfortable, " + option + " sweatsuit!"
## use the option selected to go back and get all the info from the database
df2 = session.table("ZENAS_ATHLEISURE_DB.PRODUCTS.CATALOG_FOR_WEBSITE").select(col('DIRECT_URL'), col('PRICE'), col('SIZE_LIST'), col('UPSELL_PRODUCT_DESC')).where("color_or_style = '" + option + "'")
url = df2.collect()[0][0]

# Mostrando la Imagen
st.image(url, width=400, caption= product_caption)

st.text("Price: ", df2.collect()[0][1])
st.Text("Sizes Available: ",df2.collect()[0][2])
st.Text(df2.collect()[0][3])
