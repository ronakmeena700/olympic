import function
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

data2=pd.read_csv('C:\\Users\\RONAK\\Desktop\\New folder\\ml\\olympic data\\noc_regions.csv')
data1=pd.read_csv('C:\\Users\\RONAK\\Desktop\\New folder\\ml\\olympic data\\athlete_events.csv')
data=pd.merge(data1,data2,on='NOC',how ='left')
df=function.preprocess(data)

user_menu=st.sidebar.radio('select the option below',
('Medal Tally','Overall Analysis','Country-wise Analysis','Athlete-wise  Analysis'))
if user_menu=='Medal Tally':
    year,reg=function.selection(data)
    selected_year=st.sidebar.selectbox('select year',year)
    selected_country=st.sidebar.selectbox('select country',reg)
    medal_tally=function.fect_particular(df,selected_year,selected_country)
    if selected_year=="Overall" and selected_country=="Overall":
        st.title('Overall medal tally anlaysis')
    if selected_country!= "Overall" and selected_year=="Overall":
        st.title(selected_country + " Overall analysis")
    if selected_country=="Overall" and selected_year!="Overall":
        st.title("Overall analysis of "+str(selected_year))
    if selected_country!="Overall" and selected_year!="Overall":
        st.title(selected_country+" analysis of " +str(selected_year))
    st.table(medal_tally)


if user_menu=="Overall Analysis":
    n_player=df["Name"].unique().size
    n_year=df['Year'].unique().size
    n_region=df['region'].unique().size
    n_Sport=df['Sport'].unique().size
    st.title("Overall olympic analysis")
    col1,col2=st.columns(2)
    with col1:
        st.header("Number of player")
        st.text(n_player)
    with col2:
        st.header("Number of year")
        st.text(n_year)
    col1,col2=st.columns(2)
    with col1:
        st.header("Number of countries")
        st.text(n_region)
    with col2:
        st.header("Number of Sports")
        st.text(n_Sport)
    g=function.graph1(df)
    a=px.line(g,x='Year', y='No. of country')
    st.title(" ")
    st.title(" ")
    st.title(" ")
    st.header('Number of country taking part in olympic')
    st.plotly_chart(a)
    g2=function.graph2(df)
    b=px.line(g2,x="Year",y="No. of events")
    st.title(" ")
    st.title(" ")
    st.title(" ")
    st.header('Number of events occur')
    st.plotly_chart(b)