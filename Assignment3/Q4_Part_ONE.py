
# coding: utf-8

# In[7]:

import pandas as pd

#reading csv file
movie_analysis = pd.read_csv("Data/movies_awards.csv")
movie_analysis


# In[6]:

movie_awards_lines = movie_analysis['Awards']

movie_awards_lines = movie_awards_lines.dropna(axis=0,how='any')
movie_awards_lines=pd.DataFrame(movie_awards_lines)

movie_awards_lines


# In[9]:

movie_awards_lines['Awards_won'] = movie_analysis['Awards'].str.extract("(\d+) win")
movie_awards_lines['Awards_nominated'] =  movie_analysis['Awards'].str.extract("(\d+) nomination")
movie_awards_lines['Prime_Awards_won'] = movie_analysis['Awards'].str.extract("Won (\d+) Primetime Emmy")
movie_awards_lines['Prime_Awards_nominated'] = movie_analysis['Awards'].str.extract("Nominated for (\d+) Primetime Emmy")
movie_awards_lines['Oscar_Awards_nominated'] = movie_analysis['Awards'].str.extract("Nominated for (\d+) Oscar")
movie_awards_lines['Oscar_Awards_won'] = movie_analysis['Awards'].str.extract("Won (\d+) Oscar")
movie_awards_lines['Golden_Globe_Awards_nominated'] = movie_analysis['Awards'].str.extract("Nominated for (\d+) Golden Globe")
movie_awards_lines['Golden_Globe_Awards_won'] = movie_analysis['Awards'].str.extract("Won (\d+) Golden Globe")
movie_awards_lines['BAFTA_nominated'] = movie_analysis['Awards'].str.extract("Nominated for (\d+) BAFTA")
movie_awards_lines['BAFTA_won'] = movie_analysis['Awards'].str.extract("Won (\d+) BAFTA")

final= movie_awards_lines.fillna(0)


# In[10]:

final= movie_awards_lines.fillna(0)


# In[11]:

final


# In[15]:

#converting string to int
final['Awards_won'] = final['Awards_won'].astype(str).astype(int)
final['Prime_Awards_won'] = final['Prime_Awards_won'].astype(str).astype(int)
final['Oscar_Awards_won'] = final['Oscar_Awards_won'].astype(str).astype(int)
final['Golden_Globe_Awards_won'] = final['Golden_Globe_Awards_won'].astype(str).astype(int)
final['BAFTA_won'] = final['BAFTA_won'].astype(str).astype(int)

final['Awards_nominated'] = final['Awards_nominated'].astype(str).astype(int)
final['Prime_Awards_nominated'] = final['Prime_Awards_nominated'].astype(str).astype(int)
final['Oscar_Awards_nominated'] = final['Oscar_Awards_nominated'].astype(str).astype(int)
final['Golden_Globe_Awards_nominated'] = final['Golden_Globe_Awards_nominated'].astype(str).astype(int)
final['BAFTA_nominated'] = final['BAFTA_nominated'].astype(str).astype(int)


# In[16]:

#finding total won awards
final['Total_Won_Awards'] = final['Awards_won'] + final['Prime_Awards_won'] + final['Oscar_Awards_won'] + final['Golden_Globe_Awards_won']+final['BAFTA_won']


# In[17]:

#finding total nominatted awards
final['Total_Nominated_Awards'] = final['Awards_nominated'] + final['Prime_Awards_nominated']+ final['Oscar_Awards_nominated'] + final['Golden_Globe_Awards_nominated'] + final['BAFTA_nominated'] 


# In[18]:

final


# In[20]:

final.to_csv("solution_q4_p1.csv",index = False, sep=',')


# In[ ]:



