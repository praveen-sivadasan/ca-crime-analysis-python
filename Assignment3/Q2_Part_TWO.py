
# coding: utf-8

# In[1]:

import pandas as pd
import numpy as np
import os
import calendar

#reading csv file
emp_comp = pd.read_csv("Data/employee_compensation.csv")


# In[2]:

emp_cal = emp_comp[(emp_comp['Year Type']=="Calendar")]
emp_cal


# In[5]:

job_comp=emp_cal[(emp_cal['Year Type']=='Calendar')]
job_comp=pd.DataFrame(job_comp.groupby(['Employee Identifier','Job Family']).mean())

job_comp.drop(['Year', 'Organization Group Code','Union Code'], axis=1, inplace=True)
job_comp.head()


# In[6]:

overtime=job_comp[(job_comp['Overtime']>(.05*job_comp['Salaries']))]
overtime.head()


# In[7]:

top_family=overtime
top_family=top_family.groupby([top_family.index.get_level_values(1)]).mean()


# In[8]:

top_family=top_family[['Total Benefits','Total Compensation']]
top_family['Percent_Total_Benefit']=100*(top_family['Total Benefits']/top_family['Total Compensation'])
top_family=top_family.sort_values(['Percent_Total_Benefit'], ascending=[False])
top_family.head(5)


# In[11]:

top_family.to_csv('solution_q2_p2.csv',index = True, sep=',')


# In[ ]:



