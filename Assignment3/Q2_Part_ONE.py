
# coding: utf-8

# In[2]:

import pandas as pd

#reading csv file
ec = pd.read_csv("Data/employee_compensation.csv")


# In[3]:

result = ec.groupby(['Organization Group','Department']).mean().reset_index()

final_result = result[['Organization Group','Department','Total Compensation']]

final_result


# In[5]:

#sorted_result = final_result.sort(['Organization Group','Total Compensation'],ascending=False)

sorted_result = final_result.sort(['Total Compensation'],ascending=False)
sorted_result


# In[7]:

#sorted_result_grouped = sorted_result.groupby(['Organization Group'])

reindexed_result = sorted_result.reset_index(drop=True)

reindexed_result.head()


# In[8]:

reindexed_result.to_csv('solution_q2_p1.csv',index = False, sep=',')


# In[ ]:



