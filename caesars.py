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
<h3 style="color:#313F3D;text-align:center;">Caesar's Entertainment Dashboard</h3>
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
        df_post_inplace = pd.read_csv('df_inplace_post.csv',index_col =0)
        df_pre_inplace = pd.read_csv('df_inplace_pre.csv',index_col=0)
        df_post_move = pd.read_csv('df_post_move.csv')
        df_pre_move = pd.read_csv('df_pre_move.csv')
        final_table = pd.read_csv('final_table.csv',index_col = 0)
        df_combo = pd.read_csv('df_combo.csv',index_col = 0)
        #####
        st.write('In short the overall mean for slots overall increased from 190 to 290 when dividing by days on floor.  The moved slots increased from 312 to 510 and the slot machines that stayed stationary increased from 76 to 83.', final_table.T)

        option1 = st.selectbox(
        'Select an option to choose to display the distribution.',('box','violin','rug'))
        st.write('You selected:', option1)
        fig = px.histogram(df_combo, x='mtr_win over dof', color="Time_Period", marginal=option1, # can be `box`, `violin`
                         hover_data=df_combo.columns)
        fig.update_layout(title_text = 'MTR_Win Distribution Post and Pre')

        st.plotly_chart(fig, use_container_width=True)
        st.write('There were a total of 34 slot machines starting in zone 2. 32 slot machines were then moved from other zones to zone 2. Slot machines that moved are indicated by "moving" and those that stayed in place are indicated by "inplace" under the slot logistics column.')
        st.write('This is the pre_move table for the 32 slot machines and zone 2', df_pre)
        st.write('This is the post_move table for the 32 slot machines that moved into zone 2', df_post)

        fig = go.Figure()
        fig.add_trace(go.Bar(
            x=['Pre'],
            y=pd.Series(round(df_pre.agg('mtr_win over dof').mean(),3)),
            name='Pre Move',
            marker_color='red'
        ))
        fig.add_trace(go.Bar(
            x=['Post'],
            y=pd.Series(round(df_post.agg('mtr_win over dof').mean(),3)),
            name='Post Move',
            marker_color='gold'
        ))

        # Here we modify the tickangle of the xaxis, resulting in rotated labels.
        fig.update_layout(title_text = 'Overall Post and Pre MTR over DOF Mean',barmode='group', xaxis_tickangle=-45)
        st.plotly_chart(fig, use_container_width=True)

        fig = go.Figure()
        fig.add_trace(go.Bar(
            x=['Pre'],
            y=pd.Series(round(df_pre.agg('mtr_win over dof').sum(),3)),
            name='Pre Move',
            marker_color='red'
        ))
        fig.add_trace(go.Bar(
            x=['Post'],
            y=pd.Series(round(df_post.agg('mtr_win over dof').sum(),3)),
            name='Post Move',
            marker_color='gold'
        ))

        # Here we modify the tickangle of the xaxis, resulting in rotated labels.
        fig.update_layout(title_text = 'Overall Post and Pre MTR over dof Sum',barmode='group', xaxis_tickangle=-45)
        st.plotly_chart(fig, use_container_width=True)


        fig = go.Figure()
        fig.add_trace(go.Bar(
            x=['Pre'],
            y=pd.Series(round(df_pre_move.agg('mtr_win over dof').mean(),3)),
            name='Pre Move',
            marker_color='blue'
        ))
        fig.add_trace(go.Bar(
            x=['Post'],
            y=pd.Series(round(df_post_move.agg('mtr_win over dof').mean(),3)),
            name='Post Move',
            marker_color='gold'
        ))

        # Here we modify the tickangle of the xaxis, resulting in rotated labels.
        fig.update_layout(title_text = 'Post and Pre MTR over DOF Mean moved slots',barmode='group', xaxis_tickangle=-45)
        st.plotly_chart(fig, use_container_width=True)

        fig = go.Figure()
        fig.add_trace(go.Bar(
            x=['Pre'],
            y=pd.Series(round(df_pre_inplace.agg('mtr_win over dof').mean(),3)),
            name='Pre Move',
            marker_color='silver'
        ))
        fig.add_trace(go.Bar(
            x=['Post'],
            y=pd.Series(round(df_post_inplace.agg('mtr_win over dof').mean(),3)),
            name='Post Move',
            marker_color='gold'
        ))

        # Here we modify the tickangle of the xaxis, resulting in rotated labels.
        fig.update_layout(title_text = 'Zone 2 Performance Post and Pre MTR over DOF Mean without moved slots',barmode='group', xaxis_tickangle=-45)
        st.plotly_chart(fig, use_container_width=True)

        option = st.selectbox(
        'Which of the 32 slot Machines do you want to compare?',
        ('2384807','2384808','2384809','2384810','2492692','2492693','2492696','2492697',
        '5135142','5135151','5135336','5135337','5135338','5135339','5141615','5141616','5141617',
 '5141618','B160874785','B160874786','B160874788','B160874789','B170506131','B170506132',
 'B170506133','B170506134','MRXU005523','MRXU005524','MRXU005525','MRXU005526','MRXU005527','MRXU005528'))
        st.write('You selected:', option)
        df_comb = pd.concat([df_post[df_post['c_serial_num']==option],df_pre[df_pre['c_serial_num']==option]]).reset_index(drop= True)
        st.write(df_comb.T)
        fig = go.Figure()
        fig.add_trace(go.Bar(
            x=['coin_in', 'mtr_win'],
            y=df_comb[['coin_in', 'mtr_win']].iloc[0],
            name='Post Move',
            marker_color='blue'
        ))
        fig.add_trace(go.Bar(
            x=['coin_in', 'mtr_win'],
            y=df_comb[['coin_in', 'mtr_win']].iloc[1],
            name='Pre Move',
            marker_color='lightblue'
        ))

        # Here we modify the tickangle of the xaxis, resulting in rotated labels.
        fig.update_layout(title_text = 'coin_in and mtr_win individual slots',barmode='group', xaxis_tickangle=-45)
        st.plotly_chart(fig, use_container_width=True)

        fig = go.Figure()
        fig.add_trace(go.Bar(
            x=['mtr_win over dof', 'coin_in over dof'],
            y=df_comb[['mtr_win over dof', 'coin_in over dof']].iloc[0],
            name='Post Move',
            marker_color='indianred'
        ))
        fig.add_trace(go.Bar(
            x=['mtr_win over dof', 'coin_in over dof'],
            y=df_comb[['mtr_win over dof', 'coin_in over dof']].iloc[1],
            name='Pre Move',
            marker_color='lightsalmon'
        ))

        # Here we modify the tickangle of the xaxis, resulting in rotated labels.
        fig.update_layout(title_text = 'mtr win and coin in over dof individual slots',barmode='group', xaxis_tickangle=-45)
        st.plotly_chart(fig, use_container_width=True)

        fig = go.Figure()
        fig.add_trace(go.Bar(
            x=['mtr_win over hp', 'coin_in over hp'],
            y=df_comb[['mtr_win over hp', 'coin_in over hp']].iloc[0],
            name='Post Move',
            marker_color='green'
        ))
        fig.add_trace(go.Bar(
            x=['mtr_win over hp', 'coin_in over hp'],
            y=df_comb[['mtr_win over hp', 'coin_in over hp']].iloc[1],
            name='Pre Move',
            marker_color='lightgreen'
        ))

        # Here we modify the tickangle of the xaxis, resulting in rotated labels.
        fig.update_layout(title_text = 'coin_in and mtr_win in over hp/pulls indvidual slots',barmode='group', xaxis_tickangle=-45)
        st.plotly_chart(fig, use_container_width=True)
        st.write('Since you are comparing 27 days to 76 days you would have to divide the total amount to make an equal comparison. Overall the machines performed better. This could be due to the machines from other areas being more popular which attracted more people to zone 2 to play the pre-zone 2 machines more as well.')

if __name__ == '__main__':
    main()
