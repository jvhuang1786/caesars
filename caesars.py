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
        #####
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

        st.write('What was interesting is there was decrease in table amount just on November 21st. Usuaully there are around 100 tables on the weekends and 60ish tables on the weekdays.  However, this number has been decreasing. But the amount of money actually increased on the last day.')

#Question2
    if option == 'Slot Machines Question 2':
        st.title('Slot Machine Reallocation')
        #####dataframes
        df_pre = pd.read_csv('df_pre.csv',index_col = 0)
        df_post = pd.read_csv('df_post.csv',index_col = 0)
        #####
        st.write('There were a total of 34 slot machines starting in zone 2. 32 slot machines were then moved from other zones to zone 2. Slot machines that moved are indicated by "moving" and those that stayed in place are indicated by "inplace" under the slot logistics column.')
        st.write('This is the pre_move table for the 32 slot machines and zone 2', df_pre)
        st.write('This is the post_move table for the 32 slot machines that moved into zone 2', df_post)
        option = st.selectbox(
        'Which of the 32 slot Machines do you want to compare?',
        ('2384807','2384808','2384809','2384810','2492692','2492693','2492696','2492697',
        '5135142','5135151','5135336','5135337','5135338','5135339','5141615','5141616','5141617',
 '5141618','B160874785','B160874786','B160874788','B160874789','B170506131','B170506132',
 'B170506133','B170506134','MRXU005523','MRXU005524','MRXU005525','MRXU005526','MRXU005527','MRXU005528'))
        st.write('You selected:', option)
        df_comb = pd.concat([df_post[df_post['c_serial_num']==option],
        df_pre[df_pre['c_serial_num']==option])
        st.write(df_comb.T)
        # print(df_pre[option].agg('mtr_win over dof').mean())
        #
        # print()
        # print()
        #
        # print(df_post[option].agg('coin_in over dof').mean())
        # print(df_pre[option].agg('coin_in over dof').mean())
        #
        # print()
        # print()
        #
        # print(df_post[option].agg('mtr_win over hp').mean())
        # print(df_pre[option].agg('mtr_win over hp').mean())
        # print()
        # print()
        # print(df_post[option].agg('coin_in over hp').mean())
        # print(df_pre[option].agg('coin_in over hp').mean())

if __name__ == '__main__':
    main()
