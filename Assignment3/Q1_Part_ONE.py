
# coding: utf-8

# In[5]:

import pandas as pd
import calendar

#reading csv file
vc = pd.read_csv("Data/vehicle_collisions.csv")


# In[6]:

# Convert argument to datetime and adding column to 
vc['DATE_TIME'] = pd.to_datetime(vc['DATE'])

#Adding month column vc by fetch from DATE_TIME
vc['MONTH'] = pd.DatetimeIndex(vc['DATE_TIME']).month

#Adding year column vc by fetch from DATE_TIME
vc['YEAR'] = pd.DatetimeIndex(vc['DATE']).year

vc.head()


# In[23]:

#vehicle collisions in 2016
vc_in_2016 = vc[vc['YEAR']==2016] 

#vehicles Collisions in Manhattan in 2016
vc_2016_Manhattan = vc_in_2016[vc_in_2016['BOROUGH']=='MANHATTAN']

#manhattan count accidents in each month
vc_m2016_count_Manhattan = vc_2016_Manhattan.groupby(vc_2016_Manhattan['MONTH']).agg('count')

 # To get instances of the accidents by unique keys in Manhattan
vc_m2016_count_Manhattan_unique = vc_m2016_count_Manhattan['UNIQUE KEY']

#print(vc_m2016_count_Manhattan_unique)

#nyc count accidents in month
vc_m2016_count_nyc = vc_in_2016.groupby([vc_in_2016['MONTH']]).agg('count')

 #To get instances of the accidents by unique keys in New York Overall
vc_m2016_count_nyc_unique = vc_m2016_count_nyc['UNIQUE KEY']


# In[24]:

result = pd.concat([vc_m2016_count_Manhattan_unique,vc_m2016_count_nyc_unique],axis=1)
#result This will show month index, Manhattan and NYC
result.columns.values[0]= "MANHATTAN"
result.columns.values[1]= "NYC"

#result This will add the percentage column after dividing the first two columns
result['PERCENTAGE']=result[['MANHATTAN']].div(result['NYC'],axis=0)

#TO Calculate % we need to multiple 100 to last row
result['PERCENTAGE']=result['PERCENTAGE'].apply(lambda x:x*100) 

result.index

#Adding the value of index from 1,2,3.. to Jan, Feb, March...etc
#result['MONTH'] = result.index.get_level_values('MONTH')

#import calendar
#result['MONTH'] = result.index.astype(str).astype(int).apply(lambda x: calendar.month_abbr[x])

result['MONTH'] = result.index.astype(str).astype(int)

result['MONTH'] = result['MONTH'].apply(lambda x: calendar.month_abbr[x])

result

finalresult = result[['MONTH','MANHATTAN','NYC','PERCENTAGE']]

finalresult


# In[25]:

finalresult.to_csv('solution_q1_p1.csv',index=False,sep=',')


# In[ ]:



