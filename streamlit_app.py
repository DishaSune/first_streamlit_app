import streamlit
streamlit.title('My parent new healty diner')
streamlit.header('Breakfast Menu')
streamlit.text('1.Omega 3 and Blueberry Oatmeal')
streamlit.text('2.kale,Spinach and Rocket Smoothie')
streamlit.text('3.Hard boiled free-range egg')
import pandas
my_fruit_list=pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
streamlit.multiselect("Pick some fruits:",list(my_fruit_list.index))
streamlit.dataframe(my_fruit_list)

