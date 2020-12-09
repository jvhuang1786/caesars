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
        df1 = pd.read_csv('df1.csv')
        table_count = pd.read_json('table_count.json')
        df_tables = pd.read_csv('df_tables.csv',index_col =0)

        st.write('The number of unique tables on property ABC is: ', len(df1.c_table_num.unique()))



        st.write('This is the table number and their counts through the given dates.', table_count)
        #mask = (df_tables['date'] <= start_date) & (df_tables['date'] >= end_date)
        st.write('Table count for date and Summary Statistics of Actual Win, Drop and Actual divided by Minutes Played',df_tables)

        fig = go.Figure()
        fig.add_trace(go.Scatter(x=df_tables.date, y=df_tables['table count'],
                            mode='lines',
                            line_color = 'light blue',
                            name='Number of Open Tables'))
        fig.update_layout(title_text = 'Open Table Count through the months of October to November', xaxis_rangeslider_visible = True)

        st.plotly_chart(fig, use_container_width=True)

        fig = go.Figure()

        fig.add_trace(go.Scatter(x=df_tables.date, y=df_tables['actual win mean'],
                            mode='lines',
                            line_color = 'teal',
                            name='Mean Actual Win'))
        fig.add_trace(go.Scatter(x=df_tables.date, y=df_tables['Drop mean'],
                            mode='lines',
                            line_color = 'blue',
                            name='Mean Drop'))
        fig.update_layout(title_text = 'Actual Wins and Drop', xaxis_rangeslider_visible = True)
        st.plotly_chart(fig, use_container_width=True)

        fig = px.box(df1, x="d_game_date", y="Drop",  title = 'Box Whiskers Drop')
        fig.update_traces(quartilemethod="exclusive") # or "inclusive", or "linear" by default
        fig.update_layout(title_text = 'Drop amount Box and Whiskers', xaxis_rangeslider_visible = True)
        st.plotly_chart(fig, use_container_width=True)

        fig = px.box(df1, x="d_game_date", y="f_actual_win",  title = 'Box Whiskers actual win')
        fig.update_traces(quartilemethod="exclusive") # or "inclusive", or "linear" by default
        fig.update_layout(title_text = 'Actual Win Box and Whiskers', xaxis_rangeslider_visible = True)
        st.plotly_chart(fig, use_container_width=True)

        st.write('What was interesting is there was decrease in table amount just on November 21st. Usuaully there are around 100 tables on the weekends and 70ish tables on the weekdays.  However, this number has been decreasing. But the amount of money actually increased on the last day.')

#Question2
    if option == 'Slot Machines Question 2':
        st.title('Slot Machine Reallocation')
        #####dataframes
        #####
        st.write('blah blah blah')

if __name__ == '__main__':
    main()
