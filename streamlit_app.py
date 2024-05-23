# Import python packages
import streamlit as st
from snowflake.snowpark.functions import col
import requests
import pandas

st.title('Zena\'s Amazing Athleisure Catalog')

# connect to snowflake
cnx = st.connection("snowflake")
session = cnx.session()
##my_cur = cnx.cursor()

# run a snowflake query and put it all in a var called my_catalog
##my_cur.execute("select color_or_style from ZENAS_ATHLEISURE_DB.PRODUCTS.catalog_for_website")
##my_catalog = my_cur.fetchall()

# put the data into a dataframe
#my_dataframe = session.table("ZENAS_ATHLEISURE_DB.PRODUCTS.CATALOG_FOR_WEBSITE").select(col('COLOR_OR_STYLE'), col('DIRECT_URL'))
my_dataframe = session.table("ZENAS_ATHLEISURE_DB.PRODUCTS.CATALOG_FOR_WEBSITE")
#df = pandas.DataFrame(my_catalog)
df = my_dataframe.toPandas()

# temp write the dataframe to the page so I Can see what I am working with
streamlit.write(df)
# put the first column into a list
color_list = df[0].values.tolist()
# print(color_list)
# Let's put a pick list here so they can pick the color
option = streamlit.selectbox('Pick a sweatsuit color or style:', list(color_list))

## We'll build the image caption now, since we can
#product_caption = 'Our warm, comfortable, ' + option + ' sweatsuit!'
## use the option selected to go back and get all the info from the database
#my_cur.execute("select direct_url, price, size_list, upsell_product_desc from ZENAS_ATHLEISURE_DB.PRODUCTS.catalog_for_website where color_or_style = '" + option + "';")
#df2 = my_cur.fetchone()
#streamlit.image(
#df2[0],
#width=400,
#caption= product_caption
#)
#streamlit.write('Price: ', df2[1])
#streamlit.write('Sizes Available: ',df2[2])
#streamlit.write(df2[3])
