import streamlit as st
import pandas as pd
import base64
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
from PIL import Image
from datetime import datetime


image = Image.open('images/logo.png')
st.image(image, width = 800)

caesars_titletemp = """
<div style="background-color:#E31C3C;padding:1px">
<h3 style="color:#313F3D;text-align:center;">Caesars Entertainment Dashboard</h3>
</div>
"""
st.markdown(caesars_titletemp,unsafe_allow_html=True)

def main():
    activities = ['How Many Tables Question 1', 'Slot Machines Question 2']
    option = st.sidebar.selectbox('Selection Option:', activities)


#Question1
    if option == 'How Many Tables Question 1':
        st.title('How many Open Tables')
        ##dataframes##
        df1 = pd.read_json('df1.json')
        table_count = pd.read_json('table_count.json')
        df_tables = pd.read_csv('df_tables.csv',index_col =0)
        #####
        start_date = st.sidebar.date_input('Start date', datetime.strptime('2020-10-01', '%Y-%m-%d'))
        end_date = st.sidebar.date_input('End date', datetime.strptime('2020-11-21', '%Y-%m-%d'))

        if start_date < end_date:
            st.success('Start date: `%s`\n\nEnd date:`%s`' % (start_date, end_date))
        else:
            st.error('Error: End date must fall after start date.')

        st.write('The number of unique tables on property ABC is: ', len(df1.c_table_num.unique()))



        st.write('This is the table number and their counts through the given dates.', table_count)
        mask = (df_tables['date'] >= start_date) & (df_tables['date'] <= end_date)
        st.write(df_tables.loc[mask])



        st.write('blah blah blah')

#Question2
    if option == 'Slot Machines Question 2':
        st.title('Slot Machine Reallocation')

        st.write('blah blah blah')

if __name__ == '__main__':
    main()
# This app retrieves the list of the **S&P 500** (from Wikipedia) and its corresponding **stock closing price** (year-to-date)!
# * **Python libraries:** base64, pandas, streamlit, yfinance, numpy, matplotlib
# * **Data source:** [Wikipedia](https://en.wikipedia.org/wiki/List_of_S%26P_500_companies).
# """)



# st.sidebar.header('User Input Features')
#
# # Web scraping of S&P 500 data
# #
# @st.cache
# def load_data():
#     url = 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'
#     html = pd.read_html(url, header = 0)
#     df = html[0]
#     return df
#
# df = load_data()
# sector = df.groupby('GICS Sector')
#
# # Sidebar - Sector selection
# sorted_sector_unique = sorted( df['GICS Sector'].unique() )
# selected_sector = st.sidebar.multiselect('Sector', sorted_sector_unique, sorted_sector_unique)
#
# # Filtering data
# df_selected_sector = df[ (df['GICS Sector'].isin(selected_sector)) ]
#
# st.header('Display Companies in Selected Sector')
# st.write('Data Dimension: ' + str(df_selected_sector.shape[0]) + ' rows and ' + str(df_selected_sector.shape[1]) + ' columns.')
# st.dataframe(df_selected_sector)
#
# # Download S&P500 data
# # https://discuss.streamlit.io/t/how-to-download-file-in-streamlit/1806
# def filedownload(df):
#     csv = df.to_csv(index=False)
#     b64 = base64.b64encode(csv.encode()).decode()  # strings <-> bytes conversions
#     href = f'<a href="data:file/csv;base64,{b64}" download="SP500.csv">Download CSV File</a>'
#     return href
#
# st.markdown(filedownload(df_selected_sector), unsafe_allow_html=True)
#
# # https://pypi.org/project/yfinance/
#
# data = yf.download(
#         tickers = list(df_selected_sector[:10].Symbol),
#         period = "ytd",
#         interval = "1d",
#         group_by = 'ticker',
#         auto_adjust = True,
#         prepost = True,
#         threads = True,
#         proxy = None
#     )
#
# # Plot Closing Price of Query Symbol
# def price_plot(symbol):
#   df = pd.DataFrame(data[symbol].Close)
#   df['Date'] = df.index
#   fig = plt.figure()
#   plt.fill_between(df.Date, df.Close, color='skyblue', alpha=0.3)
#   plt.plot(df.Date, df.Close, color='skyblue', alpha=0.8)
#   plt.xticks(rotation=90)
#   plt.title(symbol, fontweight='bold')
#   plt.xlabel('Date', fontweight='bold')
#   plt.ylabel('Closing Price', fontweight='bold')
#   return st.pyplot(fig)
#
# num_company = st.sidebar.slider('Number of Companies', 1, 5)
#
# if st.button('Show Plots'):
#     st.header('Stock Closing Price')
#     for i in list(df_selected_sector.Symbol)[:num_company]:
#         price_plot(i)
