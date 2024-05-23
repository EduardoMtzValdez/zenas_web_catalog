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

# temp write the dataframe to the page so I Can see what I am working with
#st.write(df)
# put the first column into a list
##color_list = df[0].values.tolist()
#print(color_list)
# Let's put a pick list here so they can pick the color
option = st.selectbox('Pick a sweatsuit color or style:', color_list)

st.stop()

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
