import numpy as np
import pandas as pd
import plotly.express as px
def preprocess(df):
    # filtering for summer olympics
    df = df[df['Season'] == 'Summer']
    # merge with region_df
    # df = df.merge(region_df, on='NOC', how='left')
    # dropping duplicates
    df.drop_duplicates(inplace=True)
    # one hot encoding medals
    df = pd.concat([df, pd.get_dummies(df['Medal'])], axis=1)
    
    
    return df

def selection(data):
    year=data["Year"].sort_values().unique().tolist()
    year.insert(0,'Overall')
    reg=data["region"].sort_values().unique().tolist()
    reg.insert(0,'Overall')
    return year,reg
def fect_particular(data,year,reg):
    
     medal_tally=data.drop_duplicates(subset=['Team', 'NOC', 'Games', 'Year', 'City', 'Sport', 'Event', 'Medal'])
     flag = 0
    #  temp = medal_tally
     if year == "Overall" and reg == "Overall":
        temp = medal_tally
     if year != "Overall" and reg == "Overall":
        temp = medal_tally[medal_tally['Year']== int(year)]
     if year == "Overall" and reg != "Overall":
        flag = 1
        temp = medal_tally[medal_tally['region']==reg]
     if year != "Overall" and reg != "Overall":
        temp = medal_tally[(medal_tally['Year']==int(year))&(medal_tally['region']==reg)]
       
     if flag == 1:
        x=temp.groupby(['Year']).sum()[['Gold','Silver','Bronze']].sort_values(by='Year').reset_index()
        
     else:
      x=temp.groupby(['region']).sum()[['Gold','Silver','Bronze']].sort_values(by='Gold', ascending=False).reset_index()  
     x['Total']=x['Gold']+x["Silver"]+x['Bronze']
    
     x["Total"]=x["Total"].astype('int')
     x["Silver"]=x["Silver"].astype('int')
     x["Gold"]=x["Gold"].astype('int')
     x["Bronze"]=x["Bronze"].astype('int')
     return x
def graph1(data):
   d=data[["Year",'region']]
   d=d.drop_duplicates()

   d=d.groupby('Year').count()[['region']].reset_index()
   d.columns=d.columns.str.replace('region','No. of country')
   # # alternate use value_counts on Year

   
   return d
def graph2(data):
   d=data[["Year",'Event']]
   d=d.drop_duplicates()
   d=d.groupby('Year').count()[['Event']].reset_index()
   d.columns=d.columns.str.replace('Event','No. of events')
   # # alternate use value_counts on Year

   return d