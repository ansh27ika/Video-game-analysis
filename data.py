from lib2to3.pgen2.pgen import DFAState
from operator import index
from turtle import title, width
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go

def data():
    df=pd.read_csv(r"/Users/anshika/Downloads/capstone3 dashboard/dataset/final_data_game.csv")
    st.title("Our Dataset")
    #st.markdown(""" ## Below is a portion of our data based on the smartphone reviews of different brands and models""")
    st.dataframe(df.head(10))
def EDA():   
    st.title('Do you play video games?Wanna do business with it?')

    df=pd.read_csv(r"/Users/anshika/Downloads/capstone3 dashboard/dataset/final_data_game.csv")
    top_10_games=pd.pivot_table(df,index="Game",values="NA_Sales",aggfunc="sum").sort_values("NA_Sales",ascending=False).head(10)
    game_options=top_10_games.index.to_list()
    #st.write(top_10_games)
    st.header("Top 10 Selling Games in North America")
    #game=st.multiselect('Which game you would like to play?',game_options,['FIFA 15'])
    #top_10_games=top_10_games[top_10_games.index.isin(game)]
    
    fig2= px.bar(top_10_games,x=top_10_games.index,y=top_10_games["NA_Sales"])
    st.write(fig2)
    
    top_10_games1=pd.pivot_table(df,index="Game",values="JP_Sales",aggfunc="sum").sort_values("JP_Sales",ascending=False).head(10)
    game_options=top_10_games1.index.to_list()
    #st.write(top_10_games1)
    st.header("Top 10 Selling Games in Japan")
    # game=st.multiselect('Which game you would like to play?',game_options,['FIFA 15'])
    # top_10_games1=top_10_games1[top_10_games1.index.isin(game)]
    
    fig4= px.bar(top_10_games1,x=top_10_games1.index,y=top_10_games1["JP_Sales"])
    st.write(fig4)
    
    top_10_games2=pd.pivot_table(df,index="Game",values="EU_Sales",aggfunc="sum").sort_values("EU_Sales",ascending=False).head(10)
    game_options=top_10_games2.index.to_list()
    #st.write(top_10_games2)
    st.header("Top 10 Selling Games  in Europe")
    # game=st.multiselect('Which game you would like to play?',game_options,['FIFA 15'])
    # top_10_games2=top_10_games2[top_10_games2.index.isin(game)]
    
    fig5= px.bar(top_10_games2,x=top_10_games2.index,y=top_10_games2["EU_Sales"])
    st.write(fig5)
    
    
    
    
    genre=pd.pivot_table(df,index="Genre",values="NA_Sales",aggfunc="sum").sort_values("NA_Sales",ascending=False)
    genre_options=genre.index.to_list()
    #st.write(genre)
    st.header("The most sold Genre in North America ")
    genre1=st.multiselect('Which genre  you would like to choose?',genre_options,['Sports'])
    genre=genre[genre.index.isin(genre1)]
    
    fig3= px.bar(genre,x=genre.index,y=genre["NA_Sales"],color=genre.index)
    st.write(fig3)
    
    
    top_10_publishers=pd.pivot_table(df,index="Publisher",values="NA_Sales",aggfunc="sum").sort_values("NA_Sales",ascending=False)
    publisher_options=top_10_publishers.index.to_list()
    #st.write(top_10_publishers)
    st.header("Publishers and their sales  in North America")
    publisher=st.multiselect('Whose publisher game you would like to play?',publisher_options,['Activision'])
    top_10_publishers=top_10_publishers[top_10_publishers.index.isin(publisher)]
    
    fig6= px.bar(top_10_publishers,x=top_10_publishers.index,y=top_10_publishers["NA_Sales"],color=top_10_publishers.index)
    st.write(fig6)
    
    df_year=pd.pivot_table(df,index="Year_of_Release",values="Global_Sales",aggfunc="sum").sort_values("Global_Sales",ascending=False)
    year=df_year.index.to_list()   
    st.header("Global Sales per Year")
    df_year=df_year[df_year.index.isin(year)]
       
    fig6= px.bar(df_year,x=df_year.index,y=df_year["Global_Sales"],color=df_year.index)
    st.write(fig6)
    
    df_year1=pd.pivot_table(df,index="Year_of_Release",values="Game",aggfunc="count").sort_values("Game",ascending=False)
    year=df_year1.index.to_list()   
    st.header("Number of games launches according to years")
    df_year=df_year1[df_year1.index.isin(year)]
       
    fig6= px.bar(df_year1,x=df_year1.index,y=df_year1["Game"],color=df_year1.index)
    st.write(fig6)
    
    
    top_5_publishers = df['Publisher']
    perc = df.loc[:,["Year_of_Release","Publisher",'Global_Sales']]
    perc['total_sales'] = perc.groupby([perc.Publisher,perc.Year_of_Release])['Global_Sales'].transform('sum')
    perc.drop('Global_Sales', axis=1, inplace=True)
    perc = perc.drop_duplicates()
    perc = perc[(perc['Year_of_Release'].astype('float')>=2006.0)]
    perc = perc.sort_values("Year_of_Release",ascending = False)
    perc = perc.loc[perc['Publisher'].isin(top_5_publishers)]
    perc = perc.sort_values("Year_of_Release")
    fig=px.bar(perc,x='Publisher', y="total_sales", animation_frame="Year_of_Release", 
    animation_group="Publisher", color="Publisher", hover_name="Publisher")
    
    fig.show()
    
    
    
    
     
    
    Genre=df.groupby(by="Genre").count()
    Genre["Global_Sales"]=Genre.iloc[:,1]*100/len(df)  
    Genre=Genre.sort_values(by="Global_Sales",ascending=False).head(10)
    st.header("Global Sales of genre")
    fig9=px.pie(Genre,values="Global_Sales", names=Genre.index)
    st.write(fig9)
    
    publisher=df.groupby(by="Publisher").count()
    publisher["Global_Sales"]=publisher.iloc[:,1]*100/len(df)  
    publisher=publisher.sort_values(by="Global_Sales",ascending=False).head(10)
    st.header("Which Publisher of games have highest sales?")
    fig10=px.pie(publisher,values="Global_Sales", names=publisher.index)
    st.write(fig10)
    
    df = df.loc[:,['Year_of_Release','NA_Sales','EU_Sales','JP_Sales','Other_Sales','Global_Sales']]
    df[['NA_sum','EU_sum','JP_sum','Other_sum', 'Global_sum']] = df.groupby('Year_of_Release')[['NA_Sales','EU_Sales','JP_Sales','Other_Sales','Global_Sales']].transform('sum')
    df.drop(['NA_Sales','EU_Sales','JP_Sales','Other_Sales','Global_Sales'], axis=1, inplace=True)
    df = df.drop_duplicates()
    df = df.sort_values('Year_of_Release')
    df1 = pd.DataFrame({'Place': ['NA_Sales']*df.shape[0], 'Year_of_Release':df['Year_of_Release'], 'Sales': df['NA_sum'], 'Global_Sales': df['Global_sum']})
    df2 = pd.DataFrame({'Place': ['EU_Sales']*df.shape[0], 'Year_of_Release':df['Year_of_Release'], 'Sales': df['EU_sum'], 'Global_Sales': df['Global_sum']})
    df3 = pd.DataFrame({'Place': ['JP_Sales']*df.shape[0], 'Year_of_Release':df['Year_of_Release'], 'Sales': df['JP_sum'], 'Global_Sales': df['Global_sum']})
    df4 = pd.DataFrame({'Place': ['Other_Sales']*df.shape[0], 'Year_of_Release':df['Year_of_Release'], 'Sales': df['Other_sum'], 'Global_Sales': df['Global_sum']})
    final = pd.concat([df1,df2,df3,df4], axis=0)
    final = final.sort_values("Year_of_Release")
    final = final[(final['Year_of_Release']>=1994.0) & (final['Year_of_Release']<=2016.0)]

    fig = px.scatter(final, x="Global_Sales", y="Sales", animation_frame="Year_of_Release", animation_group="Place", color="Place", hover_name="Place", size_max=1000, range_x=[0,768], range_y=[0,400])
    fig.update_traces(marker=dict(size=12,line=dict(width=2,color='DarkSlateGrey')),selector=dict(mode='markers'))
    fig.show()

        
    
    
    
    
      
    
    