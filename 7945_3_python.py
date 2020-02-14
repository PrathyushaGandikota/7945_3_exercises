#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
df1=pd.read_excel("SaleData.xlsx")


# In[2]:


# Q1 Find least sales amount for each item
# has been solved as an example
def least_sale(df):
 ls = df.groupby("Item")["Sale_amt"].min().reset_index()
 return ls

least_sale(df1)


# In[3]:


# Q2 compute total sales at each year X region
def sales_year_region(df):
    df['year']=pd.DatetimeIndex(df['OrderDate']).year
    a=df.groupby(["year","Region"])["Sale_amt"].sum().reset_index()
    return a
sales_year_region(df1)


# In[4]:


# Q3 append column with no of days difference from present date to each order date
from datetime import date
date.today()


# In[5]:


def days_diff(df):
    df["OrderDate"]=pd.to_datetime(df["OrderDate"]).dt.date
    #date.today()=pd.DatetimeIndex(date.today())
    df["no_of_days_diff"]=date.today() - df["OrderDate"]
    return df
days_diff(df1)


# In[6]:


# Q4 get dataframe with manager as first column and  salesman under them as lists in rows in second column.
def mgr_slsmn(df):
    df2=df.groupby('Manager')['SalesMan'].unique()
    return df2
mgr_slsmn(df1)


# In[7]:


# Q5 For all regions find number of salesman and number of units
def slsmn_units(df):
    df4=pd.DataFrame() 
    df4["Salesman_count"]=df.groupby(["Region"])["SalesMan"].nunique()
    df4["total_units"]=df.groupby(["Region"])["Units"].sum()
    return df4
slsmn_units(df1)


# In[8]:


# Q6 Find total sales as percentage for each manager
def sales_pct(df):
    df2=(df.groupby(["Manager"])["Sale_amt"].sum()/df["Sale_amt"].sum())*100
    return df2
sales_pct(df1)


# In[9]:


df=pd.read_excel("C:\\Users\\prathyusha.gandi\\Desktop\\imdb.xlsx",escapechar="//")
#df["imdbRating"]=pd.to_numeric(df.imdbRating,errors="coerce")
df["duration"]=pd.to_numeric(df.duration,errors='coerce')


# In[10]:


# Q7 get imdb rating for fifth movie of dataframe
def fifth_movie(df1):
    return df1["imdbRating"][5]
fifth_movie(df)
    


# In[11]:


# Q8 return titles of movies with shortest and longest run time
def movies(df):
    minval=df[df["duration"]==df["duration"].min()]["title"]
    maxval=df[df["duration"]==df["duration"].max()]["title"]
    return minval,maxval
    
movies(df)


# In[12]:


# Q9 sort by two columns - release_date (earliest) and Imdb rating(highest to lowest)
def sort_df(df1):
    df5=df1.sort_values(["year","imdbRating"],ascending=[True,False])
    return df5.head()
sort_df(df)


# In[15]:


#10. Subset the dataframe with movies having the following prameters. 
#revenue(gross) more than 2 million spent(budget) less than 1 million duration between 30 mintues to 180 minutes 
df=pd.read_csv("movie_metadata.csv")
def subset_data(df):
   return(df[(df.gross > 2000000) & (df.budget < 1000000) & (df.duration>30) & (df.duration < 180)])
print(subset_data(df))


# In[17]:


df3=pd.read_csv("diamonds.csv")


# In[18]:


# Q11 count the duplicate rows of diamonds DataFrame.
def dupl_rows(df):
    a=df.duplicated()
    b=df[a]
    return len(b)
dupl_rows(df3)


# In[19]:


# Q12 droping those rows where any value in a row is missing in carat and cut columns
def drop_row(df):
    df1=df.dropna(subset=["carat","cut"])
    return df1
drop_row(df3)


# In[20]:


# Q13 subset only numeric columns
def sub_numeric(df):
    df1=df._get_numeric_data()
    return df1
sub_numeric(df3)


# In[21]:


# Q14 compute volume as (x*y*z) when depth > 60 else 8
def volume(df):
    df['z']=df['z'].drop([21,432])
    df['z']=df["z"].astype(float)
    df['z'].fillna(0, inplace = True)
    vol=df["x"]*df["y"]*df["z"]
    df["volume"]=np.where(df["depth"]>60,vol,8)
    return df
volume(df3)


# In[22]:


# Q15 impute missing price values with mean
def impute(df):
    df['price'].fillna((df['price'].mean()),inplace=True)
    return df
impute(df3)


# In[ ]:


#Bonus Questions


# In[23]:


df=pd.read_excel("C:\\Users\\prathyusha.gandi\\Desktop\\imdb.xlsx",escapechar="//")
df["imdbRating"] = pd.to_numeric(df.imdbRating, errors='coerce')
df["duration"]=pd.to_numeric(df.duration,errors='coerce')
df["nrOfNominations"]=pd.to_numeric(df.nrOfNominations,errors='coerce')
df["nrOfWins"]=pd.to_numeric(df.nrOfWins,errors='coerce')


# In[24]:


#1. Generate a report that tracks the various Genere combinations for each type year on year.
#The result data frame should contain type, Genere_combo, year, avg_rating, min_rating, max_rating, total_run_time_mins 
def genre_combo(df1):
    df1['GenreCombo']=df1[df1.columns[16:]].T.apply(lambda g: ','.join(g.index[g==1]),axis=0)
    df2=df1.groupby(["type","year","GenreCombo"]).agg({"imdbRating":[min,max,np.mean],"duration":np.sum})
    return df2
genre_combo(df)


# In[25]:


#2.Is there a realation between the length of a movie title and the ratings ? 
#Generate a report that captures the trend of the number of letters in movies titles over years.
#We expect a cross tab between the year of the video release and the quantile that length fall under.
#The results should contain year, min_length, max_length, num_videos_less_than25Percentile, num_videos_25_50Percentile , num_videos_50_75Percentile, num_videos_greaterthan75Precentile 
df['Title_Length']=df['title'].apply(lambda x:len(x.split('(')[0].replace(' ','').rstrip()))
relation=df['Title_Length'].corr(df['imdbRating'])
print(relation)
def quantile():
    df['Quantile']=pd.qcut(df['Title_Length'],4,labels=False)
    df['Title_Length']=df['title'].apply(lambda x:len(x.split('(')[0].replace(' ','').rstrip()))
    df1=pd.crosstab(df.year,df.Quantile,margins=False)
    df1["min"]=df.groupby(["year"])["Title_Length"].min()
    df1["max"]=df.groupby(["year"])["Title_Length"].max()
    return df1
quantile()


# In[26]:


#3.In diamonds data set Using the volumne calculated above, create bins that have equal population within them.
#Generate a report that contains cross tab between bins and cut. 
#Represent the number under each cell as a percentage of total. 
df2=pd.read_csv("diamonds.csv")
def bins(df):
    df['z']=df['z'].drop([21,432])
    df['z']=df["z"].astype(float)
    df['z'].fillna(0, inplace = True)
    vol=df["x"]*df["y"]*df["z"]
    df["volume"]=np.where(df["depth"]>60,vol,8)
    df["bins"]=pd.qcut(df["volume"],7,labels=["A","B","C","D","E","F","G"])
    df1=(pd.crosstab(df.dropna().bins,df.cut,normalize="all"))*100
    return df1
bins(df2)


# In[27]:


df3=pd.read_csv("C:\\Users\\prathyusha.gandi\\Downloads\\movie_metadata.csv")
#4. Generate a report that tracks the Avg. imdb rating quarter on quarter, in the last 10 years, for movies that are top performing.
#You can take the top 10% grossing movies every quarter.
#Add the number of top performing movies under each genere in the report as well.
#df3=pd.read_csv("C:\\Users\\prathyusha.gandi\\Downloads\\movie_metadata.csv")
def gross(df):
    #to get the top 10 grossing movies  
    x=(df.groupby('title_year',group_keys=False).apply(lambda x: x.nlargest(int(len(x)*0.1),'gross'))).reset_index() 
    #group the title and imdb score
    y=x.groupby('title_year')['imdb_score'].mean().reset_index()
    y.rename(columns={'imdb_score':'Avg_imdb_score'},inplace=True)
    z=x.genres.str.get_dummies('|')
    a=pd.merge(x.title_year,z,on=None,left_index=True,right_index=True)
    a=a.groupby('title_year').sum()
    r=pd.merge(y,a,on='title_year')
    r=(r[r.title_year>r.title_year.max()-10]).reset_index()
    return r
gross(df3)


# In[28]:


#5.Bucket the movies into deciles using the duration. 
#Generate the report that tracks various features like nomiations, wins, count, top 3 geners in each decile
def deciles():
   df["decile"]=pd.qcut(df["duration"],10,labels=False)
   df1=df.iloc[:,17:]
   df2=df1.groupby("decile")[df1.columns.tolist()[1:28]].sum().T
   df3=df2.apply(lambda x: x.nlargest(3).index).T
   df3.columns=['top1','top2','top3']
   df4=df.groupby("decile")["nrOfNominations","nrOfWins"].sum()
   df5=pd.concat([df3,df4],axis=1)
   return df5
deciles()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




