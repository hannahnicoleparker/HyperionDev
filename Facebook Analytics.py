#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


df = pd.read_csv('flight1fbaug.csv') 


# In[3]:


video_views = df['3-second video views'].sum() # Total video views


# In[4]:


engagements = df['Engagements'].sum() # Engagements and engagement rates
followers = int(input("Number of followers: "))
engagement_rate = (engagements / followers) * 100

engagement_rate_percentage = f"{engagement_rate:.1f}%"


# In[5]:


num_rows = df.shape[0] # Number of posts this month 


# In[6]:


reach = df['People reached'].sum()


# In[7]:


average_engagements = engagements / num_rows # Average engagements per post


# In[8]:


top_posts = df.sort_values(by = 'Engagements', ascending = False).head(1)
top_post = top_posts['Permalink'].iloc[0]


# In[9]:


# Print whole report

print(f'Video views: {video_views}')
print(f'Engagement rate: {engagement_rate_percentage}')
print(f'Number of engagements: {engagements}')
print(f'Reach: {reach}')
print(f'Average engagements per post: {int(average_engagements)}')
print(f'Number of posts this month: {num_rows}')
print(f"The top performing post this month is: {top_post}")


# In[ ]:




