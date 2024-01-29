import streamlit

streamlit.title('Snowflake Badge 2 Title')

streamlit.header('Snowflake Badge 2 Header')

streamlit.text('Snowflake Badge 2 Text')

import pandas

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))
streamlit.dataframe(my_fruit_list)

