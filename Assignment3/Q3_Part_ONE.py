
# coding: utf-8

# In[2]:

import pandas as pd

#reading csv file
ec = pd.read_csv("Data/cricket_matches.csv")


# In[6]:

ec['is_home_winner']  = ec['home'].str.strip().str.lower() == ec['winner'].str.strip().str.lower()


# In[8]:

ec_home_teams = ec[ec['is_home_winner']]
ec_home_teams


# In[21]:

ec_home_teams['is_inning_1'] = ec_home_teams['home'].str.strip().str.lower() == ec_home_teams['innings1'].str.strip().str.lower()


# In[28]:

cric_home_winner_inning1 = ec_home_teams[ec_home_teams['is_inning_1']]
cric_home_winner_inning1


# In[23]:

inning1_winner_runs = cric_home_winner_inning1.groupby('home').sum()
inning1_winner_indexed = inning1_winner_runs.reset_index()


# In[24]:

final_inning1_winner = inning1_winner_indexed[['home','innings1_runs','is_inning_1']] 
final_inning1_winner


# In[25]:

ec_home_teams['is_inning_2'] = ec_home_teams['home'].str.strip().str.lower() == ec_home_teams['innings2'].str.strip().str.lower()


# In[27]:

cric_home_winner_inning2 = ec_home_teams[ec_home_teams['is_inning_2']]
cric_home_winner_inning2


# In[29]:

inning2_winner_runs = cric_home_winner_inning2.groupby('home').sum()
inning2_winner_indexed = inning2_winner_runs.reset_index()


# In[30]:

final_inning2_winner = inning2_winner_indexed[['home','innings2_runs','is_inning_2']] 
final_inning2_winner


# In[31]:

final_home_runs = pd.merge(final_inning1_winner,final_inning2_winner, on='home', how='outer')


# In[38]:

final_home_runs['innings2_runs'] = final_home_runs['innings2_runs'].fillna(0)
final_home_runs['innings1_runs'] = final_home_runs['innings1_runs'].fillna(0)
final_home_runs['is_inning_1'] = final_home_runs['is_inning_1'].fillna(0)
final_home_runs['is_inning_2'] = final_home_runs['is_inning_2'].fillna(0)

final_home_runs['Total_innings'] = final_home_runs['is_inning_1'] + final_home_runs['is_inning_2']
final_home_runs['Total_runs'] = final_home_runs['innings1_runs'] + final_home_runs['innings2_runs']
final_home_runs['Score'] = final_home_runs['Total_runs']/final_home_runs['Total_innings']


# In[41]:

final_home_runs


# In[44]:

final_home_runs_average = final_home_runs[['home','Score']]
final_home_runs_average


# In[45]:

final_home_runs_average.to_csv('solution_q3_p1.csv',index = False, sep=',')


# In[ ]:



