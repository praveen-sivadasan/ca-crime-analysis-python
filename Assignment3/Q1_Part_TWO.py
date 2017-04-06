
# coding: utf-8

# In[1]:

import pandas as pd

vc = pd.read_csv('Data/vehicle_collisions.csv')


# In[10]:

vc


# In[25]:

df_location = vc[['UNIQUE KEY','BOROUGH']]
df_vehicletype = vc[['VEHICLE 1 TYPE','VEHICLE 2 TYPE','VEHICLE 3 TYPE','VEHICLE 4 TYPE','VEHICLE 5 TYPE']]
df_vehicletype = df_vehicletype.notnull()
df_vehicletype = df_vehicletype.applymap(lambda x:1 if x else 0)
df_modified = pd.concat([df_location,df_vehicletype],axis=1)

df_modified


# In[3]:

df_total_collision = df_modified.groupby('BOROUGH').sum()
df_total_collision


# In[7]:

df_total_collision['MORE_VEHICLES_INVOLVED'] = df_total_collision['VEHICLE 4 TYPE'] + df_total_collision['VEHICLE 5 TYPE'] 
df_total_collision['THREE_VEHICLES_INVOLVED'] =  df_total_collision['VEHICLE 3 TYPE']-df_total_collision['VEHICLE 4 TYPE']
df_total_collision['TWO_VEHICLES_INVOLVED'] =  df_total_collision['VEHICLE 2 TYPE']-df_total_collision['VEHICLE 3 TYPE']
df_total_collision['ONE_VEHICLE_INVOLVED'] =  df_total_collision['VEHICLE 1 TYPE']-df_total_collision['VEHICLE 2 TYPE']
df_total_collision = df_total_collision[['ONE_VEHICLE_INVOLVED','TWO_VEHICLES_INVOLVED','THREE_VEHICLES_INVOLVED','MORE_VEHICLES_INVOLVED']]
df_total_collision


# In[9]:

df_total_collision.to_csv("Solution_q1_p2.csv",index=True,sep=',')


# In[ ]:



